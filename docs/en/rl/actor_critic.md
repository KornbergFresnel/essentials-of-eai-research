# Actor-Critic Methods

Actor-Critic methods combine the best of policy-based and value-based approaches. The **actor** (policy) decides what to do, while the **critic** (value function) evaluates how good the actions are. This section covers the major actor-critic algorithms: A2C/A3C, DDPG, TD3, and SAC.

## A2C and A3C

### A2C (Advantage Actor-Critic)

A2C is a synchronous actor-critic algorithm. Multiple parallel workers collect experience, and updates are applied synchronously.

**Actor update** (policy gradient with advantage):

$$
\nabla_\theta J \approx \frac{1}{N} \sum_{i} \sum_t \nabla_\theta \log \pi_\theta(a_t^{(i)}|s_t^{(i)}) \hat{A}_t^{(i)}
$$

**Critic update** (value function regression):

$$
\mathcal{L}(\phi) = \frac{1}{N} \sum_i \sum_t \left( V_\phi(s_t^{(i)}) - G_t^{(i)} \right)^2
$$

### A3C (Asynchronous Advantage Actor-Critic)

**A3C** (Mnih et al., 2016) was the first major actor-critic method for deep RL. Key idea: multiple workers asynchronously interact with separate environment copies and update a shared global network.

- Each worker computes gradients locally
- Gradients are applied asynchronously to the global parameters
- No replay buffer needed (on-policy, but diverse data from parallel workers)

!!! info "A2C vs. A3C"
    A2C (synchronous) typically matches A3C (asynchronous) in performance and is simpler to implement and debug. A2C is generally preferred today.

## DDPG (Deep Deterministic Policy Gradient)

**DDPG** (Lillicrap et al., 2016) extends DQN to **continuous action spaces** using a deterministic policy.

### Key Components

1. **Deterministic actor**: $\mu_\theta(s)$ outputs a continuous action directly
2. **Critic**: $Q_\phi(s,a)$ estimates the action-value
3. **Replay buffer**: off-policy learning from stored transitions
4. **Target networks**: $\mu_{\theta^-}$, $Q_{\phi^-}$ for stable targets

### Updates

**Critic** — minimize TD error:

$$
\mathcal{L}(\phi) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}} \left[ \left( Q_\phi(s,a) - y \right)^2 \right]
$$

where $y = r + \gamma Q_{\phi^-}(s', \mu_{\theta^-}(s'))$.

**Actor** — maximize Q via the deterministic policy gradient:

$$
\nabla_\theta J \approx \mathbb{E}_{s \sim \mathcal{D}} \left[ \nabla_a Q_\phi(s,a)\big|_{a=\mu_\theta(s)} \cdot \nabla_\theta \mu_\theta(s) \right]
$$

**Exploration**: Add noise to actions during data collection: $a = \mu_\theta(s) + \epsilon$, where $\epsilon \sim \mathcal{N}(0, \sigma)$ or Ornstein-Uhlenbeck process.

### Known Issues

- **Overestimation** of Q-values (same issue as DQN)
- **Brittle**: sensitive to hyperparameters
- **Exploration**: relies on simple noise, which can be insufficient

## TD3 (Twin Delayed DDPG)

**TD3** (Fujimoto et al., 2018) addresses DDPG's instabilities with three key modifications:

### 1. Twin Critics (Clipped Double Q-Learning)

Use **two** Q-networks and take the minimum for the target:

$$
y = r + \gamma \min_{j=1,2} Q_{\phi_j^-}(s', \tilde{a}')
$$

This reduces overestimation bias.

### 2. Target Policy Smoothing

Add clipped noise to the target action:

$$
\tilde{a}' = \text{clip}(\mu_{\theta^-}(s') + \text{clip}(\epsilon, -c, c), a_{\text{low}}, a_{\text{high}})
$$

where $\epsilon \sim \mathcal{N}(0, \sigma)$. This regularizes the value function by smoothing the target.

### 3. Delayed Policy Updates

Update the actor (and target networks) less frequently than the critic — typically once every 2 critic updates. This allows the critic to become more accurate before the actor changes.

TD3 is significantly more stable than DDPG and is a strong baseline for continuous control.

## SAC (Soft Actor-Critic)

**SAC** (Haarnoja et al., 2018) is the state-of-the-art off-policy actor-critic algorithm. It introduces the **maximum entropy** framework, which simultaneously maximizes expected return and policy entropy.

### Maximum Entropy Objective

$$
J(\pi) = \sum_t \mathbb{E}_{(s_t,a_t) \sim \rho_\pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot|s_t)) \right]
$$

where $\alpha$ is the temperature parameter controlling the entropy-reward trade-off.

**Why entropy?**

- **Exploration**: high-entropy policies explore more effectively
- **Robustness**: the agent learns multiple near-optimal strategies
- **Composability**: entropy-regularized policies are easier to compose and fine-tune

### Soft Bellman Equation

$$
Q^{\pi}(s,a) = r(s,a) + \gamma \mathbb{E}_{s'} \left[ V^{\pi}(s') \right]
$$

$$
V^{\pi}(s) = \mathbb{E}_{a \sim \pi} \left[ Q^{\pi}(s,a) - \alpha \log \pi(a|s) \right]
$$

### SAC Components

1. **Stochastic actor**: $\pi_\theta(a|s)$ — typically a squashed Gaussian
   - $a = \tanh(\mu_\theta(s) + \sigma_\theta(s) \cdot \epsilon)$, $\epsilon \sim \mathcal{N}(0, I)$

2. **Twin critics**: $Q_{\phi_1}(s,a)$, $Q_{\phi_2}(s,a)$ (like TD3)

3. **Automatic temperature tuning**: $\alpha$ is learned to maintain a target entropy:
   $$
   \mathcal{L}(\alpha) = \mathbb{E}_{a \sim \pi} \left[ -\alpha (\log \pi(a|s) + \bar{\mathcal{H}}) \right]
   $$
   where $\bar{\mathcal{H}}$ is the target entropy (typically $-\dim(\mathcal{A})$).

### Key Properties

- **Off-policy** — uses replay buffer, high sample efficiency
- **Stochastic policy** — natural exploration, no need for external noise
- **Stable training** — entropy regularization prevents premature convergence
- **Automatic temperature** — one less hyperparameter to tune
- **State-of-the-art** on many continuous control benchmarks

## Comparison

| | A2C | DDPG | TD3 | SAC |
|---|---|---|---|---|
| On/Off-Policy | On | Off | Off | Off |
| Policy Type | Stochastic | Deterministic | Deterministic | Stochastic |
| Action Space | Both | Continuous | Continuous | Continuous |
| Exploration | Entropy bonus | External noise | External noise | Inherent (entropy) |
| Critics | 1 | 1 | 2 (twin) | 2 (twin) |
| Typical Use | Simple tasks | Legacy | Strong baseline | State-of-the-art |

## Key References

- Mnih, V., et al. (2016). "Asynchronous Methods for Deep Reinforcement Learning." *ICML*.
- Lillicrap, T.P., et al. (2016). "Continuous control with deep reinforcement learning." *ICLR*.
- Fujimoto, S., van Hoof, H., Megerey, D. (2018). "Addressing Function Approximation Error in Actor-Critic Methods." *ICML*.
- Haarnoja, T., et al. (2018). "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor." *ICML*.
- Haarnoja, T., et al. (2018). "Soft Actor-Critic Algorithms and Applications." *arXiv:1812.05905*.
