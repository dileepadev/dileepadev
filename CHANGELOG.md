# Changelog

All notable changes to this project are documented in this file.

Changes are organized into the following categories:

- **Added:** New features or functionality introduced to the project.
- **Changed:** Modifications to existing functionality that do not add new features.
- **Fixed:** Bug fixes that resolve issues or correct unintended behavior.
- **Removed:** Features or components that have been removed from the project.

## [Unreleased]

Unreleased changes go here.

## [v2.0.0] - 2026-09-03

> [!NOTE]
> This repository stops being a profile README and becomes the **platform root**: the single
> place that holds the brand guidelines, the design system, the architecture documentation, and
> the cross-repository roadmap that the other six repositories implement against.
>
> - v2.0.0 is not a version bump. It is the move from six independently versioned projects to one
>   platform with a shared brand, a shared design system, and a single aligned baseline. All
>   seven repositories ship `2.0.0` together — the full roadmap is in [TODO.md](TODO.md).
> - **This repository is the only home for brand assets.** There is no mirror and no CDN.
>   Consuming repositories vendor what they need and record the source; hot-linking does not work,
>   because `raw.githubusercontent.com` serves CSS as `text/plain` and browsers refuse to apply it.
> - It still ships no application. There is no build, no test suite, and no dependencies.

### Added - v2.0.0

- **The brand system** under `docs/brand/` — `brand-guide.md` (marked Final and authoritative),
  `brand-tokens.css` as the canonical token sheet for the whole platform, and `design-system.md`
  as the component contract every frontend implements.
- **Brand assets** — the `dileepadev /.` lockup and the reduced `/.` mark in SVG for light and
  dark surfaces, a full favicon set, banners, covers, icons, and profile portraits. The portrait
  field was added to the guide and the portrait assets regenerated against it.
- **Platform architecture documentation** under `docs/architecture/` — `platform-overview.md`
  (the target architecture across all seven repositories, with the naming key in §2.0),
  `api-contract.md` (the canonical endpoint list and data models, including engagement, comments
  and comment reactions), `content-pipeline.md` (the blog-repo-to-site rendering path), and
  `redirects.md` (the single source of truth for URL changes on `dileepa.dev`).
- **Migration documentation** under `docs/migration/` — `v2.0.0-migration.md` for the
  cross-repository plan, sequencing and rollback, and `versioning-policy.md` for how each
  repository is versioned after the release.
- **[TODO.md](TODO.md)** — the cross-repository v2.0.0 roadmap, nine phases across seven
  repositories, plus the risk register.
- **[docs/README.md](docs/README.md)** — the platform documentation index. The repository table
  and doc map live here rather than in the profile README.
- **[AGENTS.md](AGENTS.md)** — canonical instructions for AI coding agents, and the single source
  of truth for this repository's rules. `CLAUDE.md` and `.github/copilot-instructions.md` carry
  only tool-specific notes and point back to it.
- **[DESIGN.md](DESIGN.md)** — the machine-readable design token and UI contract, for agents that
  need the values rather than the prose.
- **`.github/agents/pr-preparer.agent.md`** — a Copilot custom agent that opens pull requests
  against whatever conventions a repository actually documents, and refuses when the branch is
  not clean. Routed to request `dileepadev` as reviewer.
- **Community standards** — [CONTRIBUTING.md](CONTRIBUTING.md),
  [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) (Contributor Covenant 2.0),
  [SECURITY.md](SECURITY.md), [VERSIONING.md](VERSIONING.md), this `CHANGELOG.md`,
  [BRANCH_NAMING_GUIDELINES.md](BRANCH_NAMING_GUIDELINES.md),
  [COMMIT_MESSAGE_GUIDELINES.md](COMMIT_MESSAGE_GUIDELINES.md),
  [PULL_REQUEST_GUIDELINES.md](PULL_REQUEST_GUIDELINES.md), the five issue templates, and the
  pull request template. Adapted to this repository rather than copied — it has no build, no
  tests, and no credentials, and the documents say so.
- An extended cSpell dictionary in `.vscode/settings.json`.

### Changed - v2.0.0

