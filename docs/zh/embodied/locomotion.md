# 运动控制

学习运动控制——行走、奔跑、攀爬和在多样化地形中穿行的能力——是具身智能领域最活跃、成果最丰硕的方向之一。基于 RL 的运动控制在近年来取得了令人瞩目的成就，训练出的策略可以从仿真直接迁移到真实的四足机器人和人形机器人上。

## 问题定义

运动控制问题：

- **状态**：机器人本体感觉（关节位置 $q$、关节速度 $\dot{q}$、基座姿态、基座角速度、重力向量）+ 可选的外感觉（高度图、深度图像）
- **动作**：关节位置目标 $a_t \in \mathbb{R}^n$（发送给 PD 控制器）
- **奖励**：速度跟踪、能量效率和正则化项的组合

### 典型奖励函数

$$
r_t = \underbrace{r_{\text{tracking}}}_{\text{跟踪指令}} + \underbrace{r_{\text{style}}}_{\text{自然步态}} - \underbrace{c_{\text{energy}}}_{\text{能量效率}} - \underbrace{c_{\text{smooth}}}_{\text{动作平滑}}
$$

常见的奖励项：

| 奖励项 | 公式 | 目的 |
|--------|------|------|
| 线速度跟踪 | $\exp(-\|v_{xy} - v_{xy}^{\text{cmd}}\|^2 / \sigma)$ | 跟随速度指令 |
| 角速度跟踪 | $\exp(-\|\omega_z - \omega_z^{\text{cmd}}\|^2 / \sigma)$ | 跟随偏航率指令 |
| 基座高度 | $-(z_{\text{base}} - z_{\text{target}})^2$ | 保持目标高度 |
| 姿态 | $-\|\text{gravity\_projected}_{xy}\|^2$ | 保持直立 |
| 动作变化率 | $-\|\dot{a}_t\|^2$ | 动作平滑 |
| 力矩惩罚 | $-\|\tau_t\|^2$ | 能量效率 |
| 足部空中时间 | 摆动相持续时间的奖励 | 鼓励步态模式 |

## 核心方法

### 教师-学生框架

一种广泛使用的范式：

1. **教师策略**使用特权信息（精确地形高度图、接触力、摩擦系数）进行训练
2. **学生策略**仅使用机载传感器观测来模仿教师

这将 RL 训练（使用易于学习的特权状态）与部署约束（有限的机载传感器）解耦。

```mermaid
graph LR
    T[教师策略<br/>特权观测] -->|蒸馏| S[学生策略<br/>仅机载观测]
    SIM[仿真环境<br/>特权信息] --> T
    S --> REAL[真实机器人]
```

### 课程学习

在训练过程中逐步增加任务难度：

- **地形课程**：从平地 → 缓坡 → 台阶 → 崎岖地形 → 踏脚石
- **指令课程**：从低速开始 → 逐渐增加到全速范围
- **扰动课程**：从无外力 → 逐渐增加外部推力

### 基于参考动作的奖励塑形

使用动作捕捉数据或手工设计的参考轨迹来引导学习：

$$
r_{\text{imitation}} = \exp\left(-\alpha \sum_j \| q_j - q_j^{\text{ref}} \|^2 \right)
$$

这有助于策略发现自然的步态模式（小跑、弹跳、飞奔），而非那些不自然但能最大化奖励的行为。

## 里程碑成果

### 四足运动控制

**Learning Agile and Dynamic Motor Skills for Legged Robots**（Hwangbo et al., 2019）：

- 致动器网络建模真实电机动力学
- 训练 ANYmal 行走、从跌倒中恢复
- 最早成功实现 sim-to-real RL 运动控制的工作之一

**Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild**（Miki et al., 2022）：

- 教师-学生框架，结合本体感觉和外感觉
- ANYmal 在森林小道、雪地、台阶中穿行
- 基于信念的地形估计

**Extreme Parkour with Legged Robots**（Cheng et al., 2024）：

- 四足机器人完成跳跃、翻转、攀爬
- 通过大规模域随机化训练
- 敏捷性逼近生物体能力

### 人形运动控制

**Sim-to-Real Learning of All Common Bipedal Gaits**（Siekmann et al., 2021）：

- 在 Cassie 机器人上实现行走、跑步、跳跃
- RL + 参考动作 + 奖励塑形

**Learning Humanoid Locomotion with Transformers**（Radosavovic et al., 2024）：

- 使用观测历史的因果 Transformer 策略
- 人形机器人在多样化地形上实现鲁棒行走
- 展示了历史信息对处理延迟和不可观测状态的重要性

**Humanoid Locomotion as Next Token Prediction**（Liao et al., 2024）：

- 使用自回归模型进行感觉运动轨迹预测
- 将运动控制定义为序列建模问题

## 技术深入

### 观测历史与延迟处理

真实机器人存在传感器延迟（约 20-50ms）和致动器延迟（约 10-30ms）。解决方案：

- **堆叠观测**：将最近 $k$ 个观测拼接作为输入
- **RNN/Transformer**：用循环或注意力架构处理观测序列
- **显式延迟建模**：在训练中加入模拟延迟

### Sim-to-Real 迁移技术

| 技术 | 描述 |
|------|------|
| **域随机化** | 随机化物理、视觉和形态参数 |
| **系统辨识** | 估计真实机器人参数，匹配仿真 |
| **致动器网络** | 学习真实致动器动力学的神经网络模型 |
| **观测噪声** | 添加噪声以模拟真实传感器的不完美性 |
| **动作延迟** | 模拟通信和计算延迟 |

### 地形自适应运动

在多样化地形中穿行：

1. **基于高度图**：使用地形高度图（来自深度相机或激光雷达）作为额外输入
2. **隐式适应**：利用观测历史——策略从最近的动力学变化中隐式推断地形属性
3. **显式估计**：训练估计网络从观测历史中预测地形属性（摩擦系数、坡度）

## 常见训练配置

典型四足运动控制任务的训练参数：

| 参数 | 典型值 |
|------|--------|
| 算法 | PPO |
| 并行环境数 | 4096 - 8192 |
| 仿真平台 | Isaac Gym / Isaac Lab |
| 回合时长 | 20-30 秒 |
| 控制频率 | 50-100 Hz |
| 训练时间 | 1-4 小时（单 GPU） |
| 总环境步数 | $10^8$ - $10^9$ |
| 策略网络 | MLP (128, 64, 32) 或小型 Transformer |
| 动作空间 | 关节位置目标（四足为 12 维） |

## 核心参考文献

- Hwangbo, J., et al. (2019). "Learning Agile and Dynamic Motor Skills for Legged Robots." *Science Robotics*.
- Lee, J., et al. (2020). "Learning Quadrupedal Locomotion over Challenging Terrain." *Science Robotics*.
- Miki, T., et al. (2022). "Learning Robust Perceptive Locomotion for Quadrupedal Robots in the Wild." *Science Robotics*.
- Cheng, X., et al. (2024). "Extreme Parkour with Legged Robots." *ICRA*.
- Radosavovic, I., et al. (2024). "Learning Humanoid Locomotion with Transformers." *arXiv:2303.03381*.
- Kumar, A., et al. (2021). "RMA: Rapid Motor Adaptation for Legged Robots." *RSS*.
