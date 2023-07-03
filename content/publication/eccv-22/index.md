---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 3D Human Pose Estimation Using Möbius Graph Convolutional Networks
subtitle: ''
summary: ''
authors:
- Niloofar Azizi
- Horst Possegger
- rodola
- Horst Bischof
tags: []
categories: []
date: '2022-10-01'
lastmod: 2023-02-02T06:54:21+01:00
featured: false
draft: false
publication_short: "ECCV 2022"

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
publishDate: '2023-02-02T05:54:21.541446Z'
publication_types:
- '1'
abstract: '3D human pose estimation is fundamental to understanding human behavior. Recently, promising results have been achieved by graph convolutional networks (GCNs), which achieve state-of-the-art performance and provide rather light-weight architectures. However, a major limitation of GCNs is their inability to encode all the transformations between joints explicitly. To address this issue, we propose a novel spectral GCN using the Möbius transformation (Möbius-GCN). In particular, this allows us to directly and explicitly encode the transformation between joints, resulting in a significantly more compact representation. Compared to even the lightest architectures so far, our novel approach requires 90–98% fewer parameters, i.e. our lightest MöbiusGCN uses only 0.042M trainable parameters. Besides the drastic parameter reduction, explicitly encoding the transformation of joints also enables us to achieve state-of-the-art results. We evaluate our approach on the two challenging pose estimation benchmarks, Human3.6M and MPI-INF-3DHP, demonstrating both state-of-the-art results and the generalization capabilities of MöbiusGCN.'
publication: '*Proc. European Conference on Computer Vision (ECCV)*'

links:
- name: URL
  url: https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1049_ECCV_2022_paper.php
- name: PDF
  url: https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136610158.pdf
---
