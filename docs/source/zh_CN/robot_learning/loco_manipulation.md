# Loco-Manipulation

## Scope and Motivation

Loco-manipulation 指移动和操作同时发生、且二者不能简单分解的任务。移动底盘或腿式身体改变操作可达性，手臂和负载又改变整机质心、接触和稳定性。该问题比单独 locomotion 或固定基座 manipulation 更复杂，因为策略需要同时处理导航、接触、抓取、物体状态和全身协调。

## Problem Setting

典型任务包括移动机械臂搬运物体、四足机器人推拉门、全身控制取放物体、移动平台与双臂协作。观测通常需要机器人本体状态、末端位姿、物体 pose、接触或 grasp 状态、局部地图和任务进度。很多关键变量不可直接观测，如抓取力、摩擦、物体质量和遮挡后的接触状态。

## System / Algorithmic View

系统可采用端到端策略、层级策略或规划-控制混合结构。层级方法通常将任务分解为 base navigation、reaching、grasping、transport 和 placement，但分解边界若过硬，会在接触丰富的阶段失败。全身控制器可以统一处理 base、arm 和姿态约束，但需要明确策略输出是高层目标、末端速度还是全身关节命令。

## Implementation Notes

实现时应记录 base 和 arm 的控制频率、坐标系、碰撞检查、grasp 表示、对象 pose 来源和失败恢复策略。若策略使用目标物体的精确 pose，需要说明该 pose 来自真实感知、marker、仿真状态还是离线标注。对于长时程任务，日志应记录每个阶段的进入时间、退出条件和失败类型。

## Experimental Protocol

评估不应只看最终成功率。应分解报告到达、接触建立、抓取稳定、移动保持、放置成功和恢复行为。部分成功指标有助于定位失败发生在 locomotion、perception、grasping 还是 task planning。初始物体位置、环境布局、负载质量和障碍物应有训练/测试划分。

## Failure Modes and Limitations

常见失败包括 base-arm 干涉、抓取后质心变化导致失稳、接触状态误判、路径规划与操作目标冲突，以及长时程误差累积。仿真中的理想 grasp 和刚体接触会显著高估真实性能。若 reset 需要人工恢复物体和机器人姿态，实验吞吐会成为主要系统瓶颈。

## References

- Fu et al., "Mobile ALOHA": 移动操作数据采集和模仿学习系统。
- Cheng et al., "Learning Whole-Body Manipulation for Quadrupedal Robots": 四足全身操作参考。
- Khatib, "A Unified Approach for Motion and Force Control of Robot Manipulators": 操作控制中的经典约束视角。
