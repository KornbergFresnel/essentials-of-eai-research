# Teleoperation

## Scope and Motivation

Teleoperation 既是机器人数据来源，也是在线干预和安全 fallback。它把人类策略、设备接口、网络延迟和机器人控制栈耦合到同一个数据生成过程。遥操数据的质量不只取决于操作者技能，也取决于命令空间是否与学习策略的动作空间一致。

## Problem Setting

遥操设备包括 joystick、keyboard、VR controller、motion capture、leader-follower arm、触觉设备和共享自治接口。设备输出可能是速度、末端位移、关节目标、gripper command 或高层 skill selection。操作者看到的反馈可能来自第三视角相机、头戴显示器、力反馈或状态面板。延迟和视角会改变示教分布。

## System / Algorithmic View

遥操系统可写成三层：human command $u^H_t$，接口映射 $a_t = M(u^H_t, x_t)$，机器人控制器 $C(a_t)$。如果 $M$ 与学习策略部署时使用的 action space 不一致，示教数据需要 relabeling 或会引入分布偏移。共享自治系统还会混合人类动作和自动策略动作，因此必须记录 mode 和 arbitration 逻辑。

## Implementation Notes

日志应记录原始人类输入、映射后的机器人动作、autonomy mode、操作者 ID 或 session、延迟估计、相机视角、干预原因和安全事件。对于 intervention data，应区分主动示教、纠错、接管和 emergency stop。没有这些字段时，数据很难用于 DAgger、offline RL 或失败分析。

## Experimental Protocol

采集协议应定义任务分布、每个操作者的 episode 数、练习阶段是否计入数据、失败 episode 是否保留、何时允许人工 reset，以及示教质量标准。评估遥操系统时应报告 task success、完成时间、干预次数、operator variability 和 latency。若用于模仿学习，应报告示教动作空间与 policy action space 的一致性。

## Failure Modes and Limitations

遥操数据常包含人类偏差：操作者可能依赖视觉线索、采取保守轨迹、避开困难初始状态或在失败前主动纠正。高延迟会产生过度平滑和滞后动作。leader-follower 系统可能使演示轨迹在硬件上可行，但在 learned policy 的低频动作接口下不可复现。

## References

- Ross et al., "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning": DAgger 和交互式纠错。
- Fu et al., "Mobile ALOHA": 移动操作遥操与数据采集系统。
- Argall et al., "A Survey of Robot Learning from Demonstration": 从示教学习的经典综述。
