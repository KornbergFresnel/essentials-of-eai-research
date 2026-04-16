# 具身智能的数据采集

数据是基于学习的具身智能系统的基石。本页涵盖机器人学习数据的大规模采集策略、系统设计与关键考量——包括人类示教、自主探索与合成数据生成。

## 数据瓶颈问题

与自然语言处理或计算机视觉不同，具身智能面临独特的数据瓶颈：

- **成本高昂**：真实机器人运行成本约为每小时 10-100 美元
- **速度缓慢**：物理交互必须在实时中完成，无法批量加速
- **设备脆弱**：机器人会磨损、损坏，需要定期维护
- **多样性要求**：任务、环境和物体种类繁多
- **复用性差**：为某一任务采集的数据往往难以直接迁移到其他任务

!!! note "核心挑战"
    具身智能数据的根本困难在于：每一条数据都需要物理世界的真实交互，而物理世界既昂贵又缓慢。这与互联网数据的"免费且无限"形成了鲜明对比。

## 数据采集策略

### 1. 遥操作（人类示教）

遥操作是操作类任务中最常用的数据采集方式。详见 [遥操作](teleoperation.md) 页面。

**优势**：数据质量高、任务针对性强、能捕捉人类操作策略

**劣势**：成本高（需要人力）、难以规模化、受操作者技能水平限制

**代表系统**：

| 系统 | 硬件形态 | 特点 |
|------|---------|------|
| **ALOHA** | 双臂低成本平台 | 支持精细双手操作，成本约 2 万美元 |
| **UMI** | 通用操作接口 | 手持式采集，无需机器人硬件 |
| **GELLO** | 通用低成本领导者 | 关节空间一对一映射 |
| **VR 遥操作** | VR 手柄/手套 | 直觉式操作，适合末端执行器控制 |

### 2. 脚本化/程序化数据

利用预编程或启发式控制器生成数据：

```python
# 示例：脚本化抓取数据采集
for episode in range(num_episodes):
    object_pose = randomize_object_placement()  # 随机化物体位置
    grasp_pose = compute_antipodal_grasp(object_pose)  # 计算对跖点抓取
    trajectory = plan_trajectory(current_pose, grasp_pose)  # 规划轨迹
    execute_and_record(trajectory)  # 执行并记录
```

**优势**：成本低、可大规模扩展、无需人工介入

**劣势**：任务复杂度受限、缺乏人类直觉、每个任务需要单独工程实现

### 3. 自主探索（基于强化学习）

让机器人通过强化学习自主探索并采集数据：

- **在线 RL**：机器人与环境交互，从奖励信号中学习
- **自监督探索**：机器人自行设定目标并探索（目标条件 RL、RND 等）
- **自由游戏数据**：非结构化探索，机器人自由与环境交互

**优势**：可扩展、能发现新策略、无需人工标注

**劣势**：速度慢（实时探索）、安全隐患、稀疏奖励问题

!!! warning "安全性考量"
    自主探索时必须设置安全约束，包括力矩限制、工作空间边界和紧急停止机制。未经约束的探索可能导致机器人自身或环境的损坏。

### 4. 仿真数据

在仿真环境中生成数据：

| 方法 | 描述 | 数据规模 |
|------|------|---------|
| **仿真中的 RL** | 在并行仿真中训练 RL 策略 | $10^8$-$10^{10}$ 步 |
| **程序化生成** | 随机生成环境、物体和任务 | 理论上无限 |
| **数字孪生** | 模拟特定真实环境 | 有限但精确 |
| **合成渲染** | 结合域随机化生成训练图像 | 数百万张图像 |

!!! info "仿真到真实的鸿沟（Sim-to-Real Gap）"
    仿真数据的核心挑战是仿真与真实世界之间的差异。常见缓解手段包括：域随机化（Domain Randomization）、系统辨识（System Identification）和域自适应（Domain Adaptation）。

### 5. 互联网规模数据

利用互联网上的视频和数据资源：

- **机器人视频数据集**：聚合的真实机器人数据（如 Open X-Embodiment）
- **人类视频**：从人类示范视频中学习操作策略
- **被动视频**：互联网上的任务视频（烹饪、装配等）
- **语言标注数据**：视频-语言配对数据，用于语义对接

## 规模化数据采集

### 机器人农场

同时运行多台机器人以扩大数据采集规模：

**Google 机器人农场**：100+ 台机械臂全天候采集操作数据

**DROID（Khazatsky et al., 2024）**：分布式机器人交互数据集

