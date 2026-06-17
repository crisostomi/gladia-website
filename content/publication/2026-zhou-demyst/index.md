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
date: '2026-04-30'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "ICML 2026"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Model merging combines knowledge from separately fine-tuned models, yet the factors driving its success remain poorly understood. While recent work treats mergeability as an intrinsic property of the models, we show with an architecture-agnostic framework that it fundamentally depends on both the merging method and the partner tasks. Using L1-regularized linear optimization over a set of interpretable pairwise metrics (e.g., gradient L_2 distance), we uncover properties correlating with post-merge normalized accuracy across five merging methods. We find architecture- and method-specific variation in success drivers (64.0% average top-5 metric overlap; 79.3% sign agreement), with certain methods, notably TIES, exhibiting distinct ``fingerprints'' that diverge from the broader consensus. Crucially, however, gradient alignment metrics consistently emerge as the most fundamental signals of compatibility. These findings provide a diagnostic foundation for understanding mergeability and motivate future merge-aware fine-tuning strategies."

links:
- name: arXiv
  url : https://arxiv.org/abs/2601.22285

publication: '*Proceedings of the 43rd International Conference on Machine Learning*'
---