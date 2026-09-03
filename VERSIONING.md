# Versioning

This project follows a versioning pattern similar to [Semantic Versioning](https://semver.org/) (SemVer) for managing releases.

## Table of Contents

- [Versioning](#versioning)
  - [Table of Contents](#table-of-contents)
  - [What is versioned here](#what-is-versioned-here)
  - [Format](#format)
    - [Examples](#examples)
    - [Tag history](#tag-history)
  - [Release Process](#release-process)
    - [Typical Steps](#typical-steps)
  - [Pre-release Versions](#pre-release-versions)
  - [Viewing Tags \& Differences](#viewing-tags--differences)
  - [Questions or Issues?](#questions-or-issues)

## What is versioned here

This repository ships no application, so there is no package manifest and no version string in a
file. **The git tag is the version.** A release is a tag plus the matching section in
[CHANGELOG.md](CHANGELOG.md), and nothing else declares a number.

What the version describes is the state of the published standards — the brand guide, the token
sheet, the design system, and the architecture documentation. Consuming repositories **vendor**
those files rather than importing them, so a version here tells them which copy they are working
from. It does not move on its own: a vendored file only changes when someone deliberately
copies the new one across.

Per-repository versioning for the rest of the platform is a separate document —
[`docs/migration/versioning-policy.md`](docs/migration/versioning-policy.md).

## Format

Version numbers follow the structure:

`MAJOR.MINOR.PATCH`

- **MAJOR** – Breaking changes to a published standard: a token removed or renamed, a brand rule
  reversed, an architecture decision replaced
- **MINOR** – New documentation, new assets, or a standard extended in a backward-compatible way
- **PATCH** – Corrections that do not change what implementers must do: typos, broken links,
  clarifications

### Examples

- `2.0.0` – The platform migration: brand, design system, and architecture published together
- `2.1.0` – Adds a document or an asset without invalidating a vendored copy
- `2.0.1` – Fixes a wrong path or a broken cross-repository link

### Tag history

Tags before `v2.0.0` used a shortened two-part form (`v0.1`, `v0.2`, `v1.0`) from when this
repository held only a profile README. They are left as they are — retagging published history
costs more than the inconsistency does. From `v2.0.0` onward the full `MAJOR.MINOR.PATCH` form is
used.

## Release Process

All notable changes are documented in the [CHANGELOG.md](CHANGELOG.md) file.

### Typical Steps

1. Complete all documentation and asset work planned for the release
2. Update the `CHANGELOG.md` with categorized entries:
   - **Added**, **Changed**, **Fixed**, **Removed**
   - Security work is not a category of its own. Hardening goes under **Added** and a
     vulnerability closed goes under **Fixed**, each as a `Security` subsection inside that
     category. Anything deprecated is recorded under **Removed**, beside what replaces it
3. Check that [TODO.md](TODO.md) reflects what actually shipped, and that every file path and
   token name referenced in a changed document still exists. There is no build to catch these
4. Commit changes with a version-related message (e.g. `chore: release v1.2.0`)
5. Tag the release:

   ```bash
   git tag v1.2.0
   git push origin v1.2.0
   ```

6. Create a GitHub release and paste the relevant changelog section
7. If the token sheet or a brand asset changed, push the new copy into each consuming repository
   deliberately — nothing propagates on its own

## Pre-release Versions

For beta or release candidates, we use suffixes:

- `1.2.0-beta.1` – Beta release
- `2.0.0-rc.1` – Release candidate

These versions are intended for testing and may not be fully stable.

## Viewing Tags & Differences

List all version tags:

```bash
git tag
```

View differences between versions:

```bash
git log v1.1.0..v1.2.0
```

## Questions or Issues?

If you have questions about the versioning strategy or encounter version-related problems, feel free to open an issue on the [GitHub repository](https://github.com/dileepadev/dileepadev/issues).
