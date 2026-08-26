# TODO — v2.0.0 platform migration

Cross-repository roadmap for the v2.0.0 rebrand and platform consolidation.

> [!NOTE]
> This is the platform-level roadmap. Each repository carries its own slice in its own `TODO.md`, and the full scope for each lives in its v2.0.0 issue. This file is the source of truth for **sequencing across repositories**.

## Repositories and issues

| Repository | Role after v2.0.0 | Current | Issue |
| --- | --- | --- | --- |
| `dileepadev` | Brand + platform documentation root | — | [#1](https://github.com/dileepadev/dileepadev/issues/1) |
| `dileepa-dev` | Main website — absorbs blog, projects, events | 1.3.0 | [#15](https://github.com/dileepadev/dileepa-dev/issues/15) |
| `api-dileepa-dev` | FastAPI backend (migrated from NestJS) | 1.2.0 | [#13](https://github.com/dileepadev/api-dileepa-dev/issues/13) |
| `blog-dileepa-dev` | Content-source repository only | 1.1.0 | [#3](https://github.com/dileepadev/blog-dileepa-dev/issues/3) |
| `admin-dileepa-dev` | Admin app — new design system + FastAPI | 1.0.0 | [#4](https://github.com/dileepadev/admin-dileepa-dev/issues/4) |
| `links-dileepa-dev` | Links page — new design system | 1.0.0 | [#2](https://github.com/dileepadev/links-dileepa-dev/issues/2) |
| `dileepadev.github.io` | Public build log — GitHub activity dashboard | — | [#1](https://github.com/dileepadev/dileepadev.github.io/issues/1) |

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
- [x] `docs/brand/voice.md` — voice rules and banned-phrase list
- [x] `docs/design/design-system.md` — component contract for all three frontends
- [x] `docs/design/reference/` — HTML reference with tokens reconciled
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

## Phase 2 — API migration (`api-dileepa-dev`) — code complete, not deployed

**Blocks both frontends. Keep NestJS live until cutover is verified.**

The application is built, tested and typed. What remains needs the live cluster, a FastAPI Cloud
account, or production traffic — none of which can be done from a checkout.

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
- [ ] Stand FastAPI up alongside NestJS on a preview deployment

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
- [ ] **Run `scripts/verify_password_hash.py` against the production database** before cutover

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

- [ ] **Take a verified, restore-tested MongoDB backup**
- [x] Script rewriting the 18 blog rows off `blog.dileepa.dev`, with a rollback script. It now
      clears `banner` rather than carrying it to a new host
- [x] Dry-run and applied against `development`; the legacy-slug stub row is unpublished so it
      does not appear in the index or the sitemap
- [ ] Dry-run and apply against `production`, after the backup
- [x] Old values kept in a `legacy` field for one release
- [x] **`scripts/migrate_events_v1_to_v2.py`** — rewrites the 26 v1 `events` rows into the v2
      shape **in place**, keeping `_id`, after copying every original to `events_v1_backup`.
      Idempotent: a row already in the v2 shape is recognised and left alone
- [x] Dry-run and applied against `development` — 26 of 26 converted, no unparseable dates
- [ ] Run it against `production`, after the backup
- [x] **`scripts/migrate_v1_documents.py`** — not in the original plan. Every ported collection
      lacks `published`, `order`, `meta` and timestamps, and stores ordering as `index`. The API
      reads around all of it, but sorting happens in MongoDB, before the model's aliasing
- [x] Run against `development`
- [ ] **Run it against `production` to completion before traffic moves**

### Finish

- [x] OpenAPI metadata; docs disabled in production — in production neither the reference
      page nor the spec it reads is registered
- [x] Publish the OpenAPI spec for typed client generation — CI uploads it on every build
- [ ] Theme Scalar against the brand tokens
- [ ] Attach `api.dileepa.dev` **after** the first successful FastAPI Cloud deployment — a domain
      cannot be reserved ahead of a running app
- [ ] Enable **Zero Downtime Migration** when adding the domain, so the certificate is issued while
      Vercel still serves traffic
- [ ] Decide the plan before production traffic moves — Hobby is 0.1 vCPU / 512 MB shared with
      1-day log retention, and one custom domain total (staging would need Pro)
- [ ] Cut both consumers over; observe; **then** delete `src/`, `package.json`, and the Node toolchain
- [ ] Update `README.md`, `CHANGELOG.md`, `VERSIONING.md`; version → `2.0.0`

## Phase 3 — Main website (`dileepa-dev`)

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
- [ ] Verify both themes against the guide's contrast pairings, at 375px
- [ ] Re-evaluate Framer Motion against the new tone

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

## Phase 4 — Blog consolidation

**`blog.dileepa.dev` is retired, not redirected.** The links that pointed at it were updated at
their source, so there is no redirect layer to build and no ordering constraint gating the
decommission. What that costs is recorded in
[`docs/architecture/redirects.md`](docs/architecture/redirects.md) §1.

### Content move (`blog-dileepa-dev`) ✅

- [x] `src/content/posts/` → `content/posts/<year>/<month>/` — **17 of 18 slugs byte-identical**.
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
- [ ] Validate the front matter in CI — the check `src/content.config.ts` used to provide at
      Astro build time went with the app

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
- [ ] Delete the rest of `blog-dileepa-dev/public/` — favicon and brand images nothing reads

### Redirects that survive (`dileepa-dev`)

Only same-site rules remain. Nothing answers the old host.

- [ ] **Legacy slug, single hop:** `dileepa.dev/blog/2026-08-06-zero-to-agent-microsoft-foundry-series-kickoff`
      → `dileepa.dev/blog/2026-08-06-part-1-kicking-off-the-series`. This lived in the blog's
      deleted `astro.config.mjs` and is easy to lose with it
- [ ] **Welcome slug, single hop:** `dileepa.dev/blog/2026-02-11-welcome`
      → `dileepa.dev/blog/2026-02-10-welcome`. From the content move's rename
- [x] Same-site: `/events` **keeps its path**. The `sessions` rename is reverted, and the
      `/sessions → /events` rules exist only for links shared from a preview deployment

### SEO

- [ ] `rel=canonical` on every post pointing at its `dileepa.dev` URL
- [ ] Carry over titles, descriptions, published/updated dates, OG and Twitter cards
- [x] JSON-LD: `BlogPosting` on posts, `Event` on event pages
- [ ] Sitemap includes `/blog/*` and omits the legacy slug; submit it for `dileepa.dev`
- [ ] Remove the `blog.dileepa.dev` property from Search Console. **Not a change of address** —
      that tool requires the old URLs to 301, and they do not
- [ ] Point the Blog entry in `links-dileepa-dev/src/data/links.json` at `dileepa.dev/blog`

### Decommission

1. [ ] All 18 posts render at `dileepa.dev/blog/{slug}` — **this one still gates the rest**
2. [ ] Tag `blog-dileepa-dev` `v2.0.0` to archive the final Astro build
3. [x] Delete the Astro app and the Pages workflow
4. [ ] Disable GitHub Pages for the repository
5. [ ] Remove the `blog.dileepa.dev` DNS record
6. [x] Freeze `CHANGELOG.md`; record the move out of the application release model

## Phase 5 — Admin application (`admin-dileepa-dev`)

> [!NOTE]
> **The admin is not deployed.** It runs on localhost against whichever API `API_URL` names.
> That is why it has a single `.env` rather than the per-environment split the API and the main
> site use: two files would always hold the same values.

- [ ] Next.js → 16.3.x (**exactly matching `dileepa-dev`**), React → 19.2.x, Tailwind → 4.3.x
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
- [ ] Test the full auth flow against production data before the cutover (lockout risk)
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
- [ ] Re-record the demo video; it shows the v1.0 UI
- [ ] Generate a typed client from the OpenAPI spec, as `dileepa-dev` does

## Phase 6 — Links application (`links-dileepa-dev`)

- [ ] **Astro 5.17 → 7.x as its own commit** (two majors — isolate the break)
- [ ] Tailwind → 4.3.x; add `@astrojs/sitemap`; add Prettier with the Astro plugin
- [ ] Import brand tokens into `global.css`; remove hard-coded colours
- [ ] Rebuild `LinkCard` against the platform card contract
- [ ] Lockup, favicon, portrait `ink-800`, new banner and profile assets, rebranded 404
- [ ] Replace inline SVG strings in `links.json` with a maintainable icon approach
- [ ] **Re-point the Blog entry at `dileepa.dev/blog`**
- [ ] Close the API-integration decision and record it
- [ ] Remove `Welcome.astro` / `welcome.css` if confirmed unused
- [ ] Verify OG, Twitter card, and JSON-LD survive the upgrade

> Good canary for the token setup outside Next.js — consider shipping it early.

## Phase 7 — Public build log (`dileepadev.github.io`)

Repurposed from an image host into a static dashboard over the account's public GitHub data.
Follows the design system, so it needs Phase 3 done first.

> This repo hosts **no brand assets**. They live in `dileepadev/docs/brand/` and only there.
> Like every other frontend, this one vendors the token sheet into its own styles.

### Phase 7 Foundation

- [ ] Scaffold Astro 7 + Tailwind 4.3, matching `links-dileepa-dev`
- [ ] Import brand tokens; no hard-coded colour
- [ ] Manrope + JetBrains Mono, weights 400/500/700 — mono is the majority face on this surface
- [ ] Replace the v1 `index.html` / `styles.css` / `script.js`

### Data layer

- [ ] `scripts/fetch-github.mjs` — build-time fetch, writes `src/data/snapshot.json`
- [ ] GraphQL for repo metadata and `contributionsCollection`; REST per-repo for runs,
      deployments, releases
- [ ] Pages detail via `has_pages` + `homepage`; the `/pages` endpoint as **optional** enrichment
      (404s without a PAT — must not be a hard dependency)
- [ ] **Degrade, never fail the build** — a rate limit or 404 yields a partial snapshot plus a
      logged warning
- [ ] Commit a dated snapshot to `data/history/YYYY-MM-DD.json` on each refresh — the API has no
      memory, so trends only exist if they are recorded
- [ ] Scheduled workflow: every 6h + `workflow_dispatch` + push; commit prefix `chore(data):`
- [ ] Confirm every snapshot field is already public before writing it

### Views

- [ ] `/` — headline numbers, contribution heatmap, recent activity
- [ ] `/repos` — all public repos, sortable and filterable by language, activity, Pages
- [ ] `/activity` — chronological build log: releases, workflow runs, deployments
- [ ] `/ci` — workflow health per repo: last run, success rate, duration
- [ ] `/deployments` — the live Pages sites, with links
- [ ] Every page states when its data was last fetched

### Content rules

- [ ] **Do not lead with stars** — lead with commits, repos, deployments, languages
- [ ] Private contributions shown as an aggregate count only
- [ ] Status colour: neutral for passing and idle, `--error` for failures, `--warning` for
      in-progress, emerald for **one** headline figure per page
- [ ] No streak flames, trophies, or rank badges

### Image migration — one project at a time

- [ ] Copy each project's preview into its own repository
- [ ] Update that repo's README to the new path
- [ ] **Grep every repository for the old `dileepadev.github.io/images/...` URL** and update each hit
- [ ] Only then remove the file here — never batch this step
- [ ] Nothing here is exempt — this repo keeps no long-lived assets for other repos

### Phase 7 Finish

- [ ] Rewrite `README.md` — what the dashboard shows, data sources, refresh, migration status
- [ ] Add `CHANGELOG.md`; record version `2.0.0`

## Phase 8 — Testing and verification

### Functional

- [ ] Every v1.2.0 API endpoint has parity under FastAPI, proven by contract tests
- [ ] Auth end to end with **existing** credentials, or a forced re-login documented
- [ ] Projects: create in admin → renders on the main site
- [ ] Events: create with speakers, photos, recordings → renders correctly
- [ ] Events with no photos and no recording still render as complete pages
- [ ] A photo attached to an event appears in the homepage gallery and at `/gallery`
- [ ] All 18 blog posts render with formatting, code highlighting, ToC, share, and "Read next"
- [ ] Contact form delivers via FastAPI
- [ ] Every pre-existing admin content type still manages correctly

### Redirects and SEO

- [ ] **All 18 posts return a direct 200 at `dileepa.dev/blog/{slug}` — against production, not localhost**
- [ ] The legacy slug returns a single-hop 301 to a live 200
- [ ] No blog image is broken in any migrated post — **the three inline screenshots are known
      broken until they move to Cloudinary**
- [ ] Canonicals, sitemap, and RSS correct and submitted
- [ ] Social preview cards render on LinkedIn and X for site, blog, links

### Brand compliance

- [ ] No cyan, gold, or any second accent hue in any codebase
- [ ] Only weights 400/500/700 anywhere
- [ ] No Emerald Deep on Carbon; no Emerald Bright on Paper
- [ ] All guide contrast pairings verified in both themes
- [ ] No phrase from the §4.3 banned list in any shipped copy
- [ ] Sentence case across all four surfaces
- [ ] Colours come from tokens; no hard-coded hex in components

### Quality

- [ ] Lighthouse ≥ 95 on all four categories — homepage, a blog post, an event detail page
- [ ] `prefers-reduced-motion` honoured
- [ ] Keyboard navigation and visible focus rings on every interactive element
- [ ] Analytics reporting continuously through the rebuild

## Phase 9 — Documentation and release

- [x] `README.md` current in `dileepadev`, `dileepa-dev`, `api-dileepa-dev`, `admin-dileepa-dev`,
      `blog-dileepa-dev`. `links-dileepa-dev` and `dileepadev.github.io` still to check
- [x] `CHANGELOG.md` current in the API, the site and the admin; blog's frozen at `2.0.0`
- [x] `VERSIONING.md` — blog's replaced with a content policy. The API's still to review
- [x] `TODO.md` current in the five repositories touched so far
- [x] API documentation reflects FastAPI, the new models, and every endpoint including
      engagement and comments — `api-contract.md`, the API `README.md`, and `http/`
- [ ] All version numbers set to `2.0.0`
- [ ] Merge `feat/v2.0.0` branches (`dileepa-dev`, `api-dileepa-dev`, `admin-dileepa-dev`, `links-dileepa-dev`)
- [ ] Tag `v2.0.0` in all seven repositories
- [ ] Close all seven v2.0.0 issues
- [ ] Confirm `blog.dileepa.dev` is fully switched off: Pages disabled, DNS record removed

## Risk register

| Risk | Impact | Mitigation |
| --- | --- | --- |
| ~~Decommissioning the blog before redirects are live~~ | ~~Every indexed URL dies~~ | **Accepted, not mitigated.** `blog.dileepa.dev` is retired rather than redirected — the links that mattered were updated at their source. Indexed and third-party links to the old host will 404. See `docs/architecture/redirects.md` §1 |
| Deleting the Astro app before the main site serves the posts | The 18 posts are published nowhere | Phase 4 decommission step 1 still gates the rest: verify all 18 render at `dileepa.dev/blog/{slug}` first |
| Losing the legacy slug redirect with `astro.config.mjs` | A shared URL breaks silently, and the config it lived in is deleted | Carried over as a same-site rule on `dileepa.dev`; `redirects.md` §2 |
| bcrypt hashes incompatible between Node and `passlib` | Owner locked out of admin | Test with a real DB hash before cutover; staging rehearsal |
| Blog URL rewrite in MongoDB is destructive | Data loss | Verified backup, dry-run, `legacy` field kept one release |
| ~~Vercel Python runtime constraints~~ | ~~API cold starts or deployment failure~~ | **Moot.** The API deploys to FastAPI Cloud, not Vercel |
| A half-migrated collection sorts wrongly | Lists come back in an arbitrary order on the live site | Sorting happens in MongoDB, before the model reads `index` as `order`. Run `migrate_v1_documents.py` to completion before traffic moves |
| The events rewrite is in place and destructive | The 26 v1 rows are gone if it is wrong | Every original is copied to `events_v1_backup` first, keeping its `_id`. Restore is `db.events_v1_backup.aggregate([{ $out: "events" }])` |
| ~~Cloudinary key lacks `create`~~ | ~~Uploads 503 and the three inline blog images cannot move~~ | **Resolved.** The key was fixed and the three images moved; every post image is a Cloudinary URL |
| Hard-coded hex instead of imported tokens | Platform fragments again | Design system makes token import the only sanctioned path |
| Vendored `brand-tokens.css` copies drift | Two apps rendering different palettes | One canonical file in `dileepadev/docs/brand/`; push changes into each consuming repo deliberately |
| Broken `dileepadev.github.io` hot-links | Silent — no build fails | Audit references before deleting; migrate one project at a time |
| Dashboard build breaks on an API change | The site goes stale or offline | Fetch script degrades to a partial snapshot; never fail the build |
| A secret or private field lands in the committed snapshot | Public leak | Confirm every field is already public before adding it |
| MDX parity gap with Astro | Posts render worse than before | Port `Pre`, `SeriesBox`, `TocFab`, `Share` equivalents deliberately |
| Scope size | Stalled half-migration | Ship per-phase behind `dev` previews; keep NestJS live until cutover |
