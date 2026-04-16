# 信赖域方法：TRPO 与 PPO

朴素策略梯度方法存在一个严重问题：一次不好的梯度步可能导致策略灾难性退化，且很难恢复。**信赖域方法**通过约束每次更新中策略变化的幅度，显著提升了训练稳定性。

## 问题：策略崩溃

在标准策略梯度中，更新 $\theta \leftarrow \theta + \alpha \hat{g}$ 无法保证策略实际变化的大小。一个看似微小的参数更新可能导致动作分布的剧烈变化，引发：

1. 退化后的策略采集到质量很差的数据
2. 差数据进一步恶化策略
3. 不可逆的崩溃

## 单调改进理论

Kakade & Langford (2002) 证明了：只要控制相邻策略之间的 KL 散度，就能保证策略的单调改进：

$$
J(\pi') \geq J(\pi) + \mathbb{E}_{s \sim d^{\pi}} \left[ \mathbb{E}_{a \sim \pi'} \left[ A^{\pi}(s,a) \right] \right] - C \cdot D_{\text{KL}}^{\max}(\pi \| \pi')
$$

这为在优化过程中约束或惩罚 KL 散度提供了理论动机。

## TRPO（信赖域策略优化）

**TRPO** (Schulman et al., 2015) 将信赖域思想形式化为一个约束优化问题。

### 目标函数

在 KL 约束下最大化代理目标：

$$
\max_\theta \quad \mathbb{E}_{s,a \sim \pi_{\theta_{\text{old}}}} \left[ \frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} \hat{A}(s,a) \right]
$$

$$
\text{s.t.} \quad \mathbb{E}_s \left[ D_{\text{KL}}(\pi_{\theta_{\text{old}}}(\cdot|s) \| \pi_\theta(\cdot|s)) \right] \leq \delta
$$

其中 $\delta$ 为信赖域半径（通常取 $\delta = 0.01$）。

### 求解方法

TRPO 使用二阶近似来求解：

1. 计算策略梯度 $g = \nabla_\theta L(\theta)\big|_{\theta_\text{old}}$
2. 计算费舍尔信息矩阵 $F = \nabla_\theta^2 D_{\text{KL}}\big|_{\theta_\text{old}}$
3. 计算自然梯度方向：$\hat{s} = F^{-1}g$
4. 通过线搜索确定步长 $\beta = \sqrt{2\delta / (g^T F^{-1} g)}$
5. 更新：$\theta \leftarrow \theta_{\text{old}} + \beta \hat{s}$

实践中，$F^{-1}g$ 通过**共轭梯度法**计算（避免显式矩阵求逆）。

### 性质

- **保证单调改进**（在一定假设下）
- **训练稳定**——不会出现灾难性策略崩溃
- **计算昂贵**：需要共轭梯度求解器和线搜索
- 典型信赖域半径：$\delta \in [0.001, 0.05]$

## PPO（近端策略优化）

**PPO** (Schulman et al., 2017) 实现了与 TRPO 类似的稳定性，但只使用一阶优化，实现简单得多。

### PPO-Clip

核心思想：不使用硬 KL 约束，而是通过截断重要性采样比率来防止策略的大幅变化：

$$
L^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min\left( r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
$$

其中 $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_\text{old}}(a_t|s_t)}$ 是概率比，$\epsilon$ 是截断范围（通常取 0.1--0.2）。

**直觉**：截断操作阻止比率偏离 1 太远，从而在不需要二阶优化的情况下有效地创建了信赖域。

截断机制的工作方式：

| 优势 $\hat{A}_t$ | 比率 $r_t$ | 效果 |
|----------|-------|--------|
| $\hat{A}_t > 0$（好动作） | $r_t > 1+\epsilon$ | 截断——不过度利用 |
| $\hat{A}_t > 0$（好动作） | $r_t < 1+\epsilon$ | 未截断——鼓励该动作 |
| $\hat{A}_t < 0$（差动作） | $r_t < 1-\epsilon$ | 截断——已经远离够了 |
| $\hat{A}_t < 0$（差动作） | $r_t > 1-\epsilon$ | 未截断——继续抑制该动作 |

### PPO 完整目标

实践中 PPO 优化一个组合目标：

$$
L(\theta) = L^{\text{CLIP}}(\theta) - c_1 L^{\text{VF}}(\theta) + c_2 \mathcal{H}(\pi_\theta)
$$

- $L^{\text{VF}}$：值函数损失（$V_\phi(s)$ 与回报之间的 MSE）
- $\mathcal{H}$：熵正则项，鼓励探索
- $c_1 \approx 0.5$，$c_2 \approx 0.01$（典型值）

!!! note "伪代码：PPO-Clip"
    ```
    初始化策略 θ、值函数 φ
    for iteration = 1, 2, ... do
        用当前策略 π_θ 收集 T 个时间步的数据
        使用 GAE(γ, λ) 计算优势 Â_t
        for epoch = 1, ..., K do              // 每次迭代 K=3-10 个 epoch
            for minibatch in random_split(data) do
                计算比率 r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t)
                L_clip = min(r_t Â_t, clip(r_t, 1-ε, 1+ε) Â_t)
                L_vf = (V_φ(s_t) - G_t)²
                L = -L_clip + c1·L_vf - c2·H(π_θ)
                用梯度下降更新 θ, φ
            end for
        end for
        θ_old ← θ
    end for
    ```

### PPO 为何如此流行

1. **实现简单**——无需共轭梯度，无需线搜索
2. **训练稳定**——截断机制提供软信赖域保证
3. **通用性强**——同时适用于离散和连续动作空间
4. **易于扩展**——方便并行化（参见[分布式 RL](../distributed_rl/index.md)）
5. **鲁棒性好**——对超参数相对不敏感

PPO 是许多应用场景的**默认选择**：机器人（运动控制、操作）、游戏 AI（Dota 2、StarCraft）、大语言模型的 RLHF 等。

### 关键超参数

| 参数 | 典型范围 | 备注 |
|------|---------|------|
| 截断范围 $\epsilon$ | 0.1 -- 0.3 | 0.2 是常用默认值 |
| GAE $\lambda$ | 0.9 -- 0.99 | 0.95 最常用 |
| 折扣因子 $\gamma$ | 0.99 -- 0.999 | 取决于具体任务 |
| Epoch 数 $K$ | 3 -- 10 | 过多则有过拟合到当前批次的风险 |
| 小批量大小 | 32 -- 4096 | 任务越复杂通常越大 |
| 学习率 | 1e-4 -- 3e-4 | 通常线性衰减 |
| 熵系数 $c_2$ | 0.0 -- 0.01 | 探索需求大的任务取较高值 |

## TRPO 与 PPO 对比

| 方面 | TRPO | PPO |
|------|------|-----|
| 约束方式 | 硬 KL 约束 | 软约束（截断） |
| 优化方式 | 二阶（共轭梯度） | 一阶（Adam） |
| 实现复杂度 | 高 | 低 |
| 性能 | 理论更严格 | 实践中相当或更优 |
| 可扩展性 | 难以分布式部署 | 易于分布式部署 |
| 使用场景 | 研究、理论分析 | 工业标准 |

## 关键参考文献

- Kakade, S. & Langford, J. (2002). "Approximately Optimal Approximate Reinforcement Learning." *ICML*.
- Schulman, J., Levine, S., Abbeel, P., Jordan, M., Moritz, P. (2015). "Trust Region Policy Optimization." *ICML*.
- Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. (2017). "Proximal Policy Optimization Algorithms." *arXiv:1707.06347*.
