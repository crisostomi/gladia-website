---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Zero-Shot Quantization via Weight-Space Arithmetic"
subtitle: ''
summary: ''
authors:
- solombrino
- gargiulo
- zirilli
- zhou
- minut
- rodola

tags: []
categories: []
date: '2026-04-03'
lastmod: 2026-05-10T:26:44
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-04-03T:26:44'
publication_types:
- '3'
abstract: "We show that robustness to post-training quantization (PTQ) is a transferable direction in weight space. We call this direction the quantization vector: extracted from a donor task by simple weight-space arithmetic, it can be used to patch a receiver model and improve post-PTQ Top-1 accuracy by up to 60 points in a 3-bit setting, without receiver-side quantization-aware training (QAT). Because the method requires no receiver training data, it provides a zero-shot, low-cost alternative to QAT for extremely low-bit deployment. Across four ViT scales and 22 image classification tasks, donor quantization vectors often yield substantial gains even when donor and receiver tasks differ markedly. We further prove rigorously that quantization vectors are well-defined and do not suffer from reparameterization symmetries, and provide a local geometric account of their effect. Together, these results suggest that quantization robustness can be partially isolated, reused, and transferred through simple weight-space algebra."

links:
- name: arXiv
  url : https://arxiv.org/abs/2604.03420
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/dansolombrino/qat-transfer

publication: '*ArXiv preprint*'
---