---
title: Multitask Prompted Training Enables Zero-Shot Task Generalization
publication_types:
  - "1"
authors:
  - Victor Sanh
  - Albert Webson
  - Colin Raffel
  - Stephen H. Bach
  - BIG-Science contributors including
  - santilli
doi: 
publication: International Conference on Learning Representations
publication_short: "ICLR 2022"
abstract: Large language models have recently been shown to attain reasonable
  zero-shot generalization on a diverse set of tasks (Brown et al., 2020). It
  has been hypothesized that this is a consequence of implicit multitask
  learning in language models’ pretraining (Radford et al., 2019). Can zero-shot
  generalization instead be directly induced by explicit multitask learning? To
  test this question at scale, we develop a system for easily mapping any
  natural language tasks into a human-readable prompted form. We convert a large
  set of supervised datasets, each with multiple prompts with diverse wording.
  These prompted datasets allow for benchmarking the ability of a model to
  perform completely unseen tasks specified in natural language. We fine-tune a
  pretrained encoder-decoder model (Raffel et al., 2020; Lester et al., 2021) on
  this multitask mixture covering a wide variety of tasks. The model attains
  strong zero-shot performance on several datasets, often outperforming models
  16× its size. Further, our model attains strong performance on a subset of
  tasks from the BIG-Bench benchmark, outperforming models 6× its size. All
  trained models are available at https://github.com/bigscience-workshop/t-zero,
  and all prompts are available at
  https://github.com/bigscience-workshop/promptsource.
draft: false
featured: false
image:
  filename: featured
  focal_point: Smart
  preview_only: false
date: 2021-09-29
links:
- icon: chalkboard-user
  icon_pack: fas
  name: 'ICLR 2022 (Oral)'
  url: https://openreview.net/forum?id=9Vrb9D0WI4
---
