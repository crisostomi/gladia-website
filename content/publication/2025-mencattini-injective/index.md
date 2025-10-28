---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Language Models are Injective and Hence Invertible"
subtitle: ''
summary: ''
authors:
- Giorgos Nikolaou
- mencattini
- crisostomi
- santilli
- Yannis Panagakis
- rodola

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

tags: 
- 'featured'
categories: []
date: '2025-10-21'
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
abstract: "Transformer components such as non-linear activations and normalization are inherently non-injective, suggesting that different inputs could map to the same output and prevent exact recovery of the input from a model's representations. In this paper, we challenge this view. First, we prove mathematically that transformer language models mapping discrete input sequences to their corresponding sequence of continuous representations are injective and therefore lossless, a property established at initialization and preserved during training. Second, we confirm this result empirically through billions of collision tests on six state-of-the-art language models, and observe no collisions. Third, we operationalize injectivity: we introduce SipIt, the first algorithm that provably and efficiently reconstructs the exact input text from hidden activations, establishing linear-time guarantees and demonstrating exact invertibility in practice. Overall, our work establishes injectivity as a fundamental and exploitable property of language models, with direct implications for transparency, interpretability, and safe deployment."

links:
- name: arXiv
  url : https://arxiv.org/abs/2510.15511

publication: '*ArXiv preprint*'
---