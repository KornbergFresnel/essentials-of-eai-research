# 世界模型的表征学习

世界模型的质量在很大程度上取决于其**潜在表征**——即建模动力学所用的内部空间。本页介绍适用于世界建模的各种表征学习方法。

## 为什么需要表征学习？

直接在观测空间（如原始像素）中建模存在诸多问题：

- **高维度**：图像包含数百万像素，其中大部分是冗余的
- **无关信息**：背景细节、纹理、光照——与动力学无关
- **预测困难**：精确预测像素值极其困难

一个好的表征应该具备以下性质：

- **紧凑性**：低维，仅捕捉与任务相关的信息
- **可预测性**：支持精确的动力学预测
- **解耦性**：分离独立的变化因子
- **可控性**：捕捉智能体能够影响的方面

## 基于重建的方法

### 变分自编码器（VAE）

最常见的方法：通过联合训练编码器和解码器来学习潜在空间。

$$
\mathcal{L}_{\text{VAE}} = \mathbb{E}_{q(z|o)} [\log p(o|z)] - D_{\text{KL}}(q(z|o) \| p(z))
$$

- **编码器** $q_\phi(z|o)$：将观测映射到潜在状态的分布上
- **解码器** $p_\theta(o|z)$：从潜在状态重建观测
- **先验** $p(z)$：通常取 $\mathcal{N}(0, I)$

**应用**：World Models (Ha & Schmidhuber, 2018)、PlaNet、Dreamer (v1)

**优点**：理论成熟、潜在空间光滑、可生成观测

**缺点**：可能学到与动力学无关的特征、重建结果模糊

### VQ-VAE（向量量化变分自编码器）

将连续潜在空间替换为**离散码本**：

$$
z_q = \text{codebook}[\arg\min_k \| z_e(o) - e_k \|]
$$

其中 $\{e_k\}$ 是一组学习到的嵌入向量。

**应用**：DreamerV2（类别离散潜变量）、IRIS、Genie

**对世界模型的优势**：离散 token 使得基于 Transformer 的动力学模型成为可能，并能避免后验塌缩。

## 自监督方法（无需重建）

### 对比学习

通过拉近正样本对（同一观测的不同增强视图）、推远负样本对来学习表征。

**SimCLR / MoCo 风格**：

$$
\mathcal{L}_{\text{contrastive}} = -\log \frac{\exp(\text{sim}(z_i, z_j^+) / \tau)}{\sum_{k} \exp(\text{sim}(z_i, z_k) / \tau)}
$$

**在 RL 中的应用**：CURL（Laskin et al., 2020）将对比学习应用于 RL 观测，在基于像素的控制任务上取得了显著提升。

### 联合嵌入预测架构（JEPA）

**JEPA**（LeCun, 2022; Assran et al., 2023）通过在**嵌入空间**而非像素空间中进行预测来学习表征：

$$
\mathcal{L}_{\text{JEPA}} = \| \text{predictor}(z_x, \text{mask}) - \text{sg}[\bar{z}_y] \|^2
$$

其中 $z_x$ 是上下文编码，$\bar{z}_y$ 是目标编码（来自 EMA 编码器），$\text{sg}$ 表示停止梯度。

**对世界模型的关键优势**：

- 在表征空间（而非像素空间）中预测——聚焦于语义内容
- 避免生成像素——计算效率更高
- 通过潜在空间自然处理多模态未来

### BYOL 与自预测方法

**SPR**（Schwarzer et al., 2021）：用于 RL 的自预测表征。预测未来的潜在状态：

$$
\mathcal{L}_{\text{SPR}} = \sum_{k=1}^{K} \| \text{proj}(\hat{z}_{t+k}) - \text{sg}[\text{proj}(\bar{z}_{t+k})] \|^2
$$

这是 BYOL 的时序版本，其中预测模型在潜在空间中捕捉动力学特征。

## 结构化表征

### 物体中心表征

将场景分解为具有独立属性的离散物体：

- **Slot Attention**（Locatello et al., 2020）：通过迭代注意力机制学习将场景分解为 $K$ 个槽位
- **SAVi**（Kipf et al., 2022）：将 Slot Attention 扩展到视频，具备时序一致性
- **SLATE**（Singh et al., 2022）：将 Slot Attention 与离散自编码相结合

**为什么适用于世界模型**：物理交互本质上是以物体为中心的——物体碰撞、堆叠、掉落。物体中心的表征可以提升泛化能力和组合性。

### 基于图的表征

将世界表示为图结构，节点为实体，边为关系：

- **图神经网络模拟器**（Sanchez-Gonzalez et al., 2020）：通过粒子/物体之间的消息传递学习模拟物理
- **C-SWM**（Kipf et al., 2020）：对比学习的结构化世界模型

## RSSM（循环状态空间模型）

**RSSM**（Hafner et al., 2019）是目前最成功的潜在动力学模型，广泛应用于 Dreamer 系列。它结合了确定性和随机性两个组件：

- **确定性路径** $h_t = f(h_{t-1}, z_{t-1}, a_{t-1})$：通过 GRU 捕捉长期依赖关系
- **随机状态** $z_t \sim q(z_t | h_t, o_t)$：捕捉不确定性和多模态未来
- **先验** $z_t \sim p(z_t | h_t)$：在没有观测的情况下预测（用于想象）

组合状态 $(h_t, z_t)$ 为预测和规划提供了丰富的表征。

### 训练目标

$$
\mathcal{L} = \underbrace{\mathbb{E}_q [\log p(o_t | h_t, z_t)]}_{\text{重建}} + \underbrace{\mathbb{E}_q [\log p(r_t | h_t, z_t)]}_{\text{奖励}} - \underbrace{\beta \, D_{\text{KL}}[q(z_t|h_t, o_t) \| p(z_t|h_t)]}_{\text{KL 正则化}}
$$

## 方法对比

| 方法 | 需要重建 | 感知动力学 | 可扩展性 | 应用 |
|------|---------|-----------|---------|------|
| VAE | 是 | 否（需额外添加） | 中等 | Dreamer v1, PlaNet |
| VQ-VAE | 是 | 否 | 良好 | IRIS, Genie |
| 对比学习 | 否 | 可选 | 良好 | CURL, ATC |
| JEPA | 否 | 是 | 优秀 | V-JEPA |
| RSSM | 是 | 内置 | 中等 | Dreamer v1-v3 |
| 物体中心 | 是 | 可选 | 有限 | C-SWM, SLATE |

## 核心参考文献

- Ha, D. & Schmidhuber, J. (2018). "World Models." *NeurIPS*.
- Hafner, D., et al. (2019). "Learning Latent Dynamics for Planning from Pixels." *ICML*.
- Laskin, M., Srinivas, A., Abbeel, P. (2020). "CURL: Contrastive Unsupervised Representations for Reinforcement Learning." *ICML*.
- Schwarzer, M., et al. (2021). "Data-Efficient Reinforcement Learning with Self-Predictive Representations." *ICLR*.
- LeCun, Y. (2022). "A Path Towards Autonomous Machine Intelligence." *Technical report*.
- Locatello, F., et al. (2020). "Object-Centric Learning with Slot Attention." *NeurIPS*.
