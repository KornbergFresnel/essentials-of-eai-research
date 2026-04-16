# Policy Gradient Methods

This page covers the foundational policy gradient algorithms: **REINFORCE** and **Vanilla Policy Gradient (VPG)**. These are the simplest instantiations of the policy gradient theorem and serve as the basis for more advanced methods like TRPO and PPO.

## REINFORCE

**REINFORCE** (Williams, 1992) is the simplest policy gradient algorithm. It uses Monte Carlo returns to estimate the policy gradient.

### Algorithm

$$
\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t^{(i)} | s_t^{(i)}) \, G_t^{(i)}
$$

where $G_t^{(i)} = \sum_{t'=t}^{T} \gamma^{t'-t} r_{t'}^{(i)}$ is the reward-to-go for trajectory $i$.

!!! note "Pseudocode: REINFORCE"
    ```
    Initialize policy parameters θ
    for iteration = 1, 2, ... do
        Collect N trajectories {τ_i} by running π_θ
        For each trajectory, compute returns G_t
        Estimate gradient: ĝ = (1/N) Σ_i Σ_t ∇_θ log π_θ(a_t|s_t) G_t
        Update: θ ← θ + α ĝ
    end for
    ```

### Properties

- **Unbiased** gradient estimate (uses true Monte Carlo returns)
- **High variance** — each gradient estimate is noisy, requiring many samples
- **On-policy** — data must come from the current policy
- Requires **complete episodes** (not suitable for continuing tasks)

## Vanilla Policy Gradient (VPG)

VPG improves upon REINFORCE by adding a **learned baseline** to reduce variance.

### Algorithm

The key modification: subtract a baseline $b(s_t) \approx V^{\pi}(s_t)$ from the return:

$$
\nabla_\theta J(\theta) \approx \frac{1}{N} \sum_{i=1}^{N} \sum_{t=0}^{T} \nabla_\theta \log \pi_\theta(a_t | s_t) \left( G_t - b(s_t) \right)
$$

In practice, $b(s_t)$ is a neural network $V_\phi(s)$ trained to minimize:

$$
\mathcal{L}(\phi) = \frac{1}{NT} \sum_{i,t} \left( V_\phi(s_t^{(i)}) - G_t^{(i)} \right)^2
$$

!!! note "Pseudocode: Vanilla Policy Gradient"
    ```
    Initialize policy parameters θ, value function parameters φ
    for iteration = 1, 2, ... do
        Collect N trajectories {τ_i} by running π_θ
        Compute returns G_t for all timesteps
        Compute advantages: Â_t = G_t - V_φ(s_t)
        Update policy:  θ ← θ + α · (1/NT) Σ ∇_θ log π_θ(a_t|s_t) Â_t
        Update baseline: φ ← φ - β · ∇_φ Σ (V_φ(s_t) - G_t)²
    end for
    ```

### Advantages Over REINFORCE

- **Lower variance** due to the baseline (same expectation, reduced spread)
- **Faster convergence** in practice
- Still **unbiased** (subtracting a state-dependent baseline doesn't bias the gradient)

## Practical Considerations

### Common Issues

1. **Learning rate sensitivity**: Too large → policy collapse; too small → slow progress. Use adaptive optimizers (Adam) with careful scheduling.

2. **Reward scaling**: Normalize returns or advantages across a batch to stabilize training:
   ```python
   advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
   ```

3. **Entropy bonus**: Add $c \cdot \mathcal{H}(\pi_\theta(\cdot|s))$ to the objective to encourage exploration and prevent premature convergence.

### Implementation Tips

- Use **GAE** ($\lambda = 0.95$--$0.99$) instead of raw Monte Carlo returns for the advantage estimation
- Collect large batches (thousands of timesteps) per update to reduce variance
- Monitor the **entropy** of the policy — if it drops too fast, the policy is collapsing

## Key References

- Williams, R.J. (1992). "Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning." *Machine Learning*.
- Sutton, R.S., McAllester, D., Singh, S., Mansour, Y. (1999). "Policy Gradient Methods for Reinforcement Learning with Function Approximation." *NeurIPS*.
- Schulman, J., Moritz, P., Levine, S., Jordan, M., Abbeel, P. (2016). "High-Dimensional Continuous Control Using Generalized Advantage Estimation." *ICLR*.
