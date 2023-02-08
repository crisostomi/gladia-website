---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Neural Implicit Style-net: synthesizing shapes in a preferred style exploiting
  self supervision'
subtitle: ''
summary: ''
authors:
- fumero
- Hooman Shayani
- Aditya Sanghi
- rodola
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-02-08T15:02:10+01:00
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
publishDate: '2023-02-08T14:02:09.685097Z'
publication_types:
- '1'
abstract: We introduce a novel approach to disentangle style from content in the 3D
  domain and perform unsupervised neural style transfer. Our approach is able to extract
  style information from 3D input in a self supervised fashion, conditioning the definition
  of style on inductive biases enforced explicitly, in the form of specific augmentations
  applied to the input.This allows, at test time, to select specifically the features
  to be transferred  between two arbitrary 3D shapes, being still able to capture
  complex changes (e.g. combinations of arbitrary geometrical and topological transformations)
  with the data prior. Coupled with the choice of representing 3D shapes as neural
  implicit fields, we are able to perform style transfer in a  controllable way, handling
  a variety of transformations. We validate our approach qualitatively and quantitatively
  on a dataset with font style labels.
publication: '*NeurIPS 2022 Workshop on Symmetry and Geometry in Neural Representations*'
---
