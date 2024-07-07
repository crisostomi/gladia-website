---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Generalized Multi-Source Inference for Text Conditioned Music Diffusion Models
subtitle: ''
summary: ''
authors:
- postolache
- mariani
- Emmanouil Benetos
- cosmo
- rodola
tags:
- Signal Processing
- Music Generation
- Source Separation
categories: []
date: '2024-04-18'
lastmod: 2024-05-05T11:38:43+01:00
featured: false
draft: false
publication_short: "ICASSP 2024"
links:
- name: 'arXiv'
  url: https://arxiv.org/abs/2210.12108 

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
publishDate: '2023-02-06T10:38:42.817844Z'
publication_types:
- '1'
abstract: 'Multi-Source Diffusion Models (MSDM) allow for compositional musical generation tasks: generating a set of coherent sources, creating accompaniments, and performing source separation. Despite their versatility, they require estimating the joint distribution over the sources, necessitating pre-separated musical data, which is rarely available, and fixing the number and type of sources at training time. This paper generalizes MSDM to arbitrary time-domain diffusion models conditioned on text embeddings. These models do not require separated data as they are trained on mixtures, can parameterize an arbitrary number of sources, and allow for rich semantic control. We propose an inference procedure enabling the coherent generation of sources and accompaniments. Additionally, we adapt the Dirac separator of MSDM to perform source separation. We experiment with diffusion models trained on Slakh2100 and MTG-Jamendo, showcasing competitive generation and separation results in a relaxed data setting.'
publication: '*Proc. ICASSP*'
---
