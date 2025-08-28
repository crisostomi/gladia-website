---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "On Task Vectors and Gradients"
subtitle: ''
summary: ''
authors:
- zhou
- solombrino
- crisostomi
- Maria Sofia Bucarelli
- Giuseppe Alessio D'Inverno
- Fabrizio Silvestri
- rodola


# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

tags: []
categories: []
date: '2025-08-25'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '3'
abstract: "Task arithmetic has emerged as a simple yet powerful technique for model merging, enabling the combination of multiple finetuned models into one. Despite its empirical success, a clear theoretical explanation of why and when it works is lacking. This paper provides a rigorous theoretical foundation for task arithmetic by establishing a connection between task vectors and gradients of the task losses. We show that under standard gradient descent, a task vector generated from one epoch of finetuning is exactly equivalent to the negative gradient of the loss, scaled by the learning rate. For the practical multi-epoch setting, we prove that this equivalence holds approximately, with a second-order error term that we explicitly bound for feed-forward networks. Our empirical analysis across seven vision benchmarks corroborates our theory, demonstrating that the first-epoch gradient dominates the finetuning trajectory in both norm and direction. A key implication is that merging models finetuned for only a single epoch often yields performance comparable to merging fully converged models. These findings reframe task arithmetic as a form of approximate multitask learning, providing a clear rationale for its effectiveness and highlighting the critical role of early training dynamics in model merging."

links:
- name: arXiv
  url : https://www.arxiv.org/abs/2508.16082

publication: '*ArXiv preprint*'
---