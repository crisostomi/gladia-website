---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "The Undetected Damage of Quantization on Retrieval and How to Fix It"
subtitle: ''
summary: ''
authors:
- zhou
- zirilli
- solombrino
- Roberto Dessì
- rodola

tags: []
categories: []
date: '2026-09-27'
lastmod: 2026-09-29T00:00:00
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-09-29T00:00:00'
publication_types:
- '3'
abstract: "We show that a quantized model that keeps its classification accuracy still changes 14 to 46% of its top-1 retrieval results, and that aggregate ranking metrics reveal only part of this damage. We tie this failure to the gap between the two highest model scores and use that gap to decide when to trust a quantized answer and where additional precision should be spent. We show that the top-1 result is guaranteed to survive quantization only when this gap exceeds twice the largest rounding error. In classification, the scores are logits, and training compares the correct class against every other class, which encourages this gap. In retrieval, the scores are query-document similarities, and training compares each positive only against sampled negatives, so nothing separates the top-1 item from the second. This gap can be measured without labels. Before deployment, it predicts which models will break under quantization, and at deployment time it tells, per input, whether the quantized answer still matches the full-precision answer. Most classification inputs have a gap wide enough to trust the quantized answer, but few retrieval queries do. That gap motivates a different fix in each task. In retrieval, spending extra bit-width on the layers whose quantization moves the gap most recovers up to three-quarters of an extra bit's benefit for half its cost. In classification, routing the few low-gap inputs to full precision recovers most of the lost accuracy at a fraction of the cost."

links:
- name: PDF
  url : https://arxiv.org/pdf/2609.24322
- name: Code
  url : https://github.com/LuckerZOfficiaL/Undetected-Damage-of-Quantization

publication: '*ArXiv preprint*'
---
