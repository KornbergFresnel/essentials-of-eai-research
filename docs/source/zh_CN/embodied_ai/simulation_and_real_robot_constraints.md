# 仿真与真实机器人约束

## Scope and Motivation

仿真为具身学习提供可扩展采样、可控扰动和低成本失败，但仿真不是现实的等价替代。真实机器人引入延迟、标定、磨损、热限制、传感器噪声、人类安全和 reset 成本。仿真到真实的差距不仅来自动力学参数误差，也来自任务分布、观测管线和实验操作流程的差异。

## Problem Setting

仿真器通常假设可重复 reset、精确状态读取、理想同步、可控随机种子和可忽略硬件损耗。真实系统中，传感器时间戳可能不同步，执行器响应有带宽限制，接触模型受材料和磨损影响，校准状态会随时间变化。学习算法如果依赖这些仿真假设，部署性能会被高估。

## System / Algorithmic View

sim-to-real 差距可分为五类。动力学差距包括质量、摩擦、关节阻尼、接触模型和柔顺性。感知差距包括渲染、光照、相机噪声和遮挡。执行差距包括 actuator saturation、控制延迟和低层控制器差异。reset 差距包括初始状态分布和人工恢复流程。任务分布差距包括物体、地形、人类干预和环境变化。

Domain randomization 通过扩大训练分布提高鲁棒性，system identification 通过估计真实参数缩小仿真误差。二者不互斥：前者处理不可完全建模的不确定性，后者减少可测量的系统性偏差。

## Implementation Notes

可复现实验应记录仿真器版本、机器人模型、asset 文件、物理参数、contact solver 设置、控制频率、随机化范围、渲染设置和 reset 脚本。真实系统应记录硬件版本、标定流程、控制器版本、传感器频率、网络延迟、维护状态和安全限制。缺少这些信息时，算法结果很难和其他系统比较。

## Experimental Protocol

建议把 simulation-only assumptions 和 deployable assumptions 分开报告。前者包括 privileged state、精确 reset、无延迟控制和完美同步；后者包括真实传感器输入、实际控制频率和安全过滤器。迁移实验应报告仿真性能、带随机化仿真性能、真实系统少量试验结果，以及失败案例分类。

## Failure Modes and Limitations

随机化范围过窄会导致策略过拟合仿真；范围过宽会使训练问题过难并牺牲 nominal performance。system identification 若只匹配短期轨迹，可能无法解释接触切换和长期磨损。仿真中成功的 reset 策略也可能在真实系统中占据主要实验时间，从而改变实际吞吐。

## References

- Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World": 感知随机化代表工作。
- Peng et al., "Sim-to-Real Transfer of Robotic Control with Dynamics Randomization": 动力学随机化在控制中的应用。
- Tan et al., "Sim-to-Real: Learning Agile Locomotion for Quadruped Robots": 四足 locomotion 迁移案例。
