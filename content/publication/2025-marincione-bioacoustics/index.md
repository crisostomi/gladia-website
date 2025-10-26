---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Model Merging Enables In-Context Learning for Bioacoustics Foundation Models"
subtitle: ''
summary: ''
authors:
- marincione
- crisostomi
- Roberto Dessi
- rodola
- Emanuele Rossi

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
abstract: "General-purpose foundation models capable of generalizing across species and tasks represent a promising new frontier in bioacoustics, with NATURELM-AUDIO being one of the most prominent examples. While its domain-specific finetuning yields strong performance on bioacoustic benchmarks, we observe that it also introduces trade-offs in instruction-following flexibility. For instance, NATURELM-AUDIO achieves high accuracy when prompted for either the common or scientific name individually, but its accuracy drops significantly when both are requested in a single prompt. These effects limit zero- and few-shot generalization to novel tasks. We address this by applying a simple model merging strategy that interpolates NATURELM-AUDIO with its base language model, recovering instruction-following capabilities with minimal loss of domain expertise. Finally, we show that this enables effective few-shot in-context learning, a key capability for real-world scenarios where labeled data for new species or environments are scarce."

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=8YmupGWwvl

publication: '*NeurIPS 2025 Workshop on AI for non-human animal communication*'
---