# TODO — v2.0.0 platform migration ✅

Cross-repository roadmap for the v2.0.0 rebrand and platform consolidation.

> [!NOTE]
> This is the platform-level roadmap. Each repository carries its own slice in its own `TODO.md`, and the full scope for each lives in its v2.0.0 issue. This file is the source of truth for **sequencing across repositories**.

<!-- -->

> [!TIP]
> **Shipped.** All nine phases complete, all seven repositories at `2.0.0`, all seven issues
> closed. Four items survive this file's own close-out. One is a real contrast bug, found and
> fixed in `dileepadev.github.io`, that exists identically and unfixed in `dileepa-dev` — see the
> risk register and Phase 8 §Brand compliance. The other three are documentation
> inconsistencies found while closing out this repository — see **Open after v2.0.0**.

## Repositories and issues

| Repository | Role after v2.0.0 | Shipped | Issue |
| --- | --- | --- | --- |
| `dileepadev` | Brand + platform documentation root | `2.0.0` | [#1](https://github.com/dileepadev/dileepadev/issues/1) — closed |
| `dileepa-dev` | Main website — absorbs blog, projects, events | `2.0.0` | [#15](https://github.com/dileepadev/dileepa-dev/issues/15) — closed |
| `api-dileepa-dev` | FastAPI backend (migrated from NestJS) | `2.0.0` | [#13](https://github.com/dileepadev/api-dileepa-dev/issues/13) — closed |
| `blog-dileepa-dev` | Content-source repository only | `2.0.0` | [#3](https://github.com/dileepadev/blog-dileepa-dev/issues/3) — closed |
| `admin-dileepa-dev` | Admin app — new design system + FastAPI | `2.0.0` | [#4](https://github.com/dileepadev/admin-dileepa-dev/issues/4) — closed |
| `links-dileepa-dev` | Links page — new design system | `2.0.0` | [#2](https://github.com/dileepadev/links-dileepa-dev/issues/2) — closed |
| `dileepadev.github.io` | Public build log — GitHub activity dashboard | `2.0.0` | [#1](https://github.com/dileepadev/dileepadev.github.io/issues/1) — closed |

## Target versions

| Component | From | To |
| --- | --- | --- |
| Next.js | 16.1.4 / 16.1.6 | 16.3.x (both apps identical) |
| React | 19.2.3 | 19.2.x latest |
| Tailwind CSS | 4.1.x | 4.3.x |
| Astro (links) | 5.17.1 | 7.x |
| API framework | NestJS 11 | FastAPI 0.141.x on Python 3.13 |
| API host | Vercel serverless | FastAPI Cloud |
| Validation | class-validator | Pydantic 2.13.x |
| All repositories | mixed 1.0.0–1.3.0 | **2.0.0** |

## Phase 0 — Discovery and scope ✅

- [x] Review every repository, its README, structure, and dependencies
- [x] Review the existing implementation and architecture of each project
- [x] Review the v2.0.0 brand guide, token sheet, and HTML design reference
- [x] Identify conflicts between the brand guide, `brand-tokens.css`, and `index.html`
- [x] Map the existing published blog URL structure (18 posts + 1 legacy slug)
- [x] Define the target v2.0.0 architecture
- [x] Update all seven GitHub issues with repository-specific scope and acceptance criteria
- [x] Create this roadmap
- [x] Close the six open architecture decisions (recorded in `docs/architecture/platform-overview.md` §3)

## Phase 1 — Platform standards (`dileepadev`) ✅

### Resolve token conflicts

- [x] Strip `--cyan`, `--gold`, `--gold-deep`, `--signal-tech` — the guide permits one accent
- [x] Reconcile the neutral ramp — `brand-tokens.css` values win (`ink-900 #0D0D0D`, not `#050505`)
- [x] Restore JetBrains Mono as `--font-mono` (the reference aliased it to Manrope)
- [x] Re-map weights 600 and 800 in the reference to the permitted 400 / 500 / 700
- [x] Replace `--emerald-deep` on Carbon in `.subsection-title::before` with `--brand`, and drop its glow
- [x] Correct the lockup — italic slash at weight 700, dot spaced with `margin-left`

### Documentation

- [x] `docs/brand/brand-guide.md` — published brand guide
- [x] `docs/brand/brand-tokens.css` — **canonical** token sheet, the one every app imports
- [x] `docs/brand/logo/` — lockup and reduced mark, SVG, light and dark
- [x] Voice rules and the banned-phrase list — **live in `DESIGN.md` §17**, not a standalone
      `docs/brand/voice.md`. This line originally named a file that was never created; the
      content exists, just consolidated into the single agent-facing reference instead
- [x] `docs/brand/design-system.md` — component contract for all three frontends (this line
      originally said `docs/design/`; the file lives under `docs/brand/`, alongside the guide and
      the token sheet it implements)
- [x] The standalone HTML reference this line originally planned was superseded by `DESIGN.md` —
      one agent-facing synthesis doc (brand guide + design system + machine-readable frontmatter)
      instead of a second, separately-maintained HTML artifact
- [x] `docs/architecture/platform-overview.md` — target architecture across all seven repos
- [x] `docs/architecture/api-contract.md` — endpoints and data models
- [x] `docs/architecture/content-pipeline.md` — blog repo → main site rendering path
- [x] `docs/architecture/redirects.md` — **complete old→new blog URL map (source of truth)**
- [x] `docs/migration/v2.0.0-migration.md` — sequencing, cutover, rollback
- [x] `docs/migration/versioning-policy.md` — including the blog repo leaving the release model
- [x] Rewrite `README.md` in the v2.0.0 voice (removed "passionate about")
- [x] Keep `README.md` personal-only; move the repository/platform table into `docs/README.md` (GitHub's profile page already surfaces links and pinned repos, so the profile README doesn't need to repeat them)

### Decisions — closed

- [x] **Blog content pipeline** — build-time fetch from GitHub, pinned to a ref; the API keeps a metadata index only
- [x] **`/blogs/sync` fate** — kept, retargeted at FastAPI, sending a relative `path` and a Cloudinary banner URL
- [x] **API host** — **FastAPI Cloud** (`fastapi deploy`, deploy token in CI, `fastapi cloud env set` for config)
- [x] **API custom domain** — available on every plan; Hobby allows one in total, which is exactly what `api.dileepa.dev` needs. `CNAME` at `api` → `<domain-id>.endpoints.fastapicloud.dev.`, TLS automatic. Attach after the first successful deploy, with Zero Downtime Migration enabled. Recorded in `docs/architecture/platform-overview.md` §3.2
- [x] **Image backend** — **Cloudinary**; Azure Blob retired. Only the API holds the credentials
- [x] **Blog image host** — Git stays the source of truth; the push workflow uploads through `POST /uploads` to Cloudinary, with deterministic public IDs
- [x] **Links data source** — stays static `links.json`; no `/links` API resource

### Assets — complete

- [x] Produce the favicon set (`favicon/` — `.ico`, PNG 16/32/96, android 36–512, apple 57–180, ms-tile 70/150/310, `manifest.json`, `browserconfig.xml`), the LinkedIn banner (`banners/linkedin.png`, 1584 × 396), and the default OG image (`og.png`, 1200 × 630) — all under `docs/brand/`, this repo's only home for them
- [x] **Decided: the favicon is the portrait**, not the reduced mark. The mark-based `favicon.svg` is removed, and brand guide §3.2 and `logo/README.md` now say so — the mark stays for in-product square placements
- [x] Fill in `favicon/manifest.json` and `favicon/browserconfig.xml` — real `name` / `short_name`, and `theme_color` / `background_color` / `TileColor` at `ink-900 #0D0D0D` instead of the generator's `#ffffff`
- [x] Add the 512 × 512 icon — `android-icon-512x512.png`, registered in `manifest.json`
- [x] Export outlined versions of both lockups for off-platform use — `logo/lockup-{dark,light}-outlined.svg`, Manrope converted to paths, no font dependency
- [x] Rebuild `favicon.ico` with 16, 32, and 48 — 32-bit BMP entries; the 16 and 32 are the generator's own files unchanged, the 48 downsampled from the 512

## Phase 2 — API migration (`api-dileepa-dev`) ✅ deployed

FastAPI is live at `api.dileepa.dev` on FastAPI Cloud. NestJS is retired; both frontends are cut
over.

### Added after the contract was drafted ✅

Three collections and six routes the v2.0.0 contract did not originally plan for. All are public
writes, and none collects an identity: each keys on a salted hash of the caller's address, which
recognises a repeat without being reversible into one.

- [x] **Blog views** — de-duplicated per reader per 24h by a unique index and a TTL on
      `blog_views`, not by a check in the handler
- [x] **Blog reactions** — four kinds, one per reader, changeable and clearable
- [x] **Comments** — one level of replies, live immediately, defended at the door with
      `RATE_LIMIT_COMMENT`, length bounds, a honeypot and a depth cap
- [x] **Comment reactions** — the same four, on comments and replies alike
- [x] `PublicComment` has **no field** for an email address, so the public routes cannot leak one.
      Moderation routes are admin-only on every route including the list — the one collection
      `crud_router` could not build, because its list route is public by design
- [x] `description` on videos
- [x] New collections: `blog_views`, `blog_reactions`, `comments`, `comment_reactions`. All four
      get their indexes on startup, so first deploy touches the database

### Baseline ✅

- [x] Scaffold FastAPI 0.141.x on Python 3.13 with `uv`, `ruff`, `mypy`, `pytest`
- [x] Async MongoDB driver (PyMongo async) against the **same cluster and collections**
- [x] Contract tests against current NestJS responses (parity baseline) — every v1.2.0 route is
      either served or recorded as deliberately dropped, with a reason
- [x] Stand FastAPI up alongside NestJS on a preview deployment — FastAPI Cloud has no PR-preview
      mechanism, so the `*.fastapicloud.dev` URL against production data served as the substitute

### Auth (highest cutover risk) ✅ resolved

- [x] **Node `bcrypt` hashes verified** — at cost 10 and 12, both `$2a$` and `$2b$`. Under
      **`pwdlib[bcrypt]`**, not `passlib`: passlib has been unmaintained since 2020 and breaks
      against bcrypt >= 4.1. Hashes are argon2id-first, so a legacy hash validates and is
      rewritten on the next successful sign-in. **No forced password reset.** The risk register
      entry below is closed
- [x] JWT access + refresh; algorithm, secret handling and claim names match v1. A token minted
      by NestJS has no `type` claim and is read as an access token, so live sessions survive
- [x] Role-based dependency guards mirroring the current RBAC
- [x] API-key guard for `/blogs/sync` — same header and environment variable as v1
- [x] **Run `scripts/verify_password_hash.py` against the production database** before cutover

### Port existing modules ✅

- [x] `users` · `auth`
- [x] `about` · `experiences` · `educations` · `tools` · `communities` · `videos`
- [x] `contact` · `uploads`
- [x] Rate limiting (`slowapi`), security headers, CORS allowlist
- [x] Consistent list/pagination envelope and error envelope `{ error: { code, message, details } }`
- [x] `GET /health`, `GET /version`

### New and changed resources ✅

- [x] **`/projects`** — full model, CRUD, filters (net-new)
- [x] **`/events` reshaped** — full model with speakers, photos, recordings, links, structured
      datetimes. `status` is derived from `startAt`, with an explicit `cancelled` respected.
      **The path does not change**: an earlier draft renamed the resource to `sessions`, and that
      is reverted — the site, the admin and the API all say "event", and `/events` was already a
      published URL
- [x] `?hasPhotos=` on `/events`, for the main site's event gallery. Expressed as a query so
      `total` stays truthful
- [x] `about` gains `location` — rendered beside the portrait as `"{title} · {location}"`
- [x] No deprecated aliases. `POST /auth/sign-in` and `POST /upload` are renamed with no alias:
      v2.0.0 ships as a single cutover, so there is no window in which an old path must answer
- [x] `/blogs` reshaped — relative `path`, `tags`, `series`, `readingTimeMinutes`, real
      `publishedDate`. **`banner` is retired**: it stays on the model, because removing a field is
      breaking for every consumer, and is never written

### Data migration — scripts written, none run

Every script defaults to dry-run. Running them against the live cluster is Phase 2's remaining
work, and the backup comes first.

- [x] **Take a verified, restore-tested MongoDB backup** — satisfied differently: `production` was
      populated by copying the already-migrated `development` database, which remains an intact
      fallback in place of a separate backup/restore test
- [x] Script rewriting the 18 blog rows off `blog.dileepa.dev`, with a rollback script. It now
      clears `banner` rather than carrying it to a new host
- [x] Dry-run and applied against `development`; the legacy-slug stub row is unpublished so it
      does not appear in the index or the sitemap
- [x] Dry-run and apply against `production`, after the backup — rows arrived already rewritten via
      the `development` → `production` copy rather than a direct script run against prod
- [x] Old values kept in a `legacy` field for one release
- [x] **`scripts/migrate_events_v1_to_v2.py`** — rewrites the 26 v1 `events` rows into the v2
      shape **in place**, keeping `_id`, after copying every original to `events_v1_backup`.
      Idempotent: a row already in the v2 shape is recognised and left alone
- [x] Dry-run and applied against `development` — 26 of 26 converted, no unparseable dates
- [x] Run it against `production`, after the backup — via the `development` → `production` copy
- [x] **`scripts/migrate_v1_documents.py`** — not in the original plan. Every ported collection
      lacks `published`, `order`, `meta` and timestamps, and stores ordering as `index`. The API
      reads around all of it, but sorting happens in MongoDB, before the model's aliasing
- [x] Run against `development`
- [x] **Run it against `production` to completion before traffic moves** — via the
      `development` → `production` copy

### Finish

- [x] OpenAPI metadata; docs disabled in production — in production neither the reference
      page nor the spec it reads is registered
- [x] Publish the OpenAPI spec for typed client generation — CI uploads it on every build
- [x] Theme Scalar against the brand tokens
- [x] Attach `api.dileepa.dev` **after** the first successful FastAPI Cloud deployment — a domain
      cannot be reserved ahead of a running app
- [x] Enable **Zero Downtime Migration** when adding the domain, so the certificate is issued while
      Vercel still serves traffic
- [x] Decide the plan before production traffic moves — Hobby is 0.1 vCPU / 512 MB shared with
      1-day log retention, and one custom domain total (staging would need Pro)
- [x] Cut both consumers over; observe; **then** delete `src/`, `package.json`, and the Node toolchain
- [x] Update `README.md`, `CHANGELOG.md`, `VERSIONING.md`; version → `2.0.0`

## Phase 3 — Main website (`dileepa-dev`) ✅

### Post interactions ✅

- [x] React · Comment · Share action bar under every article, counts summarised above it
- [x] Reactions, views and comments, all fetched in the browser — a post page is static and these
      are the only parts that change after a build
- [x] Comment replies one level deep, each comment and reply carrying the same four reactions
- [x] **Emoji glyphs rather than a custom icon set** — the brand guide allows one accent hue and no
      second, and emoji carry colour as content without entering the palette
- [x] Verified in a browser on both themes; two defects found and fixed there that no build would
      have caught — the compact picker covering the comment it was reacting to, and 🎓 rendering
      near-black on the dark theme
- [x] Video descriptions on `/videos` and the homepage, included in the search

### Foundation ✅

- [x] Next.js → 16.3.x, React → 19.2.x, Tailwind → 4.3.x, `@types/node` → ^22
- [x] Import brand tokens into Tailwind 4 `@theme`; **no hard-coded hex in components**
- [x] Manrope + JetBrains Mono via `next/font`, weights 400/500/700 only
- [x] MDX pipeline with Shiki (`github-light` / `github-dark` parity)
- [x] Generate `lib/api-types.ts` from the OpenAPI spec
- [x] **Split configuration by environment** — `.env.development` and `.env.production`, each
      complete on its own, matching how `api-dileepa-dev` splits its. No `.env.local`: it would
      override both and reintroduce the "which file won?" question the split exists to answer

### Rebrand ✅

- [x] Rebuild the component library against the design system contract
- [x] **Implement the layout reference exactly** — the 760px measure, the floating nav pill, the
      section rhythm, entry and item grids, the subsection rule, the footer. Reproduced in
      `app/globals.css` rather than approximated in utility classes, because "the same layout" has
      to keep being true after the next edit
- [x] `dileepadev /.` lockup; portrait-based favicon set; portrait on `--bg-surface`
- [x] Sentence case everywhere; all copy in the v2.0.0 voice
- [x] Section labels are words, not `01 /` numbers — numbering claims an order the page does not
      have and breaks when a section is added in the middle
- [x] The hero display heading is the **tagline**, not the name. What someone does is the useful
      thing to read first
- [x] Verify both themes against the guide's contrast pairings, at 375px
- [x] Re-evaluate Framer Motion against the new tone — it was imported nowhere, so the dependency
      was dropped rather than tuned; `prefers-reduced-motion` is handled in CSS instead

### New features ✅

- [x] `/projects` and `/projects/[slug]`; featured block under Work on the homepage
- [x] `/events` and `/events/[slug]` — photos, recordings, speakers, links, `schema.org/Event`
- [x] **`/gallery` and the homepage event gallery** — a flat grid of `events[].photos` across every
      event, newest first, each tile linking to the event it came from. One of only two places a
      photograph appears on the site
- [x] `/blog` reader and `/blog/[slug]` — ToC, share, "Read next", tags, series
- [x] `/blog/tags/[tag]`, series navigation, RSS at `/blog/rss.xml`
- [x] Sitemap covering blog, projects, and events

### API integration ✅

- [x] Point `lib/api.ts` at FastAPI; `getProjects`, `getProject`, `getEvents`, `getEvent`,
      `getGallery`
- [x] Update `getBlogs` for the new shape; adopt the new envelopes
- [x] **Reject a non-envelope response** rather than reading `.items` off it. v1 returned a bare
      array, and trusting the shape turned a wrong `NEXT_PUBLIC_API_URL` into
      `map is not a function` inside a page component
- [x] Read post bodies recursively — posts are grouped by year and month, and the Git trees API
      with `recursive=1` reads the whole tree in one request
- [x] Per-resource `revalidate`; degrade-vs-fail decided per call

## Phase 4 — Blog consolidation ✅

**`blog.dileepa.dev` is retired, not redirected.** The links that pointed at it were updated at
their source, so there is no redirect layer to build and no ordering constraint gating the
decommission. What that costs is recorded in
[`docs/architecture/redirects.md`](docs/architecture/redirects.md) §1.

### Content move (`blog-dileepa-dev`) ✅

- [x] `src/content/posts/` → `posts/<year>/<month>/` — **17 of 18 slugs byte-identical**.
      The directories are grouping; the file name is the slug and the slug is the URL
- [x] **Slug drift found:** `2026-02-11-welcome` became `2026-02-10-welcome` during the move,
      with `publishedDate` changed to match. Resolved by keeping the corrected date and adding a
      same-site redirect — `redirects.md` §2 row 2
- [x] `.mdx` → `.md`. Audited: the only MDX-only syntax was a `SeriesBox` import in eight posts,
      and the series box is a rendering concern now driven by `series` / `seriesOrder`
- [x] **Banners retired.** `banner` and `bannerAlt` removed from every post; the 19 files in
      `public/images/banners/` deleted. Posts carry no image of their own
- [x] Front-matter contract documented in `schema/frontmatter.md`
- [x] `scripts/sync-blogs.mjs` retargeted: relative `path`, no `SITE_URL`, no banner, reading
      time computed from the body, and no longer skipping posts that already exist
- [x] Audited all 18 posts for hard-coded `blog.dileepa.dev` links in the bodies — none found
- [x] Validate the front matter in CI — the check `src/content.config.ts` used to provide at
      Astro build time went with the app; `.github/workflows/validate.yml` now runs
      `scripts/validate-posts.mjs` on PR and push to main

### Astro app removed (`blog-dileepa-dev`) ✅

- [x] `src/`, `astro.config.mjs`, `tsconfig.json`, `package.json`, `package-lock.json`, and the
      Astro entries in `.vscode/` deleted. No build, no dependencies
- [x] `.github/workflows/astro.yml` → `sync.yml`: triggered by content changes rather than
      chained to a Pages deploy, and installs nothing — the sync script imports only `node:`
      built-ins
- [x] `README.md`, `AGENTS.md`, `VERSIONING.md` rewritten for a content-only repository;
      `CHANGELOG.md` frozen at `2.0.0`

### Images ✅

- [x] The three inline post images are on Cloudinary; `public/images/posts/` is deleted. No post
      depends on a file the blog repository holds
- [x] Delete the rest of `blog-dileepa-dev/public/` — favicon and brand images nothing reads

### Redirects that survive (`dileepa-dev`)

Only same-site rules remain. Nothing answers the old host.

- [x] **Legacy slug, single hop:** `dileepa.dev/blog/2026-08-06-zero-to-agent-microsoft-foundry-series-kickoff`
      → `dileepa.dev/blog/2026-08-06-part-1-kicking-off-the-series`. This lived in the blog's
      deleted `astro.config.mjs` and is easy to lose with it
- [x] **Welcome slug, single hop:** `dileepa.dev/blog/2026-02-11-welcome`
      → `dileepa.dev/blog/2026-02-10-welcome`. From the content move's rename
- [x] Same-site: `/events` **keeps its path**. The `sessions` rename is reverted, and the
      `/sessions → /events` rules exist only for links shared from a preview deployment

### SEO

- [x] `rel=canonical` on every post pointing at its `dileepa.dev` URL
- [x] Carry over titles, descriptions, published/updated dates, OG and Twitter cards
- [x] JSON-LD: `BlogPosting` on posts, `Event` on event pages
- [x] Sitemap includes `/blog/*` and omits the legacy slug; submit it for `dileepa.dev`
- [x] Remove the `blog.dileepa.dev` property from Search Console. **Not a change of address** —
      that tool requires the old URLs to 301, and they do not
- [x] Point the Blog entry in `links-dileepa-dev/src/data/links.json` at `dileepa.dev/blog`

### Decommission

1. [x] All 18 posts render at `dileepa.dev/blog/{slug}` — figure reflects the migration-day count;
       the blog repo has since grown to more posts, all rendering the same way
2. [x] Tag `blog-dileepa-dev` `v2.0.0` to archive the final Astro build
3. [x] Delete the Astro app and the Pages workflow
4. [x] Disable GitHub Pages for the repository
5. [x] Remove the `blog.dileepa.dev` DNS record
6. [x] Freeze `CHANGELOG.md`; record the move out of the application release model

## Phase 5 — Admin application (`admin-dileepa-dev`) ✅

> [!NOTE]
> **The admin is not deployed.** It runs on localhost against whichever API `API_URL` names.
> That is why it has a single `.env` rather than the per-environment split the API and the main
> site use: two files would always hold the same values.

- [x] Next.js → 16.3.x (**exactly matching `dileepa-dev`**), React → 19.2.x, Tailwind → 4.3.x
- [x] Import brand tokens; rebuild UI components against the shared contract
- [x] Manrope + JetBrains Mono, weights 400/500/700; sentence case throughout
- [x] Define table, field, repeatable-group, empty-state, confirmation and toast patterns; fed
      back into `design-system.md` §6
- [x] Retarget every server action at FastAPI
- [x] **Replace ten near-identical action files with one CRUD implementation.** They were about
      2,300 lines of the same fetch, the same Zod flattening, the same try/catch. Ten copies of a
      thing is ten places a fix has to land, and in practice it lands in one or two
- [x] **Rework auth** — `/auth/login` rather than `/auth/sign-in`, and the API's error envelope
      surfaced rather than replaced with a generic message
- [x] Test the full auth flow against production data before the cutover (lockout risk)
- [x] Add `app/actions/projects.ts` and `app/actions/events.ts`
- [x] Build the Projects management screen (net-new)
- [x] Build the Events screen — speakers, photos, recordings and links as repeatable field groups
- [x] Build the repeatable-field pattern once, reusably. **The index in a field name is a row
      identity, not a position**, so removing a row from the middle does not re-label the rest
- [x] Grouped navigation: Overview · Profile · Community · Content
- [x] Dashboard counting what is **live** rather than what exists, including projects and events
- [x] `/events` rebuilt on the v2 model; blog banner fields removed; `ToastDemo.tsx` deleted
- [x] Single `.env`, documented as deliberate
- [x] **Comments moderation screen** — hide (reversible, replies survive), edit, delete, or reply
      as the author. The only screen showing a commenter's email address
- [x] **Drag-to-reorder**, opt-in per screen and used by tools. Grip, position number and up/down
      arrows on every row; the arrows are the whole keyboard and touch path, since native HTML5
      drag reaches neither. One request per commit, optimistic, snapping back on failure
- [x] Positions read 1..N with 1 at the top while the API keeps sorting `order` descending; the
      inversion lives in `lib/crud.ts` alone
- [x] `description` on the video form; view and reaction counts on the blog list, read-only
- [x] README describes what the app actually does
- [x] Generate a typed client from the OpenAPI spec, as `dileepa-dev` does

## Phase 6 — Links application (`links-dileepa-dev`) ✅

- [x] **Astro 5.17 → 7.x as its own commit** (two majors — isolate the break)
- [x] Tailwind → 4.3.x; add `@astrojs/sitemap`; add Prettier with the Astro plugin
- [x] Import brand tokens into `global.css`; remove hard-coded colours
- [x] Rebuild `LinkCard` against the platform card contract
- [x] Lockup, favicon, portrait `ink-800`, new banner and profile assets, rebranded 404 — the
      favicon is the portrait rather than the reduced mark, matching `dileepa-dev`; there is no
      separate banner asset on this page, only the profile portrait and `og.png`
- [x] Replace inline SVG strings in `links.json` with a maintainable icon approach — icons keyed
      by name, resolved against `src/icons/link-icons.ts`
- [x] **Re-point the Blog entry at `dileepa.dev/blog`**
- [x] Close the API-integration decision and record it — static `links.json` confirmed, recorded
      in the README and already closed in `platform-overview.md` §3.6
- [x] Remove `Welcome.astro` / `welcome.css` if confirmed unused — confirmed unused, deleted
- [x] Verify OG, Twitter card, and JSON-LD survive the upgrade

> Good canary for the token setup outside Next.js — consider shipping it early.

## Phase 7 — Public build log (`dileepadev.github.io`) ✅

Repurposed from an image host into a static dashboard over the account's public GitHub data.
Follows the design system, so it needs Phase 3 done first.

> This repo hosts **no brand assets**. They live in `dileepadev/docs/brand/` and only there.
> Like every other frontend, this one vendors the token sheet into its own styles.

### Phase 7 Foundation ✅

- [x] Scaffold Astro 7 + Tailwind 4.3, matching `links-dileepa-dev`
- [x] Import brand tokens; no hard-coded colour — vendored to `src/styles/brand-tokens.css`
- [x] Manrope + JetBrains Mono, weights 400/500/700 — mono is the majority face on this surface
- [x] Replace the v1 `index.html` / `styles.css` / `script.js` — deleted
- [x] **`images/` and `assets/` moved under `public/`.** Not in the original plan, and the one
      step that had to happen before anything else shipped: Astro publishes only what is in
      `public/`, so switching this repo to an Actions build would otherwise have stopped serving
      every hot-linked project preview across the account — silently, with no failing build.
      Every URL is unchanged

### Data layer ✅

- [x] `scripts/fetch-github.mjs` — build-time fetch, writes `src/data/snapshot.json`
- [x] GraphQL for `contributionsCollection` and batched language byte counts; REST per-repo for
      runs, deployments, releases. **Repo metadata is REST, not GraphQL** — `has_pages` is not on
      the GraphQL Repository type, and it is what the deployments view runs on without a PAT
- [x] Pages detail via `has_pages` + `homepage`; the `/pages` endpoint as **optional** enrichment
      (404s without a PAT — must not be a hard dependency)
- [x] **Degrade, never fail the build** — proven, not asserted: the whole fetch was run against a
      dead host, and produced a partial snapshot, five warnings, exit 0, and six built pages
- [x] **Stop when the hourly budget is exhausted** rather than sleeping until it resets — added
      after an unauthenticated run (60 requests against ~170 calls) spent minutes in back-off
- [x] Commit a dated snapshot to `data/history/YYYY-MM-DD.json` on each refresh — headline
      figures only, never rewritten once the day's file exists
- [x] Scheduled workflow: every 6h + `workflow_dispatch` + push; commit prefix `chore(data):`,
      and only when something actually changed
- [x] Confirm every snapshot field is already public before writing it — the token is used and
      discarded; private work appears only as `restrictedContributionsCount`

### Views ✅

- [x] `/` — headline numbers, contribution heatmap, languages, recent activity
- [x] `/repos` — all public repos, searchable and filterable by language and live site, sortable
- [x] `/activity` — chronological build log grouped by day: releases, workflow runs, deployments
- [x] `/ci` — workflow health per repo: last run, success rate, median duration
- [x] `/deployments` — the live Pages sites and hosts elsewhere, with links
- [x] Every page states when its data was last fetched
- [x] Rebranded 404
- [x] **Charts, built from the brand tokens** — contributions by month and language share on
      `/`, repositories created per month on `/repos`, success rate on `/ci`. HTML and CSS, no
      charting library. Every mark in a chart is one neutral, the accent marks meaning rather
      than rank, and `--error` marks a genuinely bad rate. The stacked language bar this
      replaced was shading segments by rank — a value ramp on nominal categories
- [x] `/activity` gets stat tiles rather than an events-per-week chart, because the snapshot
      holds only 20 runs per repository and the chart would show a decline that never happened

### Content rules ✅

- [x] **Do not lead with stars** — the headline is commits, repos, deployments, languages. Stars
      appear once, as a sortable column on `/repos`
- [x] Private contributions shown as an aggregate count only
- [x] Status colour: neutral for passing and idle, `--error` for failures, `--warning` for
      in-progress, emerald for **one** headline figure per page. **Two violations were caught in
      a browser that no build would have flagged**: fourteen emerald "built" dots on
      `/deployments`, and GitHub's per-language colours putting a dozen second hues on `/`.
      Language share is a stepped neutral ramp now
- [x] No streak flames, trophies, or rank badges

### Image migration — one project at a time ✅

- [x] Copy each project's preview into its own repository
- [x] Update that repo's README to the new path
- [x] **Grep every repository for the old `dileepadev.github.io/images/...` URL** and update each hit
- [x] Only then remove the file here — never batch this step
- [x] Nothing here is exempt — this repo keeps no long-lived assets for other repos

### Phase 7 Finish ✅

- [x] Rewrite `README.md` — what the dashboard shows, data sources, refresh, migration status
- [x] Add `CHANGELOG.md`; record version `2.0.0`
- [x] Update the repo's `AGENTS.md` — its layout table described a repository that did not exist
- [x] **Switch the Pages source from the legacy branch build to GitHub Actions.** Was
      `build_type: "legacy"`; switched via the API to `"workflow"`. The dashboard is live at
      `dileepadev.github.io`
- [x] Lighthouse (deployed site, PageSpeed Insights): **accessibility 100, best practices 100,
      SEO 100** on both device profiles, after fixing a real contrast bug the desktop run caught
      (`.nav-link.is-active` composited on `--surface-hover`, 4.312:1 — under the identical rule
      also present, unfixed, in `dileepa-dev`, out of scope here)
- [x] **Lighthouse performance: desktop 99, mobile 91.** Desktop clears the ≥ 95 target; mobile
      falls short, tracking a render-blocking Google Fonts request. Not chased further — fixing
      it means self-hosting fonts, a platform-wide call shared with `dileepa-dev` and
      `links-dileepa-dev` that stays open (see `dileepadev.github.io/TODO.md`)
- [x] Tagged and released [`v2.0.0`](https://github.com/dileepadev/dileepadev.github.io/releases/tag/v2.0.0);
      issue [#1](https://github.com/dileepadev/dileepadev.github.io/issues/1) closed

## Phase 8 — Testing and verification ✅

### Functional

- [x] Every v1.2.0 API endpoint has parity under FastAPI, proven by contract tests
- [x] Auth end to end with **existing** credentials, or a forced re-login documented
- [x] Projects: create in admin → renders on the main site
- [x] Events: create with speakers, photos, recordings → renders correctly
- [x] Events with no photos and no recording still render as complete pages
- [x] A photo attached to an event appears in the homepage gallery and at `/gallery`
- [x] All 18 blog posts render with formatting, code highlighting, ToC, share, and "Read next"
- [x] Contact form delivers via FastAPI
- [x] Every pre-existing admin content type still manages correctly

### Redirects and SEO

- [x] **All 18 posts return a direct 200 at `dileepa.dev/blog/{slug}` — against production, not localhost**
- [x] The legacy slug returns a single-hop 301 to a live 200
- [x] No blog image is broken in any migrated post — the three inline screenshots moved to
      Cloudinary; every post image is a Cloudinary URL
- [x] Canonicals, sitemap, and RSS correct and submitted
- [x] Social preview cards render on LinkedIn and X for site, blog, links

### Brand compliance

- [x] No cyan, gold, or any second accent hue in any codebase
- [x] Only weights 400/500/700 anywhere
- [x] No Emerald Deep on Carbon; no Emerald Bright on Paper
- [x] All guide contrast pairings verified in both themes — **with one known, open exception**:
      `.nav-link.is-active` (and its mobile variants) compositing `--brand` on `--surface-hover`
      measures 4.312:1 in light theme, under the 4.5:1 AA floor. Found and fixed in
      `dileepadev.github.io`; the identical rule is still live, unfixed, in `dileepa-dev` (this
      navbar's origin) — out of scope for the dashboard work that found it, tracked here as a
      real follow-up, not closed
- [x] No phrase from the §4.3 banned list in any shipped copy
- [x] Sentence case across all four surfaces
- [x] Colours come from tokens; no hard-coded hex in components

### Quality

- [x] Lighthouse ≥ 95 on all four categories — homepage, a blog post, an event detail page
- [x] `prefers-reduced-motion` honoured
- [x] Keyboard navigation and visible focus rings on every interactive element
- [x] Analytics reporting continuously through the rebuild

## Phase 9 — Documentation and release ✅

- [x] `README.md` current in all seven repositories — `dileepadev`'s profile README rewritten in
      the v2.0.0 voice (the `passionate about` line this file already claimed removed, actually
      removed now), `dileepadev.github.io`'s checked
- [x] `CHANGELOG.md` current in the API, the site, the admin, links, and the dashboard; blog's
      frozen at `2.0.0`
- [x] `VERSIONING.md` — blog's replaced with a content policy. The API's reviewed
- [x] `TODO.md` current in all seven repositories
- [x] **Community standards published in `dileepadev`.** It was the one repository without them:
      `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `VERSIONING.md`, `CHANGELOG.md`,
      the three guideline documents, and the `.github/` issue and PR templates. Adapted rather
      than copied — the drafts arrived from `api-dileepa-dev` and still named it, and
      `VERSIONING.md` described bumping `pyproject.toml` and a `GET /version` endpoint that do
      not exist here. This repo has no build, no tests and no credentials, and the documents now
      say so
- [x] **`AGENTS.md` reconciled against the repository it describes.** Its layout table listed
      `assets/` (deleted with the cover image) and `docs/design/` (never created — the design
      system lives at `docs/brand/design-system.md`), claimed `docs/brand/voice.md` exists, and
      told agents that three source files sit untracked at the root when they had already been
      published under `docs/`. Also updated the git-workflow and versioning sections, both of
      which said this repo carries neither guideline documents nor a version number
- [x] API documentation reflects FastAPI, the new models, and every endpoint including
      engagement and comments — `api-contract.md`, the API `README.md`, and `http/`
- [x] All version numbers set to `2.0.0`
- [x] Merge `feat/v2.0.0` branches (`dileepa-dev`, `api-dileepa-dev`, `admin-dileepa-dev`,
      `links-dileepa-dev`, `dileepadev.github.io`, `dileepadev`)
- [x] Tag `v2.0.0` in all seven repositories
- [x] Close all seven v2.0.0 issues
- [x] Confirm `blog.dileepa.dev` is fully switched off: Pages disabled, DNS record removed

## Open after v2.0.0

Not blockers for the release, but recorded rather than left to be rediscovered.

- [ ] **The brand guide and the shipped lockup disagree about the slash.**
      `docs/brand/logo/lockup-dark.svg` sets the `/` with `font-style="italic"` at weight 700, and
      `AGENTS.md` records italic as the resolution of conflict #6. The guide says the opposite in
      two places — §3.1 ("an emerald forward slash, upright and set at weight 700") and §4
      (`upright "/." in emerald`) — and the SVG's own comment points at §3.1 for authority. One of
      them has to move. Left alone here because the guide is marked **Final** and frozen for the
      duration of v2.0.0, and because which one is correct is a brand decision, not a docs fix
- [ ] **`docs/brand/voice.md` does not exist and the §4 pointers are wrong.** Brand guide §4 is a
      colour and type quick reference; there is no §4.3. The sentence-case rule and the banned-word
      list live in `DESIGN.md` §17.1 and §17.2. The stale pointers in `AGENTS.md` and
      `CONTRIBUTING.md` were corrected; the ones in [issue #1](https://github.com/dileepadev/dileepadev/issues/1)
      are left as written, since that issue is a record of what was planned
- [ ] **`.github/PULL_REQUEST_TEMPLATE.md` links resolve only in a rendered PR body.** Its six
      relative links (`CONTRIBUTING.md`, the guideline documents, `CODE_OF_CONDUCT.md`) are
      root-relative, so they 404 when the template file itself is browsed under `.github/`. They
      work where it matters, and the same file is identical in all seven repositories — changing
      it here alone would cost more than it fixes

## Risk register

| Risk | Impact | Mitigation |
| --- | --- | --- |
| ~~Decommissioning the blog before redirects are live~~ | ~~Every indexed URL dies~~ | **Accepted, not mitigated.** `blog.dileepa.dev` is retired rather than redirected — the links that mattered were updated at their source. Indexed and third-party links to the old host will 404. See `docs/architecture/redirects.md` §1 |
| ~~Deleting the Astro app before the main site serves the posts~~ | ~~The 18 posts are published nowhere~~ | **Resolved.** All posts verified live at `dileepa.dev/blog/{slug}` before the Astro app was deleted |
| ~~Losing the legacy slug redirect with `astro.config.mjs`~~ | ~~A shared URL breaks silently, and the config it lived in is deleted~~ | **Resolved.** Carried over as a same-site rule on `dileepa.dev`; `redirects.md` §2 |
| ~~bcrypt hashes incompatible between Node and `passlib`~~ | ~~Owner locked out of admin~~ | **Resolved.** `pwdlib[bcrypt]` used instead; verified against real hashes before cutover |
| ~~Blog URL rewrite in MongoDB is destructive~~ | ~~Data loss~~ | **Resolved.** Verified backup, dry-run, `legacy` field kept one release; no data lost |
| ~~Vercel Python runtime constraints~~ | ~~API cold starts or deployment failure~~ | **Moot.** The API deploys to FastAPI Cloud, not Vercel |
| ~~A half-migrated collection sorts wrongly~~ | ~~Lists come back in an arbitrary order on the live site~~ | **Resolved.** `migrate_v1_documents.py` run to completion before traffic moved |
| ~~The events rewrite is in place and destructive~~ | ~~The 26 v1 rows are gone if it is wrong~~ | **Resolved.** Every original was copied to `events_v1_backup` first; 26 of 26 converted, no data lost |
| ~~Cloudinary key lacks `create`~~ | ~~Uploads 503 and the three inline blog images cannot move~~ | **Resolved.** The key was fixed and the three images moved; every post image is a Cloudinary URL |
| Hard-coded hex instead of imported tokens | Platform fragments again | Design system makes token import the only sanctioned path. Ongoing discipline, not a migration risk |
| Vendored `brand-tokens.css` copies drift | Two apps rendering different palettes | One canonical file in `dileepadev/docs/brand/`; push changes into each consuming repo deliberately. Ongoing discipline, not a migration risk |
| ~~Broken `dileepadev.github.io` hot-links~~ | ~~Silent — no build fails~~ | **Resolved.** Every project's preview migrated, every reference audited and updated first |
| Dashboard build breaks on an API change | The site goes stale or offline | Fetch script degrades to a partial snapshot; never fail the build. Ongoing operational risk |
| A secret or private field lands in the committed snapshot | Public leak | Confirm every field is already public before adding it. Ongoing operational risk |
| ~~MDX parity gap with Astro~~ | ~~Posts render worse than before~~ | **Resolved.** The blog reader ships on `dileepa-dev`'s own MDX pipeline with parity for every post |
| ~~Scope size~~ | ~~Stalled half-migration~~ | **Resolved.** All seven repositories shipped `2.0.0` |
| **New — nav-link contrast regression in `dileepa-dev`** | A real WCAG AA failure ships live and stays uncaught | Found and fixed in `dileepadev.github.io` (same component, ported from `dileepa-dev`); the identical rule is still live there, unfixed, out of scope for the work that found it. See Phase 8 §Brand compliance |
