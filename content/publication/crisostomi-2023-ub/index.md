---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Mitigating the Burden of Redundant Datasets via Batch-Wise Unique Samples and Frequency-Aware Losses'
subtitle: ''
summary: ''
authors:
- crisostomi
- Andrea Caciolai
- Alessandro Pedrani 
- Kay Rottmann
- Alessandro Manzotti
- Enrico Palumbo
- Davide Bernardi
tags: []
categories: []
date: '2023-07-01'
lastmod: 2023-02-05T16:49:57+01:00
featured: false
draft: false
publication_short: "ACL 2023"

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
publishDate: '2023-07-01T15:50:39.853135Z'
publication_types:
- '1'
abstract: Datasets used to train deep learning models in industrial settings often exhibit skewed distributions with some samples repeated a large number of times.This paper presents a simple yet effective solution to reduce the increased burden of repeated computation on redundant datasets.Our approach eliminates duplicates at the batch level, without altering the data distribution observed by the model, making it model-agnostic and easy to implement as a plug-and-play module. We also provide a mathematical expression to estimate the reduction in training time that our approach provides. Through empirical evidence, we show that our approach significantly reduces training times on various models across datasets with varying redundancy factors, without impacting their performance on the Named Entity Recognition task, both on publicly available datasets and in real industrial settings.In the latter, the approach speeds training by up to 87{\%}, and by 46{\%} on average, with a drop in model performance of 0.2{\%} relative at worst.We finally release a modular and reusable codebase to further advance research in this area..
publication: '*Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 5: Industry Track)*'
links:
- name: URL
  url: https://aclanthology.org/2023.acl-industry.23/
---
