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
| `CHANGELOG.md` | **Built.** Release history, back to `v0.1` |
| `DESIGN.md` | **Built.** Machine-readable design token and UI contract — the values, where `docs/brand/` carries the prose |
| `docs/brand/` | **Built.** Brand guide, canonical token sheet, design system contract, logo and asset sets |
| `docs/architecture/` | **Built.** Platform overview, API contract, content pipeline, redirects |
| `docs/migration/` | **Built.** v2.0.0 migration plan, versioning policy |
| Community standards | **Built.** `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `VERSIONING.md`, the three guideline documents, and the `.github/` issue and PR templates |

## Source material — the six conflicts, and how they were settled

This section is a record, not a task. v2.0.0 published reconciled versions under `docs/`; the
three working files (`dileepa-brand-guide-v2.0.0.md`, `brand-tokens.css`, `index.html`) were
never committed at the repository root and are gone from the working tree.

Keep it because the conflicts explain *why* several token values look the way they do, and
because anyone reading an old copy of `index.html` will hit them again. The brand guide is marked
**Final** and wins; `docs/brand/brand-tokens.css` matches it; `index.html` did not. All six are
resolved in `docs/brand/design-system.md`:

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

**The rule for every downstream repo still stands:** treat `index.html` as a *layout and
structure* reference only. Every colour, type, and token value comes from
`docs/brand/brand-tokens.css`.

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

- Prose, not code. Write plainly and specifically, and explain rather than announce. The
  sentence-case rule and the banned-word list are `DESIGN.md` §17.1 and §17.2, repeated under
  **Brand rules** below. (Brand guide §4 is a colour and type quick reference, not a voice
  section — there is no §4.3, and `docs/brand/voice.md` was never created.)
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
- `docs/architecture/redirects.md` is the **single source of truth** for URL changes on
  `dileepa.dev`; `dileepa-dev` implements it. It is no longer a cross-host map — `blog.dileepa.dev`
  is retired rather than redirected, and what that costs is recorded in its §1 so the absence of a
  redirect table is not mistaken for an oversight. Two same-site slug rules survive.

## Git workflow

As of v2.0.0 this repository carries the same guideline documents the application repos do.
They are the authority; what follows is the short version.

- Branches: `feat/x`, `fix/x`, `docs/x`, `chore/x` — [BRANCH_NAMING_GUIDELINES.md](BRANCH_NAMING_GUIDELINES.md).
  `main` is protected and there is no `dev` branch here.
- Commits: `<type>(<scope>): <short message> (<issue refs>)` — types `feat`, `fix`, `docs`,
  `style`, `refactor`, `perf`, `test`, `chore`. Most work here is `docs`. Full rules in
  [COMMIT_MESSAGE_GUIDELINES.md](COMMIT_MESSAGE_GUIDELINES.md).
- Pull requests: title format and expectations in
  [PULL_REQUEST_GUIDELINES.md](PULL_REQUEST_GUIDELINES.md); body structure in
  [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).
- Reference the issue when the work traces to one; don't invent an issue number if none was
  given. v2.0.0 work traces to `refs #1`.
- Versioning: the **git tag is the version** — there is no manifest and no version string in a
  file. A release is a tag plus the matching section in [CHANGELOG.md](CHANGELOG.md). See
  [VERSIONING.md](VERSIONING.md). Tags before `v2.0.0` used a two-part form (`v0.1`, `v0.2`,
  `v1.0`) and are left as they are.

## Secrets

None. Nothing here reads an environment variable or holds a credential. If a document needs to
show a config example, use obvious placeholders and never a real value.

## Gotchas

- **`docs/design/` does not exist, and never did.** The design system lives at
  `docs/brand/design-system.md`, beside the guide it derives from. Older notes and the v2.0.0
  issue describe a `docs/design/` directory that was planned and not built; the same goes for
  `docs/brand/voice.md` — the voice rules are brand guide §4 and were never split out.
- **`README.md` is personal, not platform.** It renders on the GitHub profile page — the
  most-viewed file in the whole platform — and GitHub already surfaces this repo's links and
  pinned status from the profile itself. Repository structure, the platform table, and any
  migration status go in [`docs/README.md`](docs/README.md), never back into the profile README.
- **The guide says "change at most one thing per review."** Treat the brand guide as frozen for
  the duration of v2.0.0; queue changes for after the release.
