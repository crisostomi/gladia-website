---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Zero-Shot Duet Singing Voices Separation with Diffusion Models'
subtitle: ''
summary: ''
authors:
- Chin-Yun Yu
- postolache
- rodola
- Gyorgy Fazekas
tags: []
categories: []
date: '2023-11-04'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "SDX 2023"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-10-02T:26:44'
publication_types:
- '3'
abstract: "In recent studies, diffusion models have shown promise as priors for solving audio inverse problems, including source separation. These models allow us to sample from the posterior distribution of a target signal given an observed signal by manipulating the diffusion process. However, when separating audio sources of the same type, such as duet singing voices, the prior learned by the diffusion process may not be sufficient to maintain the consistency of the source identity in the separated audio. For example, the singer may change from one to another from time to time. Tackling this problem will be useful for separating sources in a choir, or a mixture of multiple instruments with similar timbre, without acquiring large amounts of paired data. In this paper, we examine this problem in the context of duet singing voices separation, and propose a method to enforce the coherency of singer identity by splitting the mixture into overlapping segments and performing posterior sampling in an auto-regressive manner, conditioning on the previous segment. We evaluate the proposed method on the MedleyVox dataset with different overlap ratios, and show that the proposed method outperforms naive posterior sampling baseline. Our source code and the pre-trained model are publicly available."
publication: '*Sound Demixing Workshop 2023*'
links:
- name: PDF
  url: https://sdx-workshop.github.io/papers/Yu.pdf
- name: arXiv
  url: https://arxiv.org/abs/2311.07345
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/yoyololicon/duet-svs-diffusion
---