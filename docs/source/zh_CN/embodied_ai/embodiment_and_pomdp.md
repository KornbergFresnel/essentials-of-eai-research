# 具身性与 POMDP 建模

## Scope and Motivation

具身智能中的“环境”不是一个只返回低维状态向量的抽象过程，而是由机器人形态、传感器、执行器、控制器和外部物理世界共同形成的闭环系统。身体形态决定可达动作集合和被动动力学，传感器决定可观测信息，执行器和控制器决定策略输出如何转化为物理作用。因此，具身任务的建模起点通常不是“给定状态 $s_t$”，而是“给定观测历史和受限动作接口时，智能体能否稳定改变世界”。

从这个角度看，POMDP 比完全可观测 MDP 更接近多数机器人问题。真实系统中接触状态、摩擦系数、物体质量、执行器温度、相机外参漂移和人类干预历史往往不可直接观测。即使仿真器能提供完整状态，部署策略通常也只能获得可部署观测。

## Problem Setting

一个具身智能体可以写成闭环过程：

$$
s_{t+1} \sim P(s_{t+1}|s_t, a_t), \quad
o_t \sim O(o_t|s_t), \quad
a_t \sim \pi(a_t|h_t),
$$

其中 $s_t$ 是外部世界和机器人内部状态，$o_t$ 是传感器观测，$h_t=(o_0,a_0,\dots,o_t)$ 是历史。身体形态和低层控制器不只是实现细节；它们改变 $P$、$O$ 和可行动作集合。

## Formalization

在 POMDP 视角下，策略可显式依赖历史，也可依赖估计的 belief state：

$$
b_t(s) = P(s_t=s|h_t), \quad a_t \sim \pi(a_t|b_t).
$$

实际系统中很少显式维护完整 belief。常见近似包括状态估计器、滑动窗口观测、recurrent policy、world model latent state，或由低层控制器隐式吸收部分动态不确定性。关键问题不是选择哪种记忆机制，而是说明哪些隐藏变量会影响决策，以及策略是否有足够信息区分这些变量。

## System / Algorithmic View

从系统角度看，POMDP 建模影响四个接口。第一，policy input 应区分 deployable observation 和 privileged state。第二，日志系统应记录可观测量、隐藏但可离线读取的诊断量、控制命令和安全事件。第三，训练中使用的状态估计或 recurrent module 应在评估时保持相同信息边界。第四，evaluation 应报告在不同初始状态、扰动和传感器条件下的性能，而不是只报告仿真完整状态下的训练回报。

## Implementation Notes

具身 POMDP 的实现错误通常来自信息边界不清。例如，把仿真器中的接触标签、精确物体姿态或未来命令作为 policy 输入，会得到不可部署的策略。相反，如果只给单帧图像和当前关节角，又要求策略推断速度、接触和外力，训练失败可能来自观测不足而不是算法不足。实现文档应明确每个输入字段的来源、频率、延迟、坐标系和部署可用性。

## Failure Modes and Limitations

POMDP 表述能提醒研究者注意隐藏状态，但它不会自动解决估计问题。recurrent policy 可能记忆训练分布中的伪相关，状态估计器可能在接触切换时发散，belief model 也可能在长时程任务中累积误差。对具身任务来说，形式化模型和硬件现实之间始终存在抽象误差；实验报告应把这些误差作为方法边界的一部分。

## References

- Kaelbling, Littman, and Cassandra, "Planning and Acting in Partially Observable Stochastic Domains": POMDP 经典综述。
- Sutton and Barto, *Reinforcement Learning: An Introduction*: MDP、价值函数和策略优化基础。
- Pfeifer and Bongard, *How the Body Shapes the Way We Think*: 具身形态对智能行为的影响。
