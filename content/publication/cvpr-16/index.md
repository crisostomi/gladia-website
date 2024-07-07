---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Efficient globally optimal 2d-to-3d deformable shape matching'
subtitle: ''
summary: ''
authors:
- Zorah Lähner
- rodola
- Frank Schmidt
- Michael M. Bronstein
- Daniel Cremers
tags: []
categories: []
date: '2016-06-01'
lastmod: 2023-02-02T06:55:20+01:00
featured: false
draft: false
publication_short: "CVPR 2016"

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
publishDate: '2023-02-02T05:55:19.409784Z'
publication_types:
- '1'
abstract: "We propose the first algorithm for non-rigid 2D-to-3D shape matching, where the input is a 2D shape represented as a planar curve and a 3D shape represented as a surface; the output is a continuous curve on the surface. We cast the problem as finding the shortest circular path on the product 3-manifold of the surface and the curve. We prove that the optimal matching can be computed in polynomial time with a (worst-case) complexity of O(m n^2 log(n)), where m and n denote the number of vertices on the template curve and the 3D shape respectively. We also demonstrate that in practice the runtime is essentially linear in m times n making it an efficient method for shape analysis and shape retrieval. Quantitative evaluation confirms that the method provides excellent results for sketch-based deformable 3D shape retrieval."
publication: "*Proc. Int'l Conference on Computer Vision and Pattern Recognition (CVPR)*"

links:
- name: 'PDF'
  url: https://openaccess.thecvf.com/content_cvpr_2016/papers/Lahner_Efficient_Globally_Optimal_CVPR_2016_paper.pdf
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/7780609
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/zorah/Elastic2D3D
---
