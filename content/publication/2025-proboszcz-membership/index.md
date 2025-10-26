---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Membership and Dataset Inference Attacks on Large Audio Generative Models"
subtitle: ''
summary: ''
authors:
- Jakub Proboszcz
- Paweł Kochański
- Karol Korszun
- Katarzyna Stankiewicz
- crisostomi
- strano
- rodola
- Kamil Deja
- Jan Dubiński

tags: []
categories: []
date: '2025-09-23'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "NeurIPS 2025 Workshop AI4Music"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Generative audio models, based on diffusion and autoregressive architectures, have advanced rapidly in both quality and expressiveness. This progress, however, raises pressing copyright concerns, as such models are often trained on vast corpora of artistic and commercial works. A central question is whether one can reliably verify if an artist's material was included in training, thereby providing a means for copyright holders to protect their content. In this work, we investigate the feasibility of such verification through membership inference attacks (MIA) on open-source generative audio models, which attempt to determine whether a specific audio sample was part of the training set. Our empirical results show that membership inference alone is of limited effectiveness at scale, as the per-sample membership signal is weak for models trained on large and diverse datasets. However, artists and media owners typically hold collections of works rather than isolated samples. Building on prior work in text and vision domains, in this work we focus on dataset inference (DI), which aggregates diverse membership evidence across multiple samples. We find that DI is successful in the audio domain, offering a more practical mechanism for assessing whether an artist's works contributed to model training. Our results suggest DI as a promising direction for copyright protection and dataset accountability in the era of large audio generative models."


publication: '*NeurIPS 2025 Workshop on AI for Music*'
---