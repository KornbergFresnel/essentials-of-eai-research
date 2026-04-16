# 机器人学习实践

机器人学习把策略优化、数据生成、机器人控制、实验评估和安全约束耦合在同一个系统中。一个机器人学习结果通常不只由算法决定，还取决于任务定义、遥操或自动采集流程、动作接口、reset 机制、硬件限制和评估分布。

本章采用实验系统视角组织内容。Locomotion 和 loco-manipulation 代表两类典型具身控制问题；teleoperation 和 data collection 描述数据来源；imitation、offline data、safety 和 resets 则描述训练与评估中最容易被低估的工程变量。

```{toctree}
:maxdepth: 1
:caption: 机器人学习系统

locomotion
loco_manipulation
teleoperation
data_collection
imitation_and_offline_data
safety_and_resets
```

## System View

一个可复现的机器人学习实验至少需要同时说明：任务分布、观测和动作接口、控制频率、数据采集策略、训练算法、评估协议、reset 流程、安全边界和日志 schema。缺少任意一项都可能使结果难以比较或迁移。
