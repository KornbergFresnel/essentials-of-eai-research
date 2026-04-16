# Recommended Reading List

A curated collection of textbooks, courses, blogs, and other resources for deepening your knowledge. Organized by topic and difficulty level.

## Textbooks

### Reinforcement Learning

| Book | Authors | Level | Notes |
|------|---------|-------|-------|
| *Reinforcement Learning: An Introduction* (2nd ed.) | Sutton & Barto, 2018 | Beginner-Intermediate | **The** RL textbook. Read chapters 1-6 first, then selectively. Free online. |
| *Algorithms for Decision Making* | Kochenderfer et al., 2022 | Intermediate | Broader decision-making perspective, excellent for MDPs and POMDPs. Free online. |
| *Bandit Algorithms* | Lattimore & Szepesvari, 2020 | Advanced | Rigorous treatment of exploration-exploitation. |

### Deep Learning

| Book | Authors | Level | Notes |
|------|---------|-------|-------|
| *Deep Learning* | Goodfellow, Bengio, Courville, 2016 | Beginner-Intermediate | Standard reference. Chapters 6-12 most relevant. Free online. |
| *Dive into Deep Learning* | Zhang et al., 2023 | Beginner | Interactive, code-first. Good for building implementation skills. |

### Robotics

| Book | Authors | Level | Notes |
|------|---------|-------|-------|
| *Modern Robotics* | Lynch & Park, 2017 | Intermediate | Kinematics, dynamics, control. Essential for embodied AI. |
| *Probabilistic Robotics* | Thrun, Burgard, Fox, 2005 | Intermediate | Localization, mapping, SLAM. |

## Online Courses

### Reinforcement Learning

- **[CS285: Deep Reinforcement Learning](http://rail.eecs.berkeley.edu/deeprlcourse/)** — UC Berkeley (Sergey Levine)
  The gold standard for deep RL courses. Covers policy gradient, model-based RL, offline RL, and more. Video lectures available.

- **[David Silver's RL Course](https://www.davidsilver.uk/teaching/)** — UCL
  Classic introduction to RL fundamentals. 10 lectures covering MDPs, dynamic programming, TD learning, policy gradient.

- **[Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/)** — Hugging Face
  Free, interactive course with hands-on coding. Good for beginners.

### Robotics and Embodied AI

- **[CS224R: Deep Reinforcement Learning for Robotics](https://cs224r.stanford.edu/)** — Stanford
  RL applied to robotics: sim-to-real, manipulation, locomotion.

- **[16-831: Introduction to Robot Learning](https://16-831.github.io/)** — CMU
  Covers imitation learning, RL for robotics, and data-efficient methods.

## Blogs and Technical Writing

### Must-Read Blogs

- **[Lilian Weng's Blog](https://lilianweng.github.io/)** — Exceptionally clear technical exposition of RL, world models, robotics, and more. Start with "A (Long) Peek into Reinforcement Learning."

- **[The Gradient](https://thegradient.pub/)** — Long-form articles on ML/AI research trends and perspectives.

- **[Berkeley AI Research Blog (BAIR)](https://bair.berkeley.edu/blog/)** — Research blog covering RL, robotics, and AI systems from UC Berkeley.

- **[Google DeepMind Blog](https://deepmind.google/discover/blog/)** — High-quality posts on RL breakthroughs (AlphaGo, MuZero, Gemini).

### Research Methodology

- **"An Opinionated Guide to ML Research"** — John Schulman. Practical advice on research taste and execution.
- **"How to Read a Paper"** — S. Keshav, 2007. The three-pass approach to reading research papers.
- **"Mathematical Writing"** — Donald Knuth. Timeless advice on technical writing.

## Conferences and Venues

### Primary Venues for Embodied AI

| Venue | Focus | Submission Deadline |
|-------|-------|-------------------|
| **NeurIPS** | ML/AI (broad) | May |
| **ICML** | ML (broad) | January |
| **ICLR** | Representation learning, deep learning | September |
| **CoRL** | Robot learning (focused) | June |
| **RSS** | Robotics (focused) | January |
| **ICRA** | Robotics (broad) | September |
| **IROS** | Intelligent robots | March |

### Workshops to Watch

- NeurIPS "Robot Learning" workshop
- ICRA "Learning for Agile Robotics" workshop
- CoRL spotlight talks and demos

## Software and Tools

### Essential Libraries

| Library | Purpose |
|---------|---------|
| **PyTorch** | Deep learning framework |
| **JAX** | High-performance numerical computing (popular in RL research) |
| **Gymnasium** (Gym) | Standard RL environment API |
| **MuJoCo** | Physics simulation |
| **Isaac Lab** | GPU-accelerated robot simulation |
| **Weights & Biases** | Experiment tracking |
| **Hydra** | Configuration management |

### Code Repositories to Study

- **CleanRL** — Clean, single-file RL implementations
- **Stable-Baselines3** — Reliable RL implementations
- **legged_gym** — Locomotion RL training (NVIDIA)
- **robomimic** — Robot manipulation from demonstrations
- **lerobot** — Hugging Face robot learning library

## Seminal Paper Collections

For topic-specific paper lists, see:

- [Key Papers in Deep RL](../rl/key_papers.md)
- [Key Papers in World Models](../world_models/key_papers.md)

## Staying Updated

- **ArXiv** — Set up alerts for cs.RO, cs.LG, cs.AI
- **Google Scholar** — Follow key authors in your area
- **Semantic Scholar** — AI-powered paper recommendations
- **Twitter/X** — Follow researchers, labs, and conference accounts
- **Reddit** — r/MachineLearning, r/reinforcementlearning
