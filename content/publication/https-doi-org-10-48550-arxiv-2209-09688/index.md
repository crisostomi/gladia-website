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
date: '2023-09-26'
lastmod: 2023-02-08T16:41:35+01:00
featured: false
draft: false
publication_short: "TAI"

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
abstract: "In this study, we introduce SAVAGE, a novel framework for sparse vicious adversarial link prediction attacks in graph neural networks (GNNs). While GNNs have been successful in link prediction tasks, they are susceptible to adversarial attacks where malicious nodes attempt to manipulate recommendations for a target victim. SAVAGE optimizes the attacker's goal to maximize attack effectiveness while minimizing the required malicious resources. Unlike existing methods with static resource-based upper bounds, SAVAGE employs a sparsity-enforcing mechanism to reduce the number of malicious nodes needed for the attack. Extensive experiments on real-world and synthetic datasets demonstrate the optimal tradeoff achieved by SAVAGE between a high attack success rate and the number of malicious nodes utilized. Furthermore, we demonstrate that SAVAGE can successfully target non-GNN-based link prediction systems, even those unknown at the time of the attack. This showcases the transferability of SAVAGE-generated attacks to other black-box methods for link prediction, highlighting its applicability across different real-world scenarios."
publication: '*IEEE Transactions on Artificial Intelligence*'
links:
- icon: link
  icon_pack: fas
  name: 'URL'
  url: https://ieeexplore.ieee.org/document/10264111
- icon: github
  icon_pack: fab
  name: 'GitHub'
  url: https://github.com/GiovanniTRA/SAVAGE
---
