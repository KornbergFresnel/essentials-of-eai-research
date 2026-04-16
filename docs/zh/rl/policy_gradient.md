# 策略梯度方法

本页介绍基础策略梯度算法：**REINFORCE** 和 **Vanilla Policy Gradient (VPG)**。它们是策略梯度定理最直接的实现，也是 TRPO、PPO 等更高级方法的基础。

## REINFORCE

**REINFORCE** (Williams, 1992) 是最简单的策略梯度算法，使用蒙特卡洛回报来估计策略梯度。

### 算法

$$
\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t^{(i)} | s_t^{(i)}) \, G_t^{(i)}
$$

其中 $G_t^{(i)} = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'}^{(i)}$ 是第 $i$ 条轨迹从 $t$ 时刻起的回报。

!!! note "伪代码：REINFORCE"
    ```
    初始化策略参数 θ
    for iteration = 1, 2, ... do
        运行 π_θ 收集 N 条轨迹 {τ_i}
        对每条轨迹计算回报 G_t
        估计梯度：ĝ = (1/N) Σ_i Σ_t ∇_θ log π_θ(a_t|s_t) G_t
        更新：θ ← θ + α ĝ
    end for
    ```

### 性质

- **无偏**的梯度估计（使用真实蒙特卡洛回报）
- **高方差**——每次梯度估计噪声大，需要大量样本
- **同策略**——数据必须来自当前策略
- 需要**完整回合**（不适用于持续任务）

## Vanilla Policy Gradient (VPG)

VPG 在 REINFORCE 基础上加入了**学习型基线**，以降低方差。

### 算法

核心改进：从回报中减去基线 $b(s_t) \approx V^{\pi}(s_t)$：

$$
\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t | s_t) \left( G_t - b(s_t) \right)
$$

实践中，$b(s_t)$ 用一个神经网络 $V_\phi(s)$ 来近似，通过最小化以下损失训练：

$$
\mathcal{L}(\phi) = \frac{1}{NT} \sum_{i,t} \left( V_\phi(s_t^{(i)}) - G_t^{(i)} \right)^2
$$

!!! note "伪代码：Vanilla Policy Gradient"
    ```
    初始化策略参数 θ、值函数参数 φ
    for iteration = 1, 2, ... do
        运行 π_θ 收集 N 条轨迹 {τ_i}
        计算所有时间步的回报 G_t
        计算优势：Â_t = G_t - V_φ(s_t)
        更新策略：θ ← θ + α · (1/NT) Σ ∇_θ log π_θ(a_t|s_t) Â_t
        更新基线：φ ← φ - β · ∇_φ Σ (V_φ(s_t) - G_t)²
    end for
    ```

### 相对 REINFORCE 的优势

- **更低方差**——基线降低了方差但不影响期望值
- 实践中**更快收敛**
- 仍然是**无偏**的（减去与状态相关的基线不会引入偏差）

## 实践注意事项

### 常见问题

1. **学习率敏感性**：过大会导致策略崩溃，过小则进展缓慢。建议使用自适应优化器（Adam）并配合学习率调度。

2. **奖励缩放**：对批次内的回报或优势进行标准化可稳定训练：
   ```python
   advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
   ```

3. **熵正则**：在目标中加入 $c \cdot \mathcal{H}(\pi_\theta(\cdot|s))$ 鼓励探索，防止策略过早收敛。

### 实现建议

- 使用 **GAE**（$\lambda = 0.95$--$0.99$）代替原始蒙特卡洛回报来估计优势
- 每次更新收集大批量数据（数千个时间步）以降低方差
- 监测策略的**熵值**——如果下降过快，说明策略正在崩溃

## 关键参考文献

- Williams, R.J. (1992). "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning." *Machine Learning*.
- Sutton, R.S., McAllester, D., Singh, S., Mansour, Y. (1999). "Policy Gradient Methods for Reinforcement Learning with Function Approximation." *NeurIPS*.
- Schulman, J., Moritz, P., Levine, S., Jordan, M., Abbeel, P. (2016). "High-Dimensional Continuous Control Using Generalized Advantage Estimation." *ICLR*.
