---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'From Charts to Atlas: Merging Latent Spaces into One'
subtitle: ''
summary: ''
authors:
- crisostomi
- cannistraci
- moschella
- Pietro Barbiero
- Marco Ciccone
- Pietro Lio
- rodola
tags:
- 'Model merging'
categories: []
date: '2023-11-29'
lastmod: 2023-12-16T10:57:52+01:00
featured: false
draft: false
publication_short: "NeuReps 2023"

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
publishDate: '2023-02-05T09:57:52.156096Z'
abstract: "Models trained on semantically related datasets and tasks exhibit comparable inter-sample relations within their latent spaces. We investigate in this study the aggregation of such latent spaces to create a unified space encompassing the combined information. To this end, we introduce Relative Latent Space Aggregation (RLSA), a two-step approach that first renders the spaces comparable using relative representations, and then aggregates them via a simple mean. We carefully divide a classification problem into a series of learning tasks under three different settings: sharing samples, classes, or neither. We then train a model on each task and aggregate the resulting latent spaces. We compare the aggregated space with that derived from an end-to-end model trained over all tasks and show that the two spaces are similar. We then observe that the aggregated space is better suited for classification, and empirically demonstrate that it is due to the unique imprints left by task-specific embedders within the representations. We finally test our framework in scenarios where no shared region exists and show that it can still be used to merge the spaces, albeit with diminished benefits over naive merging."
publication: '*NeurReps Workshop 2023*'
links:
- name: URL
  url: https://openreview.net/forum?id=ZFu7CPtznY
- name: PDF
  url: https://openreview.net/pdf?id=ZFu7CPtznY
---
