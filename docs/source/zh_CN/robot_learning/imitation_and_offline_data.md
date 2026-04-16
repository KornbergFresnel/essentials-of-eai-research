# Imitation Learning and Offline Data

## Scope and Motivation

模仿学习和离线强化学习将机器人训练从在线试错转向已有数据。它们适合真实机器人中昂贵、危险或低吞吐的任务，但也引入数据分布约束：策略只能可靠学习数据覆盖过的状态-动作区域。数据质量、动作空间和分布偏移往往比模型容量更关键。

## Problem Setting

给定数据集 $D=\{(o_t,a_t,r_t,o_{t+1})\}$，behavior cloning 学习 $\pi_\theta(a|o)$ 以拟合演示动作。离线 RL 试图在不继续与环境交互的情况下优化回报。两者都面临 covariate shift：策略一旦偏离演示轨迹，会访问训练数据中少见的状态。

## Formalization

BC 的典型目标为：

$$
\min_\theta \mathbb{E}_{(o,a)\sim D}[-\log \pi_\theta(a|o)].
$$

离线 RL 还需要估计 $Q(o,a)$，但如果策略选择数据分布外动作，价值估计可能过高。因此许多方法加入 conservatism、policy constraint 或 advantage-weighted regression，限制策略不要离数据支持太远。

## System / Algorithmic View

DAgger 式方法通过让当前策略执行并由专家纠错来扩展数据分布。对于机器人，这需要安全接管、快速标注和干预日志。多模态演示是另一个核心问题：同一任务可能有多个有效动作，简单均方误差会平均掉策略模式。action relabeling、goal relabeling 和 language-conditioned policy 可缓解部分问题，但需要严格记录标签来源。

## Implementation Notes

训练前应检查动作单位、频率、延迟、episode 边界和失败标签。BC 通常需要处理 action smoothing、chunk prediction、normalization 和 class imbalance。离线 RL 需要额外记录 reward、termination、discount、数据策略和 off-policy evaluation 方法。真实机器人上应避免仅凭离线验证损失选择策略，因为低损失不等价于闭环成功。

## Experimental Protocol

报告应包含数据规模、任务分布、成功/失败比例、操作者数量、policy action space、train/test split、closed-loop evaluation 和数据 ablation。对于 offline RL，应报告是否进行任何在线 fine-tuning，以及评估是否使用训练数据中的初始状态。

## Failure Modes and Limitations

BC 的主要失败是误差累积和分布偏移；offline RL 的主要失败是 OOD action 价值高估和评估不可靠。数据集偏差可能让策略只学会操作者偏好而非任务本质。若示教动作来自与部署不同的控制接口，策略可能学到无法执行的动作。

## References

- Pomerleau, "ALVINN": behavior cloning 的早期代表。
- Ross et al., DAgger: 交互式数据聚合以缓解 covariate shift。
- Kumar et al., Conservative Q-Learning: 离线 RL 中的保守价值估计。
