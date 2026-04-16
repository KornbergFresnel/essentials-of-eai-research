# Imitation Learning and Offline Data

## Scope and Motivation

Imitation learning and offline reinforcement learning shift robot training from online trial-and-error to existing data. They are attractive when real robot interaction is expensive, dangerous, or low-throughput. They also impose a distributional constraint: policies are reliable only in state-action regions covered by data. Data quality, action space, and distribution shift are often more important than model capacity.

## Problem Setting

Given a dataset $D=\{(o_t,a_t,r_t,o_{t+1})\}$, behavior cloning learns $\pi_\theta(a|o)$ by matching demonstrated actions. Offline RL attempts to optimize return without further environment interaction. Both face covariate shift: once the learned policy deviates from demonstrations, it may visit states rarely represented in the dataset.

## Formalization

A standard behavior cloning objective is:

$$
\min_\theta \mathbb{E}_{(o,a)\sim D}[-\log \pi_\theta(a|o)].
$$

Offline RL also estimates $Q(o,a)$. If the policy selects actions outside the data distribution, value estimates can be over-optimistic. Many methods therefore add conservatism, policy constraints, or advantage-weighted regression to keep the learned policy close to data support.

## System / Algorithmic View

DAgger-style methods expand the data distribution by executing the current policy and asking an expert for corrections. On robots this requires safe takeover, rapid annotation, and intervention logs. Multimodal demonstrations are another central issue: the same task may have multiple valid actions, and simple mean-squared regression can average across modes. Action relabeling, goal relabeling, and language-conditioned policies can help, but label provenance must be recorded.

## Implementation Notes

Before training, check action units, frequency, latency, episode boundaries, and failure labels. Behavior cloning often requires action smoothing, chunk prediction, normalization, and class-imbalance handling. Offline RL additionally requires rewards, termination signals, discount definitions, behavior policy information, and off-policy evaluation methods. On robots, policy selection should not rely only on offline validation loss, since low loss does not imply closed-loop success.

## Experimental Protocol

Reports should include dataset size, task distribution, success/failure ratio, number of operators, policy action space, train/test split, closed-loop evaluation, and data ablations. For offline RL, report whether any online fine-tuning is performed and whether evaluation uses initial states from the training data.

## Failure Modes and Limitations

The main failure mode of behavior cloning is compounding error under distribution shift. The main failure mode of offline RL is overestimating out-of-distribution actions and relying on unreliable policy evaluation. Dataset bias may teach operator preference rather than task structure. If demonstrations come from a different control interface than deployment, the policy may learn actions that cannot be executed.

## References

- Pomerleau, "ALVINN": early behavior cloning system.
- Ross et al., DAgger: interactive data aggregation for covariate shift.
- Kumar et al., Conservative Q-Learning: conservative value estimation for offline RL.
