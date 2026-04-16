---
hide:
  - navigation
---

# 具身智能研究基础

<div class="hero" markdown>

**面向博士研究生的系统化学习资料**

从强化学习基础到具身智能系统

</div>

---

欢迎！本资料是一份面向具身人工智能 (Embodied AI, EAI) 研究方向的综合性开源教学资源，旨在帮助博士研究生从零开始构建坚实的理论基础与系统视野。内容涵盖强化学习理论、世界模型、具身系统以及支撑大规模训练的分布式基础设施。

## 适合谁阅读？

本资料面向以下读者：

- **博士新生**——即将或刚刚进入强化学习、机器人学、具身智能等方向
- **工程师**——从传统机器学习/深度学习转向具身系统研发
- **研究人员**——希望获得一份跨领域的结构化参考资料

我们假设读者已具备以下背景：

- 线性代数、概率论、微积分
- 基本的机器学习与深度学习知识（CNN、Transformer 等）
- Python 编程及 PyTorch/JAX 使用经验

## 内容概览

<div class="feature-grid" markdown>

<div class="feature-card" markdown>

### 第一部分：强化学习

RL 核心理论——MDP、贝尔曼方程、策略梯度、值函数方法、Actor-Critic、基于模型的 RL 以及离线 RL。掌握算法层面的基本构件。

[:octicons-arrow-right-24: 开始学习](rl/index.md)

</div>

<div class="feature-card" markdown>

### 第二部分：世界模型

了解智能体如何构建对世界的内部表示——从视频预测到学习动力学模型，再到前沿的基础世界模型。

[:octicons-arrow-right-24: 深入了解](world_models/index.md)

</div>

<div class="feature-card" markdown>

### 第三部分：具身智能

运动控制、移动操作、遥操作系统，以及面向真实机器人学习的数据采集策略。

[:octicons-arrow-right-24: 进入专题](embodied/index.md)

</div>

<div class="feature-card" markdown>

### 第四部分：分布式强化学习

大规模 RL 训练——从 A3C 到 IMPALA 再到 SEED RL。理解支撑大规模 RL 实验的系统架构与框架。

[:octicons-arrow-right-24: 阅读更多](distributed_rl/index.md)

</div>

</div>

## 如何使用本资料

本资料既可以作为**教材**按顺序阅读，也可以作为**参考手册**按需查阅。建议如下：

1. **RL 初学者**：从[第一部分](rl/index.md)开始，按照核心概念、算法分类、具体算法的顺序依次阅读。

2. **具身智能方向新人**：先阅读[第一部分](rl/index.md)建立 RL 基础，然后跳转到[第三部分](embodied/index.md)。

3. **RL 系统开发者**：重点阅读[第四部分](distributed_rl/index.md)中关于分布式架构与训练扩展的内容。

4. **希望获得研究方法指导**：请参阅[成为研究者](resources/researcher_guide.md)，获取关于如何培养科研品味和推进项目的建议。

每个章节包含：

- 具有**数学严谨性**的概念讲解
- **关键论文**参考及简要说明
- 各主题之间的**关联与衔接**
- 用于检验理解的**练习题**

## 参与贡献

本资料持续更新。欢迎提交修正、建议或新内容——详见 [GitHub 仓库](https://github.com/KornbergFresnel/essentials-of-eai-research)。
