---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Multi-Way Representation Alignment"
subtitle: ''
summary: ''
authors:
- Akshit Achara
- Tatiana Gaintseva
- Mateo Mahaut
- Pritish Chakraborty
- Viktor Stenby Johansson
- Melih Barsbey
- rodola
- crisostomi


tags: []
categories: []
date: '2026-01-25'
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
abstract: "The Platonic Representation Hypothesis suggests that independently trained neural networks converge to increasingly similar latent spaces. However, current strategies for mapping these representations are inherently pairwise, scaling quadratically with the number of models and failing to yield a consistent global reference. In this paper, we study the alignment of more than 2 models. We first adapt Generalized Procrustes Analysis (GPA) to construct a shared orthogonal universe that preserves the internal geometry essential for tasks like model stitching. We then show that strict isometric alignment is suboptimal for retrieval, where agreement-maximizing methods like Canonical Correlation Analysis (CCA) typically prevail. To bridge this gap, we finally propose Geometry-Corrected Procrustes Alignment (GCPA), which establishes a robust GPA-based universe followed by a post-hoc correction for directional mismatch. Extensive experiments demonstrate that GCPA consistently improves any-to-any retrieval while retaining a practical shared reference space."

links:
- name: arXiv
  url : https://arxiv.org/abs/2602.06205

publication: '*ArXiv preprint*'
---