---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Latent spectral regularization for continual learning'
subtitle: ''
summary: ''
authors:
- Emanuele Frascaroli
- Riccardo Benaglia
- Matteo Boschini
- moschella
- Cosimo Fiorini
- rodola
- Simone Calderara
tags:
- 'continual learning'
- 'spectral methods'
categories: []
date: '2024-04-01'
lastmod: 2023-02-05T10:57:53+01:00
featured: false
draft: false
publication_short: "PRL"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-05T09:57:52.951304Z'
publication_types:
- '2'
abstract: "While biological intelligence grows organically as new knowledge is gathered throughout life, Artificial Neural Networks forget catastrophically whenever they face a changing training data distribution. Rehearsal-based Continual Learning (CL) approaches have been established as a versatile and reliable solution to overcome this limitation; however, sudden input disruptions and memory constraints are known to alter the consistency of their predictions. We study this phenomenon by investigating the geometric characteristics of the learner’s latent space and find that replayed data points of different classes increasingly mix up, interfering with classification. Hence, we propose a geometric regularizer that enforces weak requirements on the Laplacian spectrum of the latent space, promoting a partitioning behavior. Our proposal, called Continual Spectral Regularizer for Incremental Learning (CaSpeR-IL), can be easily combined with any rehearsal-based CL approach and improves the performance of SOTA methods on standard benchmarks."
publication: '*Pattern Recognition Letters*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://www.sciencedirect.com/science/article/pii/S0167865524001909
- name: arXiv
  url: https://arxiv.org/abs/2301.03345
---
