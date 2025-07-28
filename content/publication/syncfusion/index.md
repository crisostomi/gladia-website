---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'SyncFusion: Multimodal Onset-synchronized Video-to-Audio Foley Synthesis'
subtitle: ''
summary: ''
authors:
- Marco Comunità
- Riccardo F. Gramaccioni
- postolache
- rodola
- Danilo Comminiello
- Joshua D. Reiss
tags:
- Signal Processing
- Sound Effects Synthesis
- Audio-video Synchronization
categories: []
date: '2024-04-19'
lastmod: 2024-05-05T11:38:43+01:00
featured: false
draft: false
publication_short: "ICASSP 2024"
links:
- name: 'PDF'
  url: https://ieeexplore.ieee.org/abstract/document/10447063
- icon: link
  icon_pack: fas
  name: 'URL'
  url : https://mcomunita.github.io/syncfusion-webpage/
- name: 'arXiv'
  url: https://arxiv.org/abs/2310.15247
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/mcomunita/syncfusion

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-05-05T10:38:42.817844Z'
publication_types:
- '1'
abstract: "Sound design involves creatively selecting, recording, and editing sound effects for various media like cinema, video games, and virtual/augmented reality. One of the most time-consuming steps when designing sound is synchronizing audio with video. In some cases, environmental recordings from video shoots are available, which can aid in the process. However, in video games and animations, no reference audio exists, requiring manual annotation of event timings from the video. We propose a system to extract repetitive actions onsets from a video, which are then used - in conjunction with audio or textual embeddings - to condition a diffusion model trained to generate a new synchronized sound effects audio track. In this way, we leave complete creative control to the sound designer while removing the burden of synchronization with video. Furthermore, editing the onset track or changing the conditioning embedding requires much less effort than editing the audio track itself, simplifying the sonification process. We provide sound examples, source code, and pretrained models to facilitate reproducibility."
publication: '*Proc. ICASSP*'
---
