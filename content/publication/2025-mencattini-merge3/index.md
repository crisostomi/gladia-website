---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'MERGE3: Efficient Evolutionary Merging on Consumer-grade GPUs'
subtitle: ''
summary: ''
authors:
- Tommaso Mencattini
- minut
- crisostomi
- santilli
- rodola


# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

tags: []
categories: []
date: '2025-02-27'
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
abstract: "Evolutionary model merging enables the creation of high-performing multi-task models but remains computationally prohibitive for consumer hardware. We introduce MERGE3, an efficient framework that makes evolutionary merging feasible on a single GPU by reducing fitness computation costs 50× while preserving performance. MERGE3 achieves this by Extracting a reduced dataset for evaluation, Estimating model abilities using Item Response Theory (IRT), and Evolving optimal merges via IRT-based performance estimators. Our method enables state-of-the-art multilingual and cross-lingual merging, transferring knowledge across languages with significantly lower computational overhead. We provide theoretical guarantees and an open-source library, democratizing high-quality model merging."

links:
- name: arXiv
  url : https://arxiv.org/abs/2502.10436
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/tommasomncttn/mergenetic

publication: '*ArXiv preprint*'
---