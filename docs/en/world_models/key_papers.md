# Key Papers in World Models

A curated reading list of influential papers in world models, organized by topic.

!!! tip "Reading Strategy"
    Start with papers marked **(essential)** for the foundations, then explore areas relevant to your research.

## Foundational World Models

- **World Models** — Ha & Schmidhuber, NeurIPS 2018. **(essential)**
  VAE + MDN-RNN for learning a world model; training a controller in "dreams."

- **Learning Latent Dynamics for Planning from Pixels** — Hafner et al., ICML 2019. **(essential)**
  PlaNet: Recurrent State-Space Model (RSSM) + CEM planning in latent space.

- **Dream to Control: Learning Behaviors by Latent Imagination** — Hafner et al., ICLR 2020. **(essential)**
  Dreamer: actor-critic training in imagination using RSSM.

- **Mastering Atari with Discrete World Models** — Hafner et al., ICLR 2021.
  DreamerV2: discrete latent representations, KL balancing.

- **Mastering Diverse Domains through World Models** — Hafner et al., 2023. **(essential)**
  DreamerV3: symlog predictions, single hyperparameter set across many domains.

## Representation Learning

- **Auto-Encoding Variational Bayes** — Kingma & Welling, ICLR 2014. **(essential)**
  The VAE framework — foundational for many world models.

- **Neural Discrete Representation Learning** — van den Oord et al., NeurIPS 2017.
  VQ-VAE — discrete tokenization used by many recent world models.

- **CURL: Contrastive Unsupervised Representations for Reinforcement Learning** — Laskin et al., ICML 2020.
  Contrastive learning for RL representations.

- **Data-Efficient Reinforcement Learning with Self-Predictive Representations** — Schwarzer et al., ICLR 2021.
  SPR: self-predictive temporal representations.

- **A Path Towards Autonomous Machine Intelligence** — LeCun, 2022.
  Proposes JEPA as the architecture for world models. Influential vision paper.

## Video Prediction

- **Stochastic Video Generation with a Learned Prior** — Denton & Fergus, ICML 2018.
  SVG: stochastic video prediction with learned prior.

- **Stochastic Variational Video Prediction** — Babaeizadeh et al., ICLR 2018.
  SV2P: VAE-based stochastic video prediction.

- **VideoGPT: Video Generation using VQ-VAE and Transformers** — Yan et al., 2021.
  Autoregressive video generation with discrete tokens.

- **Video Diffusion Models** — Ho et al., NeurIPS 2022.
  Adapts diffusion models to video generation.

## Planning with Learned Models

- **Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models** — Chua et al., NeurIPS 2018.
  PETS: probabilistic ensembles + trajectory sampling.

- **When to Trust Your Model: Model-Based Policy Optimization** — Janner et al., NeurIPS 2019.
  MBPO: principled short-horizon model rollouts.

- **Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model** — Schrittwieser et al., Nature 2020. **(essential)**
  MuZero: learned model + MCTS, no observation prediction needed.

## Foundation World Models

- **Genie: Generative Interactive Environments** — Bruce et al., ICML 2024. **(essential)**
  Learns controllable world model from unlabeled video; creates playable environments from images.

- **Learning Interactive Real-World Simulators** — Yang et al., 2023.
  UniSim: universal simulator from diverse data.

- **Diffusion for World Modeling: Visual Details Matter in Atari** — Alonso et al., NeurIPS 2024.
  DIAMOND: diffusion-based world model competitive with DreamerV3.

- **GAIA-1: A Generative World Model for Autonomous Driving** — Hu et al., 2023.
  World model for driving: generates scenarios conditioned on text, action, and map.

## Object-Centric and Structured Models

- **Object-Centric Learning with Slot Attention** — Locatello et al., NeurIPS 2020.
  Slot Attention: unsupervised object discovery via iterative attention.

- **Contrastively-Trained Structured World Models** — Kipf et al., 2020.
  C-SWM: graph-based structured world models.

- **Learning to Simulate Complex Physics with Graph Networks** — Sanchez-Gonzalez et al., ICML 2020.
  GNN-based physics simulation.

## Video as World Model for Control

- **Transformers are Sample-Efficient World Learners** — Micheli et al., ICLR 2023.
  IRIS: Transformer world model with discrete tokens for Atari.

- **Learning Universal Policies via Text-Guided Video Generation** — Du et al., NeurIPS 2023.
  UniPi: video diffusion as universal policy interface.

## Surveys

- **Model-based Reinforcement Learning: A Survey** — Moerland et al., 2023.
  Comprehensive survey covering model learning, planning, and integration.

- **A Survey on Video Prediction: From Deterministic to Generative Approaches** — Oprea et al., 2022.
  Survey of video prediction methods and architectures.
