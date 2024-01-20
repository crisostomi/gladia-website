---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Spectral Maps for Learning on Subgraphs
subtitle: ''
summary: ''
authors:
- pegoraro
- marin
- rampini
- melzi
- cosmo
- rodola
tags:
- '"Computer Science - Machine Learning"'
- 'Spectral theory'
- 'Learning on graphs'
- 'Subgraphs'
categories: []
date: '2023-01-01'
lastmod: 2023-12-16T10:57:52+01:00
featured: false
draft: false
publication_short: "NeuReps Workshop 2023"

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
abstract: In graph learning, maps between graphs and their subgraphs frequently arise.
  For instance, when coarsening or rewiring operations are present along the pipeline,
  one needs to keep track of the corresponding nodes between the original and modified
  graphs. Classically, these maps are represented as binary node-to-node correspondence
  matrices and used as-is to transfer node-wise features between the graphs. In this
  paper, we argue that simply changing this map representation can bring notable benefits
  to graph learning tasks. Drawing inspiration from recent progress in geometry processing,
  we introduce a spectral representation for maps that is easy to integrate into existing
  graph learning models. This spectral representation is a compact and straightforward
  plug-in replacement and is robust to topological changes of the graphs. Remarkably,
  the representation exhibits structural properties that make it interpretable, drawing
  an analogy with recent results on smooth manifolds. We demonstrate the benefits
  of incorporating spectral maps in graph learning pipelines, addressing scenarios
  where a node-to-node map is not well defined, or in the absence of exact isomorphism.
  Our approach bears practical benefits in knowledge distillation and hierarchical
  learning, where we show comparable or improved performance at a fraction of the
  computational cost.
publication: '*arXiv preprint arXiv:2108.02161*'
links:
- name: URL
  url: https://arxiv.org/pdf/2205.14938.pdf
---
