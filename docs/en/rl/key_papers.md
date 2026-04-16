# Key Papers in Deep RL

A curated reading list of foundational and influential papers in deep reinforcement learning, organized by topic. For each paper, we provide a brief description of its contribution.

!!! tip "How to Use This List"
    Start with papers marked with **(essential)** — these are foundational works that every RL researcher should read. Then explore specific areas based on your research interests. Papers are listed roughly in chronological order within each section.

## Foundations

- **Playing Atari with Deep Reinforcement Learning** — Mnih et al., 2013. **(essential)**
  The original DQN paper. Demonstrated that a single architecture can learn to play Atari games from raw pixels.

- **Human-level Control through Deep Reinforcement Learning** — Mnih et al., Nature 2015. **(essential)**
  The Nature DQN paper with experience replay and target networks.

- **Policy Gradient Methods for Reinforcement Learning with Function Approximation** — Sutton et al., NeurIPS 1999. **(essential)**
  The policy gradient theorem.

## Policy Optimization

- **Trust Region Policy Optimization** — Schulman et al., ICML 2015. **(essential)**
  Monotonic improvement via KL-constrained policy updates.

- **High-Dimensional Continuous Control Using Generalized Advantage Estimation** — Schulman et al., ICLR 2016. **(essential)**
  GAE — the standard advantage estimation technique used by PPO and many others.

- **Proximal Policy Optimization Algorithms** — Schulman et al., 2017. **(essential)**
  PPO — the de facto standard on-policy algorithm. Clipped surrogate objective.

## Value-Based

- **Deep Reinforcement Learning with Double Q-learning** — van Hasselt et al., AAAI 2016.
  Fixes DQN overestimation with double Q-learning.

- **Prioritized Experience Replay** — Schaul et al., ICLR 2016.
  Sample replay transitions proportional to TD error.

- **Rainbow: Combining Improvements in Deep Reinforcement Learning** — Hessel et al., AAAI 2018.
  Combines 6 DQN improvements into one agent.

- **A Distributional Perspective on Reinforcement Learning** — Bellemare et al., ICML 2017.
  Learn the full return distribution (C51), not just the mean.

## Actor-Critic and Off-Policy

- **Asynchronous Methods for Deep Reinforcement Learning** — Mnih et al., ICML 2016.
  A3C — parallel actor-critic training.

- **Continuous Control with Deep Reinforcement Learning** — Lillicrap et al., ICLR 2016. **(essential)**
  DDPG — extends DQN to continuous actions with deterministic policy gradient.

- **Addressing Function Approximation Error in Actor-Critic Methods** — Fujimoto et al., ICML 2018. **(essential)**
  TD3 — twin critics, delayed updates, target smoothing.

- **Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL** — Haarnoja et al., ICML 2018. **(essential)**
  SAC — maximum entropy RL, automatic temperature tuning.

## Model-Based RL

- **World Models** — Ha & Schmidhuber, NeurIPS 2018.
  VAE + RNN world model for learning in imagination.

- **When to Trust Your Model: Model-Based Policy Optimization** — Janner et al., NeurIPS 2019.
  MBPO — principled short-horizon model rollouts for policy optimization.

- **Dream to Control: Learning Behaviors by Latent Imagination** — Hafner et al., ICLR 2020.
  Dreamer — RSSM world model with imagination-based actor-critic.

- **Mastering Diverse Domains through World Models** — Hafner et al., 2023. **(essential)**
  DreamerV3 — single hyperparameter set works across many domains.

- **Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model** — Schrittwieser et al., Nature 2020. **(essential)**
  MuZero — learned model + MCTS, no observation prediction needed.

## Offline RL

- **Off-Policy Deep Reinforcement Learning without Exploration** — Fujimoto et al., ICML 2019.
  BCQ — first to clearly identify and address extrapolation error in offline RL.

- **Conservative Q-Learning for Offline Reinforcement Learning** — Kumar et al., NeurIPS 2020. **(essential)**
  CQL — pessimistic value function, strong theoretical guarantees.

- **Offline Reinforcement Learning with Implicit Q-Learning** — Kostrikov et al., ICLR 2022.
  IQL — avoids OOD action queries entirely via expectile regression.

- **Decision Transformer: Reinforcement Learning via Sequence Modeling** — Chen et al., NeurIPS 2021.
  RL as sequence prediction with Transformers, conditioned on desired returns.

## Exploration

- **Curiosity-driven Exploration by Self-Supervised Prediction** — Pathak et al., ICML 2017.
  ICM — intrinsic reward from prediction error in feature space.

- **Exploration by Random Network Distillation** — Burda et al., ICLR 2019.
  RND — simple and effective exploration via random network prediction error.

- **Go-Explore: A New Approach for Hard-Exploration Problems** — Ecoffet et al., Nature 2021.
  Archive-based exploration for extremely sparse reward environments.

## Multi-Agent RL

- **Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments** — Lowe et al., NeurIPS 2017.
  MADDPG — centralized training, decentralized execution.

- **QMIX: Monotonic Value Function Factorisation for DMARL** — Rashid et al., ICML 2018.
  Value decomposition for cooperative multi-agent RL.

- **The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games** — Yu et al., NeurIPS 2022.
  MAPPO — simple PPO adaptation works remarkably well for multi-agent tasks.

## RL for Real-World Applications

- **Sim-to-Real: Learning Agile Locomotion For Quadruped Robots** — Tan et al., RSS 2018.
  Early demonstration of sim-to-real transfer for robot locomotion.

- **Learning Agile and Dynamic Motor Skills for Legged Robots** — Hwangbo et al., Science Robotics 2019.
  Actuator network + RL for ANYmal locomotion.

- **Learning Dexterous In-Hand Manipulation** — OpenAI et al., IJRR 2020.
  Rubik's cube solving with a robot hand via massive domain randomization.

## Surveys and Tutorials

- **An Introduction to Deep Reinforcement Learning** — François-Lavet et al., 2018.
  Comprehensive introduction to deep RL methods.

- **Offline Reinforcement Learning: Tutorial, Review, and Perspectives** — Levine et al., 2020.
  Excellent survey of offline RL.

- **A Survey on Model-based Reinforcement Learning** — Moerland et al., 2023.
  Comprehensive survey of model-based approaches.
