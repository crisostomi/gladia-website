---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation"
subtitle: ''
summary: ''
authors:
- zirilli
- marincione
- Evgenios M. Kornaropoulos
- Giuseppe Ateniese
- rodola


tags: []
categories: []
date: '2026-09-01'
lastmod: 2026-09-04T00:00:00
featured: false
draft: false
publication_short: "arXiv preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-09-04T00:00:00'
publication_types:
- '3'
abstract: "Fully homomorphic encryption (FHE) allows a server to run a language model directly on encrypted user prompts, but current approaches remain prohibitively slow. Ciphertexts natively support only addition, multiplication, and rotation, and multiplications may be composed only to a bounded depth before a costly bootstrapping operation is needed to continue. Every nonlinearity must therefore be approximated by an iterative method, and each iteration uses multiplications. A higher iteration count buys precision but exhausts the available depth faster and triggers more bootstraps, which dominate latency. Existing approaches fix the iteration counts uniformly across the model rather than tailoring them to each site's error tolerance. We introduce Homomorphic Encryption-Aware Training (HEAT), a fine-tuning method that makes the per-nonlinearity iteration counts learnable, enabling them and the model weights to co-adapt during training. HEAT optimizes iterations with respect to the task objective, allowing the model to adapt to approximation errors encountered during inference without architectural changes or retraining from scratch. On encrypted GPT-2 decoding, HEAT reduces iterations by 3.1×, bootstraps by 1.6×, and end-to-end latency by 1.4×, while improving decode agreement over the calibrated baseline."

links:
- name: arXiv
  url : https://arxiv.org/abs/2609.01730
- name: Code
  url : https://github.com/gladia-research-group/heat
- name: Model
  url : https://huggingface.co/gladia/heat-gpt2-small-openwebtext

publication: '*arXiv preprint*'
---
