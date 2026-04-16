# 具身智能评估协议

## Scope and Motivation

具身智能评估不能只依赖训练回报。奖励函数常包含 shaping terms，reset 和 termination 规则会影响回报，安全过滤器可能掩盖策略失败，仿真状态可能提供真实系统不可用的信息。因此，评估协议应把任务成功、鲁棒性、泛化、安全和系统吞吐分开报告。

## Problem Setting

评估对象不是孤立策略，而是包含观测管线、低层控制器、安全监控和 reset 流程的完整系统。一个策略在固定初始状态和无扰动环境中成功，并不说明它能处理不同物体、地形、光照、接触条件或传感器延迟。

## Formalization

可以将评估分布写成：

$$
\xi \sim p_{\mathrm{eval}}(\xi), \quad \tau \sim P(\tau|\pi,\xi),
$$

其中 $\xi$ 包含任务参数、初始状态、场景、物体、地形和扰动。报告指标应同时覆盖成功率 $P(\mathrm{success})$、平均回报、完成时间、安全违规次数、能耗和恢复行为。

## Experimental Protocol

评估集应从训练分布中显式划分。可划分的维度包括任务目标、场景、地形、物体实例、初始状态、外部扰动和传感器条件。每个维度都应说明是 interpolation、extrapolation 还是 in-distribution 评估。统计报告应包含 episode 数、随机种子、环境变体数和置信区间或标准误。

## Failure Modes and Limitations

常见 evaluation leakage 包括：评估策略使用 privileged state，reset policy 把失败状态排除在外，early termination 使危险行为不会计入后续指标，成功阈值在方法调参后被修改，以及人工干预未记录。另一个风险是只报告 aggregate success rate，而不分析失败类型。

## Connections to Literature

具身评估应结合强化学习的 seed/return 报告规范、机器人学的任务成功和安全指标，以及数据集评估中的 train/test split 思想。对于机器人系统，qualitative failure analysis 不是附录，而是解释算法边界的重要证据。

## References

- Henderson et al., "Deep Reinforcement Learning That Matters": RL 实验可复现性和统计报告。
- Dulac-Arnold et al., "Challenges of Real-World Reinforcement Learning": 真实系统中的约束、延迟和安全问题。
- Agarwal et al., "Deep Reinforcement Learning at the Edge of the Statistical Precipice": 聚合指标和统计不确定性分析。
