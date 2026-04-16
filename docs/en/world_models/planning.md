# Planning with World Models

Given a learned world model, how do we use it for decision-making? This page covers planning algorithms that leverage world models — from simple shooting methods to sophisticated tree search and imagination-based policy learning.

## The Planning Problem

Given a world model $f_\theta$ (transition dynamics) and a reward model $r_\theta$, find an action sequence that maximizes expected cumulative reward:

$$
a_{t:t+H-1}^* = \arg\max_{a_{t:t+H-1}} \sum_{k=0}^{H-1} \gamma^k \hat{r}_{t+k}
$$

where $\hat{s}_{t+k+1} = f_\theta(\hat{s}_{t+k}, a_{t+k})$ and $\hat{r}_{t+k} = r_\theta(\hat{s}_{t+k}, a_{t+k})$.

## Random Shooting

The simplest approach: sample many random action sequences and pick the best one.

1. Sample $N$ action sequences: $\{a_{t:t+H-1}^{(i)}\}_{i=1}^{N}$
2. Roll out each through the model to get predicted returns
3. Execute the first action of the best sequence

**Pros**: Simple, parallelizable
**Cons**: Inefficient in high-dimensional action spaces, scales poorly with horizon

## Cross-Entropy Method (CEM)

**CEM** iteratively refines the action distribution:

!!! note "Pseudocode: CEM Planning"
    ```
    Initialize action distribution: μ, σ (e.g., uniform)
    for iteration = 1, ..., I do
        Sample N action sequences from N(μ, σ²)
        Roll out each through the model, compute returns
        Select top-K sequences (elites)
        Update μ, σ to fit the elite set
    end for
    Return μ (or the best elite sequence)
    ```

CEM is widely used in model-based RL (e.g., PlaNet, PETS) due to its simplicity and effectiveness.

**Key parameters**:

- Population size $N$ (typically 500-1000)
- Elite fraction (typically top 10%)
- Number of iterations $I$ (typically 5-10)
- Planning horizon $H$ (typically 5-30 steps)

## Model Predictive Control (MPC)

MPC is a **receding horizon** approach:

1. At each real timestep, plan $H$ steps ahead using the model
2. Execute only the **first action** of the planned sequence
3. Re-plan at the next timestep with updated state

```mermaid
graph LR
    S[Current State] --> P[Plan H steps]
    P --> E[Execute first action]
    E --> O[Observe new state]
    O --> S
```

MPC naturally handles model errors by constantly re-planning from the true state.

**Used by**: PETS (Chua et al., 2018), PlaNet (Hafner et al., 2019)

### PETS (Probabilistic Ensemble Trajectory Sampling)

**PETS** combines ensemble models with CEM planning:

1. Train an ensemble of $B$ dynamics models
2. For each CEM sample, use **trajectory sampling** — randomly switch between ensemble members at each timestep
3. This propagates both aleatoric (environment) and epistemic (model) uncertainty through the plan

## Monte Carlo Tree Search (MCTS)

MCTS builds a search tree by balancing exploration and exploitation:

1. **Selection**: Traverse tree using UCT (Upper Confidence bound for Trees)
2. **Expansion**: Add a new node
3. **Simulation**: Roll out a policy from the new node
4. **Backpropagation**: Update value estimates up the tree

### MCTS with Learned Models

**AlphaZero** (Silver et al., 2018): MCTS with a neural network providing:

- Prior policy $p(a|s)$ for guiding search
- Value estimate $v(s)$ for evaluating leaf nodes

**MuZero** (Schrittwieser et al., 2020): MCTS with a **fully learned** model:

- No access to true environment rules
- Learned dynamics model for tree expansion
- Achieved superhuman performance in Go, chess, shogi, and Atari

### MCTS vs. Shooting Methods

| Aspect | Shooting / CEM | MCTS |
|--------|---------------|------|
| Action space | Continuous (natural) | Discrete (natural) |
| Planning depth | Moderate (5-30) | Deep (hundreds) |
| Computation | Moderate | High |
| Best for | Continuous control | Games, structured problems |

## Imagination-Based Policy Learning

Instead of planning online (at every timestep), learn a policy by training on **imagined rollouts** from the model. This amortizes the planning cost into the policy network.

### Dreamer's Approach

Dreamer (Hafner et al., 2020) trains actor-critic networks purely in imagination:

1. **World model** generates imagined trajectories in latent space:
   $z_{t+1} = \text{dyn}_\theta(z_t, a_t)$

2. **Critic** estimates values along imagined trajectories:
   $V_\psi(z_t) \approx \mathbb{E}\left[\sum_{k=0}^{H} \gamma^k r_{t+k}\right]$

3. **Actor** is updated to maximize imagined returns:
   $\max_\phi \mathbb{E}\left[\sum_{k=0}^{H} \gamma^k \left(r_{t+k} + \eta \mathcal{H}(\pi_\phi(\cdot|z_{t+k}))\right)\right]$

4. **Backpropagate** through the entire imagined trajectory (straight-through gradients for discrete actions in DreamerV2/V3)

**Key advantage**: After training, the policy runs in real-time — no expensive search at decision time.

### SVG (Stochastic Value Gradient)

**SVG** (Heess et al., 2015): Differentiates through the learned dynamics model to compute policy gradients:

$$
\nabla_\phi J \approx \nabla_\phi \sum_{t=0}^{H} r(s_t, a_t), \quad \text{where } s_{t+1} = f_\theta(s_t, a_t), \; a_t = \pi_\phi(s_t)
$$

This uses the full gradient through the model (unlike REINFORCE-style gradients), reducing variance.

## Video Prediction as Planning

Recent work uses video prediction models directly for planning:

**UniPi** (Du et al., 2023):

1. Use a text-conditioned video diffusion model to generate future video
2. Extract actions from the generated video using an inverse dynamics model
3. The video model serves as both the world model and the planner

This approach leverages the rich world knowledge in large video models.

## Comparison of Planning Approaches

| Method | When to Use | Strengths | Weaknesses |
|--------|-------------|-----------|------------|
| Random Shooting | Prototyping | Simplest | Inefficient |
| CEM | Continuous MPC | Good balance of quality/speed | Limited horizon |
| MCTS | Discrete, deep reasoning | Optimal with budget | Expensive, discrete |
| Imagination (Dreamer) | Real-time control | Fast at test time, continuous | Needs good model |
| SVG | Differentiable models | Low variance gradients | Exploding/vanishing gradients |
| Video-based (UniPi) | Rich visual tasks | Leverages pretrained models | Slow, coarse |

## Key References

- Chua, K., et al. (2018). "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." *NeurIPS*.
- Hafner, D., et al. (2019). "Learning Latent Dynamics for Planning from Pixels." *ICML*.
- Silver, D., et al. (2018). "A General Reinforcement Learning Algorithm that Masters Chess, Shogi, and Go Through Self-Play." *Science*.
- Schrittwieser, J., et al. (2020). "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model." *Nature*.
- Hafner, D., et al. (2020). "Dream to Control: Learning Behaviors by Latent Imagination." *ICLR*.
- Du, Y., et al. (2023). "Learning Universal Policies via Text-Guided Video Generation." *NeurIPS*.
