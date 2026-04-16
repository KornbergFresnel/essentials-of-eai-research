# 分布式强化学习系统

## Learning Goals

本章解释大规模强化学习系统如何把采样、学习、回放、评估和实验管理连接起来。

## Prerequisites

建议先理解基本 RL 训练循环、深度学习训练和常见并行计算概念。

## Core Concepts

分布式 RL 的核心矛盾是数据由环境交互产生，而学习又会不断改变策略。系统需要在吞吐、样本效率、策略新鲜度和稳定性之间取舍。

## Algorithms / System Design

典型组件包括 rollout worker、learner、replay buffer、parameter server、evaluator 和 experiment manager。同步系统更容易分析，异步系统吞吐更高但更难调试 stale policy。

## Practical Notes

系统日志应同时记录环境步数、梯度步数、样本延迟、队列长度、worker 崩溃、评估指标和 checkpoint。只看 reward curve 无法定位系统瓶颈。

## Common Pitfalls

- 混淆 sample throughput 和 learning progress。
- 不记录 policy version，导致数据来源不可追踪。
- evaluator 使用训练环境状态或不固定评估协议。

## Recommended Reading

- Espeholt et al., IMPALA.
- Horgan et al., Ape-X.
- Ray RLlib documentation for system patterns.
- CleanRL for single-file algorithm baselines.

## Exercises / Research Questions

画出一个 distributed actor-learner 系统，并标注每条数据流的延迟、失败模式和日志指标。

## Glossary

- Rollout worker：负责和环境交互、生成轨迹的进程。
- Learner：负责根据数据更新模型参数的进程。
- Replay buffer：存储经验数据供 off-policy 学习使用的组件。
