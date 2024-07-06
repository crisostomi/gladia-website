---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Sparse Vicious Attacks on Graph Neural Networks
subtitle: ''
summary: ''
authors:
- trappolini
- maiorca
- severino
- rodola
- Fabrizio Silvestri
- Gabriele Tolomei
tags:
- Machine Learning (cs.LG)
- Cryptography and Security (cs.CR)
- 'FOS: Computer and information sciences'
- 'FOS: Computer and information sciences'
categories: []
date: '2022-01-01'
lastmod: 2023-02-08T16:41:35+01:00
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
publishDate: '2023-02-08T15:41:34.158908Z'
publication_types:
- '0'
abstract: Graph Neural Networks (GNNs) have proven to be successful in several predictive
  modeling tasks for graph-structured data. Amongst those tasks, link prediction is
  one of the fundamental problems for many real-world applications, such as recommender
  systems. However, GNNs are not immune to adversarial attacks, i.e., carefully crafted
  malicious examples that are designed to fool the predictive model. In this work,
  we focus on a specific, white-box attack to GNN-based link prediction models, where
  a malicious node aims to appear in the list of recommended nodes for a given target
  victim. To achieve this goal, the attacker node may also count on the cooperation
  of other existing peers that it directly controls, namely on the ability to inject
  a number of ``vicious'' nodes in the network. Specifically, all these malicious
  nodes can add new edges or remove existing ones, thereby perturbing the original
  graph. Thus, we propose SAVAGE, a novel framework and a method to mount this type
  of link prediction attacks. SAVAGE formulates the adversary's goal as an optimization
  task, striking the balance between the effectiveness of the attack and the sparsity
  of malicious resources required. Extensive experiments conducted on real-world and
  synthetic datasets demonstrate that adversarial attacks implemented through SAVAGE
  indeed achieve high attack success rate yet using a small amount of vicious nodes.
  Finally, despite those attacks require full knowledge of the target model, we show
  that they are successfully transferable to other black-box methods for link prediction.
publication: '*arXiv*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://arxiv.org/abs/2209.09688
---
