---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Model Merging Improves Zero-Shot Generalization in Bioacoustic Foundation Models"
subtitle: ''
summary: ''
authors:
- marincione
- crisostomi
- Roberto Dessi
- rodola
- rossi

tags: []
categories: []
date: '2025-10-02'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "NeurIPS 2025 Workshop AiForAnimalComms"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Foundation models capable of generalizing across species and tasks represent a promising new frontier in bioacoustics, with NatureLM being one of the most prominent examples. While its domain-specific fine-tuning yields strong performance on bioacoustic benchmarks, we observe that it also introduces trade-offs in instruction-following flexibility. For instance, NatureLM achieves high accuracy when prompted for either the common or scientific name individually, but its accuracy drops significantly when both are requested in a single prompt. We address this by applying a simple model merging strategy that interpolates NatureLM with its base language model, recovering instruction-following capabilities with minimal loss of domain expertise. Finally, we show that the merged model exhibits markedly stronger zero-shot generalization, achieving over a 200% relative improvement and setting a new state-of-the-art in closed-set zero-shot classification of unseen species."

links:
- name: arXiv
  url: https://arxiv.org/abs/2511.05171
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=8YmupGWwvl
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/gladia-research-group/model-merging-NatureLM-audio
- icon: award
  icon_pack: fas
  name: 'Spotlight (top 15%)'

publication: '*NeurIPS 2025 Workshop on AI for non-human animal communication*'
---