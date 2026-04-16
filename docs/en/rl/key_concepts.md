# Key Concepts in Reinforcement Learning

This page introduces the foundational concepts of reinforcement learning. We cover the mathematical framework (MDPs), the core objects (policies, value functions), the key equations (Bellman equations), and the fundamental challenges (exploration vs. exploitation).

## The Agent-Environment Interface

At its core, RL is about an **agent** interacting with an **environment** over discrete time steps. At each step $t$:

1. The agent observes a state $s_t \in \mathcal{S}$
2. The agent selects an action $a_t \in \mathcal{A}$ according to its policy
3. The environment transitions to a new state $s_{t+1}$ and emits a reward $r_t \in \mathbb{R}$

The agent's goal is to learn a behavior (policy) that maximizes the **cumulative reward** it receives over time.

## Markov Decision Process (MDP)

The standard mathematical formulation for RL problems is the **Markov Decision Process**, defined by the tuple $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$:

| Symbol | Meaning |
|--------|---------|
| $\mathcal{S}$ | State space |
| $\mathcal{A}$ | Action space |
| $P(s' \mid s, a)$ | Transition dynamics — probability of next state $s'$ given current state $s$ and action $a$ |
| $R(s, a, s')$ | Reward function |
| $\gamma \in [0, 1)$ | Discount factor |

The **Markov property** states that the future is conditionally independent of the past given the present:

$$
P(s_{t+1} \mid s_t, a_t, s_{t-1}, a_{t-1}, \ldots) = P(s_{t+1} \mid s_t, a_t)
$$

!!! note "When Markov Doesn't Hold"
    In practice, agents often observe partial state information (e.g., a robot's camera image doesn't reveal hidden object positions). This leads to **Partially Observable MDPs (POMDPs)**, where the agent receives observations $o_t$ instead of true states $s_t$. Many practical RL systems handle partial observability by using observation histories or recurrent policies.

## Return and Discount Factor

The **return** $G_t$ is the total discounted reward from time step $t$:

$$
G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k}
$$

The discount factor $\gamma$ controls the trade-off between immediate and future rewards:

- $\gamma \to 0$: myopic agent, only cares about immediate reward
- $\gamma \to 1$: far-sighted agent, values future reward almost as much as immediate

!!! tip "Why Discount?"
    Discounting serves multiple purposes: (1) it ensures the return is finite for infinite-horizon problems, (2) it models preference for sooner rewards, and (3) it reduces variance in return estimates.

## Policy

A **policy** $\pi$ defines the agent's behavior — how it selects actions given states.

**Stochastic policy**: $\pi(a \mid s) = P(a_t = a \mid s_t = s)$

**Deterministic policy**: $a = \mu(s)$

The goal of RL is to find an **optimal policy** $\pi^*$ that maximizes the expected return:

$$
\pi^* = \arg\max_\pi \mathbb{E}_{\tau \sim \pi} \left[ \sum_{t=0}^{\infty} \gamma^t r_t \right]
$$

where $\tau = (s_0, a_0, r_0, s_1, a_1, r_1, \ldots)$ denotes a trajectory sampled under policy $\pi$.

## Value Functions

Value functions estimate "how good" it is for the agent to be in a given state (or to take a given action in a state) under a policy $\pi$.

### State-Value Function

$$
V^\pi(s) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s \right] = \mathbb{E}_{\pi} \left[ \sum_{k=0}^{\infty} \gamma^k r_{t+k} \mid s_t = s \right]
$$

### Action-Value Function (Q-Function)

$$
Q^\pi(s, a) = \mathbb{E}_{\pi} \left[ G_t \mid s_t = s, a_t = a \right]
$$

The relationship between $V$ and $Q$:

$$
V^\pi(s) = \mathbb{E}_{a \sim \pi(\cdot|s)} \left[ Q^\pi(s, a) \right]
$$

### Advantage Function

The **advantage function** measures how much better an action is compared to the average:

$$
A^\pi(s, a) = Q^\pi(s, a) - V^\pi(s)
$$

The advantage function is central to many policy gradient algorithms (PPO, TRPO, GAE).

## Bellman Equations

The Bellman equations express a recursive relationship between value functions.

### Bellman Expectation Equation

For $V^\pi$:

$$
V^\pi(s) = \sum_{a} \pi(a|s) \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^\pi(s') \right]
$$

For $Q^\pi$:

$$
Q^\pi(s,a) = R(s,a) + \gamma \sum_{s'} P(s'|s,a) \sum_{a'} \pi(a'|s') Q^\pi(s',a')
$$

### Bellman Optimality Equation

For the optimal value functions $V^*$ and $Q^*$:

$$
V^*(s) = \max_a \left[ R(s,a) + \gamma \sum_{s'} P(s'|s,a) V^*(s') \right]
$$

$$
Q^*(s,a) = R(s,a) + \gamma \sum_{s'} P(s'|s,a) \max_{a'} Q^*(s',a')
$$

!!! info "Why Bellman Equations Matter"
    Almost all RL algorithms are, at their core, methods for approximately solving the Bellman equations. Value-based methods directly approximate $V^*$ or $Q^*$. Policy-based methods optimize $\pi$ to implicitly satisfy optimality. Understanding Bellman equations is essential for understanding RL.

## Exploration vs. Exploitation

A fundamental challenge in RL is the **exploration-exploitation trade-off**:

- **Exploitation**: Choose actions that maximize expected reward based on current knowledge
- **Exploration**: Try new actions to discover potentially better strategies

Common exploration strategies:

| Strategy | Description |
|----------|-------------|
| **$\varepsilon$-greedy** | With probability $\varepsilon$, take a random action; otherwise, take the greedy action |
| **Boltzmann (softmax)** | Sample actions proportional to $\exp(Q(s,a)/\tau)$ where $\tau$ is temperature |
| **UCB** | Choose actions that maximize $Q(s,a) + c\sqrt{\ln(t)/N(s,a)}$ |
| **Entropy regularization** | Add entropy bonus to the objective: $\mathcal{H}(\pi(\cdot|s))$ |
| **Intrinsic motivation** | Reward curiosity — visiting novel states (ICM, RND, etc.) |

## Temporal Difference Learning

**Temporal Difference (TD)** learning is a central idea in RL that combines Monte Carlo sampling with bootstrapping from value estimates.

The simplest TD update (TD(0)) for estimating $V^\pi$:

$$
V(s_t) \leftarrow V(s_t) + \alpha \left[ r_t + \gamma V(s_{t+1}) - V(s_t) \right]
$$

where $\delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$ is the **TD error**.

TD learning has several advantages over Monte Carlo methods:

- **Lower variance** (bootstraps from value estimates instead of full returns)
- **Online learning** (updates after each step, not after complete episodes)
- **Works for continuing tasks** (doesn't require episodes to terminate)

!!! tip "TD vs Monte Carlo vs Dynamic Programming"
    - **Dynamic Programming**: Requires full model $P(s'|s,a)$, bootstraps, no sampling
    - **Monte Carlo**: Model-free, no bootstrapping, requires complete episodes
    - **TD Learning**: Model-free, bootstraps, online — combines advantages of both

## What's Next

With these core concepts in place, proceed to:

- [Algorithm Taxonomy](algorithm_taxonomy.md) — How RL algorithms are organized
- [Intro to Policy Optimization](intro_policy_optimization.md) — The policy gradient theorem
