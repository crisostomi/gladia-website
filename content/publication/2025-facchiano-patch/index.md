---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Activation Patching for Interpretable Steering in Music Generation"
subtitle: ''
summary: ''
authors:
- facchiano
- strano
- crisostomi
- tallini
- mencattini
- Fabio Galasso
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
abstract: "Understanding how large audio models represent music, and using that understanding to steer generation, is both challenging and underexplored. Inspired by mechanistic interpretability in language models, where direction vectors in transformer residual streams are key to model analysis and control, we investigate similar techniques in the audio domain. This paper presents the first study of latent direction vectors in large audio models and their use for continuous control of musical attributes in text-to-music generation. Focusing on binary concepts like tempo (fast vs. slow) and timbre (bright vs. dark), we compute steering vectors using the difference-in-means method on curated prompt sets. These vectors, scaled by a coefficient and injected into intermediate activations, allow fine-grained modulation of specific musical traits while preserving overall audio quality. We analyze the effect of steering strength, compare injection strategies, and identify layers with the greatest influence. Our findings highlight the promise of direction-based steering as a more mechanistic and interpretable approach to controllable music generation."

links:
- name: arXiv
  url : https://arxiv.org/abs/2504.04479

publication: '*ArXiv preprint*'
---