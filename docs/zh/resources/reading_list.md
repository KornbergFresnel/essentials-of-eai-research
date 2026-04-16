# 推荐阅读清单

精选教材、课程、博客和其他资源，帮助你深入拓展知识。按主题和难度等级组织。

## 教材

### 强化学习

| 书名 | 作者 | 难度 | 说明 |
|------|------|------|------|
| *Reinforcement Learning: An Introduction*（第2版） | Sutton & Barto, 2018 | 入门-中级 | **RL 圣经**。建议先读 1-6 章，再按需选读。免费在线。 |
| *Algorithms for Decision Making* | Kochenderfer et al., 2022 | 中级 | 更广泛的决策视角，MDP 和 POMDP 讲解出色。免费在线。 |
| *Bandit Algorithms* | Lattimore & Szepesvari, 2020 | 高级 | 对探索-利用问题的严格理论处理。 |

### 深度学习

| 书名 | 作者 | 难度 | 说明 |
|------|------|------|------|
| *Deep Learning* | Goodfellow, Bengio, Courville, 2016 | 入门-中级 | 标准参考书。第 6-12 章与 RL 最相关。免费在线。 |
| *Dive into Deep Learning* | Zhang et al., 2023 | 入门 | 交互式、代码驱动。适合建立实现能力。中文版质量尤佳。 |
| *Understanding Deep Learning* | Prince, 2023 | 中级 | 新书，覆盖 Transformer、扩散模型等最新架构。免费在线。 |

### 机器人学

| 书名 | 作者 | 难度 | 说明 |
|------|------|------|------|
| *Modern Robotics* | Lynch & Park, 2017 | 中级 | 运动学、动力学、控制。具身智能的必备基础。 |
| *Probabilistic Robotics* | Thrun, Burgard, Fox, 2005 | 中级 | 定位、建图、SLAM。经典之作。 |
| *Robotics: Modelling, Planning and Control* | Siciliano et al., 2010 | 中级-高级 | 全面覆盖机器人控制理论。 |

!!! tip "中文资源推荐"
    - 周志华《机器学习》（西瓜书）：机器学习基础的优秀中文教材
    - 邱锡鹏《神经网络与深度学习》：免费在线，覆盖深度学习核心内容
    - 张伟楠等《动手学强化学习》：配合代码实践，适合入门

## 在线课程

### 强化学习

- **[CS285: Deep Reinforcement Learning](http://rail.eecs.berkeley.edu/deeprlcourse/)** — UC Berkeley（Sergey Levine）
  深度 RL 课程的黄金标准。涵盖策略梯度、基于模型的 RL、离线 RL 等。视频公开。

- **[David Silver's RL Course](https://www.davidsilver.uk/teaching/)** — UCL
  经典 RL 基础课程。10 讲涵盖 MDP、动态规划、TD 学习、策略梯度。

- **[Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/)** — Hugging Face
  免费、交互式课程，含实践编程。适合初学者。

- **[CS234: Reinforcement Learning](https://web.stanford.edu/class/cs234/)** — Stanford（Emma Brunskill）
  理论与应用并重，对 RL 的数学基础讲解扎实。

### 机器人与具身智能

- **[CS224R: Deep Reinforcement Learning for Robotics](https://cs224r.stanford.edu/)** — Stanford
  RL 在机器人中的应用：Sim-to-Real、操作、运动控制。

- **[16-831: Introduction to Robot Learning](https://16-831.github.io/)** — CMU
  涵盖模仿学习、RL 在机器人中的应用、数据高效方法。

### 数学基础

- **[Mathematics for Machine Learning](https://mml-book.github.io/)** — Deisenroth et al.
  如果你的数学基础需要补强，这是最佳起点。免费在线。

- **[Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)** — Boyd & Vandenberghe
  理解优化算法的理论基础。免费在线。

## 博客与技术写作

### 必读博客

- **[Lilian Weng 的博客](https://lilianweng.github.io/)** — 对 RL、世界模型、机器人等主题极为清晰的技术阐述。推荐从 "A (Long) Peek into Reinforcement Learning" 开始。

- **[The Gradient](https://thegradient.pub/)** — ML/AI 研究趋势的长文分析与评论。

- **[Berkeley AI Research Blog (BAIR)](https://bair.berkeley.edu/blog/)** — UC Berkeley 的研究博客，覆盖 RL、机器人和 AI 系统。

- **[Google DeepMind Blog](https://deepmind.google/discover/blog/)** — RL 突破性成果的高质量文章（AlphaGo、MuZero、Gemini）。

- **[Hugging Face Blog](https://huggingface.co/blog)** — 开源模型和工具的发布动态，含大量实用教程。

### 研究方法论

- **"An Opinionated Guide to ML Research"** — John Schulman。关于研究品味和执行力的实用建议。
- **"How to Read a Paper"** — S. Keshav, 2007。论文阅读的三遍法。
- **"Mathematical Writing"** — Donald Knuth。技术写作的永恒建议。

## 会议与期刊

### 具身智能的主要会议

| 会议 | 领域侧重 | 投稿截止 |
|------|---------|---------|
| **NeurIPS** | ML/AI（广泛） | 5 月 |
| **ICML** | ML（广泛） | 1 月 |
| **ICLR** | 表征学习、深度学习 | 9 月 |
| **CoRL** | 机器人学习（专注） | 6 月 |
| **RSS** | 机器人（专注） | 1 月 |
| **ICRA** | 机器人（广泛） | 9 月 |
| **IROS** | 智能机器人 | 3 月 |

### 值得关注的研讨会

- NeurIPS "Robot Learning" 研讨会
- ICRA "Learning for Agile Robotics" 研讨会
- CoRL 特邀报告与演示

!!! info "如何跟踪会议动态"
    建议关注各会议的官方 Twitter/X 账号和 OpenReview 页面。CoRL 和 RSS 是具身智能领域最对口的会议，审稿过程相对透明（OpenReview）。

## 软件工具

### 核心库

| 库 | 用途 |
|---|------|
| **PyTorch** | 深度学习框架 |
| **JAX** | 高性能数值计算（在 RL 研究中日益流行） |
| **Gymnasium**（Gym） | 标准 RL 环境 API |
| **MuJoCo** | 物理仿真 |
| **Isaac Lab** | GPU 加速机器人仿真 |
| **Weights & Biases** | 实验追踪 |
| **Hydra** | 配置管理 |

### 值得研读的代码仓库

- **CleanRL** — 清晰的单文件 RL 实现
- **Stable-Baselines3** — 可靠的 RL 实现
- **legged_gym** — 运动控制 RL 训练（NVIDIA）
- **robomimic** — 从示教学习的机器人操作
- **lerobot** — Hugging Face 机器人学习库

## 经典论文合集

按主题分类的论文列表，参见：

- [深度 RL 经典论文](../rl/key_papers.md)
- [世界模型经典论文](../world_models/key_papers.md)

## 保持更新

- **ArXiv** — 设置 cs.RO、cs.LG、cs.AI 的关键词提醒
- **Google Scholar** — 关注你研究领域的关键作者
- **Semantic Scholar** — AI 驱动的论文推荐
- **Twitter/X** — 关注研究者、实验室和会议账号
- **Reddit** — r/MachineLearning、r/reinforcementlearning
- **知乎** — 机器学习和机器人相关话题，中文社区讨论活跃
