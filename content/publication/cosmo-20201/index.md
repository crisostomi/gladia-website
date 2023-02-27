---
# Documentation: https://wowchemy.com/docs/managing-content/

title: The Average Mixing Kernel Signature
subtitle: ''
summary: ''
authors:
- cosmo
- Giorgia Minello
- Michael M. Bronstein
- Luca Rossi
- Andrea Torsello
tags: []
categories: []
date: '2020-01-01'
lastmod: 2023-02-08T19:53:24+01:00
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
publishDate: '2023-02-08T18:53:23.821876Z'
publication_types:
- '2'
abstract: We introduce the Average Mixing Kernel Signature (AMKS), a novel signature
  for points on non-rigid three-dimensional shapes based on the average mixing kernel
  and continuous-time quantum walks. The average mixing kernel holds information on
  the average transition probabilities of a quantum walk between each pair of vertices
  of the mesh until a time T. We define the AMKS by decomposing the spectral contributions
  of the kernel into several bands, allowing us to limit the influence of noise-dominated
  high-frequency components and obtain a more descriptive signature. We also show
  through a perturbation theory analysis of the kernel that choosing a finite stopping
  time T leads to noise and deformation robustness for the AMKS. We perform an extensive
  experimental evaluation on two widely used shape matching datasets under varying
  level of noise, showing that the AMKS outperforms two state-of-the-art descriptors,
  namely the Heat Kernel Signature (HKS) and the similarly quantum-walk based Wave
  Kernel Signature (WKS). © 2020, Springer Nature Switzerland AG.
publication: '*Lecture Notes in Computer Science (including subseries Lecture Notes
  in Artificial Intelligence and Lecture Notes in Bioinformatics)*'
doi: 10.1007/978-3-030-58565-5_1
links:
- name: 'PDF'
  url: https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650001.pdf
- name: GitHub
  url: https://github.com/lcosmo/amks-descriptor
---
