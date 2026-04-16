# Data Collection

## Scope and Motivation

机器人数据采集不是被动记录，而是实验系统设计。采集策略决定数据覆盖、失败分布、动作可执行性、标注质量和后续算法可用性。没有 schema、同步和版本管理的数据集，即使规模很大，也很难支撑可复现研究。

## Problem Setting

一条 episode 通常包括传感器观测、机器人状态、人类输入或策略动作、奖励或任务标签、终止条件、reset 信息和元数据。对于多相机、多机器人或人机协作系统，时间同步和坐标系记录与数据本身同等重要。数据集还应保留失败样本，因为失败分布决定策略边界。

## System / Algorithmic View

采集系统可以分为 acquisition、validation、annotation、storage 和 indexing 五层。acquisition 负责同步记录；validation 检查丢帧、动作饱和、传感器异常和安全事件；annotation 产生 success、phase、failure reason 或 language instruction；storage 保证原始数据和处理后数据可追踪；indexing 支持按任务、场景、对象和质量筛选。

## Implementation Notes

建议定义最小 episode schema：

| Field | Description |
| --- | --- |
| `episode_id` | 全局唯一标识，包含数据版本和采集批次。 |
| `timestamps` | 所有传感器、动作和事件的时钟。 |
| `observations` | 图像、proprioception、force、语言或任务规格。 |
| `actions` | 人类输入、策略输出和低层控制命令。 |
| `labels` | success、phase、failure reason、quality flag。 |
| `reset` | 初始状态、reset 方法和人工干预。 |
| `metadata` | 硬件、软件、校准、场景、操作者和任务参数。 |

## Experimental Protocol

报告数据集时应说明任务分布、采集策略、操作者数量、自动/人工比例、失败保留规则、质检规则、标注流程、版本号和剔除标准。对于持续更新的数据集，应保证训练和评估引用明确版本，而不是浮动目录。

## Failure Modes and Limitations

常见失败包括 timestamp drift、相机外参变化、episode 边界错误、失败样本被过滤、success label 与真实任务不一致、metadata 缺失和处理脚本覆盖原始数据。数据覆盖不足会使离线评估过于乐观，尤其在长尾初始状态和接触失败上。

## References

- Brohan et al., RT-1: 大规模机器人数据和任务条件化策略。
- Walke et al., "BridgeData V2": 多任务机器人数据集构建参考。
- Open X-Embodiment Collaboration, RT-X: 跨机器人数据整合和策略训练参考。
