---

title: "ReMatching: Low-Resolution Representations for Scalable Shape Correspondence"
subtitle: ''
summary: ''
authors:
- maggioli
- baieri
- rodola
- melzi

tags:
    - shape matching
    - spectral methods
    - functional maps

categories: []
date: '2024-07-05'
lastmod: 2024-07-05T16:50:39+01:00
featured: false
draft: false

image:
  caption: ''
  focal_point: ''
  preview_only: false

projects: []
publishDate: '2024-07-05T15:50:38.894577Z'
publication_types:
- '1'

abstract: We introduce ReMatching, a novel shape correspondence solution based on the functional maps framework. Our method, by exploiting a new and appropriate re-meshing paradigm, can target shape-matching tasks even on meshes counting millions of vertices, where the original functional maps does not apply or requires a massive computational cost. The core of our procedure is a time-efficient remeshing algorithm which constructs a low-resolution geometry while acting conservatively on the original topology and metric. These properties allow translating the functional maps optimization problem on the resulting low-resolution representation, thus enabling efficient computation of correspondences with functional map approaches. Finally, we propose an efficient technique for extending the estimated correspondence to the original meshes. We show that our method is more efficient and effective through quantitative and qualitative comparisons, outperforming state-of-the-art pipelines in quality and computational cost.

publication: 'Proc. ECCV'
publication_short: "ECCV 2024"

links:
- name: PDF
  url: https://arxiv.org/pdf/2305.09274
---
