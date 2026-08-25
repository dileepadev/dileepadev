# Redirects

**Source of truth for the blog URL migration.** `dileepa-dev` implements this map;
`blog-dileepa-dev` depends on it. If these three ever disagree about where an old URL points,
this file is right.

## 1. What is at stake

18 posts are published and indexed at `blog.dileepa.dev`. Getting this wrong drops indexed
traffic silently — nothing errors, nothing fails a build, and the ranking takes months to
recover if it recovers at all.

The mitigation is that the path shape does not change. Only the host does.

```text
blog.dileepa.dev/blog/{slug}   →   dileepa.dev/blog/{slug}
```

Keeping `/blog/{slug}` identical makes the map mechanical, and mechanical maps are the kind
that survive review.

## 2. The hosting problem

**`blog.dileepa.dev` is served from GitHub Pages, which cannot issue 301s.**

This is the blocker, and it has to be solved before anything is switched off.

### Recommended: move the DNS to Vercel

Repoint the `blog.dileepa.dev` DNS record at Vercel and serve the redirects from the
`dileepa-dev` project, conditioned on host:

```ts
// next.config.ts
async redirects() {
  return [
    {
      source: "/blog/:slug",
      has: [{ type: "host", value: "blog.dileepa.dev" }],
      destination: "https://dileepa.dev/blog/:slug",
      permanent: true,
    },
    // ... the rest of the table below
  ];
}
```

Real 301s, one hop, full ranking transfer.

### Fallback: meta-refresh stubs on Pages

Keep a minimal Pages site of per-slug HTML stubs with `<meta http-equiv="refresh">` and
`<link rel="canonical">`. Search engines treat these as soft redirects: ranking transfer is
slower and less reliable, and some crawlers will not follow them at all.

Use this only if the DNS move cannot happen, and treat it as temporary.

> **Order matters.** The DNS record must point at whatever serves the 301s **before** GitHub
> Pages is disabled. Disabling Pages first means every published URL dies at DNS resolution,
> which is worse than a 404 — there is nothing to redirect from.

## 3. Post URLs

All 18 keep their path. Old host `blog.dileepa.dev`, new host `dileepa.dev`, 301 permanent.

| # | Path — unchanged on both hosts |
| --- | --- |
| 1 | `/blog/2026-02-11-building-ai-agents-with-microsoft-technologies` |
| 2 | `/blog/2026-02-11-welcome` |
| 3 | `/blog/2026-02-12-personalize-your-vs-code-ai-with-custom-agents` |
| 4 | `/blog/2026-02-16-what-is-microsoft-foundry` |
| 5 | `/blog/2026-02-19-a-practical-guide-to-backdating-git-commits` |
| 6 | `/blog/2026-02-19-github-contributions-not-showing-on-the-graph-fix` |
| 7 | `/blog/2026-02-26-naming-conventions-in-programming` |
| 8 | `/blog/2026-02-27-running-ollama-ai-models-on-a-midrange-laptop-my-experience` |
| 9 | `/blog/2026-08-06-part-1-kicking-off-the-series` |
| 10 | `/blog/2026-08-07-the-ai-engineering-stack-what-i-use-and-why` |
| 11 | `/blog/2026-08-12-part-2-your-first-foundry-project` |
| 12 | `/blog/2026-08-13-part-3-building-your-first-agent` |
| 13 | `/blog/2026-08-14-part-4-picking-the-right-model` |
| 14 | `/blog/2026-08-15-part-5-giving-your-agent-tools-and-knowledge` |
| 15 | `/blog/2026-08-16-part-6-multi-agent-systems` |
| 16 | `/blog/2026-08-17-part-7-tracing-and-evaluating-agents` |
| 17 | `/blog/2026-08-18-part-8-locking-it-down-for-production` |
| 18 | `/blog/2026-08-21-what-is-microsoft-agent-framework` |

## 4. Legacy slug

One redirect already exists inside the blog's `astro.config.mjs` and is easy to lose along with
that file. It must survive as a **single hop** on both hosts:

| From | To |
| --- | --- |
| `blog.dileepa.dev/blog/2026-08-06-zero-to-agent-microsoft-foundry-series-kickoff` | `dileepa.dev/blog/2026-08-06-part-1-kicking-off-the-series` |
| `dileepa.dev/blog/2026-08-06-zero-to-agent-microsoft-foundry-series-kickoff` | `dileepa.dev/blog/2026-08-06-part-1-kicking-off-the-series` |

Two rules, not one chained through the first. A redirect to a redirect loses ranking signal and
is flagged in most SEO audits.

The blog's sitemap currently filters this slug out so the stub is not indexed as a real page.
The new sitemap must not list it either.

