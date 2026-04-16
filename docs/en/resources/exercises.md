# Exercises

Hands-on exercises to deepen your understanding. Each exercise set corresponds to a section of the resource and builds progressively from conceptual to implementation challenges.

## Part I: Reinforcement Learning

### Exercise Set 1: Fundamentals

!!! question "1.1 Bellman Equation Derivation"
    Derive the Bellman expectation equation for $Q^\pi(s,a)$ starting from the definition of the action-value function. Show all steps.

!!! question "1.2 Discount Factor Analysis"
    Consider a simple MDP with two states and deterministic transitions. The agent receives reward +1 at every step. Compute $V^\pi(s_0)$ analytically for $\gamma = 0.9$ and $\gamma = 0.99$. What happens as $\gamma \to 1$?

!!! question "1.3 Advantage Function Properties"
    Prove that $\mathbb{E}_{a \sim \pi}[A^\pi(s,a)] = 0$ for any state $s$ and policy $\pi$. Why is this property useful for variance reduction?

### Exercise Set 2: Policy Gradient

!!! question "2.1 Implement REINFORCE"
    Implement REINFORCE from scratch in PyTorch. Train it on `CartPole-v1`. Plot the learning curve (episode return vs. training step) over 5 random seeds.

    **Bonus**: Add a learned baseline and compare the learning curves with and without the baseline.

!!! question "2.2 Variance Analysis"
    Empirically compare the variance of the policy gradient estimator using:
    (a) Full trajectory return
    (b) Reward-to-go
    (c) Reward-to-go with baseline

    Estimate the variance by computing the gradient over many trajectories and measuring its variance.

!!! question "2.3 Implement PPO"
    Implement PPO-Clip with GAE. Train on `HalfCheetah-v4` (MuJoCo). Compare with your REINFORCE implementation on CartPole. Key components:

    - Clipped surrogate objective
    - Value function loss
    - Entropy bonus
    - GAE advantage estimation
    - Mini-batch updates over multiple epochs

### Exercise Set 3: Value-Based Methods

!!! question "3.1 Implement DQN"
    Implement DQN with experience replay and target networks. Train on `PongNoFrameskip-v4`. Key components:

    - Frame stacking (4 frames)
    - $\epsilon$-greedy exploration with annealing
    - Experience replay buffer
    - Target network (update every 10K steps)

!!! question "3.2 Double DQN"
    Modify your DQN to use Double Q-learning. Compare the Q-value estimates (plot Q-values over training) between DQN and Double DQN.

## Part II: World Models

### Exercise Set 4: Representation Learning

!!! question "4.1 Train a VAE"
    Train a convolutional VAE on frames from a simple environment (e.g., `CartPole` rendered). Visualize the latent space and reconstructions.

    - What happens when you change $\beta$ in the $\beta$-VAE objective?
    - Can you find meaningful structure in the latent space?

!!! question "4.2 Latent Dynamics Model"
    Extend Exercise 4.1: train a latent dynamics model on top of the VAE.

    1. Collect trajectories from a random policy
    2. Train: encoder, decoder, transition model
    3. Evaluate: predict 10 steps ahead, visualize reconstructed observations
    4. Measure prediction error vs. rollout horizon

### Exercise Set 5: Planning

!!! question "5.1 CEM Planning"
    Implement CEM planning with a learned dynamics model.

    1. Train a dynamics model on CartPole transitions
    2. Implement CEM to plan action sequences
    3. Use MPC (re-plan at each step) to control the environment
    4. Compare with a random policy and a trained RL policy

## Part III: Embodied AI

### Exercise Set 6: Locomotion

!!! question "6.1 Train a Walking Policy"
    Using Isaac Gym (or MuJoCo), train a quadruped locomotion policy with PPO:

    1. Set up the environment with a simple quadruped (e.g., ANYmal or Unitree Go1)
    2. Design a reward function for velocity tracking
    3. Train with domain randomization (at least 3 randomized parameters)
    4. Evaluate: plot tracking error vs. commanded velocity

!!! question "6.2 Terrain Curriculum"
    Extend Exercise 6.1 with a terrain curriculum:

    1. Start training on flat ground
    2. Gradually introduce slopes, then stairs, then rough terrain
    3. Compare learning curves with and without curriculum
    4. Analyze what terrain types are hardest

### Exercise Set 7: Data Collection

!!! question "7.1 Behavior Cloning Pipeline"
    Build a complete behavior cloning pipeline:

    1. Collect 100 demonstrations (can be scripted for simplicity) of a pick-and-place task
    2. Train a BC policy (MLP or simple Transformer)
    3. Evaluate success rate
    4. Analyze failure modes — when does BC fail?

## Part IV: Distributed RL

### Exercise Set 8: Scaling

!!! question "8.1 Vectorized Environments"
    Benchmark the effect of environment parallelism:

    1. Run PPO on CartPole with 1, 4, 16, 64, 256, 1024 parallel environments
    2. Plot: wall-clock time to reach a target return vs. number of environments
    3. Plot: sample efficiency (return vs. total environment steps) vs. number of environments
    4. Where does adding more environments stop helping?

!!! question "8.2 Profiling"
    Profile an RL training run (e.g., PPO on a MuJoCo task):

    1. Measure time spent in: environment stepping, policy inference, gradient computation, data transfer
    2. Identify the bottleneck
    3. Propose and implement one optimization
    4. Measure the speedup

## General Research Exercises

!!! question "R.1 Paper Reproduction"
    Choose a paper from the [Key Papers](../rl/key_papers.md) list and reproduce its main result:

    1. Implement the algorithm from the paper description (not from existing code)
    2. Run the same experiment setup
    3. Compare your results to the reported results
    4. Write a 1-page report on what you learned, including any discrepancies

!!! question "R.2 Ablation Study"
    Take any algorithm you've implemented and perform a thorough ablation study:

    1. Identify 3-5 design choices (e.g., network size, learning rate schedule, advantage estimation method)
    2. Test each choice independently
    3. Present results in a clear table or figure
    4. Which design choices matter most?
