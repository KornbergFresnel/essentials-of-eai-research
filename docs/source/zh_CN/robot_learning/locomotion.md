# Locomotion

## Scope and Motivation

Locomotion 是机器人学习中最典型的连续控制问题之一。策略必须在接触切换、欠驱动动力学、地形扰动和执行器限制下维持稳定运动。与静态 manipulation 相比，locomotion 的失败通常是系统级的：一次足端接触误差可能在数百毫秒内放大为跌倒，评估也必须覆盖命令分布、地形分布和外部扰动。

## Problem Setting

一个 locomotion 任务通常给定速度命令、目标方向或轨迹，策略输出低层控制命令。观测可能包括 base orientation、angular velocity、joint positions、joint velocities、历史动作、接触估计和局部地形信息。对真实机器人而言，base linear velocity 和足端接触状态未必可靠可测，因此状态估计质量会直接影响策略。

## Formalization

可将命令条件策略写成：

$$
a_t \sim \pi(a_t | o_t, c_t), \quad c_t \sim p(c),
$$

其中 $c_t$ 是速度、转向或姿态命令。奖励通常包含 tracking、energy、stability、smoothness 和 contact 项：

$$
r_t = r_{\mathrm{track}} - \lambda_E E_t - \lambda_\Delta \|a_t-a_{t-1}\|^2 + r_{\mathrm{contact}}.
$$

这些项不是中性的；它们定义了期望 gait、速度范围和能耗偏好。

## System / Algorithmic View

动作接口常见为 joint position target、joint torque、residual action 或高层 gait/velocity command。位置目标配合 PD 控制器更稳定，torque 控制更直接但安全风险更高。很多系统采用 teacher-student、privileged critic 或 terrain encoder：训练时利用地形和动力学参数，部署时用历史观测或感知模块近似。

## Implementation Notes

实现报告应说明控制频率、policy 频率、PD 增益、动作裁剪、命令采样分布、terrain curriculum、termination 条件和 reset 逻辑。足端接触、base velocity 和地形高度图若来自仿真 privileged state，应标记为不可部署输入。真实系统还需要记录电机温度、关节限位、急停策略和跌倒检测。

## Experimental Protocol

评估应覆盖 nominal tracking、速度范围外推、地形变化、推搡扰动和长时程稳定性。指标包括 tracking error、跌倒率、单位距离能耗、足端滑移、恢复时间和硬件安全事件。只报告平均回报会掩盖高风险失败，尤其在真实机器人上。

## Failure Modes and Limitations

常见失败包括 reward hacking、过度依赖平坦地形、动作抖动、电机过热、接触估计错误和 reset 分布过窄。仿真中看似稳定的 gait 可能依赖不真实摩擦或无延迟控制。强 domain randomization 可提高鲁棒性，但也可能牺牲速度和能耗。

## References

- Kumar et al., "RMA: Rapid Motor Adaptation for Legged Robots": 适应性 locomotion 系统。
- Tan et al., "Sim-to-Real: Learning Agile Locomotion for Quadruped Robots": 四足机器人 sim-to-real 案例。
- Peng et al., "Learning Agile Robotic Locomotion Skills by Imitating Animals": gait 学习和动作风格参考。
