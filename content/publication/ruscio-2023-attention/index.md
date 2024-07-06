---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Attention-likelihood relationship in transformers'
subtitle: ''
summary: ''
authors:
- Valeria Ruscio
- maiorca
- Fabrizio Silvestri
tags: []
categories: []
date: '2023-03-15'
lastmod: 2023-03-15T:26:44
featured: false
draft: false
publication_short: ""

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
publishDate: '2023-03-15T:26:44'
publication_types:
- '3'
abstract: 'We analyze how large language models (LLMs) represent out-of-context words, investigating their reliance on the given context to capture their semantics. Our likelihood-guided text perturbations reveal a correlation between token likelihood and attention values in transformer-based language models. Extensive experiments reveal that unexpected tokens cause the model to attend less to the information coming from themselves to compute their representations, particularly at higher layers. These findings have valuable implications for assessing the robustness of LLMs in real-world scenarios. Fully reproducible codebase at https://github.com/Flegyas/AttentionLikelihood .'
publication: '*arXiv preprint arXiv:2303.08288*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url : https://arxiv.org/abs/2303.08288
- name: PDF
  url: https://arxiv.org/pdf/2303.08288.pdf
---
