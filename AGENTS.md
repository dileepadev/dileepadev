# AGENTS.md

Canonical instructions for AI coding agents working in this repository.

> This file is the **single source of truth**. `CLAUDE.md` and
> `.github/copilot-instructions.md` intentionally contain only tool-specific notes and point
> back here. Add shared rules **here only** — duplicating them causes drift and contradictory
> guidance.

## What this is

`dileepadev` is the **platform root** — the GitHub profile repository, and as of v2.0.0 the
single place that holds brand guidelines, the design system, architecture documentation, and
the cross-repository migration roadmap for the whole `dileepa.dev` platform.

It ships no application. Nothing here builds, tests, or deploys. What it produces is the
description that six other repositories implement against.

| Repository | Role | v2.0.0 issue |
| --- | --- | --- |
| `dileepadev` | Brand + platform documentation root | #1 |
| `dileepa-dev` | Main website — blog, projects, events | dileepa-dev#15 |
| `api-dileepa-dev` | FastAPI backend (migrated from NestJS) | api-dileepa-dev#13 |
| `blog-dileepa-dev` | Content-source repository only | blog-dileepa-dev#3 |
| `admin-dileepa-dev` | Admin app | admin-dileepa-dev#4 |
| `links-dileepa-dev` | Links page | links-dileepa-dev#2 |
| `dileepadev.github.io` | Public build log — GitHub activity dashboard | dileepadev.github.io#1 |

[TODO.md](TODO.md) holds the full v2.0.0 roadmap across all seven repositories and is the place
to check what is planned, what is done, and in what order things must happen.

## Layout

| Path | Status |
| --- | --- |
| `README.md` | **Built.** The GitHub profile README — rendered on the profile page. Personal only: no platform, migration, or link content — GitHub already surfaces those from the profile |
| `docs/README.md` | **Built.** Platform documentation index — the repository table and doc map that used to live in `README.md` |
| `TODO.md` | **Built.** Cross-repository v2.0.0 roadmap |
| `assets/` | **Built.** `cover.png` for the profile README |
| `docs/brand/` | **Built.** Brand guide, canonical token sheet, logo, voice |
| `docs/design/` | **Built.** Design system contract, reconciled HTML reference |
| `docs/architecture/` | **Built.** Platform overview, API contract, content pipeline, redirects |
| `docs/migration/` | **Built.** v2.0.0 migration plan, versioning policy |

## Source material — read before writing any brand doc

Three working files sit untracked at the repository root:
`dileepa-brand-guide-v2.0.0.md`, `brand-tokens.css`, `index.html`.

> [!IMPORTANT]
> **Do not commit these three files at the repository root.** They are raw source material.
> The task is to publish reconciled versions under `docs/`, not to check the working copies in.

They disagree with each other. The brand guide is marked **Final** and wins; `brand-tokens.css`
matches it; `index.html` does not. Six known conflicts, all of which must be resolved in
`docs/design/design-system.md` before any application implements them:

1. `index.html` declares `--cyan`, `--gold`, `--gold-deep`, `--signal-tech`. The guide permits
   **one accent**. Strip them.
2. The neutral ramps differ. `index.html` uses `ink-900 #050505`, `ink-800 #0D0D0D`,
   `ink-700 #141414`, `ink-600 #1D1D1D`, `ink-400 #8D8D8D`, `paper-200 #E4E4DA`,
   `paper-400 #6B6B62`, `paper-900 #12140F`. `brand-tokens.css` wins — the published contrast
   ratios were measured against its values.
3. `index.html` sets `--font-mono: "Manrope"` and never loads JetBrains Mono. The guide requires
   JetBrains Mono for code and data.
4. `index.html` loads weights `400;500;600;700;800` and uses 600 and 800. The guide permits
   **400, 500, 700 only**.
5. `.subsection-title::before` puts `--emerald-deep` on Carbon — the guide names that as the one
   hard failure. Use `--brand` so it flips per theme.
6. The lockup is `dileepadev /.` — neutral wordmark, *italic* emerald slash, then an emerald dot.
   `index.html` renders the slash non-italic at weight 600 and spaces the dot with `margin-right`
   rather than `margin-left`, so it reads as `/ .` rather than `/.`

**The rule for every downstream repo:** `index.html` is a *layout and structure* reference.
Every colour, type, and token value comes from `brand-tokens.css`.

