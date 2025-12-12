---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "LoopGen: Training-Free Loopable Music Generation"
subtitle: ''
summary: ''
authors:
- marincione
- strano
- crisostomi
- Roberto Ribuoli
- rodola


# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

tags: []
categories: []
date: '2025-06-07'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "ISMIR 2025"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Loops--short audio segments designed for seamless repetition--are central to many music genres, particularly those rooted in dance and electronic styles. However, current generative music models struggle to produce truly loopable audio, as generating a short waveform alone does not guarantee a smooth transition from its endpoint back to its start, often resulting in audible discontinuities. Loops--short audio segments designed for seamless repetition--are central to many music genres, particularly those rooted in dance and electronic styles. However, current generative music models struggle to produce truly loopable audio, as generating a short waveform alone does not guarantee a smooth transition from its endpoint back to its start, often resulting in audible discontinuities. We address this gap by modifying a non-autoregressive model (MAGNeT) to generate tokens in a circular pattern, letting the model attend to the beginning of the audio when creating its ending. This inference-only approach results in generations that are aware of future context and loop naturally, without the need for any additional training or data. We evaluate the consistency of loop transitions by computing token perplexity around the seam of the loop, observing a 55% improvement. Blind listening tests further confirm significant perceptual gains over baseline methods, improving mean ratings by 70%. Taken together, these results highlight the effectiveness of inference-only approaches in improving generative models and underscore the advantages of non-autoregressive methods for context-aware music generation."

links:
- name: arXiv
  url : https://arxiv.org/abs/2504.04466

publication: '*International Society for Music Information Retrieval Conference*'
---
