---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'PC-GAU: PCA Basis of Scattered Gaussians for Shape Matching via Functional
  Maps'
subtitle: ''
summary: ''
authors:
- Michele Colombo
- Giacomo Boracchi
- melzi
tags: []
categories: []
date: '2022-01-01'
lastmod: 2023-02-08T15:02:25+01:00
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

links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://diglib.eg.org/bitstream/handle/10.2312/stag20221250/001-009.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/michele-colombo/PC-Gau_STAG2022
  
# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-02-08T14:02:25.143647Z'
publication_types:
- '1'
abstract: Shape matching is a central problem in geometry processing applications,
  ranging from texture transfer to statistical shape analysis. The functional maps
  framework provides a compact representation of correspondences between discrete
  surfaces, which is then converted into point-wise maps required by real-world applications.
  The vast majority of methods based on functional maps involve the eigenfunctions
  of the Laplace-Beltrami Operator (LB) as the functional basis. A primary drawback
  of the LB basis is that its energy does not uniformly cover the surface. This fact
  gives rise to regions where the estimated correspondences are inaccurate, typically
  at tiny parts and protrusions. For this reason, state-of-the-art procedures to convert
  the functional maps (represented in the LB basis) into point-wise correspondences
  are often error-prone. We propose PCGAU, a new functional basis whose energy spreads
  on the whole shape more evenly than LB. As such, PC-GAU can replace the LB basis
  in existing shape matching pipelines. PC-GAU consists of the principal vectors obtained
  by applying Principal Component Analysis (PCA) to a dictionary of sparse Gaussian
  functions scattered on the surfaces. Through experimental evaluation of established
  benchmarks, we show that our basis produces more accurate point-wise maps —- compared
  to LB - when employed in the same shape-matching pipeline.
publication: '*Smart Tools and Applications in Graphics - Eurographics Italian Chapter
  Conference*'
---
