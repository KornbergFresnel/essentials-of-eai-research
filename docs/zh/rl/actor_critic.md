# Actor-Critic 方法

Actor-Critic 方法融合了策略方法和值函数方法的优势。**Actor**（策略）决定执行什么动作，**Critic**（值函数）评估动作的好坏。本节介绍主要的 Actor-Critic 算法：A2C/A3C、DDPG、TD3 和 SAC。

## A2C 与 A3C

### A2C（优势 Actor-Critic）

A2C 是一种同步 Actor-Critic 算法。多个并行工作器采集经验数据，然后同步地进行参数更新。

**Actor 更新**（使用优势函数的策略梯度）：

$$
\nabla_\theta J \approx \frac{1}{N} \sum_{i} \sum_t \nabla_\theta \log \pi_\theta(a_t^{(i)}|s_t^{(i)}) \hat{A}_t^{(i)}
$$

**Critic 更新**（值函数回归）：

$$
\mathcal{L}(\phi) = \frac{1}{N} \sum_i \sum_t \left( V_\phi(s_t^{(i)}) - G_t^{(i)} \right)^2
$$

### A3C（异步优势 Actor-Critic）

**A3C** (Mnih et al., 2016) 是深度 RL 中第一个重要的 Actor-Critic 方法。核心思想：多个工作器异步地与各自独立的环境副本交互，并更新共享的全局网络。

- 每个工作器在本地计算梯度
- 梯度异步地应用于全局参数
- 无需经验回放缓冲区（同策略，但并行采集带来了数据多样性）

!!! info "A2C vs. A3C"
    A2C（同步版）在性能上通常与 A3C（异步版）持平，且更易于实现和调试。当前实践中一般优先选择 A2C。

## DDPG（深度确定性策略梯度）

**DDPG** (Lillicrap et al., 2016) 将 DQN 的思想扩展到**连续动作空间**，使用确定性策略。

### 核心组件

1. **确定性 Actor**：$\mu_\theta(s)$ 直接输出连续动作值
2. **Critic**：$Q_\phi(s,a)$ 估计动作值函数
3. **经验回放缓冲区**：支持异策略学习
4. **目标网络**：$\mu_{\theta^-}$、$Q_{\phi^-}$，用于稳定训练目标

### 更新规则

**Critic** —— 最小化 TD 误差：

$$
\mathcal{L}(\phi) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}} \left[ \left( Q_\phi(s,a) - y \right)^2 \right]
$$

其中 $y = r + \gamma Q_{\phi^-}(s', \mu_{\theta^-}(s'))$。

**Actor** —— 通过确定性策略梯度最大化 Q：

$$
\nabla_\theta J \approx \mathbb{E}_{s \sim \mathcal{D}} \left[ \nabla_a Q_\phi(s,a)\big|_{a=\mu_\theta(s)} \cdot \nabla_\theta \mu_\theta(s) \right]
$$

**探索**：在数据采集时对动作添加噪声：$a = \mu_\theta(s) + \epsilon$，其中 $\epsilon \sim \mathcal{N}(0, \sigma)$ 或 Ornstein-Uhlenbeck 过程。

### 已知问题

- Q 值**过估计**（与 DQN 相同的问题）
- **脆弱**：对超参数敏感
- **探索不足**：依赖简单噪声，在复杂环境中可能不够

## TD3（双延迟 DDPG）

**TD3** (Fujimoto et al., 2018) 针对 DDPG 的不稳定性提出了三项关键改进：

### 1. 双 Critic（截断双 Q 学习）

使用**两个** Q 网络，取较小值作为目标：

$$
y = r + \gamma \min_{j=1,2} Q_{\phi_j^-}(s', \tilde{a}')
$$

这有效降低了过估计偏差。

### 2. 目标策略平滑

对目标动作添加截断噪声：

$$
\tilde{a}' = \text{clip}(\mu_{\theta^-}(s') + \text{clip}(\epsilon, -c, c), a_{\text{low}}, a_{\text{high}})
$$

