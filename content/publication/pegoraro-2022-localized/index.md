---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Localized Shape Modelling with Global Coherence: An Inverse Spectral Approach'
subtitle: ''
summary: ''
authors:
- pegoraro
- melzi
- Umberto Castellani
- marin
- rodola
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-02-05T10:57:53+01:00
featured: false
draft: false

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
publishDate: '2023-02-05T09:57:52.951304Z'
publication_types:
- '1'
abstract: Many natural shapes have most of their characterizing features concentrated
  over a few regions in space. For example, humans and animals have distinctive head
  shapes, while inorganic objects like chairs and airplanes are made of well-localized
  functional parts with specific geometric features. Often, these features are strongly
  correlated -- a modification of facial traits in a quadruped should induce changes
  to the body structure. However, in shape modelling applications, these types of
  edits are among the hardest ones; they require high precision, but also a global
  awareness of the entire shape. Even in the deep learning era, obtaining manipulable
  representations that satisfy such requirements is an open problem posing significant
  constraints. In this work, we address this problem by defining a data-driven model
  upon a family of linear operators (variants of the mesh Laplacian), whose spectra
  capture global and local geometric properties of the shape at hand. Modifications
  to these spectra are translated to semantically valid deformations of the corresponding
  surface. By explicitly decoupling the global from the local surface features, our
  pipeline allows to perform local edits while simultaneously maintaining a global
  stylistic coherence. We empirically demonstrate how our learning-based model generalizes
  to shape representations not seen at training time, and we systematically analyze
  different choices of local operators over diverse shape categories.
publication: '*Computer Graphics Forum*'
---
