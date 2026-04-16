# Teleoperation

## Scope and Motivation

Teleoperation is both a source of robot data and a mechanism for online intervention and safety fallback. It couples human strategy, device interface, network latency, and the robot control stack into a single data-generation process. Demonstration quality depends not only on operator skill, but also on whether the command space matches the action space of the learned policy.

## Problem Setting

Teleoperation devices include joysticks, keyboards, VR controllers, motion capture, leader-follower arms, haptic devices, and shared-autonomy interfaces. Device output may represent velocity, end-effector displacement, joint targets, gripper commands, or high-level skill selection. Operator feedback may come from third-person cameras, head-mounted displays, force feedback, or state dashboards. Latency and viewpoint change the demonstration distribution.

## System / Algorithmic View

A teleoperation system can be modeled in three layers: human command $u^H_t$, interface mapping $a_t=M(u^H_t,x_t)$, and robot controller $C(a_t)$. If $M$ differs from the learned policy's deployment action space, demonstrations require relabeling or introduce distribution shift. Shared-autonomy systems mix human and autonomous actions, so mode and arbitration logic must be logged.

## Implementation Notes

Logs should include raw human input, mapped robot action, autonomy mode, operator ID or session, latency estimates, camera viewpoint, intervention reason, and safety events. For intervention data, distinguish demonstration, correction, takeover, and emergency stop. Without these fields, the dataset is difficult to use for DAgger, offline RL, or failure analysis.

## Experimental Protocol

A collection protocol should define task distribution, number of episodes per operator, whether practice episodes are included, whether failed episodes are retained, when manual reset is allowed, and demonstration quality criteria. Teleoperation systems should be evaluated by task success, completion time, number of interventions, operator variability, and latency. If data is used for imitation learning, report alignment between teleoperation and policy action spaces.

## Failure Modes and Limitations

Teleoperation data often contains human bias. Operators may rely on visual cues, choose conservative trajectories, avoid difficult initial states, or correct before visible failure. High latency produces over-smoothed and delayed actions. Leader-follower demonstrations may be feasible on hardware but impossible to reproduce with a low-frequency learned policy.

## References

- Ross et al., "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning": DAgger and interactive correction.
- Fu et al., "Mobile ALOHA": mobile manipulation teleoperation and data collection.
- Argall et al., "A Survey of Robot Learning from Demonstration": classical survey of learning from demonstration.
