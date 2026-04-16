# 机器人学习实践

## Learning Goals

本章关注 locomotion、loco-manipulation、遥操和数据采集这些当前最需要先建立工程直觉的主题。

## Prerequisites

建议先理解强化学习基础、具身任务建模和基本机器人控制。

## Core Concepts

机器人学习不是单纯训练一个 policy。你还需要决定数据如何来、任务如何 reset、失败如何处理、动作由谁执行、评估如何保证公平。

## Algorithms / System Design

- Locomotion：关注稳定性、速度、能耗、地形适应和扰动恢复。
- Loco-manipulation：同时处理移动和操作，难点在接触、长时程目标和全身协调。
- Teleoperation：用人类操作生成演示数据，也可作为安全 fallback。
- Data Collection：设计覆盖任务分布的数据流程，记录 observation、action、reward、success、metadata。

## Practical Notes

数据采集系统应记录时间戳、控制频率、坐标系、相机参数、机器人状态和人工标注。没有 metadata 的机器人数据通常很难复用。

## Common Pitfalls

- 只追求数据量，不控制数据质量和覆盖范围。
- 忽略 reset 成本，使实验吞吐远低于预期。
- 遥操接口和学习 policy 的动作空间不一致。

## Recommended Reading

- Kumar et al., RMA for legged locomotion.
- Brohan et al., RT-1 and RT-2.
- Fu et al., Mobile ALOHA.

## Exercises / Research Questions

设计一个遥操采集协议：每条 episode 需要记录哪些数据，如何标记失败，如何保证后续训练可用？

## Glossary

- Loco-manipulation：移动和操作同时发生的机器人任务。
- Teleoperation：人类远程控制机器人执行任务。
- Dataset metadata：描述数据采集条件、设备、任务和质量的信息。
