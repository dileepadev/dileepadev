# Platform overview — v2.0.0

The target architecture for the `dileepa.dev` platform. Seven repositories, one brand, one API,
one baseline version.

## 1. What changes

v2.0.0 is the transition from six independently versioned projects to one platform.

| | v1.x | **v2.0.0** |
| --- | --- | --- |
| Websites | 3 (main, blog, links) | 2 (main, links) |
| Blog | Standalone Astro site on GitHub Pages | A section of the main website |
| Backend | NestJS 11 on Vercel serverless | FastAPI on FastAPI Cloud |
| Content types | about, experiences, educations, communities, tools, events, videos, blogs | + **projects**; **events** reshaped in place |
| Brand | v1, per-app | v2.0.0, one token sheet |
| Versions | 1.0.0 – 1.3.0, drifting | **2.0.0** everywhere |

## 2. Surfaces

### 2.0 Naming key

Read this before the diagrams. Three of these names look almost identical and mean different
things:

| Looks like | Is | Not to be confused with |
| --- | --- | --- |
| `dileepadev` | The **platform root repo** — docs only, no site | — |
| `dileepa-dev` | The **main website repo** (hyphen) | `dileepadev`, the root repo |
| `dileepa.dev` | The **domain** that `dileepa-dev` serves (dot) | `dileepa-dev`, the repo |

The full mapping:

| Repository | Domain it serves |
| --- | --- |
| `dileepadev` | — (docs only) |
| `dileepa-dev` | `dileepa.dev` |
| `api-dileepa-dev` | `api.dileepa.dev` |
| `admin-dileepa-dev` | `admin.dileepa.dev` |
| `links-dileepa-dev` | `links.dileepa.dev` |
| `blog-dileepa-dev` | — (content only; `blog.dileepa.dev` retired in v2.0.0) |
| `dileepadev.github.io` | `dileepadev.github.io` — repo name and domain are the same string |

> **Convention for every diagram in this documentation:** nodes are **repository names**.
> Anything that is not a repository name is an external service (`MongoDB Atlas`, `Cloudinary`,
> `GitHub API`). Domains appear only in the tables above and below, never as diagram nodes.

Two different things connect these repositories, and it helps to keep them apart. **Standards**
flow one way at design time. **Data** flows a different way at build and run time.

### 2.1 What follows the standards

