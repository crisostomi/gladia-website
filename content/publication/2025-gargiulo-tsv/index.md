---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Task Singular Vectors: Reducing Task Interference in Model Merging'
subtitle: ''
summary: ''
authors:
- Antonio Andrea Gargiulo
- crisostomi
- Maria Sofia Bucarelli
- Simone Scardapane
- Fabrizio Silvestri
- rodola

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

tags: 
- 'featured'
categories: []
date: '2025-02-27'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "CVPR 2025"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Task Arithmetic has emerged as a simple yet effective method to merge models without additional training. However, by treating entire networks as flat parameter vectors, it overlooks key structural information and is susceptible to task interference. In this paper, we study task vectors at the layer level, focusing on task layer matrices and their singular value decomposition. In particular, we concentrate on the resulting singular vectors, which we refer to as Task Singular Vectors (TSV). Recognizing that layer task matrices are often low-rank, we propose TSV-Compress (TSV-C), a simple procedure that compresses them to 10% of their original size while retaining 99% of accuracy. We further leverage this low-rank space to define a new measure of task interference based on the interaction of singular vectors from different tasks. Building on these findings, we introduce TSV-Merge (TSV-M), a novel model merging approach that combines compression with interference reduction, significantly outperforming existing methods."

links:
- name: arXiv
  url : https://arxiv.org/abs/2412.00081
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/AntoAndGar/task_singular_vectors

publication: '*The IEEE/CVF Conference on Computer Vision and Pattern Recognition 2025 (CVPR)*'
---