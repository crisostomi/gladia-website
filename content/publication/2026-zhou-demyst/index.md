---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Demystifying Mergeability: Interpretable Properties to Predict Model Merging Success"
subtitle: ''
summary: ''
authors:
- zhou
- Bo Zhao
- Rose Yu
- rodola


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
abstract: "Model merging combines knowledge from separately fine-tuned models, yet success factors remain poorly understood. While recent work treats mergeability as an intrinsic property, we show with an architecture-agnostic framework that it fundamentally depends on both the merging method and the partner tasks. Using linear optimization over a set of interpretable pairwise metrics (e.g., gradient L2 distance), we uncover properties correlating with post-merge performance across four merging methods. We find substantial variation in success drivers (46.7% metric overlap; 55.3% sign agreement), revealing method-specific 'fingerprints'. Crucially, however, subspace overlap and gradient alignment metrics consistently emerge as foundational, method-agnostic prerequisites for compatibility. These findings provide a diagnostic foundation for understanding mergeability and motivate future fine-tuning strategies that explicitly encourage these properties."

links:
- name: arXiv
  url : https://arxiv.org/abs/2601.22285

publication: '*ArXiv preprint*'
---