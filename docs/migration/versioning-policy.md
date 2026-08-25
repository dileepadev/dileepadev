# Versioning policy

How each repository is versioned from v2.0.0 onward.

## 1. The baseline

v2.0.0 is the point where every repository lines up. Before it, versions drifted — `1.0.0`
through `1.3.0` across six repos, with the two Next.js apps a patch release apart from each
other for no reason anyone could name.

| Repository | v1.x | v2.0.0 |
| --- | --- | --- |
| `dileepa-dev` | 1.3.0 | **2.0.0** |
| `api-dileepa-dev` | 1.2.0 | **2.0.0** |
| `blog-dileepa-dev` | 1.1.0 | **2.0.0** — final release |
| `admin-dileepa-dev` | 1.0.0 | **2.0.0** |
| `links-dileepa-dev` | 1.0.0 | **2.0.0** |
| `dileepadev.github.io` | none | **2.0.0** |
| `dileepadev` | none | not versioned |

## 2. After v2.0.0: independent again, deliberately

Aligning at 2.0.0 does not mean lockstep forever. Forcing five repositories to release together
means either releasing things that did not change, or holding back things that are ready.

**From v2.0.1 onward each application versions independently on SemVer:**

- **MAJOR** — incompatible API change or a breaking update
- **MINOR** — backward-compatible feature
- **PATCH** — backward-compatible fix

What v2.0.0 buys is a **common floor**. Every repo is on the same brand, the same design
system, and the same API contract. Drift from here is intentional and visible, not accidental.

### The one coupling that stays

`dileepa-dev` and `admin-dileepa-dev` must run **identical** Next.js and React versions. They
share a design system and component patterns, and a framework difference between them is how
the platform fragments again. Upgrade them in the same pull request or not at all.

## 3. Repository-specific rules

### `blog-dileepa-dev` — leaves the release model

v2.0.0 is the **final release** associated with this repository. After it:

- `main` is the source of truth for content.
- No standalone blog website.
- **No application releases for content changes.** Publishing a post is a commit, not a release.
- `CHANGELOG.md` is frozen at `2.0.0` with a note explaining the transition.
- `VERSIONING.md` is replaced by a short content policy.
- `package.json` is removed, or kept only for tooling and clearly not describing an application.

A content repository with a version number invites the question of what `2.1.0` would mean.
There is no good answer, so the number goes.

### `dileepadev` — not versioned

Brand and documentation. The brand guide carries its own version (2.0.0, Final); the repository
does not need one.

### `dileepadev.github.io` — versioned, barely

Gets a `2.0.0` and a `CHANGELOG.md` so it sits inside the platform's story. v2.0.0 is where it
stops being an image directory and becomes the public build log, so it now has a build like any
other frontend and versions normally from here.

## 4. Release process

Unchanged from the existing `VERSIONING.md` in each repo:

1. Complete the features and fixes planned for the release.
2. Update `CHANGELOG.md` with categorised entries — **Added**, **Changed**, **Fixed**, **Removed**.
3. Bump the version in `package.json` (or `pyproject.toml` for the API).
4. Commit as `chore: release v2.0.0`.
5. Tag: `git tag v2.0.0 && git push origin v2.0.0`.
6. Optionally create a GitHub release with the changelog section.

Pre-releases use `2.1.0-beta.1` and `3.0.0-rc.1` suffixes.

## 5. Branches

`main` is production. `dev` is preview, where the repo has one. Feature work happens on
`feat/x`, `fix/x`, `docs/x`, `chore/x`.

v2.0.0 work lives on `feat/v2.0.0` in `dileepa-dev`, `api-dileepa-dev`, `admin-dileepa-dev`,
and `links-dileepa-dev`.

## 6. The v2.0.0 tag

Two of these tags mean more than a version bump and should be created deliberately:

- **`blog-dileepa-dev` `v2.0.0`** — archives the final Astro build. It is the only way to
  reconstruct the old site if the migration missed something. Tag it **before** deleting the
  application.
- **`api-dileepa-dev` `v2.0.0`** — the last commit where the NestJS implementation still exists
  alongside FastAPI. Tag it before removing `src/`.