## 5. Non-post URLs

| From | To | Type |
| --- | --- | --- |
| `blog.dileepa.dev/` | `dileepa.dev/blog` | 301 |
| `blog.dileepa.dev/blog` | `dileepa.dev/blog` | 301 |
| `blog.dileepa.dev/about` | `dileepa.dev/#about` | 301 |
| `blog.dileepa.dev/404` | `dileepa.dev/blog` | 301 |
| `blog.dileepa.dev/sitemap-index.xml` | `dileepa.dev/sitemap.xml` | 301 |
| `blog.dileepa.dev/sitemap-0.xml` | `dileepa.dev/sitemap.xml` | 301 |
| `blog.dileepa.dev/*` (anything else) | `dileepa.dev/blog` | 301 |

The catch-all matters. Anything indexed that this table missed lands somewhere useful rather
than on a 404.

## 6. Image URLs

Blog images are embedded in already-published post bodies and stored in the API's v1
`bannerUrl` column. They need redirects for the same reason the posts do — **including the
banners**, which are retired going forward but remain indexed at their old URLs.

The mapping is a rule rather than a list:

| From | To |
| --- | --- |
| `blog.dileepa.dev/images/banners/<file>` | `res.cloudinary.com/<cloud>/image/upload/blog/banners/<file>` |
| `blog.dileepa.dev/images/posts/<slug>/<file>` | `res.cloudinary.com/<cloud>/image/upload/blog/posts/<slug>/<file>` |
| `blog.dileepa.dev/images/brand/<file>` | `dileepa.dev/<file>` — the main site's `public/` |

19 banners and 3 inline post images are affected. Detail in
[`content-pipeline.md`](content-pipeline.md) §4.

## 7. Same-site redirects on dileepa.dev

**`/events` keeps its path.** An earlier draft of the migration renamed the resource to
`sessions` and this table carried `/events → /sessions`. That rename is reverted: the site, the
admin and the API all say "event", and the published URL never had to move at all. Nothing to do
here is the best outcome available for an indexed URL.

The `/sessions` rules run the other way, and exist only because that path was reachable on a
preview deployment of the `feat/v2.0.0` branch:

| From | To | Type |
| --- | --- | --- |
| `dileepa.dev/sessions` | `dileepa.dev/events` | 301 |
| `dileepa.dev/sessions/:slug` | `dileepa.dev/events/:slug` | 301 |

`/communities` and `/videos` keep their paths. `/gallery` is new in v2.0.0 and replaces nothing.
If any of them moves, it goes in this table.

## 8. SEO tasks

Redirects alone are not the whole job.

- [ ] `rel=canonical` on every post pointing at the `dileepa.dev` URL
- [ ] Title, description, banner, published and updated dates carried across intact
- [ ] Open Graph and Twitter card metadata preserved per post
- [ ] JSON-LD `BlogPosting` on post pages
- [ ] New sitemap includes `/blog/*`, `/projects/*`, `/events/*`
- [ ] Old sitemap URL redirects, and keeps redirecting for **at least 6 months**
- [ ] Google Search Console **change of address** from the `blog.dileepa.dev` property to
      `dileepa.dev`
- [ ] Resubmit the new sitemap; watch the coverage report for the transfer
- [ ] Update the Blog entry in `links-dileepa-dev/src/data/links.json` to point at
      `dileepa.dev/blog` directly — a bio link should not depend on a redirect

## 9. Verification

**Against production. Not localhost, not a preview deployment.**

```bash
# every post URL: expect a single 301 to a live 200
for slug in <the 18 slugs>; do
  curl -sIL -o /dev/null -w "%{http_code} %{num_redirects} %{url_effective}\n" \
    "https://blog.dileepa.dev/blog/$slug"
done
```

Pass criteria, all three:

- `num_redirects` is **1**. A 2 means a chain — find it and flatten it.
- Final status is **200**, not 404.
- `url_effective` is the expected `dileepa.dev` URL.

Then, by hand:

- [ ] The legacy slug resolves in one hop from both hosts
- [ ] A banner image URL from a published post resolves
- [ ] `blog.dileepa.dev/` and `/about` land correctly
- [ ] An unmapped path hits the catch-all rather than a 404
- [ ] The canonical tag on a migrated post names the `dileepa.dev` URL

## 10. Lifetime

**Keep the redirect layer live for at least 12 months** — not until launch, not until traffic
looks fine.

Shared links, bookmarks, and citations from other people's posts keep arriving for years, and
the cost of keeping a redirect rule is nothing. Removing it is what costs.

Set a calendar reminder rather than trusting that anyone will remember to check.
