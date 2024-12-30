---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'COCOLA: Coherence-Oriented Contrastive Learning of Musical Audio Representations'
subtitle: ''
summary: ''
authors:
- Ruben Ciranni
- mariani
- mancusi
- postolache
- Giorgio Fabbro
- rodola
- cosmo
tags: []
categories: []
date: '2024-12-30'
lastmod: 2023-10-02T:26:44
featured: false
draft: false
publication_short: "ICASSP 2025"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-10-02T:26:44'
publication_types:
- '3'
abstract: "We present COCOLA (Coherence-Oriented Contrastive Learning for Audio), a contrastive learning method for musical audio representations that captures the harmonic and rhythmic coherence between samples. Our method operates at the level of stems (or their combinations) composing music tracks and allows the objective evaluation of compositional models for music in the task of accompaniment generation. We also introduce a new baseline for compositional music generation called CompoNet, based on ControlNet, generalizing the tasks of MSDM, and quantify it against the latter using COCOLA. We release all models trained on public datasets containing separate stems (MUSDB18-HQ, MoisesDB, Slakh2100, and CocoChorales)."
publication: '*Proc. ICASSP*'
links:
- name: arXiv
  url : https://arxiv.org/abs/2404.16969
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/gladia-research-group/cocola
---