# Content pipeline

How blog content gets from `blog-dileepa-dev` onto `dileepa.dev/blog`.

## 1. The shape of it

> Diagram nodes are **repository names**; anything else is an external service. See the naming
> key in [`platform-overview.md`](platform-overview.md) §2.0.

```text
  blog-dileepa-dev            Git is the source of truth
  └── content/posts/2026/08/2026-08-21-what-is-microsoft-agent-framework.md
            │
            │  push to main
            ▼
  ┌─────────────────────────────────────────────────────────┐
  │  workflow: sync                                         │
  │  front matter ──▶ POST /blogs/sync                      │
  └─────────────────────────────────────────────────────────┘
            │
            ▼
     api-dileepa-dev                          Cloudinary
     metadata index only                      images a post links to
            │                                    │
            │  GET /blogs at build time          │  <img src> at runtime
            ▼                                    │
  ┌─────────────────────────────────────────────────────────┐
  │  dileepa-dev  build                                     │
  │  • post bodies  ◀── GitHub API, pinned ref              │
  │  • post list    ◀── api-dileepa-dev                     │
  │  → /blog and /blog/[slug] as static pages               │
  └─────────────────────────────────────────────────────────┘
```

Three stores, each holding what it is good at: **Git** holds the words, **Cloudinary** holds the
images, **MongoDB** holds the index.

Posts are grouped `content/posts/<year>/<month>/<slug>.md`. The directories are grouping only —
they were never part of the URL and are stripped when the id becomes a slug. **The file name is
the slug, and the slug is the URL.**

## 2. Why this split

The alternative — pushing rendered post bodies into MongoDB and reading everything from the API
— was rejected. It would take content out of Git, make the most static pages on the site depend
on a database at build time, and turn a post revision into a database write with no diff.

The alternative of a Git submodule was also rejected: every content change would cost two
commits, one in the blog repo and one bumping the pointer in the site repo.

Build-time fetch keeps the properties that matter. Content is reviewable as a diff, the blog is
a directory of Markdown that survives any framework change, and once a build ships, nothing at
runtime can take the blog down.

**The trade-off, stated plainly:** publishing a post requires a rebuild of the main site. That
is a webhook, and for a blog that publishes a few times a month it is the right cost.

## 3. Fetching post bodies

The main site reads MDX from GitHub at build time, **pinned to a ref** — a tag or a commit SHA,
not `main`. An unpinned fetch means a build's output depends on when it ran, which makes
rebuilds non-reproducible and lets an in-progress content edit ship by accident.

Pin in the site repo's configuration, and bump it deliberately when publishing.

```http
GET https://api.github.com/repos/dileepadev/blog-dileepa-dev/git/trees/<sha>?recursive=1
GET https://raw.githubusercontent.com/dileepadev/blog-dileepa-dev/<sha>/content/posts/<year>/<month>/<slug>.md
```

The Git trees API rather than the contents API: posts are nested under year and month, and
`recursive=1` returns the whole tree in one request instead of one per month. Check the response's
`truncated` flag rather than assuming — a silently short list looks exactly like posts having been
deleted.

The repo is public, so unauthenticated requests work. Use a token anyway in CI — the
unauthenticated rate limit is low enough that a build fetching 18 posts plus a directory listing
can hit it on a busy day, and the failure looks like a content bug rather than a rate limit.

**Cache the fetch.** A build that pulls 18 files over the network on every hot reload is
unusable locally. Cache by ref, since a pinned ref's content cannot change.

## 4. Images

### Posts hold no images

**A post carries no image of its own.** No banner, no `content/images/` directory, nothing in the
repository but words. Anything a post shows is an ordinary Markdown image in the body pointing at
a URL:

```md
![The Foundry project overview](https://res.cloudinary.com/dileepadev/image/upload/blog/foundry-overview.png)
```

This is what an author writes anyway, and it removes a whole moving part: there is no image sync
step, no deterministic-public-id rule to keep two repositories agreeing on, and no way for a
post's images to be out of step with its words.

Upload an image through `POST /uploads` — the admin's media screen, or the endpoint directly with
the `BLOG_SYNC_API_KEY` — and paste the URL it returns. **The blog repo never holds Cloudinary
credentials.** It has one key, the one it already had.

### Photographs on the platform

Photographs appear in exactly two places on `dileepa.dev`: the hero portrait, and the event
gallery composed from `events[].photos`. That is the whole image budget, and it is what makes a
page of photographs read as a deliberate section rather than decoration sprayed across the site.

Blog post images are not photographs in this sense — they are screenshots and diagrams inside an
article, and they are the article's business.

### The old image URLs still need redirecting

