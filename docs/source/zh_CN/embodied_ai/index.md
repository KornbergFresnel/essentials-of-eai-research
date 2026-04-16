# 具身智能基础

## Learning Goals

本章把抽象 RL 概念连接到有身体的智能体：传感器、执行器、动力学、环境约束和真实实验成本。

## Prerequisites

建议具备基本机器人学、控制、强化学习和深度学习背景。

## Core Concepts

具身智能研究智能体如何通过身体与环境交互。身体不是算法外部的细节，它决定了动作空间、观测模式、探索风险和任务可行性。

## Mathematical Formulation

具身任务通常更接近 POMDP：智能体得到观测 $o_t$，执行动作 $a_t$，环境状态 $s_t$ 可能包含不可直接测量的接触、物体属性或外部扰动。

## Algorithms / System Design

具身系统需要把 perception、state estimation、policy、low-level control、安全监控和数据记录连接起来。学习算法必须和控制频率、传感器延迟、执行器限制共同设计。

## Practical Notes

仿真任务应记录物理参数、domain randomization、控制频率和 reset 逻辑。真实机器人实验应记录硬件状态、校准流程和失败恢复方案。

## Common Pitfalls

- 把仿真中的 privileged state 当作真实机器人可用输入。
- 忽略控制频率和 latency。
- 只报告成功案例，不分析失败分布。

## Recommended Reading

- Levine et al., learning hand-eye coordination.
- Tobin et al., domain randomization.
- OpenAI et al., dexterous manipulation from pixels.

## Exercises / Research Questions

选择一个具身任务，列出它的观测、动作、动力学约束、安全约束和评估指标。

## Glossary

- Proprioception：机器人自身状态感知，如关节角、速度和力矩。
- Sim-to-real：从仿真训练迁移到真实硬件。
