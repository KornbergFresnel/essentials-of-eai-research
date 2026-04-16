# What Are World Models?

A **world model** is a learned internal representation of environment dynamics that allows an agent to predict future states, reason about consequences of actions, and plan without direct interaction.

## Formal Definition

A world model can be described as a learned function (or set of functions):

$$
\hat{s}_{t+1}, \hat{r}_t = f_\theta(s_t, a_t)
$$

More generally, in the latent space formulation:

- **Encoder**: $z_t = \text{enc}_\theta(o_t)$ — maps observations to latent states
- **Dynamics**: $z_{t+1} = \text{dyn}_\theta(z_t, a_t)$ — predicts next latent state
- **Decoder**: $\hat{o}_t = \text{dec}_\theta(z_t)$ — reconstructs observations (optional)
- **Reward predictor**: $\hat{r}_t = \text{rew}_\theta(z_t, a_t)$ — predicts reward

## The Cognitive Science Perspective

The concept of "mental models" has deep roots in cognitive science:

- **Kenneth Craik (1943)**: Proposed that organisms carry "small-scale models" of the external world, used for prediction and planning
- **Predictive processing**: The brain is fundamentally a prediction machine, constantly generating and updating predictions about sensory input
- **Mental simulation**: Humans can "imagine" the consequences of actions before taking them

World models in AI formalize this intuition: equip artificial agents with the ability to simulate the consequences of their actions internally.

## Types of World Models

### By Prediction Space

| Type | Predicts | Examples |
|------|----------|---------|
| **Observation-space** | Raw pixels/observations $\hat{o}_{t+1}$ | SVG, SV2P, FitVid |
| **Latent-space** | Compact latent state $z_{t+1}$ | Dreamer, RSSM, JEPA |
| **Reward/value only** | Reward $\hat{r}_t$ and/or value $\hat{v}_t$ | MuZero |

### By Architecture

| Architecture | Description | Examples |
|-------------|-------------|---------|
| **RNN-based** | Recurrent dynamics in latent space | World Models (Ha & Schmidhuber), RSSM |
| **Transformer-based** | Sequence model over state-action tokens | IRIS, TransDreamer, Genie |
| **Diffusion-based** | Denoising diffusion for future prediction | UniSim, DIAMOND |
| **State-space models** | Structured state-space layers | S4WM |

### By Scope

| Scope | Description | Examples |
|-------|-------------|---------|
| **Task-specific** | Trained on one environment | Dreamer on DMControl |
| **Domain-specific** | Trained on one domain (e.g., driving) | MILE, GAIA-1 |
| **Foundation** | Trained on diverse data, generalizes broadly | Genie, UniSim |

## Core Challenges

### 1. Compounding Error

Small prediction errors accumulate over long rollouts:

$$
\text{Error at step } H \propto \sum_{t=1}^{H} \epsilon_t \approx H \cdot \bar{\epsilon}
$$

This limits the useful prediction horizon and is addressed via:

- Short rollouts (MBPO)
- Latent-space prediction (reduces dimensionality of error)
- Ensemble disagreement (quantify and manage uncertainty)

### 2. Partial Observability

Real environments are partially observable — the agent doesn't see the full state. World models must infer latent state from observation history:

$$
z_t = f(o_1, a_1, o_2, a_2, \ldots, o_t)
$$

This is typically handled with recurrent architectures (GRU, LSTM, RSSM).

### 3. Multi-Modal Futures

The future is often stochastic — multiple outcomes are possible from the same state and action. Deterministic models collapse to the mean prediction. Stochastic models must capture the distribution of possible futures.

Approaches:

- **VAE-based**: latent stochastic variables $z \sim q(z|o)$
- **Discrete tokens**: categorical distributions (DreamerV2)
- **Diffusion models**: generate diverse samples
- **Mixture models**: explicitly model multiple modes

### 4. Long-Horizon Reasoning

Many tasks require reasoning over long time horizons (hundreds to thousands of steps). Key challenges:

- Compounding error over long rollouts
- Memory requirements
- Capturing long-range dependencies

## A Brief History

| Year | Milestone |
|------|-----------|
| 1991 | **Dyna** (Sutton) — model-based RL framework |
| 2015 | **PILCO** — Gaussian processes for model-based RL |
| 2018 | **World Models** (Ha & Schmidhuber) — VAE+RNN, learning in dreams |
| 2019 | **PlaNet / RSSM** (Hafner et al.) — recurrent state-space model |
| 2020 | **Dreamer** (Hafner et al.) — actor-critic in latent imagination |
| 2020 | **MuZero** (Schrittwieser et al.) — learned model + MCTS |
| 2021 | **DreamerV2** — discrete latent representations |
| 2023 | **DreamerV3** — universal world model across domains |
| 2023-24 | **Foundation world models** — Genie, UniSim, DIAMOND, Cosmos |

## What's Next

- [Representation Learning](representation_learning.md) — How to learn good latent spaces
- [Video Prediction](video_prediction.md) — Predicting visual futures
- [Planning](planning.md) — Using world models for decision-making
- [Foundation World Models](foundation_models.md) — The frontier