## Brand rules that must never be broken

- Emerald is the only accent. No second hue, anywhere, ever.
- Never Emerald Deep (`#087F5B`) on Carbon. Never Emerald Bright (`#23B888`) on Paper.
- Manrope for display and UI, JetBrains Mono for code and data. No third family.
- Weights 400, 500, 700 only. No 600.
- Sentence case everywhere — headings, buttons, nav, labels.
- The wordmark is never emerald; the `/.` is never the neutral text colour.
- Banned words, without exception: *passionate about, leveraging, cutting-edge, revolutionize,
  game-changing, unlock, seamless, AI enthusiast, thought leader, journey, humbled to announce,
  10x.*

## Toolchain

None. No `package.json`, no build step, no dependencies, no tests. This is a Markdown and asset
repository. Do not add a build system to it without a concrete reason.

If a linter is ever added, it should be a Markdown linter in CI and nothing more.

## Coding standards

- Prose, not code. Write in the voice defined in the brand guide §4 — plain, specific,
  unhurried. Explain rather than announce.
- The test for any sentence: could someone who hasn't built anything have written it? If yes,
  cut it and replace it with the specific.
- Markdown only. Tables for anything comparative. Fenced code blocks with a language tag.
- **Diagram nodes are repository names, never domains.** `dileepa-dev`, not `dileepa.dev`.
  Anything that is not a repo name is an external service (`MongoDB Atlas`, `Cloudinary`,
  `GitHub API`). Domains belong in tables, where they can be labelled. The naming key in
  `docs/architecture/platform-overview.md` §2.0 is the reference — three of these names differ
  only by a hyphen or a dot, and mixing them is the single easiest way to make a diagram
  unreadable six months from now.
- Documents here are read by people implementing in six other repositories — be exact about
  file paths, token names, and version numbers. Vague guidance produces drift.
- When a decision is still open, say so explicitly and record the recommendation and the
  alternatives. Do not present an unmade decision as settled.

## Testing

There is nothing to run. Verification here means:

- Every file path, token name, and hex value referenced in a doc actually exists.
- Cross-repository links resolve.
- The token values in `docs/brand/brand-tokens.css` match what the applications import.

## Docs

This repository *is* the docs. Two specific ownership rules:

- `docs/brand/brand-tokens.css` is the **canonical** token sheet, and this repo is the **only**
  place brand assets live. There is no mirror and no CDN — `dileepadev.github.io` is a dashboard,
  not an asset host.

  Applications **vendor** the file: copy it into their own repo and record where it came from.
  They must never hot-link it, because `raw.githubusercontent.com` serves CSS as `text/plain`
  and browsers refuse to apply a stylesheet with that content type. Vendoring means copying the
  *file*; it never means copying values out of it into components.

  Every vendored copy is a copy that can drift. When this file changes, the change has to be
  pushed into each consuming repo deliberately.
- `docs/architecture/redirects.md` is the **single source of truth** for the blog URL map.
  `dileepa-dev` implements it and `blog-dileepa-dev` depends on it. Three places must never
  disagree about which old URL points where.

## Git workflow

This repository does not carry the guideline documents the application repos do. The
conventions still apply:

- Branches: `feat/x`, `fix/x`, `docs/x`, `chore/x`. `main` is protected.
- Commits: `<type>(<scope>): <short message> (<issue refs>)` — types `feat`, `fix`, `docs`,
  `style`, `refactor`, `perf`, `test`, `chore`. Most work here is `docs`.
- Reference the issue when the work traces to one; don't invent an issue number if none was
  given. v2.0.0 work traces to `refs #1`.
- Versioning: this repo has no version number and does not need one.

## Secrets

None. Nothing here reads an environment variable or holds a credential. If a document needs to
show a config example, use obvious placeholders and never a real value.

## Gotchas

- **The three root files are untracked on purpose.** `git add .` in this repository will stage
  them. Stage explicitly.
- **`README.md` is personal, not platform.** It renders on the GitHub profile page — the
  most-viewed file in the whole platform — and GitHub already surfaces this repo's links and
  pinned status from the profile itself. Repository structure, the platform table, and any
  migration status go in [`docs/README.md`](docs/README.md), never back into the profile README.
- **The guide says "change at most one thing per review."** Treat the brand guide as frozen for
  the duration of v2.0.0; queue changes for after the release.
