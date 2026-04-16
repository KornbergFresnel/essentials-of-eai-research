# Representation Learning for World Models

The quality of a world model depends critically on its **latent representation** — the internal space in which it models dynamics. This page covers the key approaches to learning representations suitable for world modeling.

## Why Representation Learning?

Operating directly in observation space (e.g., raw pixels) is problematic:

- **High dimensionality**: images have millions of pixels, most of which are redundant
- **Irrelevant information**: background details, textures, lighting — not relevant to dynamics
- **Prediction difficulty**: predicting exact pixel values is extremely hard

A good representation should be:

- **Compact**: low-dimensional, capturing only task-relevant information
- **Predictive**: support accurate dynamics prediction
- **Disentangled**: separate independent factors of variation
- **Controllable**: capture aspects that the agent can influence

## Reconstruction-Based Methods

### Variational Autoencoder (VAE)

The most common approach: learn a latent space by jointly training an encoder and decoder.

$$
\mathcal{L}_{\text{VAE}} = \mathbb{E}_{q(z|o)} [\log p(o|z)] - D_{\text{KL}}(q(z|o) \| p(z))
$$

- **Encoder** $q_\phi(z|o)$: maps observations to a distribution over latent states
- **Decoder** $p_\theta(o|z)$: reconstructs observations from latent states
- **Prior** $p(z)$: typically $\mathcal{N}(0, I)$

**Used by**: World Models (Ha & Schmidhuber, 2018), PlaNet, Dreamer (v1)

**Pros**: Well-understood, produces smooth latent spaces, generates observations

**Cons**: May learn features irrelevant to dynamics, blurry reconstructions

### VQ-VAE (Vector-Quantized VAE)

Replaces the continuous latent space with a **discrete codebook**:

$$
z_q = \text{codebook}[\arg\min_k \| z_e(o) - e_k \|]
$$

where $\{e_k\}$ is a learned set of embedding vectors.

**Used by**: DreamerV2 (categorical discrete latents), IRIS, Genie

**Advantages for world models**: Discrete tokens enable Transformer-based dynamics models and avoid posterior collapse.

## Self-Supervised Methods (No Reconstruction)

### Contrastive Learning

Learn representations by pulling together positive pairs (augmented views of the same observation) and pushing apart negative pairs.

**SimCLR / MoCo style**:

$$
\mathcal{L}_{\text{contrastive}} = -\log \frac{\exp(\text{sim}(z_i, z_j^+) / \tau)}{\sum_{k} \exp(\text{sim}(z_i, z_k) / \tau)}
$$

**For RL**: CURL (Laskin et al., 2020) applies contrastive learning to RL observations, showing significant improvement on pixel-based control tasks.

### Joint Embedding Predictive Architecture (JEPA)

**JEPA** (LeCun, 2022; Assran et al., 2023) learns by predicting in **embedding space** rather than pixel space:

$$
\mathcal{L}_{\text{JEPA}} = \| \text{predictor}(z_x, \text{mask}) - \text{sg}[\bar{z}_y] \|^2
$$

where $z_x$ is the context encoding, $\bar{z}_y$ is the target encoding (from an EMA encoder), and $\text{sg}$ denotes stop-gradient.

**Key advantages for world models**:

- Predicts in representation space (not pixel space) — focuses on semantic content
- Avoids generating pixels — more computationally efficient
- Naturally handles multi-modal futures through the latent space

### BYOL and Self-Predictive Methods

**SPR** (Schwarzer et al., 2021): Self-Predictive Representations for RL. Predicts future latent states:

$$
\mathcal{L}_{\text{SPR}} = \sum_{k=1}^{K} \| \text{proj}(\hat{z}_{t+k}) - \text{sg}[\text{proj}(\bar{z}_{t+k})] \|^2
$$

This is a temporal version of BYOL, where the prediction model captures dynamics in latent space.

## Structured Representations

### Object-Centric Representations

Decompose scenes into discrete objects with individual properties:

- **Slot Attention** (Locatello et al., 2020): Learns to decompose scenes into $K$ slots via iterative attention
- **SAVi** (Kipf et al., 2022): Extends slot attention to video with temporal consistency
- **SLATE** (Singh et al., 2022): Combines slot attention with discrete autoencoding

**Why for world models**: Physical interactions are fundamentally object-centric — objects collide, stack, fall. Object-centric representations can improve generalization and compositionality.

### Graph-Based Representations

Represent the world as a graph where nodes are entities and edges are relations:

- **Graph Neural Network Simulators** (Sanchez-Gonzalez et al., 2020): Learn to simulate physics by message-passing between particles/objects
- **C-SWM** (Kipf et al., 2020): Contrastively-learned structured world models

## The RSSM (Recurrent State-Space Model)

The **RSSM** (Hafner et al., 2019) is the most successful latent dynamics model, used across the Dreamer family. It combines deterministic and stochastic components:

- **Deterministic path** $h_t = f(h_{t-1}, z_{t-1}, a_{t-1})$: captures long-term dependencies via GRU
- **Stochastic state** $z_t \sim q(z_t | h_t, o_t)$: captures uncertainty and multi-modal futures
- **Prior** $z_t \sim p(z_t | h_t)$: predicted without observation (for imagination)

The combined state $(h_t, z_t)$ provides a rich representation for both prediction and planning.

### Training Objective

$$
\mathcal{L} = \underbrace{\mathbb{E}_q [\log p(o_t | h_t, z_t)]}_{\text{reconstruction}} + \underbrace{\mathbb{E}_q [\log p(r_t | h_t, z_t)]}_{\text{reward}} - \underbrace{\beta \, D_{\text{KL}}[q(z_t|h_t, o_t) \| p(z_t|h_t)]}_{\text{KL regularization}}
$$

## Comparison of Approaches

| Approach | Reconstruction | Dynamics-aware | Scalable | Used by |
|----------|---------------|---------------|----------|---------|
| VAE | Yes | No (add separately) | Moderate | Dreamer v1, PlaNet |
| VQ-VAE | Yes | No | Good | IRIS, Genie |
| Contrastive | No | Optional | Good | CURL, ATC |
| JEPA | No | Yes | Excellent | V-JEPA |
| RSSM | Yes | Built-in | Moderate | Dreamer v1-v3 |
| Object-centric | Yes | Optional | Limited | C-SWM, SLATE |

## Key References

- Ha, D. & Schmidhuber, J. (2018). "World Models." *NeurIPS*.
- Hafner, D., et al. (2019). "Learning Latent Dynamics for Planning from Pixels." *ICML*.
- Laskin, M., Srinivas, A., Abbeel, P. (2020). "CURL: Contrastive Unsupervised Representations for Reinforcement Learning." *ICML*.
- Schwarzer, M., et al. (2021). "Data-Efficient Reinforcement Learning with Self-Predictive Representations." *ICLR*.
- LeCun, Y. (2022). "A Path Towards Autonomous Machine Intelligence." *Technical report*.
- Locatello, F., et al. (2020). "Object-Centric Learning with Slot Attention." *NeurIPS*.
