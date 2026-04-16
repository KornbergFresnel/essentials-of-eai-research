# 深度强化学习关键论文

按主题整理的深度强化学习基础性和具有重要影响力的论文列表。每篇论文附有对其核心贡献的简要说明。

!!! tip "阅读建议"
    优先阅读标记为 **（必读）** 的论文——这些是每位 RL 研究者都应该精读的奠基之作。然后根据自己的研究方向深入探索特定领域。每个类别内的论文大致按时间顺序排列。

## 基础工作

- **Playing Atari with Deep Reinforcement Learning** — Mnih et al., 2013. **（必读）**
  原始 DQN 论文。首次证明单一架构能从原始像素输入学会玩 Atari 游戏。

- **Human-level Control through Deep Reinforcement Learning** — Mnih et al., Nature 2015. **（必读）**
  Nature 版 DQN 论文，提出经验回放和目标网络。

- **Policy Gradient Methods for Reinforcement Learning with Function Approximation** — Sutton et al., NeurIPS 1999. **（必读）**
  策略梯度定理的奠基论文。

## 策略优化

- **Trust Region Policy Optimization** — Schulman et al., ICML 2015. **（必读）**
  通过 KL 散度约束实现策略更新的单调改进。

- **High-Dimensional Continuous Control Using Generalized Advantage Estimation** — Schulman et al., ICLR 2016. **（必读）**
  广义优势估计（GAE）——PPO 等算法使用的标准优势估计技术。

- **Proximal Policy Optimization Algorithms** — Schulman et al., 2017. **（必读）**
  PPO——当前最主流的在策略算法。采用截断代理目标函数。

## 基于值函数的方法

- **Deep Reinforcement Learning with Double Q-learning** — van Hasselt et al., AAAI 2016.
  用双 Q 学习修正 DQN 的过高估计问题。

- **Prioritized Experience Replay** — Schaul et al., ICLR 2016.
  按 TD 误差大小的比例采样经验回放中的转移。

- **Rainbow: Combining Improvements in Deep Reinforcement Learning** — Hessel et al., AAAI 2018.
  将六项 DQN 改进融合为一个智能体。

- **A Distributional Perspective on Reinforcement Learning** — Bellemare et al., ICML 2017.
  学习完整的回报分布（C51），而非仅学习均值。

## Actor-Critic 与离策略方法

- **Asynchronous Methods for Deep Reinforcement Learning** — Mnih et al., ICML 2016.
  A3C——异步并行 Actor-Critic 训练。

- **Continuous Control with Deep Reinforcement Learning** — Lillicrap et al., ICLR 2016. **（必读）**
  DDPG——将 DQN 扩展到连续动作空间，使用确定性策略梯度。

- **Addressing Function Approximation Error in Actor-Critic Methods** — Fujimoto et al., ICML 2018. **（必读）**
  TD3——双评价网络、延迟更新、目标平滑。

- **Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL** — Haarnoja et al., ICML 2018. **（必读）**
  SAC——最大熵强化学习，自动温度调节。

## 基于模型的强化学习

- **World Models** — Ha & Schmidhuber, NeurIPS 2018.
  VAE + RNN 世界模型，在"梦境"中学习。

- **When to Trust Your Model: Model-Based Policy Optimization** — Janner et al., NeurIPS 2019.
  MBPO——有原则地进行短时域模型展开以优化策略。

- **Dream to Control: Learning Behaviors by Latent Imagination** — Hafner et al., ICLR 2020.
  Dreamer——基于 RSSM 世界模型的想象力 Actor-Critic 训练。

- **Mastering Diverse Domains through World Models** — Hafner et al., 2023. **（必读）**
  DreamerV3——单组超参数横跨多种任务域。

- **Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model** — Schrittwieser et al., Nature 2020. **（必读）**
  MuZero——学习模型 + MCTS，无需预测观测。

## 离线强化学习

- **Off-Policy Deep Reinforcement Learning without Exploration** — Fujimoto et al., ICML 2019.
  BCQ——首次明确提出并解决离线 RL 中的外推误差问题。

- **Conservative Q-Learning for Offline Reinforcement Learning** — Kumar et al., NeurIPS 2020. **（必读）**
  CQL——悲观价值函数，具有强理论保证。

- **Offline Reinforcement Learning with Implicit Q-Learning** — Kostrikov et al., ICLR 2022.
  IQL——通过期望分位回归完全避免分布外动作查询。

- **Decision Transformer: Reinforcement Learning via Sequence Modeling** — Chen et al., NeurIPS 2021.
  用 Transformer 将 RL 重新定义为序列预测，以期望回报为条件。

## 探索

- **Curiosity-driven Exploration by Self-Supervised Prediction** — Pathak et al., ICML 2017.
  ICM——利用特征空间中的预测误差作为内在奖励驱动探索。

- **Exploration by Random Network Distillation** — Burda et al., ICLR 2019.
  RND——通过随机网络预测误差实现简单高效的探索。

- **Go-Explore: A New Approach for Hard-Exploration Problems** — Ecoffet et al., Nature 2021.
  基于档案的探索方法，专攻极端稀疏奖励环境。

## 多智能体强化学习

- **Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments** — Lowe et al., NeurIPS 2017.
  MADDPG——集中训练、分散执行。

- **QMIX: Monotonic Value Function Factorisation for DMARL** — Rashid et al., ICML 2018.
  协作式多智能体 RL 的值函数分解方法。

- **The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games** — Yu et al., NeurIPS 2022.
  MAPPO——简单的 PPO 改编方案在多智能体任务中表现出色。

## 面向真实世界应用的 RL

- **Sim-to-Real: Learning Agile Locomotion For Quadruped Robots** — Tan et al., RSS 2018.
  早期的机器人运动 sim-to-real 迁移成功案例。

- **Learning Agile and Dynamic Motor Skills for Legged Robots** — Hwangbo et al., Science Robotics 2019.
  致动器网络 + RL 用于 ANYmal 的运动控制。

- **Learning Dexterous In-Hand Manipulation** — OpenAI et al., IJRR 2020.
  通过大规模域随机化实现机器手解魔方。

## 综述与教程

- **An Introduction to Deep Reinforcement Learning** — Francois-Lavet et al., 2018.
  全面介绍深度 RL 各类方法。

- **Offline Reinforcement Learning: Tutorial, Review, and Perspectives** — Levine et al., 2020.
  优秀的离线 RL 综述。

- **A Survey on Model-based Reinforcement Learning** — Moerland et al., 2023.
  基于模型方法的全面综述。
