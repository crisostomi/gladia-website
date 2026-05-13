---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Communicating Sound Through Natural Language"
subtitle: ''
summary: ''
authors:
- rossi
- rodola

tags: []
categories: []
date: '2026-04-29'
lastmod: 2026-05-10T:26:44
featured: false
draft: false
publication_short: "Preprint"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '2026-04-03T:26:44'
publication_types:
- '3'
abstract: "Natural language is widely used to describe, prompt, and control audio systems, but rarely serves as the representation carrying audio itself. We introduce lexical acoustic coding (LAC), a framework in which pre-trained LLM sender and receiver agents transmit sound through natural language. Under fixed system prompts, the agents write their own analysis and synthesis code, communicating only through a lexical sentence, shared vocabulary, and optional symbolic music structure. The sender analyzes an input waveform into interpretable, non-learned acoustic descriptors, quantizes each with a feature-specific interval vocabulary, and verbalizes the lexical code as English. The receiver parses the sentence back into lexical-acoustic constraints and renders a waveform through closed-loop refinement. The transmitted text serves as both a rich caption and as the transport representation itself. We frame LAC as a finite-rate lossy quantizer, exposing trade-offs between vocabulary size, rate, and fidelity. Experiments on short sounds and symbolic music transfer show that plain text preserves measurable acoustic structure while remaining interpretable, editable, and native to LLM-mediated communication."

links:
- name: arXiv
  url : https://arxiv.org/abs/2605.08750
- icon: chalkboard-user
  icon_pack: fas
  name: 'Demo'
  url: https://erodola.github.io/lac-demo/

publication: '*ArXiv preprint*'
---