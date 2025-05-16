---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Update Your Transformer to the Latest Release: Re-Basin of Task Vectors"
subtitle: ''
summary: ''
authors:
- Filippo Rinaldi
- Giacomo Capitani
- Lorenzo Bonicelli
- Angelo Porrello
- crisostomi
- Federico Bolelli
- rodola
- Elisa Ficarra
- Simone Calderara 



tags: []
categories: []
date: '2025-05-01'
lastmod: 2025-02-27T:26:44
featured: false
draft: false
publication_short: "ICML 2025"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2025-27-02T:26:44'
publication_types:
- '1'
abstract: "Foundation models serve as the backbone for numerous specialized models developed through fine-tuning. However, when the underlying pretrained model is updated or retrained (e.g., on larger and more curated datasets), the fine-tuned model becomes obsolete, losing its utility and requiring retraining. This raises the question: is it possible to transfer fine-tuning to a new release of the model? In this work, we investigate how to transfer fine-tuning to a new checkpoint without having to re-train, in a data-free manner. To do so, we draw principles from model re-basin and provide a recipe based on weight permutations to re-base the modifications made to the original base model, often called task vector. In particular, our approach tailors model re-basin for Transformer models, taking into account the challenges of residual connections and multi-head attention layers. Specifically, we propose a two-level method rooted in spectral theory, initially permuting the attention heads and subsequently adjusting parameters within select pairs of heads. Through extensive experiments on visual and textual tasks, we achieve the seamless transfer of fine-tuned knowledge to new pre-trained backbones without relying on a single training step or datapoint."


publication: '*Proceedings of the 42nd International Conference on Machine Learning*'
---