`dileepadev` ships no application. It holds the brand, the design system, and the architecture
docs, and [Project #1](https://github.com/users/dileepadev/projects/1) tracks the work across
every repository below.

```text
  dileepadev
  brand · design system · architecture docs
  Project #1 tracks work across every repository
        │
        │  standards every surface implements
        │
        ├──▶  dileepa-dev             → dileepa.dev            Next.js 16 · Vercel
        ├──▶  admin-dileepa-dev       → admin.dileepa.dev      Next.js 16 · Vercel
        ├──▶  links-dileepa-dev       → links.dileepa.dev      Astro 7 · GitHub Pages
        ├──▶  dileepadev.github.io    → dileepadev.github.io   Astro 7 · GitHub Pages
        └──▶  api-dileepa-dev         → api.dileepa.dev        FastAPI · FastAPI Cloud
```

Every arrow is design-time only. `dileepadev` deploys nothing and serves nothing — each
repository builds and deploys itself.

### 2.2 What talks to what

Repository names throughout. External services are the only non-repo nodes.

```text
  dileepa-dev ─────────────read───────────┐
                                          │
  admin-dileepa-dev ────read + write──────┤
                                          ▼
                                  api-dileepa-dev ──────┬─────▶  MongoDB Atlas
                                          ▲             │
                                          │             └─────▶  Cloudinary
                            image upload  │                      all platform images
                                          │
  blog-dileepa-dev ───────────────────────┘
        │
        └────build-time fetch of post bodies────▶  dileepa-dev
                                                   renders /blog

  dileepadev.github.io ────build-time────▶  GitHub API
                                            public account data

  links-dileepa-dev ────  static data, reads nothing
```

Three of these are build-time edges, not runtime ones. `dileepa-dev` fetches blog bodies from
Git at build; `dileepadev.github.io` fetches GitHub data at build; both bake the result into
static output. Only the two Next.js apps talk to the API while a visitor is on the page.

| Surface | Repo | Stack | Host |
| --- | --- | --- | --- |
| `dileepa.dev` | `dileepa-dev` | Next.js 16.3, React 19.2, Tailwind 4.3 | Vercel |
| `api.dileepa.dev` | `api-dileepa-dev` | FastAPI 0.141, Python 3.13, Pydantic 2.13 | FastAPI Cloud |
| `admin.dileepa.dev` | `admin-dileepa-dev` | Next.js 16.3, React 19.2, Tailwind 4.3 | Vercel |
| `links.dileepa.dev` | `links-dileepa-dev` | Astro 7, Tailwind 4.3 | GitHub Pages |
| — (content only) | `blog-dileepa-dev` | Markdown + images | none |
| `dileepadev.github.io` | `dileepadev.github.io` | Astro 7, Tailwind 4.3 | GitHub Pages |
| — (docs only) | `dileepadev` | Markdown | none |

`preview.dileepa.dev` tracks the `dev` branch of `dileepa-dev`.

## 3. Decisions

These were open at the start of Phase 1. They are now closed. Changing one is a platform-level
decision, not a repo-level one.

### 3.1 Blog content pipeline — build-time fetch from GitHub

The main site fetches MDX and front matter from `blog-dileepa-dev` at build time via the GitHub
contents/raw API, pinned to a commit or tag. The API keeps a **metadata index only** — enough
to list posts, search them, and manage them from admin. It does not store post bodies.

Git stays the source of truth for content. There is no submodule to bump, and a database outage
cannot take the blog offline once a build has shipped.

Rejected: a submodule (every content change costs two commits); storing rendered bodies in
MongoDB (content leaves Git, and the site gains a runtime dependency for its most static pages).

Detail: [`content-pipeline.md`](content-pipeline.md).

### 3.2 API host — FastAPI Cloud

The backend deploys with `fastapi deploy`, using a deploy token in CI:

```yaml
- run: uv run fastapi deploy
  env:
    FASTAPI_CLOUD_TOKEN: ${{ secrets.FASTAPI_CLOUD_TOKEN }}
    FASTAPI_CLOUD_APP_ID: ${{ secrets.FASTAPI_CLOUD_APP_ID }}
```

Configuration goes through `fastapi cloud env set`, with `--secret` for anything sensitive:

```bash
fastapi cloud env set ENVIRONMENT "production"
fastapi cloud env set --secret MONGODB_URI "..."
```

Secrets are write-only — they cannot be read back after creation, so keep the authoritative
copy in a password manager. **Environment changes require a redeploy to take effect.**

If the app entrypoint is not in a standard location, declare it in `pyproject.toml`:

```toml
[tool.fastapi]
entrypoint = "src.main:app"
```

This removes the serverless constraints that shaped the NestJS deployment — notably the
CDN-served Swagger workaround, which exists only because Vercel's bundle limits made the normal
static assets awkward. FastAPI Cloud serves the built-in docs directly.

#### Custom domains — confirmed available

Custom domains are available on every plan. **Hobby allows one in total**; Pro allows twenty.
One is enough: `api.dileepa.dev` is the only hard-coded API host in the platform.

It is a subdomain, so it attaches with a single `CNAME` at `api` pointing to
`<domain-id>.endpoints.fastapicloud.dev.`, where the domain ID is issued by the dashboard when
the domain is added. Apex domains need two `A` records instead; that case does not apply here.
TLS certificates are issued, installed, and renewed automatically through Google Trust Services.
If a CAA record exists on `dileepa.dev`, it must authorise `pki.goog; cansignhttpexchanges=yes`
or issuance fails.

Three constraints follow, and they shape the order of the cutover:

- **The app needs one successful deployment before a domain can be attached.** A domain is
  attached to a running app; it cannot be reserved ahead of one.
- **Enable Zero Downtime Migration when adding the domain.** `api.dileepa.dev` is live on
  Vercel. ZDM adds `TXT` and `CNAME` records at `_acme-challenge` so the certificate is issued
  while Vercel still serves traffic — the switch then becomes a DNS change with a valid
  certificate already in place, instead of a gap between repoint and issue.
- **One custom domain means one environment.** On Hobby it goes to production. Staging and
  preview stay on their `*.fastapicloud.dev` URLs, which is what they are for. A second custom
  domain — `api-staging.dileepa.dev` — requires Pro.

DNS propagation is documented as usually minutes, up to 48 hours. If DNS is ever moved to
Cloudflare, every verification record must be set to **DNS only** (grey cloud); proxied records
prevent validation and certificate issue.

The remaining question is not availability but capacity: Hobby runs at 0.1 vCPU / 512 MB shared
with 1-day log retention. That is a plan decision to make before production traffic moves, not a
blocker on the migration.

### 3.3 Image backend — Cloudinary

One image store for the whole platform: uploads from admin, event photos, project galleries,
and blog banners. Azure Blob Storage is retired.

Cloudinary is already a working dependency in the API, has transforms and a CDN built in, and
`res.cloudinary.com` is already in the main site's `next.config.ts` `remotePatterns`.

**Only the API holds Cloudinary credentials.** Every other surface uploads through
`POST /uploads` and receives a URL back. No other repo gets a Cloudinary key.

### 3.4 Blog images — Git plus Cloudinary, via the API

Images live in `blog-dileepa-dev/content/images/` — Git remains the source of truth. On push to
`main`, a workflow uploads new or changed images **through the API's upload endpoint**, which
puts them in Cloudinary and returns the URL.

The blog repo therefore needs no Cloudinary credentials — only the `BLOG_SYNC_API_KEY` it
already has.

Because the Cloudinary `public_id` is derived deterministically from the repo path, the main
site can construct an image URL without a database lookup. The stored record exists for admin
visibility and for redirecting the old `blog.dileepa.dev/images/**` URLs, not for resolution.

Detail: [`content-pipeline.md`](content-pipeline.md) §4.

### 3.5 `dileepadev.github.io` — public build log

The repository is repurposed from an image host into a **static dashboard over the account's
public GitHub data** — repositories, commits, workflow runs, releases, deployments, and
languages, fetched at build time and baked into static output. No runtime API calls.

It hosts nothing else. **Brand assets live in `dileepadev/docs/brand/` and only there** — there
is no mirror here and no CDN. Consuming repos vendor what they need; see §3.7.

Project preview images move out to the repositories they document. Because GitHub Pages cannot
redirect and every one of those paths is hot-linked from a README, they migrate **one project
at a time**, and a file is removed only after every reference to it has been updated.

Everything except `GET /repos/{o}/{r}/pages` reads unauthenticated; that endpoint requires admin
on the repo, so it is optional enrichment over the public `has_pages` and `homepage` fields
rather than a hard dependency.

Detail: `dileepadev.github.io/AGENTS.md`.

### 3.6 Links data — stays static

`links-dileepa-dev` keeps `src/data/links.json` as its source. No `/links` API resource.

The data changes roughly twice a year. An API resource would add an endpoint, an admin screen,
and a rebuild trigger, and would give a page that currently cannot fail a way to fail. The one
required change is re-pointing the Blog entry at `dileepa.dev/blog`.

Revisit only if link data starts changing monthly.

### 3.7 Brand assets — one home, vendored out

All brand assets live in `dileepadev/docs/brand/`: the guide, the canonical token sheet, the
logo lockups, voice. Nothing is mirrored, served, or CDN-hosted.

Consuming repositories **vendor** what they need — copy the token sheet into their styles, the
favicon into `public/` — and record where it came from.

Hot-linking is not an option: `raw.githubusercontent.com` serves CSS as `text/plain`, and
browsers refuse to apply a stylesheet with that content type. If a served URL is ever genuinely
needed, jsDelivr serves repo files with correct MIME and CDN caching
(`cdn.jsdelivr.net/gh/dileepadev/dileepadev@<tag>/docs/brand/brand-tokens.css`), pinned to a tag
rather than a branch. That is an escape hatch, not the plan.

**The cost of vendoring is drift.** Every copy has to be updated deliberately when the canonical
file changes. That is accepted in exchange for no runtime dependency on GitHub serving a file
correctly.

## 4. Data flow

**Reads.** The main site fetches from FastAPI at build time and revalidates on a per-resource
interval. Blog post bodies come from GitHub at build time and are not fetched at runtime.

**Writes.** Only admin writes, through server actions, authenticated with a JWT. The public
site's one write is the contact form (`POST /contact`), which is rate-limited and unauthenticated.

**Content sync.** Pushing to the blog repo's `main` triggers a workflow that uploads changed
images through the API and syncs post metadata to `POST /blogs/sync`, authenticated with an API
key. Nothing else writes to the API without a JWT.

## 5. Versions

| Component | Target |
| --- | --- |
| Next.js | 16.3.x — **identical** in `dileepa-dev` and `admin-dileepa-dev` |
| React | 19.2.x |
| Tailwind CSS | 4.3.x |
| Astro | 7.x |
| FastAPI | 0.141.x |
| Python | 3.13 |
| Pydantic | 2.13.x |
| Uvicorn | 0.52.x |
| Node types | ^22 |

Version drift between the two Next apps is what v2.0.0 exists to end. They upgrade together or
not at all.

## 6. Sequencing

1. **Standards** — this repo. Blocks everything.
2. **API** — FastAPI, projects, the events reshape, the blog reshape. Blocks both frontends.
3. **Main site** — rebrand, projects, events, the event gallery, blog reader.
4. **Blog consolidation and redirects** — the highest-consequence step. See [`redirects.md`](redirects.md).
5. **Admin** — rebrand, FastAPI, projects, events.
6. **Links** — Astro 7, rebrand.
7. **Public build log** — the dashboard, then preview screenshots last.

Full task list in [`../../TODO.md`](../../TODO.md). Cutover and rollback detail in
[`../migration/v2.0.0-migration.md`](../migration/v2.0.0-migration.md).

## 7. Constraints that shape the design

- **GitHub Pages cannot issue 301s.** `blog.dileepa.dev` is served from Pages today, so its DNS
  must move to a host that can redirect before the Astro site is switched off.
- **`dileepadev.github.io` images are hot-linked** from READMEs across many repositories, with no
  redirect layer available. Preview images migrate out one project at a time, and a file is
  removed only once every reference to it has been updated.
- **The API holds every platform credential.** MongoDB, JWT signing, Cloudinary, Resend, and the
  blog sync key. No other repo gets any of them.
- **`NEXT_PUBLIC_`-prefixed variables ship to the browser.** Nothing secret goes behind that prefix.
- **The token sheet has one canonical copy** in this repo, and no served mirror. Applications
  vendor it; each vendored copy must be updated deliberately when the canonical file changes.
