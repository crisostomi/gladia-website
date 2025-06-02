---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "MASS: MoErging through Adaptive Subspace Selection"
subtitle: ''
summary: ''
authors:
- crisostomi
- zirilli
- gargiulo
- Maria Sofia Bucarelli
- Simone Scardapane
- Fabrizio Silvestri
- Iacopo Masi
- rodola


# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

tags: []
categories: []
date: '2025-04-06'
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
abstract: "Model merging has recently emerged as a lightweight alternative to ensembling, combining multiple fine-tuned models into a single set of parameters with no additional training overhead. Yet, existing merging methods fall short of matching the full accuracy of separately fine-tuned endpoints. We present MASS (MoErging through Adaptive Subspace Selection), a new approach that closes this gap by unifying multiple fine-tuned models while retaining near state-of-the-art performance across tasks. Building on the low-rank decomposition of per-task updates, MASS stores only the most salient singular components for each task and merges them into a shared model. At inference time, a non-parametric, data-free router identifies which subspace (or combination thereof) best explains an input's intermediate features and activates the corresponding task-specific block. This procedure is fully training-free and introduces only a two-pass inference overhead plus a ~2 storage factor compared to a single pretrained model, irrespective of the number of tasks. We evaluate MASS on CLIP-based image classification using ViT-B-16, ViT-B-32 and ViT-L-14 for benchmarks of 8, 14 and 20 tasks respectively, establishing a new state-of-the-art. Most notably, MASS recovers up to ~98% of the average accuracy of individual fine-tuned models, making it a practical alternative to ensembling at a fraction of the storage cost."

links:
- name: arXiv
  url : https://arxiv.org/abs/2504.05342

publication: '*ArXiv preprint*'
---