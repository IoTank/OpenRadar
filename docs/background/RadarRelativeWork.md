---
title: RadarRelativeWork
date: 2020-04-29 15:57:50
img: https://cdn.pixabay.com/photo/2017/11/27/21/31/computer-2982270__340.jpg
categories: AIOT
reprintPolicy: cc_by
cover: false
tags:
  - radar
---

### 1. Super-resolution

> Wang, Jiaming, et al. "Unsupervised Remote Sensing Super-Resolution via Migration Image Prior." *arXiv preprint arXiv:2105.03579* (2021).[论文链接](https://arxiv.org/abs/2105.03579)  [项目链接](https://github.com/jiaming-wang/MIP)

> 文章提出一个全新的无监督学习框架：MIP"，可以在没有低/高分辨率图像对的情况下实现了 SR 任务。首先，将随机噪声图通过一个设计好的生成对抗网络（GAN）进行重建。然后，所提出的方法将参考图像转换为隐空间作为迁移图像的先验。最后，通过隐式方法更新输入噪声，并进一步迁移参考图像的纹理和结构化信息。在 Draper 数据集上的大量实验结果表明，MIP 在数量上和质量上都比最先进的方法有了明显的改进。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210528104811313.png)

### 2. Search

> Kreuziger, Tristan, Mahdyar Ravanbakhsh, and Begüm Demir. "A Novel Triplet Sampling Method for Multi-Label Remote Sensing Image Search and Retrieval." *arXiv preprint arXiv:2105.03647* (2021). [论文链接](https://arxiv.org/abs/2105.03647)  [项目链接](https://git.tu-berlin.de/rsim/image-retrieval-from-triplets)

> 学习遥感（RS）图像之间的相似性是基于内容的RS图像检索（CBIR）的基础.作者在深度神经网络（DNNs）的框架内提出一种新的三联体采样方法，该方法是针对多标签 RS CBIR 问题而定义的。所提出的方法基于两个主要步骤，选择一小部分最具代表性和信息量的三联体。在第一步中，使用迭代算法从当前的小批量中选择一组在嵌入空间中彼此不同的锚点。在第二步中，通过评估相关度、困难度和基于新的排名策略的图像之间的多样性，为每个锚选择不同的正面和负面图像集。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210528105007362.png)

### 3. Align

> **SIPSA-Net: Shift-Invariant Pan Sharpening with Moving Object Alignment for Satellite Imagery** 

> 用于移动目标对齐的 shift-invariant pan-sharpening（SIPSA-Net），是第一个考虑到移动目标区域的这种大的错位来进行 pan-sharpened 方法。通过实验表明，与最先进的方法相比，SIPSA-Net 可以生成 pan-sharpened 图像，在视觉质量和对齐方面有显著的改善。

![](https://gitee.com/github-25970295/blogpictureV2/raw/master/image-20210528105123789.png)