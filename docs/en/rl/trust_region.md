# Trust Region Methods: TRPO and PPO

Vanilla policy gradient methods suffer from a critical problem: a bad gradient step can catastrophically degrade the policy, and there's no easy way to recover. **Trust region methods** address this by constraining how much the policy can change in a single update, leading to dramatically more stable training.

## The Problem: Policy Collapse

In standard policy gradient, the update $\theta \leftarrow \theta + \alpha \hat{g}$ has no guarantee about how much the policy actually changes. A seemingly small parameter update can cause a large change in the action distribution, leading to:

1. Collecting bad data with the degraded policy
2. Further degrading the policy from that bad data
3. Irreversible collapse

## Monotonic Improvement Theory

Kakade & Langford (2002) showed that policy improvement can be guaranteed if we control the KL divergence between consecutive policies. Specifically:

$$
J(\pi') \geq J(\pi) + \mathbb{E}_{s \sim d^{\pi}} \left[ \mathbb{E}_{a \sim \pi'} \left[ A^{\pi}(s,a) \right] \right] - C \cdot D_{\text{KL}}^{\max}(\pi \| \pi')
$$

This motivates constraining or penalizing the KL divergence during optimization.

## TRPO (Trust Region Policy Optimization)

**TRPO** (Schulman et al., 2015) formalizes the trust region idea as a constrained optimization problem.

### Objective

Maximize the surrogate objective subject to a KL constraint:

$$
\max_\theta \quad \mathbb{E}_{s,a \sim \pi_{\theta_{\text{old}}}} \left[ \frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} \hat{A}(s,a) \right]
$$

$$
\text{s.t.} \quad \mathbb{E}_s \left[ D_{\text{KL}}(\pi_{\theta_{\text{old}}}(\cdot|s) \| \pi_\theta(\cdot|s)) \right] \leq \delta
$$

where $\delta$ is the trust region radius (typically $\delta = 0.01$).

### Solution Method

TRPO uses a second-order approximation:

1. Compute the policy gradient $g = \nabla_\theta L(\theta)\big|_{\theta_\text{old}}$
2. Compute the Fisher information matrix $F = \nabla_\theta^2 D_{\text{KL}}\big|_{\theta_\text{old}}$
3. Compute the natural gradient direction: $\hat{s} = F^{-1}g$
4. Line search with step size $\beta = \sqrt{2\delta / (g^T F^{-1} g)}$
5. Update: $\theta \leftarrow \theta_{\text{old}} + \beta \hat{s}$

In practice, $F^{-1}g$ is computed using the **conjugate gradient** method (avoiding explicit matrix inversion).

### Properties

- **Guaranteed monotonic improvement** (under certain assumptions)
- **Stable training** — no catastrophic policy collapse
- **Expensive**: requires conjugate gradient solver and line search
- Typical trust region: $\delta \in [0.001, 0.05]$

## PPO (Proximal Policy Optimization)

**PPO** (Schulman et al., 2017) achieves similar stability to TRPO but with a much simpler implementation using only first-order optimization.

### PPO-Clip

The key idea: instead of a hard KL constraint, clip the importance sampling ratio to prevent large policy changes:

$$
L^{\text{CLIP}}(\theta) = \mathbb{E}_t \left[ \min\left( r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t \right) \right]
$$

where $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_\text{old}}(a_t|s_t)}$ is the probability ratio, and $\epsilon$ is the clip range (typically 0.1--0.2).

**Intuition**: The clipping prevents the ratio from moving too far from 1 in either direction, effectively creating a trust region without second-order optimization.

How the clipping works:

| Advantage $\hat{A}_t$ | Ratio $r_t$ | Effect |
|----------|-------|--------|
| $\hat{A}_t > 0$ (good action) | $r_t > 1+\epsilon$ | Clipped — don't over-exploit |
| $\hat{A}_t > 0$ (good action) | $r_t < 1+\epsilon$ | Not clipped — encourage this action |
| $\hat{A}_t < 0$ (bad action) | $r_t < 1-\epsilon$ | Clipped — already moved away enough |
| $\hat{A}_t < 0$ (bad action) | $r_t > 1-\epsilon$ | Not clipped — discourage this action |

### Full PPO Objective

In practice, PPO optimizes a combined objective:

$$
L(\theta) = L^{\text{CLIP}}(\theta) - c_1 L^{\text{VF}}(\theta) + c_2 \mathcal{H}(\pi_\theta)
$$

- $L^{\text{VF}}$: Value function loss (MSE between $V_\phi(s)$ and returns)
- $\mathcal{H}$: Entropy bonus for exploration
- $c_1 \approx 0.5$, $c_2 \approx 0.01$ (typical)

!!! note "Pseudocode: PPO-Clip"
    ```
    Initialize policy θ, value function φ
    for iteration = 1, 2, ... do
        Collect T timesteps with current policy π_θ
        Compute advantages Â_t using GAE(γ, λ)
        for epoch = 1, ..., K do          // K = 3-10 epochs per iteration
            for minibatch in random_split(data) do
                Compute ratio r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t)
                L_clip = min(r_t Â_t, clip(r_t, 1-ε, 1+ε) Â_t)
                L_vf = (V_φ(s_t) - G_t)²
                L = -L_clip + c1·L_vf - c2·H(π_θ)
                Update θ, φ with gradient descent on L
            end for
        end for
        θ_old ← θ
    end for
    ```

### Why PPO is So Popular

1. **Simple implementation** — no conjugate gradient, no line search
2. **Stable** — clipping provides soft trust region guarantees
3. **General** — works for discrete and continuous action spaces
4. **Scalable** — easily parallelized (see [Distributed RL](../distributed_rl/index.md))
5. **Robust** — relatively insensitive to hyperparameters

PPO is the **default choice** for many applications: robotics (locomotion, manipulation), game AI (Dota 2, StarCraft), RLHF for language models, and more.

### Key Hyperparameters

| Parameter | Typical Range | Notes |
|-----------|--------------|-------|
| Clip range $\epsilon$ | 0.1 -- 0.3 | 0.2 is a common default |
| GAE $\lambda$ | 0.9 -- 0.99 | 0.95 is typical |
| Discount $\gamma$ | 0.99 -- 0.999 | Task-dependent |
| Epochs $K$ | 3 -- 10 | More epochs → risk of overfitting to batch |
| Minibatch size | 32 -- 4096 | Larger for more complex tasks |
| Learning rate | 1e-4 -- 3e-4 | Often linearly annealed |
| Entropy coeff $c_2$ | 0.0 -- 0.01 | Higher for exploration-heavy tasks |

## TRPO vs. PPO

| Aspect | TRPO | PPO |
|--------|------|-----|
| Constraint | Hard KL constraint | Soft (clipping) |
| Optimization | 2nd order (conjugate gradient) | 1st order (Adam) |
| Implementation | Complex | Simple |
| Performance | Slightly more principled | Comparable or better in practice |
| Scalability | Harder to distribute | Easy to distribute |
| Usage | Research, theory | Industry standard |

## Key References

- Kakade, S. & Langford, J. (2002). "Approximately Optimal Approximate Reinforcement Learning." *ICML*.
- Schulman, J., Levine, S., Abbeel, P., Jordan, M., Moritz, P. (2015). "Trust Region Policy Optimization." *ICML*.
- Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. (2017). "Proximal Policy Optimization Algorithms." *arXiv:1707.06347*.
