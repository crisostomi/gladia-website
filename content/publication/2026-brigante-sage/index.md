---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "SAGE: Semantic Audio Generative Encoder"
subtitle: ''
summary: ''
authors:
- brigante
- cerovaz
- marincione
- strano
- zhou
- rodola
- mancusi

tags: []
categories: []
date: '2026-10-03'
lastmod: 2026-10-03T00:00:00
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-10-03T00:00:00'
publication_types:
- '3'
abstract: "Audio autoencoders compress waveforms into compact latent representations that serve as the interface between raw audio and downstream models. Current systems navigate a three-way trade-off between reconstruction quality, semantic structure of the latent space, and inference speed, typically favoring one or two of these at the expense of the others. This paper introduces SAGE, Semantic Audio Generative Encoder: a compact variational autoencoder, trained solely on publicly available music, that shapes its latent by distilling embeddings from a pretrained audio-text model. This 105M-parameter model runs at the inference cost of Stable Audio Open and reaches the listening-test quality of SAME-L, an autoencoder 8x larger and 4x slower, while surpassing both on objective perceptual and distributional metrics of reconstruction. Furthermore, it sets the state of the art on all nineteen probing tasks of latent semantics, in domain and out of domain. These results establish SAGE as a lightweight audio autoencoder that strikes the best balance of the three-way trade-off among those we evaluate, combining high reconstruction fidelity, state-of-the-art semantic structure, and fast inference."

links:
- name: PDF
  url : https://arxiv.org/pdf/2609.32755
- name: Code
  url : https://github.com/francescobrigante/SAGE
- name: Website
  url : https://sage-music.pages.dev/

publication: '*ArXiv preprint*'
---
