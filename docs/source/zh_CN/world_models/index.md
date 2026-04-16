# 世界模型

## Learning Goals

本章介绍世界模型为什么重要、它预测什么、如何用于规划和策略学习，以及它在具身任务中经常遇到哪些失败模式。

## Prerequisites

建议先理解 MDP/POMDP、监督学习、序列建模和基本强化学习算法。

## Core Concepts

世界模型是智能体对环境变化规律的内部预测模型。它可以预测下一状态、未来观测、奖励、终止条件，或在潜在空间中预测抽象动态。

## Mathematical Formulation

一个常见形式是学习 $p_\theta(z_{t+1}, r_t | z_t, a_t)$，其中 $z_t$ 是由观测编码得到的潜在状态。策略可以在真实环境中学习，也可以在模型生成的 imagined rollout 中学习。

## Algorithms / System Design

世界模型系统通常包含 encoder、dynamics model、reward model、decoder 或 prediction head，以及使用模型进行 planning 或 policy optimization 的模块。

## Practical Notes

模型预测误差会沿时间累积。短期预测准确不代表长期 rollout 可用。评估时应同时看 one-step prediction、多步 rollout、策略性能和模型失效案例。

## Common Pitfalls

- 只优化像素重建，忽略任务相关信息。
- 在训练分布外 rollout 过长。
- 不区分表示学习失败和控制策略失败。

## Recommended Reading

- Ha and Schmidhuber, World Models.
- Hafner et al., Dreamer 系列工作。
- Sutton, Dyna architecture.

## Exercises / Research Questions

为一个移动机器人任务设计世界模型：哪些变量应进入潜在状态，哪些预测目标对控制最有帮助？

## Glossary

- 潜在状态：从高维观测中压缩出的任务相关表示。
- Imagined rollout：在学习到的模型中展开的虚拟轨迹。
