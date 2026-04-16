# 强化学习基础

## Learning Goals

本章帮助你建立强化学习的基本语言：什么是环境、状态、动作、奖励、策略、价值函数和回报，以及这些概念如何连接到机器人和世界模型研究。

## Prerequisites

你应熟悉基本概率、期望、梯度下降和神经网络训练。若对控制理论有基础，会更容易理解连续控制任务。

## Core Concepts

强化学习研究智能体如何通过与环境交互来优化长期目标。标准形式通常用马尔可夫决策过程描述：环境在状态之间转移，智能体根据策略选择动作，并从奖励信号中学习。

在具身智能中，状态通常不能被完整观测。机器人只能看到传感器读数、关节状态、图像或触觉信号，因此很多问题更接近部分可观测马尔可夫决策过程。

## Mathematical Formulation

一个 MDP 可以写作五元组 $(S, A, P, R, \gamma)$。策略 $\pi(a|s)$ 给出在状态 $s$ 下选择动作 $a$ 的概率。目标通常是最大化折扣回报：

$$
J(\pi)=\mathbb{E}_{\tau \sim \pi}\left[\sum_{t=0}^{T}\gamma^t r_t\right].
$$

价值函数 $V^\pi(s)$ 估计从状态 $s$ 出发的期望回报，动作价值函数 $Q^\pi(s,a)$ 估计从状态动作对出发的期望回报。

## Algorithms / System Design

常见算法族包括：

- Policy Gradient：直接优化策略参数，适合连续动作，但方差较高。
- Actor-Critic：同时学习策略和价值函数，用 critic 降低梯度估计方差。
- Q-Learning：学习动作价值函数，常用于离散动作或经过特殊处理的连续控制。
- Model-Based RL：学习或使用环境模型进行规划，和世界模型研究直接相关。

## Practical Notes

实践中的 RL 往往比公式更脆弱。你需要记录随机种子、环境版本、奖励设计、终止条件、归一化方式、评估频率和 checkpoint。单条 learning curve 很少足够支撑结论。

## Common Pitfalls

- 把训练回报当成最终性能，而不做独立评估。
- 调奖励函数后不记录变更，导致实验不可比较。
- 忽略环境 reset、early termination 和 safety constraint 对结果的影响。
- 在机器人任务中默认仿真状态完全可观测，导致方法无法迁移到真实系统。

## Recommended Reading

- [OpenAI Spinning Up](https://spinningup.openai.com/en/latest/)：经典深度强化学习概念、算法和实现参考。建议与本章并行阅读，用它补足 PPO、TRPO、SAC、DDPG 等算法细节。
- Sutton and Barto, *Reinforcement Learning: An Introduction*.
- Lillicrap et al., Continuous control with deep reinforcement learning.
- Haarnoja et al., Soft Actor-Critic.

## Exercises / Research Questions

1. 选一个机器人任务，把它写成 MDP 或 POMDP：观测是什么，动作是什么，奖励如何定义？
2. 比较 policy gradient 和 actor-critic：critic 在实际训练中解决了什么问题，又引入了什么风险？
3. 阅读 Spinning Up 中一个算法页面，写出它的目标函数、主要近似和实现假设。

## Glossary

- MDP：状态完全可观测的强化学习问题形式。
- POMDP：智能体只能获得部分观测的问题形式。
- 策略：从观测或状态到动作分布的映射。
- 回报：沿一条轨迹累积得到的长期奖励。
- World Model：对环境动态、观测或潜在状态演化的预测模型。
