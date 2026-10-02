---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "On Emergent Capabilities and Model Merging"
subtitle: ''
summary: ''
authors:
- zhou
- rodola

tags: []
categories: []
date: '2026-09-21'
lastmod: 2026-10-02T00:00:00
featured: false
draft: false
publication_short: "NeurIPS 2026 Workshop NNA (Spotlight)"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-09-29T00:00:00'
publication_types:
- '1'
abstract: "Fine-tuned checkpoints and adapters now fill public repositories, and the most common operation applied to these artifacts is model merging: arithmetic on their weights that assembles capabilities cheaply. We ask what this operation does to emergent capabilities: behaviors an artifact carries that were never an explicit training target. Studying two independent testbeds (activation oracles and emergent-misaligned models) across three model families, we find that the answer is threefold. First, merging preserves an emergent capability that both parents carry: merging two misaligned checkpoints retains most of their broad misalignment across the whole mixing range. Second, merging cannot create an emergent capability that is superadditive in its parents: no weighted merge of two single-task oracles reaches the jointly-trained oracle's auditing ability. Third, when only one parent carries the capability, merging dilutes it faster than the trained capability that accompanies it: the gap is significant in most settings. In short, emergent behaviors of an artifact do not compose the way its trained capability does."

links:
- name: PDF
  url : https://arxiv.org/pdf/2609.24504

publication: '*NeurIPS 2026 Workshop on Neural Network Artifacts as a New Data Modality*'
---