- **The profile README is rewritten in the v2.0.0 voice** and is personal only — no platform
  table, no migration status. GitHub's profile page already surfaces links and pinned
  repositories, and the repository table now lives in [docs/README.md](docs/README.md). The
  "passionate about" opening is gone — `DESIGN.md` §17.2 bans it without exception.
- **The six token conflicts between the source documents were resolved before any application
  implemented them**, and the resolution is recorded in `design-system.md`: the second accent
  (`--cyan`, `--gold`, `--gold-deep`, `--signal-tech`) stripped, the neutral ramp taken from
  `brand-tokens.css` because the published contrast ratios were measured against it, JetBrains
  Mono actually loaded for code and data, weights restricted to 400/500/700, Emerald Deep taken
  off Carbon, and the lockup's slash set at weight 700 with the dot spaced by `margin-left` so it
  reads `/.` rather than `/ .`.
- **`blog.dileepa.dev` is recorded as retired, not redirected.** `redirects.md` §1 states the
  decision and what it costs — indexed and third-party links to the old host will 404 — so the
  absence of a redirect table is not mistaken for an oversight. Two same-site slug rules survive.
  The change was propagated across the architecture docs and the roadmap, and the gate on the
  blog decommission was lifted.
- The brand documentation was reconciled against what actually shipped, rather than against what
  was planned.
- The roadmap was rewritten as each phase closed, including the host retirement in Phase 4 and
  the post-contract work.

### Fixed - v2.0.0

- The redirect status code is recorded as **308**, not 301 — the distinction matters to the
  implementation in `dileepa-dev`.
- The posts directory path in the content pipeline was wrong and is corrected.
- The data-flow and image claims in the architecture documentation described a pipeline that was
  never built; they now describe the one that was.
- The image items in the redirect map were left open after the work was done, and are closed.
- A `txt` code fence was missing its language tag in `design-system.md`.
- An MD028 lint warning between the two header alerts in `TODO.md`.

### Removed - v2.0.0

- **`assets/cover.png`** and the cover image from the profile README. The banner it was doing the
  job of now lives under `docs/brand/covers/`, and the profile README carries an SVG header
  instead.
- The three untracked working files at the repository root
  (`dileepa-brand-guide-v2.0.0.md`, `brand-tokens.css`, `index.html`) were never committed as-is.
  Reconciled versions were published under `docs/` instead, and `index.html` survives only as a
  layout reference — every colour, type and token value comes from `brand-tokens.css`.

## [v1.0] - 2026-08-23

### Changed - v1.0

- The profile README was cut back to a two-line introduction. The "What you'll find here",
  "Currently exploring", and remaining list sections were removed, taking the file from 29 lines
  to 3.
- `assets/cover.png` was replaced with a smaller export — 718 KB down to 448 KB.

### Removed - v1.0

- The cover image was dropped from the README. The file stayed in `assets/`, unreferenced, until
  v2.0.0.

## [v0.2] - 2026-08-06

### Added - v0.2

- `assets/cover.png` — the cover image, committed to the repository instead of being hot-linked
  from GitHub user-attachments as it was in v0.1.
- `.gitignore`, covering `*.code-workspace`.
- `.vscode/settings.json`.
- The README gained "What you'll find here" and "Currently exploring" sections listing the
  areas of work — AI agents, LLM applications, MCP integrations, cloud and backend engineering.

### Changed - v0.2

- The README heading became `# Hi there 👋`, and the introduction was expanded from three bullets
  to prose naming the kind of work.

## [v0.1] - 2026-02-28

### Added - v0.1

- The initial GitHub profile README, with a cover image hot-linked from GitHub
  user-attachments.
- The MIT `LICENSE`.

<!-- e.g., -->
<!-- Unreleased -->
<!-- v2.0.0 -->
<!-- v1.1.0 -->
<!-- v1.0.0 -->
<!-- v0.0.1 -->

[Unreleased]: https://github.com/dileepadev/dileepadev/branches
[v2.0.0]: https://github.com/dileepadev/dileepadev/releases/tag/v2.0.0
[v1.0]: https://github.com/dileepadev/dileepadev/releases/tag/v1.0
[v0.2]: https://github.com/dileepadev/dileepadev/releases/tag/v0.2
[v0.1]: https://github.com/dileepadev/dileepadev/releases/tag/v0.1
