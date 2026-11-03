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

| Repository             | Role                                         | v2.0.0 issue           | v2.1.0 issue           |
| ---------------------- | -------------------------------------------- | ---------------------- | ---------------------- |
| `dileepadev`           | Brand + platform documentation root          | #1                     | #4                     |
| `dileepa-dev`          | Main website — blog, projects, events        | dileepa-dev#15         | dileepa-dev#27         |
| `api-dileepa-dev`      | FastAPI backend (migrated from NestJS)       | api-dileepa-dev#13     | api-dileepa-dev#29     |
| `blog-dileepa-dev`     | Content-source repository only               | blog-dileepa-dev#3     | —                      |
| `admin-dileepa-dev`    | Admin app                                    | admin-dileepa-dev#4    | admin-dileepa-dev#10   |
| `links-dileepa-dev`    | Links page                                   | links-dileepa-dev#2    | links-dileepa-dev#5    |
| `dileepadev.github.io` | Public build log — GitHub activity dashboard | dileepadev.github.io#1 | dileepadev.github.io#7 |

[TODO.md](TODO.md) records the v2.1.0 scope, release status and tracking issues. Detailed
checklists and progress belong in GitHub issues, not in `TODO.md`. Completed v2.0.0 migration
history lives in `CHANGELOG.md` and `docs/migration/`.

## Layout

| Path                 | Status                                                                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `README.md`          | **Built.** The GitHub profile README — rendered on the profile page. Personal only: no platform or migration content — GitHub already surfaces those from the profile                                                                                         |
| `docs/README.md`     | **Built.** Platform documentation index — the repository table and doc map that used to live in `README.md`                                                                                                                                                   |
| `TODO.md`            | **Built.** v2.1.0 scope, release status and tracking issue links                                                                                                                                                                                              |
| `CHANGELOG.md`       | **Built.** Release history, back to `v0.1`                                                                                                                                                                                                                    |
| `DESIGN.md`          | **Built.** Machine-readable design token and UI contract — the values, where `docs/brand/` carries the prose. An exact copy of the website's                                                                                                                  |
| `docs/brand/`        | **Built.** The brand guide, canonical token sheet and design system contract, OG cards, favicons and portraits (exact copies of the website), plus the logo, pillar icons and the animated profile README cover drawn here. `docs/brand/README.md` is the map |
| `docs/architecture/` | **Built.** Platform overview, API contract, content pipeline, redirects                                                                                                                                                                                       |
| `docs/migration/`    | **Built.** v2.0.0 migration plan, versioning policy                                                                                                                                                                                                           |
| Community standards  | **Built.** `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `VERSIONING.md`, the three guideline documents, and the `.github/` issue and PR templates                                                                                                  |

## Brand rules that must never be broken

These are the **v2.1.0** rules (dileepadev#4).

- **No brand hue.** The accent is the text colour — `--brand` is Ink 100 `#F1F1F1` on Carbon and
  Paper 900 `#131313` on Paper. Colour appears only as a state: `--success`, `--error`,
  `--warning`. Never add a hue as an accent.
- Components use semantic tokens only — never a hex, never a raw ramp token.
- Three text steps: `--fg` for titles, `--fg-body` for running text, `--fg-muted` for metadata.
- Manrope for display and UI, JetBrains Mono for code and data. No third family.
- Weights 400, 500, 700 only. No 600. Every heading is 500; 700 is the display line and
  `<strong>` only. Nothing smaller than 13px (`--text-label`).
- Corners are fixed (panel, tile, block, inline), capsule (every control and field), or
  concentric (a row inside a tile). Never invent a radius.
- An edge means it acts: buttons, selects and interactive chips take `--border-strong`, fields
  take `--border-input`, labels take none.
- Every text link carries an arrow — `→` on the site, `↗` off it.
- The logo is the handle, `@dileepadev`: the `@` in `--fg-muted`, the wordmark in `--fg`, both
  Manrope 500, no gap. Black and white only.
- Sentence case everywhere — headings, buttons, nav, labels.
- Banned words, without exception: _passionate about, leveraging, cutting-edge, revolutionize,
  game-changing, unlock, seamless, AI enthusiast, thought leader, journey, humbled to announce,
  10x._

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
- Each imported file still matches the website's `v2.1.0` tag, byte for byte.

## Docs

This repository _is_ the docs. Two specific ownership rules:

- `docs/brand/brand-tokens.css` is the **canonical** token sheet, and this repo is the **only**
  place brand assets live. There is no mirror and no CDN — `dileepadev.github.io` is a dashboard,
  not an asset host.

  Applications **vendor** the file: copy it into their own repo and record where it came from.
  They must never hot-link it, because `raw.githubusercontent.com` serves CSS as `text/plain`
  and browsers refuse to apply a stylesheet with that content type. Vendoring means copying the
  _file_; it never means copying values out of it into components.

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
  given. v2.0.0 work traced to `refs #1`; v2.1.0 work traces to `refs #4`.
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
  `docs/brand/voice.md` — the voice rules are in `DESIGN.md` §17 and were never split out.
- **`README.md` is personal, not platform.** It renders on the GitHub profile page — the
  most-viewed file in the whole platform — and GitHub already surfaces this repo's links and
  pinned status from the profile itself. Repository structure, the platform table, and any
  migration status go in [`docs/README.md`](docs/README.md), never back into the profile README.
- **v2.1.0 was designed on `dileepa-dev` first, not here.** The brand guide, design system, token
  sheet, `DESIGN.md`, OG cards, favicons and portraits are exact copies of the website at its
  `v2.1.0` tag. `docs/brand/README.md` records the commit and maps each file to its source. Do not add tokens, tune values or fix anything in a copy: change the website, ship its
  tag, then copy again. Because copies are exact, relative links inside `DESIGN.md` follow the
  website's layout, where `docs/brand-guide.md` is here `docs/brand/brand-guide.md`.
- **The brand version is 2.1.0, deliberately.** Every brand file carries `v2.1.0`; do not relabel
  it 3.0 even though `VERSIONING.md` would call a reversed brand rule major.
- **Check sheet content as well as its label.** The current sheet is headed
  `brand tokens v2.1.0`, has `--fg-body` and `--border-input`, and sets
  `--brand: var(--ink-100)` on Carbon. An older emerald sheet was also labelled `v2.1`, so a
  header alone proves nothing. When an application re-vendors the sheet, compare its copy with
  this repository's tag, not with the label.
- **The logo, pillar icons and the profile README cover are generated; do not edit their output.**
  `docs/brand/logo/` and `icons/` each have a generator and a README, and
  `docs/brand/github-readme.svg` is built by `github-readme.py` beside it. Change the generator (or
  a pillar's `-symbol.svg`) and rebuild. Social platform covers are not kept here, because they
  change; [`docs/brand/social-cover-guide.md`](docs/brand/social-cover-guide.md) says how to make
  one. The OG cards, `og.png` and `og2.png`, are separate and are exact copies of the website's.
