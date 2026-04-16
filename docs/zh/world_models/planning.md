# 基于世界模型的规划

在拥有学习到的世界模型之后，如何利用它进行决策？本页介绍利用世界模型的各类规划算法——从简单的随机射击法到精密的树搜索和基于想象力的策略学习。

## 规划问题

给定世界模型 $f_\theta$（转移动力学）和奖励模型 $r_\theta$，寻找最大化期望累积奖励的动作序列：

$$
a_{t:t+H-1}^* = \arg\max_{a_{t:t+H-1}} \sum_{k=0}^{H-1} \gamma^k \hat{r}_{t+k}
$$

其中 $\hat{s}_{t+k+1} = f_\theta(\hat{s}_{t+k}, a_{t+k})$，$\hat{r}_{t+k} = r_\theta(\hat{s}_{t+k}, a_{t+k})$。

## 随机射击法

最简单的方法：采样大量随机动作序列，选择最优者。

1. 采样 $N$ 个动作序列：$\{a_{t:t+H-1}^{(i)}\}_{i=1}^{N}$
2. 将每个序列在模型中展开，计算预测回报
3. 执行最优序列的第一个动作

**优点**：简单，易于并行化

**缺点**：在高维动作空间中效率低下，随时域增长扩展性差

## 交叉熵方法（CEM）

**CEM** 通过迭代优化动作分布来改进搜索：

!!! note "CEM 规划伪代码"
    ```
    初始化动作分布：μ, σ（如均匀分布）
    for iteration = 1, ..., I do
        从 N(μ, σ²) 中采样 N 个动作序列
        在模型中展开每个序列，计算回报
        选择回报最高的 K 个序列（精英集）
        更新 μ, σ 使其拟合精英集
    end for
    返回 μ（或最优精英序列）
    ```

CEM 由于其简洁性和有效性，被广泛应用于基于模型的 RL 中（如 PlaNet、PETS）。

**关键参数**：

- 种群大小 $N$（通常 500-1000）
- 精英比例（通常取前 10%）
- 迭代次数 $I$（通常 5-10）
- 规划时域 $H$（通常 5-30 步）

## 模型预测控制（MPC）

MPC 是一种**滚动时域**方法：

1. 在每个真实时间步，使用模型向前规划 $H$ 步
2. 仅执行规划序列的**第一个动作**
3. 在下一时间步根据更新后的状态重新规划

```mermaid
graph LR
    S[当前状态] --> P[规划 H 步]
    P --> E[执行第一个动作]
    E --> O[观测新状态]
    O --> S
```

MPC 通过不断从真实状态重新规划，天然地处理了模型误差。

**应用**：PETS（Chua et al., 2018）、PlaNet（Hafner et al., 2019）

### PETS（概率集成轨迹采样）

**PETS** 将集成模型与 CEM 规划相结合：

1. 训练 $B$ 个动力学模型的集成
2. 对每个 CEM 样本，使用**轨迹采样**——在每个时间步随机切换集成成员
3. 这样可以将环境不确定性（认知不确定性）和模型不确定性（偶然不确定性）都传播到规划中

## 蒙特卡洛树搜索（MCTS）

MCTS 通过平衡探索与利用来构建搜索树：

1. **选择**：用 UCT（树的置信上界）遍历树
2. **扩展**：添加新节点
3. **模拟**：从新节点展开策略
4. **回溯**：沿树向上更新价值估计

### 结合学习模型的 MCTS

**AlphaZero**（Silver et al., 2018）：MCTS 与神经网络结合，后者提供：

- 先验策略 $p(a|s)$ 指导搜索方向
- 价值估计 $v(s)$ 评估叶节点

**MuZero**（Schrittwieser et al., 2020）：结合**完全学习的模型**进行 MCTS：

- 无需访问真实环境规则
- 使用学习到的动力学模型扩展搜索树
- 在围棋、国际象棋、将棋和 Atari 上达到超人水平

### MCTS 与射击方法的对比

| 方面 | 射击法 / CEM | MCTS |
|------|-------------|------|
| 动作空间 | 连续（天然适合） | 离散（天然适合） |
| 规划深度 | 中等（5-30） | 深（数百步） |
| 计算量 | 中等 | 大 |
| 最适场景 | 连续控制 | 博弈、结构化问题 |

## 基于想象力的策略学习

与其在每个时间步进行在线规划，不如通过在模型产生的**想象轨迹**上训练来学习一个策略。这将规划的成本**分摊**到策略网络中。

### Dreamer 的方法

Dreamer（Hafner et al., 2020）完全在想象中训练 Actor-Critic 网络：

1. **世界模型**在潜在空间中生成想象轨迹：
   $z_{t+1} = \text{dyn}_\theta(z_t, a_t)$

2. **评价网络（Critic）**沿想象轨迹估计价值：
   $V_\psi(z_t) \approx \mathbb{E}\left[\sum_{k=0}^{H} \gamma^k r_{t+k}\right]$

3. **策略网络（Actor）**被更新以最大化想象回报：
   $\max_\phi \mathbb{E}\left[\sum_{k=0}^{H} \gamma^k \left(r_{t+k} + \eta \mathcal{H}(\pi_\phi(\cdot|z_{t+k}))\right)\right]$

4. **梯度反向传播**贯穿整个想象轨迹（DreamerV2/V3 中对离散动作使用直通梯度）

**核心优势**：训练完成后，策略可以实时运行——无需在决策时进行昂贵的搜索。

### SVG（随机值梯度）

**SVG**（Heess et al., 2015）：通过学习到的动力学模型微分来计算策略梯度：

$$
\nabla_\phi J \approx \nabla_\phi \sum_{t=0}^{H} r(s_t, a_t), \quad \text{其中 } s_{t+1} = f_\theta(s_t, a_t), \; a_t = \pi_\phi(s_t)
$$

这利用了通过模型的完整梯度（不同于 REINFORCE 风格的梯度），从而降低了方差。

## 视频预测作为规划

近年来的研究直接利用视频预测模型进行规划：

**UniPi**（Du et al., 2023）：

1. 使用文本条件的视频扩散模型生成未来视频
2. 利用逆动力学模型从生成的视频中提取动作
3. 视频模型同时充当世界模型和规划器

这种方法充分利用了大型视频模型中蕴含的丰富世界知识。

## 规划方法对比

| 方法 | 适用场景 | 优势 | 劣势 |
|------|---------|------|------|
| 随机射击 | 原型验证 | 最简单 | 效率低 |
| CEM | 连续 MPC | 质量与速度的良好平衡 | 时域有限 |
| MCTS | 离散、深度推理 | 在计算预算内最优 | 计算成本高，限于离散空间 |
| 想象力（Dreamer） | 实时控制 | 测试时快速，支持连续空间 | 依赖良好的模型 |
| SVG | 可微模型 | 低方差梯度 | 梯度爆炸/消失问题 |
| 基于视频（UniPi） | 丰富视觉任务 | 利用预训练模型 | 速度慢、粒度粗 |

## 核心参考文献

- Chua, K., et al. (2018). "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." *NeurIPS*.
- Hafner, D., et al. (2019). "Learning Latent Dynamics for Planning from Pixels." *ICML*.
- Silver, D., et al. (2018). "A General Reinforcement Learning Algorithm that Masters Chess, Shogi, and Go Through Self-Play." *Science*.
- Schrittwieser, J., et al. (2020). "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model." *Nature*.
- Hafner, D., et al. (2020). "Dream to Control: Learning Behaviors by Latent Imagination." *ICLR*.
- Du, Y., et al. (2023). "Learning Universal Policies via Text-Guided Video Generation." *NeurIPS*.
