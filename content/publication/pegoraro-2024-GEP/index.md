---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Geometric Epitope and Paratope Prediction'
subtitle: ''
summary: ''
authors:
- pegoraro
- Clementine Domine
- rodola
- Petar Velickovic
- Andreea Deac
tags:
- 'Machine Learning'
- 'Geometry Processing'
- 'Computational Biology'
categories: []
date: '2024-07-10'
lastmod: 2023-02-05T10:57:53+01:00
featured: false
draft: false
publication_short: "Bioinformatics"

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
abstract: "Identifying the binding sites of antibodies is essential for developing vaccines and synthetic antibodies. In this article, we investigate the optimal representation for predicting the binding sites in the two molecules and emphasize the importance of geometric information. Specifically, we compare different geometric deep learning methods applied to proteins’ inner (I-GEP) and outer (O-GEP) structures. We incorporate 3D coordinates and spectral geometric descriptors as input features to fully leverage the geometric information. Our research suggests that different geometrical representation information is useful for different tasks. Surface-based models are more efficient in predicting the binding of the epitope, while graph models are better in paratope prediction, both achieving significant performance improvements. Moreover, we analyze the impact of structural changes in antibodies and antigens resulting from conformational rearrangements or reconstruction errors. Through this investigation, we showcase the robustness of geometric deep learning methods and spectral geometric descriptors to such perturbations."
publication: '*Bioinformatics*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://academic.oup.com/bioinformatics/article/40/7/btae405/7710426
- name: 'PDF'
  url: https://academic.oup.com/bioinformatics/article-pdf/40/7/btae405/58531211/btae405.pdf
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/Marco-Peg/GEP
---