其中 $\epsilon \sim \mathcal{N}(0, \sigma)$。通过平滑目标来正则化值函数。

### 3. 延迟策略更新

Actor（及目标网络）的更新频率低于 Critic——通常每 2 次 Critic 更新才更新一次 Actor。这使得 Critic 在 Actor 变化之前变得更加准确。

TD3 比 DDPG 稳定得多，是连续控制任务的强基线。

## SAC（软 Actor-Critic）

**SAC** (Haarnoja et al., 2018) 是当前最先进的异策略 Actor-Critic 算法。它引入了**最大熵**框架，同时最大化期望回报和策略熵。

### 最大熵目标

$$
J(\pi) = \sum_t \mathbb{E}_{(s_t,a_t) \sim \rho_\pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot|s_t)) \right]
$$

其中 $\alpha$ 是温度参数，控制熵与奖励之间的权衡。

**为什么要引入熵？**

- **促进探索**：高熵策略探索更充分
- **鲁棒性**：智能体学习多种接近最优的策略
- **可组合性**：熵正则化的策略更易于组合和微调

### 软贝尔曼方程

$$
Q^{\pi}(s,a) = r(s,a) + \gamma \mathbb{E}_{s'} \left[ V^{\pi}(s') \right]
$$

$$
V^{\pi}(s) = \mathbb{E}_{a \sim \pi} \left[ Q^{\pi}(s,a) - \alpha \log \pi(a|s) \right]
$$

### SAC 的组件

1. **随机 Actor**：$\pi_\theta(a|s)$ —— 通常使用压缩高斯分布 (Squashed Gaussian)
   - $a = \tanh(\mu_\theta(s) + \sigma_\theta(s) \cdot \epsilon)$，$\epsilon \sim \mathcal{N}(0, I)$

2. **双 Critic**：$Q_{\phi_1}(s,a)$、$Q_{\phi_2}(s,a)$（与 TD3 相同）

3. **自动温度调节**：$\alpha$ 通过学习来维持目标熵：
   $$
   \mathcal{L}(\alpha) = \mathbb{E}_{a \sim \pi} \left[ -\alpha (\log \pi(a|s) + \bar{\mathcal{H}}) \right]
   $$
   其中 $\bar{\mathcal{H}}$ 是目标熵（通常取 $-\dim(\mathcal{A})$）。

### 关键特性

- **异策略**——使用经验回放，样本效率高
- **随机策略**——自然探索，无需额外噪声
- **训练稳定**——熵正则化防止过早收敛
- **自动温度**——减少一个需要手动调节的超参数
- 在多个连续控制基准上达到**最优水平**

## 对比总结

| | A2C | DDPG | TD3 | SAC |
|---|---|---|---|---|
| 同/异策略 | 同策略 | 异策略 | 异策略 | 异策略 |
| 策略类型 | 随机 | 确定性 | 确定性 | 随机 |
| 动作空间 | 两者 | 连续 | 连续 | 连续 |
| 探索方式 | 熵正则 | 外部噪声 | 外部噪声 | 内生（熵） |
| Critic 数量 | 1 | 1 | 2（双） | 2（双） |
| 典型用途 | 简单任务 | 历史方法 | 强基线 | 当前最优 |

## 关键参考文献

- Mnih, V., et al. (2016). "Asynchronous Methods for Deep Reinforcement Learning." *ICML*.
- Lillicrap, T.P., et al. (2016). "Continuous control with deep reinforcement learning." *ICLR*.
- Fujimoto, S., van Hoof, H., Megerey, D. (2018). "Addressing Function Approximation Error in Actor-Critic Methods." *ICML*.
- Haarnoja, T., et al. (2018). "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor." *ICML*.
- Haarnoja, T., et al. (2018). "Soft Actor-Critic Algorithms and Applications." *arXiv:1812.05905*.