Retiring banners does not un-publish the 19 banner URLs that are already indexed, and three
posts embed `blog.dileepa.dev/images/posts/**` screenshots in bodies that are live today. Those
URLs die with GitHub Pages unless something answers them.

The mapping is a rule, so the redirect is a rule:

```http
blog.dileepa.dev/images/banners/<file>  →  res.cloudinary.com/<cloud>/image/upload/blog/banners/<file>
blog.dileepa.dev/images/posts/<slug>/<file> → .../blog/posts/<slug>/<file>
```

Recorded in [`redirects.md`](redirects.md). Nothing new is uploaded under those public IDs —
they exist to keep already-published URLs resolving, and nothing more.

## 5. Metadata sync

The workflow syncs front matter to `POST /blogs/sync`, upsert-by-slug and idempotent — the
property `scripts/sync-blogs.mjs` already had and keeps. With images out of the pipeline this is
now the whole of it.

### What must change in the sync script

The v1 script writes absolute URLs built from `SITE_URL`, defaulting to `https://blog.dileepa.dev`:

```js
link: `${SITE_URL}/blog/${slug}`,
bannerUrl: frontmatter.banner ? `${SITE_URL}${frontmatter.banner}` : "",
```

Both are wrong after consolidation, and both are already in the database on all 18 rows. The v2
script sends:

```js
path: `/blog/${slug}`,                       // relative
publishedDate, updatedDate, tags, series, readingTimeMinutes,
draft, featured, order, sourcePath, contentHash,
```

`canonicalUrl` is composed by the API from `path` and its own `SITE_URL`, so the blog repo does
not need to know where the site lives. There is no `banner`.

`SITE_URL` is removed entirely.

### One more fix worth making

The v1 script **skipped** any post whose slug already existed, so an edited post never updated in
the index. Since the endpoint is an upsert, the skip was never needed. The v2 script sends every
post and lets the upsert decide; `contentHash` is stored so a change is visible in the record
rather than inferred.

## 6. Front matter

The contract. Field names are load-bearing — the main site renders from them and the API keys
off them.

| Field | Type | Required |
| --- | --- | --- |
| `title` | string | yes |
| `description` | string | yes |
| `publishedDate` | ISO date | yes |
| `updatedDate` | ISO date | no |
| `tags` | string[] | defaults to `[]` |
| `draft` | boolean | defaults to `false` |
| `series` | string | no |
| `seriesOrder` | number | no |

**Validate in CI in the blog repo.** A malformed post should fail there, where the author sees
it, rather than in the main site's build where it looks like a site bug.

## 7. Rendering parity

The Astro blog has features the Next reader must match, or the migration is a downgrade:

| Feature | Astro | Next equivalent |
| --- | --- | --- |
| Code highlighting | Shiki, `github-light` / `github-dark` | Shiki via the MDX pipeline, same themes |
| Code block chrome | `components/mdx/Pre.astro` | Custom `pre` component |
| Table of contents | `TocFab.astro` from `headings` | `rehype-slug` + heading extraction |
| Share | `Share.astro` | Equivalent component |
| Series navigation | `SeriesBox.astro` | From `series` / `seriesOrder` |
| Read next | Latest + tag-related, at build | Same logic over the fetched post set |
| Sitemap | `@astrojs/sitemap` | Next sitemap, including `/blog/*` |
| RSS | — | New: `/blog/rss.xml` |

**Audited, and done.** The only MDX-only syntax was a `SeriesBox` import in eight posts. The
series box is a rendering concern, so it is rendered from the `series` and `seriesOrder` front
matter by both readers, and the posts are plain `.md` — a materially simpler build, and content
that survives any change of framework.

## 8. Publishing a post, end to end

1. Write `content/posts/<year>/<month>/YYYY-MM-DD-slug.md` in the blog repo. **The file name is
   the URL**; the directories are grouping.
2. If the post needs an image, upload it through `POST /uploads` and paste the URL into the body.
3. Push to `main`. The workflow syncs the metadata.
4. Bump the pinned content ref in `dileepa-dev` and deploy.
5. The post is live at `dileepa.dev/blog/<slug>`.

Steps 4 and 5 can be automated with a repository-dispatch webhook from the blog repo into the
site repo's deploy. Do that once the manual flow has been run a few times and is understood.

## 9. Constraints

- **Never rename a published slug.** It is the URL. There is no way to notice the break from
  inside the blog repo.
- **Pin the content ref.** An unpinned build is not reproducible.
- **The blog repo holds one credential** — `BLOG_SYNC_API_KEY`. If it ever needs a Cloudinary
  key, the design has gone wrong.
- **Front-matter field names are an interface.** Renaming one breaks rendering in one repo and
  data in another.
- **The API stores metadata, never bodies.** If post content starts appearing in MongoDB, the
  source of truth has quietly moved.
