# Safety and Resets

## Scope and Motivation

安全和 reset 不是实验外围设施，而是机器人学习系统的一部分。安全策略改变可执行动作集合，reset 策略改变初始状态分布，二者都会影响训练数据、评估结果和实验吞吐。忽略它们会使算法结果不可复现，甚至不可安全部署。

## Problem Setting

机器人实验中的安全约束包括 workspace limit、速度/力/力矩上限、碰撞检测、急停、温度限制、电池状态和人类进入工作区检测。Reset 包括机器人姿态恢复、物体重置、场景清理、校准检查和失败后诊断。对于长时程任务，reset 成本可能超过策略执行时间。

## System / Algorithmic View

安全系统可分为预防、监测和恢复三层。预防层通过动作限幅、控制屏障或规划约束减少危险动作。监测层检测碰撞、跌倒、越界和传感器异常。恢复层执行急停、软复位、人工接管或自动 reset。学习系统必须记录这些事件，否则训练数据和评估统计会混入未说明的人工策略。

## Implementation Notes

每次 episode 应记录 safety state、constraint violation、reset reason、reset duration、human intervention 和 hardware fault。Reset distribution 应被视为任务定义的一部分：如果训练只从人工摆好的容易状态开始，评估就不能声称覆盖自然初始分布。安全过滤器若修改策略动作，应同时记录 raw action 和 filtered action。

## Experimental Protocol

实验报告应包含 wall-clock time、robot uptime、policy execution time、reset time、人工干预时间和失败恢复次数。性能指标应区分 task failure、safety stop、hardware fault 和 operator abort。评估中如果允许人工恢复或中途干预，应明确计入失败或单独报告。

## Failure Modes and Limitations

过强安全过滤器可能让策略看起来稳定，但实际能力来自规则系统。过弱安全策略会增加硬件损坏和数据中断。自动 reset 若只处理常见失败，会让罕见但危险的失败被排除在评估之外。吞吐统计若不包含 reset 和人工时间，会高估真实实验效率。

## References

- Dulac-Arnold et al., "Challenges of Real-World Reinforcement Learning": 真实 RL 中安全和约束问题。
- García and Fernández, "A Comprehensive Survey on Safe Reinforcement Learning": 安全强化学习综述。
- Ray et al., "Benchmarking Safe Exploration in Deep Reinforcement Learning": 安全探索评估参考。
