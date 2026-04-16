# Value-Based Methods

Value-based methods learn the optimal action-value function $Q^*(s,a)$ and derive the policy from it. These methods are particularly effective for **discrete action spaces** and form the foundation for many practical RL systems.

## Q-Learning

**Q-learning** (Watkins, 1989) is the foundational off-policy value-based algorithm. It learns $Q^*$ using the Bellman optimality equation:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s,a) \right]
$$

Key properties:

- **Off-policy**: uses $\max_{a'}$ regardless of which action was actually taken
- **Tabular**: original form stores Q-values in a table (only for small state spaces)
- **Converges** to $Q^*$ under mild conditions (all state-action pairs visited infinitely often)

## DQN (Deep Q-Network)

**DQN** (Mnih et al., 2013, 2015) scaled Q-learning to high-dimensional state spaces (e.g., Atari pixel inputs) by using neural networks as function approximators.

### Key Innovations

1. **Experience Replay**: Store transitions $(s, a, r, s')$ in a replay buffer $\mathcal{D}$ and sample random minibatches for training. This breaks temporal correlations and improves data efficiency.

2. **Target Network**: Maintain a separate target network $Q_{\theta^-}$ (updated slowly) to stabilize training:

$$
\mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}} \left[ \left( r + \gamma \max_{a'} Q_{\theta^-}(s', a') - Q_\theta(s, a) \right)^2 \right]
$$

The target network is updated periodically: $\theta^- \leftarrow \theta$ every $C$ steps, or via Polyak averaging: $\theta^- \leftarrow \tau\theta + (1-\tau)\theta^-$.

### Known Issues

1. **Overestimation bias**: The $\max$ operator tends to overestimate Q-values
2. **Discrete actions only**: Cannot directly handle continuous action spaces
3. **Sample inefficiency**: Despite replay buffer, still needs millions of frames

## Double DQN

**Double DQN** (van Hasselt et al., 2016) addresses overestimation by decoupling action selection from evaluation:

$$
y = r + \gamma Q_{\theta^-}(s', \arg\max_{a'} Q_\theta(s', a'))
$$

Instead of using the target network for both selecting and evaluating the best next action, Double DQN:

- **Selects** the best action using the online network $Q_\theta$
- **Evaluates** that action using the target network $Q_{\theta^-}$

This simple change significantly reduces overestimation.

## Dueling DQN

**Dueling DQN** (Wang et al., 2016) modifies the network architecture to separately estimate state value and advantage:

$$
Q_\theta(s,a) = V_\theta(s) + A_\theta(s,a) - \frac{1}{|\mathcal{A}|} \sum_{a'} A_\theta(s,a')
$$

The network has two "streams" that share early layers:

- **Value stream**: estimates $V(s)$
- **Advantage stream**: estimates $A(s,a)$ for each action

This is beneficial because in many states, the value of the state matters more than the advantage of specific actions.

## Prioritized Experience Replay

**PER** (Schaul et al., 2016) improves replay by sampling transitions proportional to their TD error:

$$
p_i \propto |\delta_i|^\alpha + \epsilon
$$

where $\delta_i$ is the TD error of transition $i$, $\alpha$ controls the degree of prioritization, and $\epsilon$ is a small constant.

Importance sampling weights correct for the bias introduced by non-uniform sampling:

$$
w_i = \left( \frac{1}{N \cdot P(i)} \right)^\beta
$$

## Rainbow DQN

**Rainbow** (Hessel et al., 2018) combines six extensions of DQN into a single agent:

| Component | Contribution |
|-----------|-------------|
| Double Q-learning | Reduces overestimation |
| Prioritized replay | Focuses on important transitions |
| Dueling architecture | Separates state value and advantage |
| Multi-step returns | Uses $n$-step returns for lower bias |
| Distributional RL (C51) | Learns return distribution, not just mean |
| Noisy Nets | Parameter-space exploration |

Rainbow significantly outperforms any individual component, demonstrating the complementary benefits of these techniques.

## Distributional RL

Instead of estimating the **expected** return $Q(s,a) = \mathbb{E}[G_t]$, distributional RL learns the **full distribution** of returns.

**C51** (Bellemare et al., 2017): Represents the return distribution as a categorical distribution over $N=51$ fixed atoms:

$$
Z_\theta(s,a) = \{z_i, p_i(s,a)\}_{i=1}^{N}
$$

**QR-DQN** (Dabney et al., 2018): Uses quantile regression to learn a set of quantile values.

**IQN** (Dabney et al., 2018): Samples quantile fractions from a uniform distribution, allowing implicit representation of any return distribution.

Distributional RL provides:

- More stable learning (richer gradient signal)
- Better performance in practice
- Natural risk-sensitive decision making

## When to Use Value-Based Methods

**Good fit:**

- Discrete action spaces (games, navigation, combinatorial optimization)
- Off-policy learning is important (sample efficiency, offline data)
- Environment has rich visual observations (DQN-style architectures excel here)

**Not ideal:**

- Continuous action spaces (need actor-critic instead)
- Need stochastic policies (value-based methods are inherently deterministic)
- Very high-dimensional action spaces

## Key References

- Watkins, C.J.C.H. & Dayan, P. (1992). "Q-learning." *Machine Learning*.
- Mnih, V., et al. (2015). "Human-level control through deep reinforcement learning." *Nature*.
- van Hasselt, H., Guez, A., Silver, D. (2016). "Deep Reinforcement Learning with Double Q-learning." *AAAI*.
- Wang, Z., et al. (2016). "Dueling Network Architectures for Deep Reinforcement Learning." *ICML*.
- Schaul, T., et al. (2016). "Prioritized Experience Replay." *ICLR*.
- Hessel, M., et al. (2018). "Rainbow: Combining Improvements in Deep Reinforcement Learning." *AAAI*.
- Bellemare, M.G., Dabney, W., Munos, R. (2017). "A Distributional Perspective on Reinforcement Learning." *ICML*.
