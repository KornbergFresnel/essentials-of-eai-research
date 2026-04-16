# 观测空间与动作空间

## Scope and Motivation

观测空间和动作空间不是数据格式选择，而是对机器人学习问题的建模。它们决定策略能够利用哪些信息、需要补偿哪些隐藏变量、输出如何被低层控制器解释，以及实验结果能否迁移到真实系统。相同算法在不同 observation/action interface 下可能对应完全不同的问题。

## Problem Setting

具身观测通常由多模态信号组成：proprioception 提供关节角、速度、力矩和机体姿态；视觉提供 RGB、深度、点云或语义特征；触觉和力/力矩传感器提供接触信息；语言或任务规格定义目标。仿真还可能提供 privileged state，例如物体精确 pose、接触标签和地形高度图。部署策略应明确哪些量来自真实传感器，哪些只用于 critic、teacher 或诊断。

## Formalization

观测可写成乘积空间或字典结构：

$$
o_t = \{q_t, \dot q_t, I_t, f_t, g_t, m_t\},
$$

其中 $q_t,\dot q_t$ 是机器人状态，$I_t$ 是视觉输入，$f_t$ 是力或触觉信号，$g_t$ 是任务目标，$m_t$ 是元数据或模式标志。动作不是直接作用在世界上的抽象变量，而是低层控制器的命令：

$$
u_t = C(a_t, x_t), \quad s_{t+1} \sim P(s_t, u_t),
$$

其中 $C$ 可能是 PD 控制器、逆运动学、全身控制器或安全过滤器。

## System / Algorithmic View

常见动作参数化包括 joint position target、joint velocity、torque、end-effector delta、whole-body velocity command、action chunk 和高层 skill command。位置目标稳定但可能限制动态行为，torque 控制表达力强但对模型误差和安全更敏感，end-effector 动作便于操作任务但隐藏了冗余自由度和碰撞约束。action chunk 可降低决策频率，但会改变 closed-loop 反馈结构。

## Implementation Notes

实现时应记录时间戳、坐标系、归一化统计量、frame stacking、action repeat、控制频率、动作裁剪和 smoothing。观测同步尤其重要：相机、机器人状态和遥操输入若存在不同延迟，简单拼接会制造不可见的时序偏差。动作空间也应记录单位和语义，例如“末端位移”是世界系、机体系还是相机系。

## Experimental Protocol

报告一个机器人学习实验时，应列出：policy 可见观测、critic 或 teacher 使用的额外状态、传感器频率、policy 频率、低层控制频率、动作限幅、动作平滑、坐标系定义和归一化方法。如果实验比较算法，应保持 observation/action interface 不变，否则差异可能来自问题重定义。

## Failure Modes and Limitations

最常见的失败是 privileged information leakage、坐标系混淆、动作饱和和频率不一致。另一个常见问题是训练时观测干净且同步，部署时观测有丢帧、延迟和漂移。动作空间若与数据采集接口不一致，behavior cloning 会学习到不可执行或分布偏移严重的命令。

## References

- Levine et al., "End-to-End Training of Deep Visuomotor Policies": 视觉运动策略的早期代表。
- Peng et al., "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization": 动作接口和动力学随机化相关参考。
- Brohan et al., RT-1: 大规模机器人数据中观测、动作和任务规格的工程化实例。
