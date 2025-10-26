---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Two-Scale Latent Dynamics for Recurrent-Depth Transformers"
subtitle: ''
summary: ''
authors:
- pappone
- crisostomi
- rodola


tags: []
categories: []
date: '2025-09-27'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '3'
abstract: "Recurrent-depth transformers scale test-time compute by iterating latent computations before emitting tokens. We study the geometry of these iterates and argue for a simple, two-scale operational picture: (i) within a looped block, updates act as small-scale refinements; (ii) across consecutive blocks, states undergo a larger-scale drift. Across checkpoints, our measurements show that loop steps become smaller and increasingly orthogonal to one another, indicating better local modeling of fine structure rather than merely pushing in a single direction. These dynamics motivate an early-exit mechanism based on the model's second-order difference in step-size, which we show is superior in terms of performance, stability and time-efficiency, when compared to the KL-divergence exit strategy of Geiping et al. and its naive first-order counterpart."

links:
- name: arXiv
  url : https://arxiv.org/abs/2509.23314

publication: '*ArXiv preprint*'
---