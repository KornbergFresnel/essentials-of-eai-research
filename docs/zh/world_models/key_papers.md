# 世界模型关键论文

按主题整理的世界模型领域具有重要影响力的论文列表。

!!! tip "阅读策略"
    优先阅读标记为 **（必读）** 的论文以打好基础，然后根据自身研究方向深入探索相关领域。

## 奠基性世界模型

- **World Models** — Ha & Schmidhuber, NeurIPS 2018. **（必读）**
  VAE + MDN-RNN 世界模型；在"梦境"中训练控制器。

- **Learning Latent Dynamics for Planning from Pixels** — Hafner et al., ICML 2019. **（必读）**
  PlaNet：循环状态空间模型（RSSM）+ 潜在空间中的 CEM 规划。

- **Dream to Control: Learning Behaviors by Latent Imagination** — Hafner et al., ICLR 2020. **（必读）**
  Dreamer：基于 RSSM 的想象力 Actor-Critic 训练。

- **Mastering Atari with Discrete World Models** — Hafner et al., ICLR 2021.
  DreamerV2：离散潜在表征，KL 平衡技术。

- **Mastering Diverse Domains through World Models** — Hafner et al., 2023. **（必读）**
  DreamerV3：symlog 预测，单组超参数横跨多个领域。

## 表征学习

- **Auto-Encoding Variational Bayes** — Kingma & Welling, ICLR 2014. **（必读）**
  VAE 框架——众多世界模型的基础。

- **Neural Discrete Representation Learning** — van den Oord et al., NeurIPS 2017.
  VQ-VAE——许多最新世界模型所采用的离散标记化方法。

- **CURL: Contrastive Unsupervised Representations for Reinforcement Learning** — Laskin et al., ICML 2020.
  面向 RL 表征的对比学习。

- **Data-Efficient Reinforcement Learning with Self-Predictive Representations** — Schwarzer et al., ICLR 2021.
  SPR：自预测时序表征。

- **A Path Towards Autonomous Machine Intelligence** — LeCun, 2022.
  提出 JEPA 作为世界模型的架构。具有广泛影响的愿景论文。

## 视频预测

- **Stochastic Video Generation with a Learned Prior** — Denton & Fergus, ICML 2018.
  SVG：带学习先验的随机视频预测。

- **Stochastic Variational Video Prediction** — Babaeizadeh et al., ICLR 2018.
  SV2P：基于 VAE 的随机视频预测。

- **VideoGPT: Video Generation using VQ-VAE and Transformers** — Yan et al., 2021.
  基于离散 token 的自回归视频生成。

- **Video Diffusion Models** — Ho et al., NeurIPS 2022.
  将扩散模型适配于视频生成。

## 基于学习模型的规划

- **Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models** — Chua et al., NeurIPS 2018.
  PETS：概率集成 + 轨迹采样。

- **When to Trust Your Model: Model-Based Policy Optimization** — Janner et al., NeurIPS 2019.
  MBPO：有原则的短时域模型展开。

- **Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model** — Schrittwieser et al., Nature 2020. **（必读）**
  MuZero：学习模型 + MCTS，无需预测观测。

## 基础世界模型

- **Genie: Generative Interactive Environments** — Bruce et al., ICML 2024. **（必读）**
  从无标签视频中学习可控世界模型；从图片创建可交互环境。

- **Learning Interactive Real-World Simulators** — Yang et al., 2023.
  UniSim：基于多样化数据的通用模拟器。

- **Diffusion for World Modeling: Visual Details Matter in Atari** — Alonso et al., NeurIPS 2024.
  DIAMOND：基于扩散的世界模型，性能可与 DreamerV3 媲美。

- **GAIA-1: A Generative World Model for Autonomous Driving** — Hu et al., 2023.
  面向自动驾驶的世界模型：根据文本、动作和地图条件生成驾驶场景。

## 物体中心与结构化模型

- **Object-Centric Learning with Slot Attention** — Locatello et al., NeurIPS 2020.
  Slot Attention：通过迭代注意力实现无监督物体发现。

- **Contrastively-Trained Structured World Models** — Kipf et al., 2020.
  C-SWM：基于图的结构化世界模型。

- **Learning to Simulate Complex Physics with Graph Networks** — Sanchez-Gonzalez et al., ICML 2020.
  基于 GNN 的物理模拟。

## 视频作为控制的世界模型

- **Transformers are Sample-Efficient World Learners** — Micheli et al., ICLR 2023.
  IRIS：基于 Transformer 和离散 token 的 Atari 世界模型。

- **Learning Universal Policies via Text-Guided Video Generation** — Du et al., NeurIPS 2023.
  UniPi：视频扩散作为通用策略接口。

## 综述

- **Model-based Reinforcement Learning: A Survey** — Moerland et al., 2023.
  全面涵盖模型学习、规划和集成的综合综述。

- **A Survey on Video Prediction: From Deterministic to Generative Approaches** — Oprea et al., 2022.
  视频预测方法与架构综述。
