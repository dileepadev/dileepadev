# Redirects

**Source of truth for URL changes on `dileepa.dev`.** `dileepa-dev` implements this map. If the
code and this file disagree, this file is right.

## 1. `blog.dileepa.dev` is retired, not redirected

The blog moved from `blog.dileepa.dev` to `dileepa.dev/blog` in v2.0.0. The path shape did not
change — only the host:

```text
blog.dileepa.dev/blog/{slug}   →   dileepa.dev/blog/{slug}   (same path, new host)
```

**No redirect layer was built.** The decision was to update the links at their source instead:
the shared links on social posts now point at `dileepa.dev/blog/{slug}` directly, and the
`blog.dileepa.dev` host is switched off.

### What this costs, stated plainly

A redirect covers every inbound link. Updating links at the source covers only the links you
control. So:

- **Search-engine results pointing at `blog.dileepa.dev` will 404** until they are recrawled and
  dropped. There is no 301, so there is no ranking transfer — the old URLs die rather than
  handing their signal to the new ones.
- **Third-party inbound links break.** Anyone who linked to a post from their own blog, a
  newsletter, or an aggregator has a dead link, and there is no way to enumerate them.
- **Bookmarks and shared links break** wherever they were saved outside the accounts that were
  updated.

This was accepted deliberately. The blog is young, the traffic is small, and the shared links
that mattered were reachable and have been changed. It is recorded here because the cost is real
and invisible — nothing errors, nothing fails a build — and a future reader should not mistake
the absence of a redirect table for an oversight.

### Consequences for the decommission

Because nothing needs to answer the old host, the ordering constraint that used to govern this
migration is gone. GitHub Pages can be disabled and the DNS record removed without waiting on a
redirect layer, and the Astro application has already been deleted.

## 2. Legacy slug — same-site, still required

Two posts have been renamed since publication. Both need a same-site rule on `dileepa.dev`, and
neither is optional — they cost nothing, and both old slugs were live long enough to be shared.

| From | To | Type |
| --- | --- | --- |
| `dileepa.dev/blog/2026-08-06-zero-to-agent-microsoft-foundry-series-kickoff` | `dileepa.dev/blog/2026-08-06-part-1-kicking-off-the-series` | 301 |
| `dileepa.dev/blog/2026-02-11-welcome` | `dileepa.dev/blog/2026-02-10-welcome` | 301 |

**Row 1** existed in the blog's `astro.config.mjs`, which is deleted — it is easy to lose with
that file.

**Row 2** comes from the v2.0.0 content move, which renamed `2026-02-11-welcome` to
`2026-02-10-welcome` and changed its `publishedDate` to match. The corrected date is kept and the
old URL redirects to it.

The sitemap must list neither old slug.

## 3. Same-site redirects on dileepa.dev

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

## 4. Post URLs

All 18 posts are served at `dileepa.dev/blog/{slug}`. No redirect rule is needed for any of them —
the list is here so the set is enumerable when verifying the migration.

| # | Path |
| --- | --- |
| 1 | `/blog/2026-02-11-building-ai-agents-with-microsoft-technologies` |
| 2 | `/blog/2026-02-10-welcome` — renamed from `2026-02-11-welcome`; §2 row 2 |
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

**Never rename a published file.** The file name is the slug and the slug is the URL, and nothing
in `blog-dileepa-dev` will notice the break. A rename means a new row in §2.

> [!WARNING]
> **This already happened once.** The v2.0.0 content move renamed `2026-02-11-welcome` to
> `2026-02-10-welcome`, and nothing in either repository noticed — it surfaced only when the
> sync script's output was read against the published URL list. It is resolved by row 2 of §2.
> Note what it cost: a redirect rule that has to be carried forever, for a rename that bought a
> one-day date correction.

## 5. Images

Blog images live on Cloudinary and are referenced by absolute URL from inside post bodies. They
are not served by this site and need no redirect.

Three screenshots used to be an exception — root-relative paths the retired Astro app served — and
they are now on Cloudinary like everything else. **No post depends on a file the blog repository
holds.** Detail in [`content-pipeline.md`](content-pipeline.md) §4.

The 19 retired banner URLs are not redirected, for the same reason as §1.

## 6. SEO

What still applies now that the cross-host migration is off the table:

- [ ] `rel=canonical` on every post pointing at its `dileepa.dev` URL
- [ ] Title, description, published and updated dates carried across intact
- [ ] Open Graph and Twitter card metadata preserved per post
- [x] JSON-LD `BlogPosting` on post pages, `Event` on event pages
- [ ] Sitemap includes `/blog/*`, `/projects/*`, `/events/*`, and excludes the legacy slug
- [ ] Submit the sitemap for `dileepa.dev` in Search Console
- [ ] Remove the `blog.dileepa.dev` property from Search Console once the host is switched off.
      **Do not file a change of address** — that tool requires the old URLs to 301 to the new
      ones, and they do not
- [ ] Update the Blog entry in `links-dileepa-dev/src/data/links.json` to point at
      `dileepa.dev/blog` — a bio link should not depend on a host that no longer exists

## 7. Verification

**Against production. Not localhost, not a preview deployment.**

```bash
# every post URL: expect a direct 200, no redirect
for slug in <the 18 slugs>; do
  curl -sIL -o /dev/null -w "%{http_code} %{num_redirects} %{url_effective}\n" \
    "https://dileepa.dev/blog/$slug"
done
```

Pass criteria:

- Status is **200**, and `num_redirects` is **0** for all 18.
- **Both** §2 rows return exactly **one** 301, landing on a 200.
- The `/sessions` rules in §3 each return one 301.

Then, by hand:

- [ ] The canonical tag on each post names its own `dileepa.dev` URL
- [ ] The sitemap lists all 18 posts and omits the legacy slug
- [x] The three inline images in `2026-02-12-personalize-your-vs-code-ai-with-custom-agents`
      resolve — moved to Cloudinary
