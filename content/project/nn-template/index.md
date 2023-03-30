---
title: NN Template
summary: Popular template to bootstrap the *scaffolding* for your PyTorch project with [PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning), [Hydra](https://github.com/facebookresearch/hydra), [DVC](https://dvc.org/doc/start/data-versioning), [Weights and Biases](https://wandb.ai/home), and [Streamlit](https://streamlit.io/).

tags:
- deeplearning
- opensource
date: "2021-03-31T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: "https://grok-ai.github.io/nn-template"

image:
  focal_point: Smart



authors:
  - maiorca
  - moschella

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ''

---

## Git is Not Enough

Version control and multi-user collaboration are problems largely solved by git for classic codebases. Unfortunately, git alone is not enough to handle the lifecycle of a modern ML (research) project, where many different problems arise:

- Data versioning: can you recover the pre-processed data a model has been trained with? What if the data is a work in progress?

- Hyperparameters comparison: can you reliably say which hyperparameters are the best?

- Model comparison: can you identify which approach/model is the best?

- Sweeps: can you easily search for the best hyperparameters and models?

- Code organization and reproducibility: how steep is the codebase learning curve?

You have to tackle all the previous problems simultaneously: a jumble for each new project.

## ML Tooling

Luckily many great tools have been developed to solve or alleviate these obstacles. Examples are *PyTorch Lightning* to organize your code, *DVC* for data versioning, *Weights & Biases* to compare and analyze your experiments, *Hydra* for configurations and sweeps, *Streamlit* to interact and showcase your system.

### Tooling Scaffolding

These tools must work together in each project: a non-project-specific scaffolding that can and should be abstracted. `nn-template` is exactly this: a generic template to bootstrap your project, enforcing code best practices.

It provides boilerplate code for:

- [PyTorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning), lightweight PyTorch wrapper for high-performance AI research.
- [Hydra](https://github.com/facebookresearch/hydra), a framework for elegantly configuring complex applications.
- [DVC](https://dvc.org/doc/start/data-versioning), track large files, directories, or ML models. Think "Git for data".
- [Weights and Biases](https://wandb.ai/home), organize and analyze machine learning experiments. *(educational account available)*
- [Streamlit](https://streamlit.io/), turns data scripts into shareable web apps in minutes.

You can click [here](https://github.com/lucmos/nn-template/generate) to start a project with this template.
