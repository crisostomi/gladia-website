# upload-paper

Interactive workflow for adding a new entry under `content/publication/`. Ask the user for each field **one at a time** in the order below — do not batch questions, do not assume answers. After each answer, repeat back what you captured in one short line and move to the next field.

This workflow is tool-neutral. Any AI coding assistant can follow it. Trigger phrases: "add a paper", "upload a paper", "add a publication", or similar.

## Before starting

1. Confirm you're in the `gladia-website` repo root by checking that `content/publication/` exists.
2. List existing authors (e.g. `ls content/authors/`) so you can recognize folder keys when the user lists co-authors. Keep this list in mind — you'll need it during the authors step.
3. Look at a recent example (e.g. `content/publication/2025-crisostomi-mass/index.md`) to anchor on current frontmatter conventions if anything below is unclear.

## Fields to collect (ask one at a time, in this order)

1. **Title** — full paper title, no surrounding quotes.
2. **Slug** — folder name under `content/publication/`. Suggest a default in the form `YYYY-<firstauthorlastname>-<keyword>` (lowercase, hyphens, no spaces), e.g. `2026-rossi-diffusion`. Confirm the suggestion with the user; let them override.
3. **Authors** — ask for the full author list **in order**, one comma-separated line. Then, for each name, decide:
   - If a folder exists at `content/authors/<key>/`, use the lowercase folder key (typically the surname, e.g. `crisostomi`, `rodola`).
   - Otherwise use the full "Firstname Lastname" string.
   Show the resolved list back to the user and ask them to confirm or correct any entry. If a name is close to but not exactly a folder key (e.g. user wrote "Rodolà" but the folder is `rodola`), prefer the folder key and tell the user you matched it.
4. **Author notes (optional)** — ask only if relevant: equal contribution, corresponding author, etc. If yes, collect one note per author position; leave blank for authors with no note. Skip the `author_notes` frontmatter block entirely if all are blank.
5. **Date** — publication date in `YYYY-MM-DD`. This drives ordering on the site.
6. **Publication type** — Wowchemy enum. Ask the user which applies and map to the number:
   - `1` = Conference paper
   - `2` = Journal article
   - `3` = Preprint / Working paper
   - `4` = Report
   - `5` = Book
   - `6` = Book section
   - `7` = Thesis
   - `8` = Patent
   Default to `1` if the venue is a conference.
7. **publication_short** — short venue label shown in listings, e.g. `ICLR 2026`, `CVPR 2025 Workshop CV4Animals`, `NeurIPS 2025`.
8. **publication** — full venue string with markdown italics, e.g. `*International Conference on Learning Representations (ICLR 2026)*`. Offer to auto-expand common acronyms (ICLR/NeurIPS/CVPR/ICCV/ECCV/ICML/AAAI/EMNLP/ACL) and confirm.
9. **Abstract** — paste the full abstract as a single block. Strip any surrounding quotes/whitespace and inline it as a YAML double-quoted string (escape inner `"` as `\"`).
10. **Links** — ask for each link the user wants to include. Common ones: `arXiv`, `PDF`, `Code`, `Project`, `Video`, `Poster`, `Slides`. Accept "none" / "done" to stop. Each becomes an entry in the `links:` list with `name` and `url`.
11. **Featured** — `true` if it should surface on the homepage Publications widget, otherwise `false`. Default `false`.
12. **BibTeX** — paste a full `@inproceedings{...}` / `@article{...}` block. Optional but strongly recommended (enables the "Cite" button via `partials/my_page_links.html`). If the user skips it, do not create `cite.bib`.
13. **Featured image** — ask if they have a `featured.png` they want to include. If yes, ask for an absolute path on disk and copy it into the new folder. If no, skip — the entry will still build.

## Writing the files

Once everything is collected, summarize the captured values back to the user in a compact block and ask for a final "go" before writing.

Then create:

- `content/publication/<slug>/index.md` — frontmatter only, ending with `---`, no body content (matches existing entries). Use this template, omitting any optional sections that were skipped:

```yaml
---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "<title>"
subtitle: ''
summary: ''
authors:
- <author1>
- <author2>


# Author notes (optional)
author_notes:
  - '<note for author1, or empty string>'
  - '<note for author2, or empty string>'

tags: []
categories: []
date: '<YYYY-MM-DD>'
lastmod: <YYYY-MM-DDTHH:MM:SS>
featured: <true|false>
draft: false
publication_short: "<short venue>"

image:
  caption: ''
  focal_point: 'Center'
  preview_only: false

projects: []
publishDate: '<YYYY-MM-DDTHH:MM:SS>'
publication_types:
- '<type number as string>'
abstract: "<abstract>"

links:
- name: <Link name>
  url : <url>

publication: '<full venue>'
---
```

- `content/publication/<slug>/cite.bib` — only if BibTeX was provided. Write the block verbatim.
- `content/publication/<slug>/featured.png` — only if the user provided a path; copy it into place.

## After writing

1. Confirm the files exist (e.g. `ls content/publication/<slug>/`).
2. Tell the user how to preview: `hugo server -D` then visit `http://localhost:1313/publication/<slug>/`.
3. Remind them that production build on Netlify uses **HUGO_VERSION 0.108.0** (older than local `0.119.0` per `.tool-versions`) — if anything looks off in prod, that gap is the first suspect.
4. Do **not** commit or push. Leave that to the user.

## Pitfalls to avoid

- Don't invent author folder keys. If unsure whether a name has a folder, check `content/authors/` rather than guessing — a wrong key renders as a broken profile link.
- Don't reorder authors. The `authors:` list must match the paper's author order exactly.
- Don't wrap the abstract in extra quotes inside the YAML string. One pair of outer `"..."` only; escape any inner `"` with `\"`.
- Don't set `featured: true` casually — the homepage Publications widget surfaces these, so confirm with the user.
- Don't create a `_index.md` inside the publication folder — it's `index.md` (no underscore). The underscore form is for section landings, not leaf pages.
- Don't rename or "clean up" existing publications while adding the new one. Scope stays on the new entry.
