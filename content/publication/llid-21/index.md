---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Cluster-driven Graph Federated Learning over Multiple Domains
subtitle: ''
summary: ''
authors:
- Debora Caldarola
- Massimiliano Mancini
- Fabio Galasso
- Marco Ciccone
- rodola
- Barbara Caputo
tags: []
categories: []
date: '2021-06-01'
lastmod: 2023-02-02T06:54:27+01:00
featured: false
draft: false
publication_short: "CVPR L2ID 2021"

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
publishDate: '2023-02-02T05:54:27.368785Z'
publication_types:
- '1'
abstract: 'Federated Learning (FL) deals with learning a central model (i.e. the server) in privacy-constrained scenarios, where data are stored on multiple devices (i.e. the clients). The central model has no direct access to the data, but only to the updates of the parameters computed locally by each client. This raises a problem, known as statistical heterogeneity, because the clients may have different data distributions (i.e. domains). This is only partly alleviated by clustering the clients. Clustering may reduce heterogeneity by identifying the domains, but it deprives each cluster model of the data and supervision of others. Here we propose a novel Cluster-driven Graph Federated Learning (FedCG). In FedCG, clustering serves to address statistical heterogeneity, while Graph Convolutional Networks (GCNs) enable sharing knowledge across them. FedCG: i. identifies the domains via an FL-compliant clustering and instantiates domain-specific modules (residual branches) for each domain; ii. connects the domain-specific modules through a GCN at training to learn the interactions among domains and share knowledge; and iii. learns to cluster unsupervised via teacher-student classifier-training iterations and to address novel unseen test domains via their domain soft-assignment scores. Thanks to the unique interplay of GCN over clusters, FedCG achieves the state-of-the art on multiple FL benchmarks.'
publication: "*Proc. Int'l Conference on Computer Vision and Pattern Recognition (CVPR)\
  \ - Workshop on Learning from Limited or Imperfect Data (L2ID)*"
links:
- name: URL
  url: https://www.computer.org/csdl/proceedings-article/cvprw/2021/489900c743/1yVzUPAEtyM
- name: PDF
  url: https://openaccess.thecvf.com/content/CVPR2021W/LLID/papers/Caldarola_Cluster-Driven_Graph_Federated_Learning_Over_Multiple_Domains_CVPRW_2021_paper.pdf
---
