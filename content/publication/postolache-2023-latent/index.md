---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Latent Autoregressive Source Separation
subtitle: ''
summary: ''
authors:
- Emilian Postolache
- Giorgio Mariani
- Michele Mancusi
- Andrea Santilli
- Luca Cosmo
- Emanuele Rodolà
tags: []
categories: []
date: '2023-01-01'
lastmod: 2023-02-06T11:38:44+01:00
featured: false
draft: false

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
publishDate: '2023-02-06T10:38:43.595207Z'
publication_types:
- '1'
abstract: Autoregressive models have achieved impressive results over a wide range
  of domains in terms of generation quality and downstream task performance. In the
  continuous domain, a key factor behind this success is the usage of quantized latent
  spaces (e.g., obtained via VQ-VAE autoencoders), which allow for dimensionality
  reduction and faster inference times. However, using existing pre-trained models
  to perform new non-trivial tasks is difficult since it requires additional fine-tuning
  or extensive training to elicit prompting. This paper introduces LASS as a way to
  perform vector-quantized Latent Autoregressive Source Separation (i.e., de-mixing
  an input signal into its constituent sources) without requiring additional gradient-based
  optimization or modifications of existing models. Our separation method relies on
  the Bayesian formulation in which the autoregressive models are the priors, and
  a discrete (non-parametric) likelihood function is constructed by performing frequency
  counts over latent sums of addend tokens. We test our method on images and audio
  with several sampling strategies (e.g., ancestral, beam search) showing competitive
  results with existing approaches in terms of separation quality while offering at
  the same time significant speedups in terms of inference time and scalability to
  higher dimensional data.
publication: '*Proc. AAAI*'
---
