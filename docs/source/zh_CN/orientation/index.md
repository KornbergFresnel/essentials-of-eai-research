# 使用指南

## Learning Goals

读完本章后，你应该能够判断自己该从哪一部分开始，知道学习强化学习和具身智能研究需要哪些先修知识，并建立一种可持续更新的研究笔记习惯。

## Prerequisites

建议具备基本概率论、线性代数、优化、深度学习和 Python 实验经验。机器人方向的读者还应熟悉基本动力学、控制和仿真概念。

## Core Concepts

这份资料按照“问题定义 - 算法 - 具身约束 - 系统架构 - 研究实践”的顺序组织。低年级博士不需要一次读完所有内容，但需要知道每一层在研究中的作用。

## Practical Notes

阅读时建议维护三类笔记：概念卡片、论文摘要和实验记录。概念卡片回答“这个对象是什么”；论文摘要回答“这篇工作解决了什么问题”；实验记录回答“我做了什么、结果如何、下一步是什么”。

## Common Pitfalls

- 只看算法公式，不记录实验设置。
- 只调工程参数，不回到问题定义。
- 只复现单个结果，不比较 baseline 和 ablation。

## Recommended Reading

- Sutton and Barto, *Reinforcement Learning: An Introduction*.
- OpenAI Spinning Up for classical deep RL background.

## Exercises / Research Questions

写一页自己的研究地图：你的课题中哪些部分是 RL，哪些部分是世界模型，哪些部分是机器人系统，哪些部分是实验基础设施？

## Glossary

- 轨迹：智能体与环境交互得到的状态、动作、奖励序列。
- 可复现性：他人或未来的你能根据记录重新得到可比较结果的程度。