- 76K 条示教，涵盖 564 个任务
- 跨多个研究机构采集
- 标准化硬件与数据格式

### 舰队学习（Fleet Learning）

利用已部署的机器人持续采集与学习：

1. 将部分训练好的策略部署到机器人舰队
2. 在正常运行过程中采集交互数据
3. 集中聚合数据，重新训练模型
4. 将更新后的模型推送至整个舰队

### Open X-Embodiment

**Open X-Embodiment (OXE)** 是目前最大的聚合式机器人学习数据集：

- 超过 100 万条真实机器人片段
- 涵盖 22 种机器人本体
- 527 项技能，跨越 160K+ 个任务
- 支持训练通用机器人策略（RT-X）

## 数据格式与标准

### 主流格式

| 格式 | 描述 | 使用方 |
|------|------|--------|
| **RLDS** | 强化学习数据集（基于 TensorFlow） | OXE, RT-X |
| **HDF5** | 层次化数据格式，灵活通用 | RoboMimic |
| **LeRobot** | Hugging Face 机器人数据格式 | LeRobot 生态 |
| **zarr** | 分块压缩数组存储 | Diffusion Policy |

### 应当记录的内容

每条示教片段应记录：

- **观测**：多视角相机图像、本体感知（关节角度/角速度）、力/扭矩传感
- **动作**：关节指令、末端执行器位姿
- **元数据**：任务描述、成功/失败标记、时间戳、标定参数
- **语言**：任务的自然语言描述

## 数据增强

通过增强技术扩大有效数据集规模：

### 几何增强

- 随机相机视角扰动
- 物体位姿随机化
- 工作空间缩放与旋转

### 视觉增强

- 颜色抖动、随机遮挡
- 背景随机化
- 光照变化

### 轨迹增强

- 向动作序列添加噪声（提高鲁棒性）
- 时间拉伸轨迹（速度变化）
- 镜像/翻转轨迹

### 生成式增强

- 使用扩散模型生成新颖视觉场景
- 使用大语言模型生成任务描述
- 使用世界模型想象新情景

## 从示教到策略

利用采集数据学习策略的常见方法：

### 行为克隆（Behavior Cloning, BC）

监督学习方法，直接拟合专家动作分布：

$$
\pi_\theta(a|o) = \arg\min_\theta \mathbb{E}_{(o,a) \sim \mathcal{D}} [\mathcal{L}(\pi_\theta(o), a)]
$$

方法简洁，但存在**分布偏移（distribution shift）**问题——小误差会随时间累积放大。

!!! tip "缓解分布偏移"
    DAgger（Dataset Aggregation）通过在训练策略的轨迹上收集专家标注来缓解分布偏移。实践中常结合数据增强和动作分块（action chunking）来提升 BC 的鲁棒性。

### 扩散策略（Diffusion Policy）

**Diffusion Policy**（Chi et al., 2023）使用扩散过程建模动作分布：

$$
p_\theta(a_{t:t+H} | o_t) \text{ 通过迭代去噪过程生成}
$$

其核心训练目标为去噪得分匹配：

$$
\mathcal{L}(\theta) = \mathbb{E}_{k, \epsilon, a_0} \left[ \| \epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_k} \, a_0 + \sqrt{1 - \bar{\alpha}_k} \, \epsilon, \, o_t, \, k) \|^2 \right]
$$

当前在示教学习领域达到最优性能，能够处理**多模态动作分布**。

### 动作分块与 Transformer（ACT）

**ACT**（Zhao et al., 2023）使用 Transformer 预测未来动作块：

$$
a_{t:t+k} = \text{Transformer}(o_t, \text{style\_variable})
$$

通过重叠动作块的时间集成（temporal ensembling）减少抖动行为。ACT 特别适用于 ALOHA 等双臂操作平台。

### 逆强化学习 / 奖励学习

从示教中学习奖励函数，再用 RL 优化策略：

- 相比 BC 更鲁棒（不受分布偏移困扰）
- 流水线更复杂，训练成本更高

## 核心参考文献

- Brohan, A., et al. (2023). "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control." *CoRL*.
- Chi, C., et al. (2023). "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion." *RSS*.
- Khazatsky, A., et al. (2024). "DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset." *RSS*.
- Open X-Embodiment Collaboration. (2024). "Open X-Embodiment: Robotic Learning Datasets and RT-X Models." *ICRA*.
- Zhao, T.Z., et al. (2023). "Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware." *RSS*.
- Ross, S., et al. (2011). "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning." *AISTATS*.
