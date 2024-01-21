---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'ASIF: Coupled Data Turns Unimodal Models to Multimodal Without Training'
subtitle: ''
summary: ''
authors:
- norelli
- fumero
- maiorca
- moschella
- rodola
- Francesco Locatello

tags:
- '"Computer Science - Machine Learning"'
- 'featured'

categories: []
date: '2023-12-12'
lastmod: 2023-02-06T10:57:46+01:00
featured: false
draft: false
publication_short: "NeurIPS 2023"

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
publishDate: '2023-02-05T09:57:45.717269Z'
publication_types:
- '2'
abstract: CLIP proved that aligning visual and language spaces is key to solving many
  vision tasks without explicit training, but required to train image and text encoders
  from scratch on a huge dataset. LiT improved this by only training the text encoder
  and using a pre-trained vision network. In this paper, we show that a common space
  can be created without any training at all, using single-domain encoders (trained
  with or without supervision) and a much smaller amount of image-text pairs. Furthermore,
  our model has unique properties. Most notably, deploying a new version with updated
  training samples can be done in a matter of seconds. Additionally, the representations
  in the common space are easily interpretable as every dimension corresponds to the
  similarity of the input to a unique entry in the multimodal dataset. Experiments
  on standard zero-shot visual benchmarks demonstrate the typical transfer ability
  of image-text models. Overall, our method represents a simple yet surprisingly strong
  baseline for foundation multi-modal models, raising important questions on their
  data efficiency and on the role of retrieval in machine learning.
  
links:
  - name: PDF
    url: https://arxiv.org/pdf/2210.01738.pdf
  - name: html
    url: https://neurips.cc/virtual/2023/poster/71339
  - name: arXiv
    url: https://arxiv.org/abs/2210.01738
  - name: Poster
    url: https://drive.google.com/file/d/1irucKF7d8LbWfrVFX4vNHL9sVdh3Zu8v/view
  - icon: twitter
    icon_pack: fab
    name: Thread
    url: https://x.com/noranta4/status/1734020892282278210?s=20
  - icon: github
    icon_pack: fab
    name: 'GitHub'
    url: https://github.com/noranta4/ASIF
  - icon:  chalkboard-user
    icon_pack: fas
    name: 'NeurIPS 2023'
    url: https://neurips.cc/virtual/2023/poster/71339

    
publication: '*NeurIPS 2023*'
---
