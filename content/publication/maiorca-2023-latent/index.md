---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Latent Space Translation via Semantic Alignment'
subtitle: ''
summary: ''
authors:
- maiorca
- moschella
- norelli
- fumero
- Francesco Locatello
- rodola

tags:
- '"Computer Science - Machine Learning"'

categories: []
date: '2023-09-30'
lastmod: 2022-09-30T11:32:00+02:00
featured: false
draft: false
publication_short: "NeurIPS 2023"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: 'Left'
  preview_only: false

links:
- name: 'PDF'
  url: https://openreview.net/pdf?id=pBa70rGHlr
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openreview.net/forum?id=pBa70rGHlr
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/Flegyas/latent-translation

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2022-04-28T10:30:59.888843Z'
# https://docs.citationstyles.org/en/stable/specification.html#namespacing
publication_types:
- '1'
abstract: 'Different neural models often exhibit similar latent spaces when exposed to semantically similar data; however, this inherent similarity may not always be immediately apparent. Leveraging this observation, our work shows how representations learned from these neural modules can be translated between different pre-trained networks via simpler transformations than previously thought. An advantage of this approach is the ability to estimate these transformations using standard, well-understood algebraic procedures that have closed-form solutions. Our method directly estimates a transformation between two given latent spaces, thereby enabling effective stitching of encoders and decoders without additional training. We extensively validate the adaptability of this translation procedure in different experimental settings: across various trainings, architectures (e.g., ResNet, CNN, ViT), and in multiple downstream tasks (classification, reconstruction). Notably, we show how it is possible to zero-shot stitch text encoders and vision decoders, or vice-versa, yielding surprisingly good classification performance in this multimodal setting.'

publication: '*Thirty-seventh Conference on Neural Information Processing Systems (NeurIPS 2023)*'

---
