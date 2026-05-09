---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "PHALAR: Phasors for Learned Musical Audio Representations"
subtitle: ''
summary: 'We train a contrastive learning music model for stem retrieval, it achieves state-of-the-art due to its phase-aware architecture.'
authors:
- marincione
- mancusi
- strano
- cerovaz
- crisostomi
- Roberto Ribuoli
- rodola


tags: []
categories: []
date: '2026-05-09'
lastmod: ''
featured: false
draft: false
publication_short: "ICML 2026"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-05-05T16:19:58'
publication_types:
- '1'
abstract: "Stem retrieval, the task of matching missing stems to a given audio submix, is a key challenge currently limited by models that discard temporal information. We introduce PHALAR, a contrastive framework achieving a relative accuracy increase of up to 70% over the state-of-the-art while requiring <50% of the parameters and a 7× training speedup. By utilizing a Learned Spectral Pooling layer and a complex-valued head, PHALAR enforces pitch-equivariant and phase-equivariant biases. PHALAR establishes new retrieval state-of-the-art across MoisesDB, Slakh, and ChocoChorales, correlating significantly higher with human coherence judgment than semantic baselines. Finally, zero-shot beat tracking and linear chord probing confirm that PHALAR captures robust musical structures beyond the retrieval task."

links:
- name: arXiv
  url : https://arxiv.org/abs/2605.03929
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=7sYtYeiJan
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/gladia-research-group/phalar

publication: '*Proceedings of the 43rd International Conference on Machine Learning*'
---