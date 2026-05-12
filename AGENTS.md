# AGENTS.md

Guidance for any AI coding assistant working in this repo (Claude Code, Cursor, Codex, Aider, etc.). Tool-specific entry points (e.g. `CLAUDE.md`, `.cursorrules`) should link or symlink to this file rather than duplicate it.

## What this is

The public website for the GLADIA research group (Sapienza, University of Rome). It is a Hugo site built on the **Wowchemy v5 academic theme**, pulled in as a Hugo Module (see `go.mod` + `config/_default/config.yaml` `module.imports`). There is no local copy of the theme — most layouts/partials/i18n live inside the Wowchemy module on disk under `$GOPATH`/Hugo's module cache. The repo only contains content, configuration, and a small number of layout overrides.

Deployment is via Netlify (`netlify.toml`) — pushes to `main` trigger a production build.

## Common commands

```bash
hugo server -D            # local dev server with drafts (default http://localhost:1313)
hugo --gc --minify        # production build into ./public (same as Netlify)
hugo mod get -u            # update Wowchemy modules (rare — pinned in go.mod)
hugo mod clean             # clear the module cache if a build acts up
```

Toolchain pins:
- `.tool-versions` requests **hugo extended 0.119.0** locally and **go 1.22.12**.
- `netlify.toml` builds with **HUGO_VERSION = 0.108.0** — the production build uses an older Hugo than local. If a feature works locally but breaks on Netlify, suspect this gap first.

There is no test suite, no linter, no JS bundler, no `npm` workflow — `package-lock.json` is essentially empty. All build logic is Hugo + Wowchemy modules.

## Content architecture

Hugo's "section = directory under `content/`" model applies. The important sections:

- **`content/home/*.md`** — the single-page homepage. Each `.md` is a Wowchemy *widget* (`widget: pages`, `aboutv2`, `people`, `contact`, …) with `headless: true`. The `weight` field controls vertical order on the homepage. To toggle a section, flip `active:` or change `weight`. Navbar anchors in `config/_default/menus.yaml` reference these by filename (e.g. `#about`, `#news`, `#people`).
- **`content/authors/<username>/`** — one folder per group member, with `_index.md` (frontmatter: `role`, `bio`, `user_groups`, `social`, `organizations`, …) plus `avatar.jpg`. The `user_groups` field is what the People widget filters on (`Principal Investigator`, `Postdocs`, `PhD Students`, `Intern`, `Alumni` — see `content/home/people.md`). The folder name is the canonical author key referenced from publications.
- **`content/publication/<slug>/`** — one folder per paper, with `index.md` (frontmatter: `authors`, `date`, `publication_short`, `publication_types`, `abstract`, `links`, …), optional `cite.bib` (enables the "Cite" button via the `my_page_links.html` partial), and an optional `featured.png` thumbnail. `authors` entries that match an `authors/<key>` folder render as linked profiles; free-form strings render as plain text.
- **`content/news/<YYYY-MM-DD>/index.md`** — one folder per news item; the homepage News widget surfaces the most recent N items.
- **`content/project/`, `content/talks/`, `content/slides/`, `content/post/`, `content/nexus/`** — additional Wowchemy content types. `nexus` is a custom standalone page (linked from the navbar).
- **`content/admin/`** — Netlify CMS config (the CMS is enabled via the `wowchemy-plugin-netlify-cms` module).

`config/_default/config.yaml` sets `ignoreFiles: [\.ipynb$, .ipynb_checkpoints$, \.Rmd$, \.Rmarkdown$, _cache$]` — Jupyter/R notebooks committed inside `content/` are intentionally not built. Don't rename them to `.md` to "fix" them being skipped without checking why they're there.

## Configuration layout

All site config lives under `config/_default/`:
- `config.yaml` — Hugo-level config + module imports.
- `params.yaml` — Wowchemy site params (theme, SEO, analytics, footer copyright, search/comment providers, etc.).
- `menus.yaml` — navbar.
- `languages.yaml` — i18n (currently English only).

Theme tokens (colors/fonts) are in `data/themes/minimal.toml` and `data/fonts/`. `params.yaml` selects the active theme/font by name (`appearance.theme_day: minimal`).

## Layout overrides

`layouts/partials/` mirrors the Wowchemy module path — anything placed here shadows the upstream version. Current overrides:
- `partials/blocks/v1/aboutv2.html`, `partials/blocks/v1/news.html` — overridden homepage widgets.
- `partials/views/community/news.html`, `paper.html`, `projects.html` — list-view templates referenced from `content/home/*.md` via `design.view: community/news` etc.
- `partials/my_page_links.html`, `page_author_card.html` — overridden buttons/cards.

When fixing a rendering issue, first check whether a partial of the same path exists locally (override) before assuming the bug is in the Wowchemy module.

## Conventions and gotchas

- **Adding a person**: create `content/authors/<key>/_index.md` + `avatar.jpg`, set `user_groups` to one of the values listed in `content/home/people.md`. Reference them from publications by `<key>` (folder name, lowercase) in the `authors` list.
- **Adding a publication**: create `content/publication/<slug>/index.md`. Use the existing entries (e.g. `2025-crisostomi-mass/`) as templates — keep `publication_types` (Wowchemy enum: `1` = conference paper, etc.), `publication_short`, and `date` (drives ordering). Featured papers surface on the homepage when tagged `featured`. See [`agents/upload-paper.md`](agents/upload-paper.md) for the full interactive workflow.
- **Adding news**: create `content/news/<YYYY-MM-DD>/index.md`. The date in the folder name does not drive ordering — the `date:` frontmatter does.
- **The site is single-page on the homepage**: most navbar links are anchors (`#about`, `#news`, `#people`) that scroll to homepage widgets, not real routes. `Publications` and `NeXuS` are the exceptions (real subpages).
- **Footer credits** are hardcoded in `params.yaml` (`footer.copyright.notice`). Edits to maintainer attribution go there, not in a layout.

## Agent workflows

Reusable, interactive workflows live under [`agents/`](agents/) so any tool can consume them:

- [`agents/upload-paper.md`](agents/upload-paper.md) — add a new publication to `content/publication/`, end-to-end.

Tool-specific shims (e.g. Claude Code skills in `.claude/skills/`) should be thin wrappers that read and follow the canonical `agents/*.md` document.
