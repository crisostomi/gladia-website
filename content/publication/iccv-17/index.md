---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Deep Functional Maps: Structured Prediction for Dense Shape Correspondence'
subtitle: ''
summary: ''
authors:
- Or Litany
- Tal Remez
- rodola
- Alex M. Bronstein
- Michael M. Bronstein
tags: ["featured"]
categories: []
date: '2017-10-01'
lastmod: 2023-02-02T06:55:02+01:00
featured: false
draft: false
publication_short: "ICCV 2017"
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
publishDate: '2023-02-02T05:55:01.947539Z'
publication_types:
- '1'
abstract: "We introduce a new framework for learning dense correspondence between deformable 3D shapes. Existing learning based approaches model shape correspondence as a labelling problem, where each point of a query shape receives a label identifying a point on some reference domain; the correspondence is then constructed a posteriori by composing the label predictions of two input shapes. We propose a paradigm shift and design a structured prediction model in the space of functional maps, linear operators that provide a compact representation of the correspondence. We model the learning process via a deep residual network which takes dense descriptor fields defined on two shapes as input, and outputs a soft map between the two given objects. The resulting correspondence is shown to be accurate on several challenging benchmarks comprising multiple categories, synthetic models, real scans with acquisition artifacts, topological noise, and partiality."
publication: "*Proc. Int'l Conference on Computer Vision (ICCV)*"

links:
- name: 'PDF'
  url: https://openaccess.thecvf.com/content_ICCV_2017/papers/Litany_Deep_Functional_Maps_ICCV_2017_paper.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://openaccess.thecvf.com/content_iccv_2017/html/Litany_Deep_Functional_Maps_ICCV_2017_paper.html
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/orlitany/DeepFunctionalMaps
---
