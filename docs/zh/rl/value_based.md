# 基于值函数的方法

基于值函数的方法学习最优动作值函数 $Q^*(s,a)$，并从中导出策略。这类方法对**离散动作空间**尤其有效，是许多实用 RL 系统的基石。

## Q-Learning

**Q-learning** (Watkins, 1989) 是基于值函数的异策略算法的奠基之作。它利用贝尔曼最优方程来学习 $Q^*$：

$$
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s,a) \right]
$$

关键性质：

- **异策略**：无论实际执行了哪个动作，更新都使用 $\max_{a'}$
- **表格型**：原始形式在表格中存储 Q 值（仅适用于小状态空间）
- 在温和条件下**收敛**到 $Q^*$（要求所有状态-动作对被无限次访问）

## DQN（深度 Q 网络）

**DQN** (Mnih et al., 2013, 2015) 利用神经网络作为函数逼近器，将 Q-learning 扩展到高维状态空间（如 Atari 像素输入）。

### 核心创新

1. **经验回放 (Experience Replay)**：将转移 $(s, a, r, s')$ 存储在回放缓冲区 $\mathcal{D}$ 中，训练时随机采样小批量。这打破了时间上的相关性，提高了数据利用率。

2. **目标网络 (Target Network)**：维护一个独立的目标网络 $Q_{\theta^-}$（缓慢更新）以稳定训练：

$$
\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q_{\theta^-}(s', a') - Q_\theta(s, a) \right)^2 \right]
$$

目标网络的更新方式：每隔 $C$ 步硬更新 $\theta^- \leftarrow \theta$，或通过 Polyak 平均进行软更新：$\theta^- \leftarrow \tau\theta + (1-\tau)\theta^-$。

### 已知问题

1. **过估计偏差**：$\max$ 算子倾向于高估 Q 值
2. **仅适用于离散动作**：无法直接处理连续动作空间
3. **样本效率**：尽管使用了回放缓冲区，仍需数百万帧

## Double DQN

**Double DQN** (van Hasselt et al., 2016) 通过将动作选择与动作评估解耦来缓解过估计问题：

$$
y = r + \gamma Q_{\theta^-}(s', \arg\max_{a'} Q_\theta(s', a'))
$$

与 DQN 不同，Double DQN：

- 用**在线网络** $Q_\theta$ **选择**最优下一步动作
- 用**目标网络** $Q_{\theta^-}$ **评估**该动作的价值

这个简单的改动就能显著降低过估计。

## Dueling DQN

**Dueling DQN** (Wang et al., 2016) 修改了网络架构，分别估计状态值和优势：

$$
Q_\theta(s,a) = V_\theta(s) + A_\theta(s,a) - \frac{1}{|\mathcal{A}|} \sum_{a'} A_\theta(s,a')
$$

网络包含共享底层特征后分叉的两个"流"：

- **值流 (Value stream)**：估计 $V(s)$
- **优势流 (Advantage stream)**：估计每个动作的 $A(s,a)$

这种设计的好处在于：在许多状态下，状态本身的价值比各动作之间的差异更为重要。

## 优先经验回放 (PER)

**PER** (Schaul et al., 2016) 根据转移的 TD 误差大小来确定采样优先级：

$$
p_i \propto |\delta_i|^\alpha + \epsilon
$$

其中 $\delta_i$ 是转移 $i$ 的 TD 误差，$\alpha$ 控制优先化程度，$\epsilon$ 是一个小常数。

非均匀采样引入的偏差通过重要性采样权重来修正：

$$
w_i = \left( \frac{1}{N \cdot P(i)} \right)^\beta
$$

## Rainbow DQN

**Rainbow** (Hessel et al., 2018) 将 DQN 的六项改进整合为一个完整的智能体：

| 组件 | 贡献 |
|------|------|
| Double Q-learning | 减少过估计 |
| 优先经验回放 | 聚焦于重要转移 |
| Dueling 架构 | 分离状态值与优势 |
| 多步回报 | 使用 $n$ 步回报降低偏差 |
| 分布式 RL (C51) | 学习回报分布而非仅均值 |
| NoisyNet | 参数空间探索 |

Rainbow 的性能显著优于任何单一组件，证明了这些技术具有互补效应。

## 分布式强化学习

传统方法只估计回报的**期望值** $Q(s,a) = \mathbb{E}[G_t]$，而分布式 RL 学习回报的**完整分布**。

**C51** (Bellemare et al., 2017)：用 $N=51$ 个固定支撑点上的类别分布来表示回报分布：

$$
Z_\theta(s,a) = \{z_i, p_i(s,a)\}_{i=1}^{N}
$$

**QR-DQN** (Dabney et al., 2018)：利用分位数回归来学习一组分位数值。

**IQN** (Dabney et al., 2018)：从均匀分布中采样分位数比例，能隐式表示任意回报分布。

分布式 RL 的优势：

- 更稳定的学习（更丰富的梯度信号）
- 更好的实际性能
- 天然支持风险敏感型决策

## 何时使用值函数方法

**适合的场景：**

- 离散动作空间（游戏、导航、组合优化）
- 异策略学习至关重要时（样本效率、离线数据）
- 环境具有丰富的视觉观测（DQN 类架构擅长此类输入）

**不太理想的场景：**

- 连续动作空间（应使用 Actor-Critic 方法）
- 需要随机策略（值函数方法本质上是确定性的）
- 动作空间维度很高

## 关键参考文献

- Watkins, C.J.C.H. & Dayan, P. (1992). "Q-learning." *Machine Learning*.
- Mnih, V., et al. (2015). "Human-level control through deep reinforcement learning." *Nature*.
- van Hasselt, H., Guez, A., Silver, D. (2016). "Deep Reinforcement Learning with Double Q-learning." *AAAI*.
- Wang, Z., et al. (2016). "Dueling Network Architectures for Deep Reinforcement Learning." *ICML*.
- Schaul, T., et al. (2016). "Prioritized Experience Replay." *ICLR*.
- Hessel, M., et al. (2018). "Rainbow: Combining Improvements in Deep Reinforcement Learning." *AAAI*.
- Bellemare, M.G., Dabney, W., Munos, R. (2017). "A Distributional Perspective on Reinforcement Learning." *ICML*.
