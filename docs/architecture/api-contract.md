# API contract — v2.0.0

The endpoint and data-model contract for `api.dileepa.dev`. Written here so
`api-dileepa-dev` implements against a stated shape, and `dileepa-dev` and
`admin-dileepa-dev` consume the same one.

**Implementation:** FastAPI 0.141.x · Python 3.13 · Pydantic 2.13.x · MongoDB Atlas ·
FastAPI Cloud.

## 1. Conventions

### Envelopes

Collection endpoints return a consistent envelope:

```json
{ "items": [ ... ], "total": 42, "limit": 20, "offset": 0 }
```

Single-resource endpoints return the object directly.

### Errors

One shape everywhere, replacing the NestJS exception filter's output:

```json
{ "error": { "code": "not_found", "message": "No event with slug 'foo'", "details": null } }
```

`code` is a stable machine-readable string. `message` is written for a person and surfaces
directly in the admin UI, so it follows the voice rules — say what failed and what to do, never
"Something went wrong".

### Common query parameters

`?limit=` `?offset=` `?featured=` `?tag=` `?published=` where each applies. Public callers only
ever see `published: true` records; admin authenticates and sees everything.

### Fields on every resource

`id` · `createdAt` · `updatedAt` · `published` (bool) · `order` (int) · `meta` (free-form object)

**`order` is a priority: higher values sort first.** This is v1's `index` under a new name and
with the same meaning — v1 sorted `index: -1` for exactly this reason — so one rule holds across
every resource and the rename is not also a behaviour change. `scripts/migrate_v1_documents.py`
performs the rename; the API reads either field name so it is correct before that runs.

`meta` is the forward-compatibility hatch. New metadata that doesn't justify a schema change
lands there rather than becoming a new resource. It is never used for anything a query filters on.

**`id`, not `_id`.** v1 returned raw Mongoose documents, `_id` and `__v` included. v2.0.0 maps
every response through a model, so a schema change cannot silently become an API change.

### Dates

All datetimes are ISO 8601, timezone-aware, stored UTC. **This is a change** — v1 stored dates
as free-text strings on events, blogs, videos, and communities, which is why none of them sort
reliably.

## 2. Endpoints

Admin writes follow one pattern on every resource: `POST /{resource}`,
`PATCH /{resource}/{id}`, `DELETE /{resource}/{id}`, and `PATCH /{resource}/order` for bulk
reordering. `PATCH` is a partial update — only the fields sent are changed. `about` is a
singleton, so its writes take no id. Reads accept an id or a slug wherever a resource has one.

| Endpoint | Public | Admin | Notes |
| --- | --- | --- | --- |
| `POST /auth/login` | — | ✓ | Returns access + refresh tokens |
| `POST /auth/refresh` | — | ✓ | Re-reads the user, so a disabled account cannot refresh |
| `GET /auth/profile` | — | ✓ | |
| `GET /about` | ✓ | CRUD | Singleton. Gains `location` in v2.0.0 — free text, rendered beside the portrait as `"{title} · {location}"` |
| `GET /experiences` | ✓ | CRUD | |
| `GET /educations` | ✓ | CRUD | |
| `GET /tools` | ✓ | CRUD | |
| `GET /communities` | ✓ | CRUD | |
| `GET /videos` | ✓ | CRUD | Gains `description` in v2.0.0 |
| **`GET /projects`** | ✓ | CRUD | **New** |
| **`GET /projects/{slug}`** | ✓ | — | **New** |
| **`GET /events`** | ✓ | CRUD | **Reshaped** — same path, new model |
| **`GET /events/{slug}`** | ✓ | — | **New** — v1 addressed events by `_id` |
| `GET /blogs` | ✓ | CRUD | Reshaped |
| `GET /blogs/{slug}` | ✓ | — | New |
| `POST /blogs/sync` | — | API key | Blog repo pipeline |
| **`GET /blogs/{slug}/engagement`** | ✓ | — | **New.** Views, reaction counts, and this caller's own reaction |
| **`POST /blogs/{slug}/views`** | ✓ | — | **New.** De-duplicated per reader per 24h |
| **`POST /blogs/{slug}/reactions`** | ✓ | — | **New.** Set, change, or clear one reaction |
| **`GET /blogs/{slug}/comments`** | ✓ | — | **New.** The thread. Never returns an email |
| **`POST /blogs/{slug}/comments`** | ✓ | — | **New.** Live immediately; rate-limited, honeypotted |
| **`POST /blogs/{slug}/comments/{id}/reactions`** | ✓ | — | **New.** Same four reactions; works on replies too |
| **`GET /comments`** | — | ✓ | **New.** The moderation queue. **Not public** — it holds emails |
| **`POST /comments`** | — | ✓ | **New.** The owner's own reply |
| **`PATCH /comments/{id}`** | — | ✓ | **New.** Edit or hide |
| **`DELETE /comments/{id}`** | — | ✓ | **New.** Permanent |
| `POST /uploads` | — | ✓ / API key | Cloudinary-backed |
| `GET /uploads` | — | ✓ | |
| `DELETE /uploads/{publicId}` | — | ✓ | `publicId` is a path: Cloudinary ids contain slashes |
| `POST /contact` | ✓ | — | Rate-limited, unauthenticated |
| `GET /health` | ✓ | — | New. **503** when MongoDB is unreachable |
| `GET /version` | ✓ | — | New |
| `GET /` | ✓ | — | `{ name, version, docs, website }`. v1 returned `Hello World!` |
| `GET /docs` | ✓ | — | The API reference, rendered by Scalar. **Development only** |

There is **no `/users` resource**, by decision — see §10.

### Deprecations

**There are none.** v2.0.0 is a single cutover: the API and every consumer are released at the
same time, so there is no window in which a v1 path has to keep answering, and nothing is
carried forward waiting to be removed in a later version.

The v1 paths below return `404`. Every caller moves in this release.

| v1 path | Successor |
| --- | --- |
| `GET /events` | Same path, the standard envelope rather than v1's bare array, and the v2 model |
| `POST` `PATCH` `DELETE /events/{id}` | The same verbs against `/events/{slug}` |
| `POST /auth/sign-in` | `POST /auth/login` |
| `POST /upload` | `POST /uploads` |
| `GET /upload` | `GET /uploads` |
| `DELETE /upload/{publicId}` | `DELETE /uploads/{publicId}` |

`api-dileepa-dev`'s `tests/contract/test_v1_parity.py` records each of these with its reason and
fails if a v1 route is neither served nor listed, and `tests/test_openapi.py` fails if any
operation is published with `deprecated: true`.

**This puts the consumers on a hard deadline.** `admin-dileepa-dev` calls `POST /auth/sign-in`,
`GET`/`POST`/`PATCH`/`DELETE /events` and `POST`/`DELETE /upload` today; all of them have to be
retargeted and deployed together with the API, not after it.

One thing does survive the cutover, and it is not an alias: tokens minted by the NestJS app
carry no `type` claim and are still read as access tokens, so a session that was live when
traffic moved is not signed out by the move. That is bounded by token expiry rather than by a
release — `REFRESH_TOKEN_EXPIRE_DAYS` after the cutover, 30 days by default.

## 3. Projects

Net-new. There is no `projects` module in v1, despite the admin README advertising one.

```python
class Project:
    id: str
    slug: str                      # unique, indexed — the public URL segment
    name: str
    tagline: str
    description: str               # markdown
    status: Literal["active", "maintained", "archived", "concept"]
    role: str | None
    period: Period                 # { start: date, end: date | None }
    stack: list[str]
    categories: list[str]
    tags: list[str]
    links: ProjectLinks            # { repo, demo, docs, caseStudy, package } — all optional
    cover: Image | None            # { url, alt }
    gallery: list[GalleryItem]     # { url, alt, caption, order }
    highlights: list[str]
    metrics: list[Metric]          # { label, value }
    featured: bool
    order: int
    published: bool
    seo: Seo                       # { metaTitle, metaDescription, ogImage }
    meta: dict
    createdAt: datetime
    updatedAt: datetime
```

**Filters:** `?featured=` `?status=` `?tag=` `?category=` `?limit=` `?offset=`
**Default sort:** `featured` desc, then `order` **desc**, then `period.start` desc.

> `order` is a priority — higher first — everywhere on the platform, so this reads desc rather
> than the asc an earlier draft of this document specified. One rule beats two.

## 4. Events

`events` keeps its path and its collection name, and changes shape. v1 carried seven flat fields
— title, date (a string), location, format, description, url, index — and none of the speakers,
photos, recordings, slug or structured time this needs.

> **On the name.** An earlier draft of this contract called the resource `sessions`, on the
> reasoning that a talk is a session *at* an event. In practice the site, the admin and the
> person writing the records all say "event", and a name nobody uses is a name that gets
> mistyped. `scripts/migrate_events_v1_to_v2.py` rewrites the v1 rows in place, keeping their
> `_id` and copying the originals to `events_v1_backup` first.

```python
class Event:
    id: str
    slug: str                      # unique, indexed
    title: str
    summary: str                   # one line, for cards
    description: str               # markdown, for the detail page
    type: Literal["workshop", "talk", "webinar", "meetup", "bootcamp", "panel", "other"]
    format: Literal["in_person", "online", "hybrid"]
    startAt: datetime              # tz-aware
    endAt: datetime | None
    timezone: str                  # IANA, e.g. "Asia/Colombo"
    status: Literal["upcoming", "completed", "cancelled"]
    location: Location | None      # { venue, city, country, mapUrl } — null when online
    host: Host | None              # { name, organizer, organizerUrl } — the conference or
                                   #   meetup series this ran under, not the event itself
    speakers: list[Speaker]        # { name, role, profileUrl, avatarUrl, isHost }
    cover: Image | None
    photos: list[Photo]            # { url, alt, caption, credit, width, height, order }
    recordings: list[Recording]    # { platform, url, embedUrl, durationSeconds, language }
    slides: Slides | None          # { url, provider }
    links: list[EventLink]         # { label, url, kind }
    tags: list[str]
    series: Series | None          # { name, order } — mirroring blog posts
    audienceSize: int | None
    featured: bool
    order: int
    published: bool
    seo: Seo
    meta: dict
    createdAt: datetime
    updatedAt: datetime
```

`links[].kind` ∈ `registration` · `announcement` · `repo` · `resource` · `recap`
`recordings[].platform` ∈ `youtube` · `linkedin` · `other`

**Filters:** `?status=` `?type=` `?format=` `?year=` `?tag=` `?featured=` `?hasPhotos=`
`?limit=` `?offset=`
**Default sort:** `startAt` desc for completed, `startAt` asc for upcoming.

`?hasPhotos=true` exists for the main site's event gallery, which is a flat grid of photographs
across every event. Expressing it as a query rather than fetching everything and filtering keeps
`total` truthful, which is what makes the gallery pageable.

### Two rules worth stating

**`status` is derived, not typed.** Compute it from `startAt` against now, but allow an explicit
override so a cancelled event stays cancelled. A field a human has to remember to update goes
stale within a month.

**Photos and recordings are optional, and the UI must survive both being empty.** An in-person
event with no photos yet and an online event before its recording is published are both normal
states, not degraded ones.

`photos[]` is also the **only** source of the main site's event gallery. There is no `/photos`
resource and there should not be one: a photograph has no life of its own away from the event it
was taken at, and the caption needs the event's title and date to mean anything.

### Why this shape is extensible

The platform plan requires that new event metadata not force another major architectural
change. Three mechanisms cover it:

- `photos[]`, `recordings[]`, `speakers[]`, and `links[]` are arrays of objects — new kinds of
  each are new entries, not new resources.
- New scalar fields land as optional with a default, which is backward-compatible in Pydantic
  and in Mongo.
- `meta` absorbs anything genuinely one-off.

What would force a major change is a new *relationship* — events belonging to a series, say.
If that becomes likely, model it now as an optional `series: { name, order } | None`, mirroring
blog posts.

## 5. Blogs

Reshaped for a blog that now lives on the main website.

```python
class BlogPost:
    id: str
    slug: str                      # unique, indexed — matches the Markdown filename
    title: str
    description: str
    path: str                      # "/blog/{slug}" — RELATIVE
    canonicalUrl: str              # "https://dileepa.dev/blog/{slug}"
    publishedDate: datetime        # was a string
    updatedDate: datetime | None
    tags: list[str]
    series: Series | None          # { name, order }
    banner: Image | None           # { url, alt } — always null; see below
    readingTimeMinutes: int
    draft: bool
    featured: bool
    order: int
    sourcePath: str                # "posts/{year}/{month}/{slug}.md" in the blog repo
    contentHash: str               # detects changed content on sync
    published: bool
    seo: Seo
    meta: dict
    legacy: Legacy | None          # { link, bannerUrl, date, excerpt } — one release only
    views: int                     # readers write this, not the admin
    reactions: ReactionCounts      # { liked, insightful, useful, learned }
    createdAt: datetime
    updatedAt: datetime
```

### What changed and why

| v1 | v2.0.0 | Reason |
| --- | --- | --- |
| `link` — absolute `https://blog.dileepa.dev/...` | `path` — relative, plus `canonicalUrl` | The host is gone; consumers compose the URL |
| `bannerUrl` — absolute, on the blog host | `banner: { url, alt }` — always `null` | Banners are retired; see below |
| `date: str` | `publishedDate: datetime` | Strings don't sort |
| `excerpt` | `description` | Matches the front-matter field name |
| — | `tags`, `series`, `readingTimeMinutes`, `updatedDate`, `draft`, `sourcePath`, `contentHash` | Already in front matter, previously discarded |
| — | `views`, `reactions` | New in v2.0.0; see **Engagement** below |

**The API stores metadata only.** Post bodies stay in Git and are fetched by the main site at
build time. See [`content-pipeline.md`](content-pipeline.md).

### Engagement — views and reactions

Two counters on a post, written by readers rather than by the admin or the pipeline.

```text
GET  /blogs/{slug}/engagement   -> { slug, views, reactions, viewerReaction }
POST /blogs/{slug}/views        -> the same shape, after counting
POST /blogs/{slug}/reactions    -> the same shape, after applying { reaction }

reactions      { liked, insightful, useful, learned }   counts
viewerReaction one of those four, or null               this caller's own
```

**The vocabulary is closed.** Four reactions, validated as an enum. An open set turns a counter
into free-text storage, and a reaction only one person can send is not a signal anyone can read.

**One reaction per reader per post, changeable.** Sending a different one moves the vote; sending
the one already chosen — or `null` — clears it. The buttons are toggles, and a toggle that cannot
untoggle is a trap. The aggregate on the post moves by the delta, so the counts stay right without
recounting the reactions collection on every write.

**No identity is collected.** Both endpoints key on `sha256(JWT_SECRET : slug : address)`. That is
enough to recognise a repeat and not enough to reconstruct who it was. The slug is inside the hash
rather than beside it, so a key from one post cannot be replayed against another.

**Views de-duplicate per reader per 24 hours**, and the de-duplication is a unique index, not a
check in the handler:

| Collection | Holds | Index |
| --- | --- | --- |
| `blog_views` | one opaque key per reader per post per window | unique on `key`; TTL on `expiresAt` |
| `blog_reactions` | that key against the reaction chosen | unique on `(slug, key)` |

A read-then-write would let two concurrent requests both conclude they are the first. Here the
second insert fails and the increment simply does not happen. A duplicate is **not** an error to
the caller — they asked for the post to be counted and it already is — so it returns the current
numbers with the same 200 as a first view.

The TTL index is what stops `blog_views` growing without bound; Mongo deletes each row once its
window passes.

**Counts are read-only everywhere except these endpoints.** `views` and `reactions` are absent
from `BlogCreate`, `BlogUpdate` and `BlogSync`, so neither an admin edit nor a content re-sync can
overwrite them. `/blogs/sync` writes with `$set` over the fields it sends, and these are not among
them — there is a test that says so, because a counter a routine re-sync zeroes is worse than no
counter.

**Engagement on an unpublished post is a 404, not a 403.** Confirming that a slug exists but is
hidden leaks the thing being hidden.

### Comments

Readers comment on posts. **There is no approval queue** — a comment is visible the moment it is
posted. That is a deliberate trade: a conversation that waits on a moderator is not a
conversation. The cost is that spam reaches readers until it is removed, so every defence is at
the door rather than in a queue behind it:

| Defence | What it stops |
| --- | --- |
| `RATE_LIMIT_COMMENT`, 6/minute per address | A spam run. Looser than contact's 3/minute — a reader may legitimately reply twice |
| `body` ≤ 4000, `author` ≤ 80 | One request carrying an essay |
| Honeypot field | Bots that fill in every input they find |
| Depth cap of 1 | A thread the layout has no room for |

**The honeypot answers 201 and stores nothing.** Telling a bot which field caught it is how it
learns to stop tripping it, so a rejected submission is indistinguishable from an accepted one.
`accepted: false` is in the body for a human client; no legitimate reader can trip it.

#### Two shapes, and the difference is the point

```text
PublicComment   slug, author, body, parentId, authorIsOwner,
                reactions, viewerReaction, timestamps
Comment         ...plus email, published, key
```

`PublicComment` is what a reader gets. It **has no field for an email address**, so the public
endpoint cannot serialise one — the guarantee is the shape of the model, not a filter someone has
to remember to apply. `Comment` is admin-only and carries the email and the hashed commenter key.

This is also why the admin routes are written out rather than built with `crud_router`. That
helper's list route is deliberately public — it is what serves `/projects` and `/events` to the
website — and `/comments` is the one collection here where public read access would disclose
something a reader gave in confidence.

#### Threading is one level deep

`parentId` points at a top-level comment. A reply to a reply is **re-parented** to the thread it
belongs to rather than rejected: the reader did nothing wrong, and the comment still belongs
under that conversation. A parent on a different post is not honoured.

**A reply outlives its parent.** Hiding or deleting a comment promotes its replies to top level
rather than taking them with it — the person who wrote the reply is not responsible for the
comment above it.

#### `authorIsOwner`

Set by `POST /comments` and by nothing else. A reader cannot claim the badge because
`CommentCreate` has no field for it and `ApiModel` forbids extra fields — the distinction is
enforced by the shape of the request rather than by a check that could be forgotten.

#### Comments carry the same four reactions

A comment — or a reply, which is a comment — offers `liked` / `insightful` / `useful` /
`learned`, exactly as a post does. One vocabulary across the site means one enum in the API and
one picker in the UI; two vocabularies would mean teaching readers two.

The toggle rule is identical too, and is applied by the *same code*:
`app/services/reactions.py`. It was written twice before that module existed — once for posts and
once for comments — and the way two copies drift is a count that no longer matches the records
behind it, which nothing would report. The service addresses the subject and the per-reader
record by filter, so it knows nothing about blogs or comments.

`viewerReaction` on a comment is **filled in per request, not stored**. The stored document holds
counts; what a particular reader chose lives in `comment_reactions`. Reading a thread resolves
all of them in **one** query with `$in` across the thread — one query per comment would be forty
round trips on a forty-comment thread, on the hottest read the blog has.

**The slug in the reaction path is not decorative.** It is checked against the comment, which
keeps a comment id from being reacted to through a post it does not belong to, and makes an
unpublished post's thread unreachable here for the same reason it is unreachable everywhere else.

| Collection | Holds | Index |
| --- | --- | --- |
| `comment_reactions` | one reader's choice per comment | unique on `(commentId, key)` |

#### Hiding versus deleting

`published: false` takes a comment off the site and keeps the row; it is reversible and keeps the
thread beneath it addressable. `DELETE` is permanent. Prefer hiding unless the content has to go.

### Banners are retired

Posts carry no image of their own. Anything a post shows is an ordinary Markdown image in the
body, pointing at a URL — which is what an author writes anyway, and it survives any change of
host or renderer without a database migration.

`banner` **stays on the model.** Removing a field from a response is a breaking change for every
consumer that reads it, and buys nothing: the field is one nullable object. It is written by
nothing and read by nothing, and `scripts/migrate_blog_urls.py` clears it while archiving the v1
`bannerUrl` into `legacy`.

The same rule holds across the platform. Photographs appear in exactly two places on
`dileepa.dev`: the hero portrait, and the event gallery composed from `events[].photos`.

### Migration

All 18 existing rows carry `blog.dileepa.dev` absolutes in `link` and `bannerUrl`. Those URLs no
longer resolve — the host is retired — so every row has to be rewritten. Rewriting is
destructive:

1. Take a **verified, restore-tested** MongoDB backup.
2. Dry-run the migration and diff the output.
3. Write the new fields; keep the old values under `legacy: { link, bannerUrl }`.
4. Drop `legacy` once the rewritten URLs are confirmed good in production and the rollback
   window has passed. This is a data safety net, not a deprecated interface: it is bounded by
   confidence in the rewrite rather than by a version, and `scripts/rollback_blog_urls.py`
   reads it, so dropping it early removes the undo.

## 6. Auth

JWT access + refresh. Role-based dependency guards mirroring the v1 RBAC. An API-key guard
covers `POST /blogs/sync` and the blog pipeline's uploads.

> **The cutover risk in this migration.** Existing password hashes were produced by Node's
> `bcrypt`. They must validate under `passlib[bcrypt]`. **Test against a real hash pulled from
> the database before committing to the approach.** Also confirm the JWT algorithm, secret
> handling, and claim names match, or every existing session is invalidated.
>
> If they cannot be made compatible, a forced password reset is acceptable — but it must be
> planned, documented in `CHANGELOG.md`, and executed with a working recovery path. Discovering
> it at cutover means being locked out of the admin.

## 7. Uploads

`POST /uploads` is the only path to Cloudinary. Nothing else in the platform holds Cloudinary
credentials.

**Callers:** admin (JWT) for content images; the blog repo's workflow (API key) for banners and
inline post images.

**Response:**

```json
{ "url": "https://res.cloudinary.com/<cloud>/image/upload/v.../blog/banners/<slug>.png",
  "publicId": "blog/banners/<slug>",
  "width": 1200, "height": 630, "format": "png", "bytes": 184320 }
```

**Deterministic `public_id`.** Uploads from the blog pipeline derive their `public_id` from the
repo path, with `overwrite=true` and `invalidate=true`. Re-uploading the same path replaces the
asset and purges the CDN cache, which makes the pipeline idempotent and lets the main site
construct image URLs without a database lookup.

Azure Blob Storage is retired. Remove its configuration and code paths, and drop
`dileepadev.blob.core.windows.net` from the main site's `remotePatterns` once no stored URL
references it.

## 8. Consuming the contract

The OpenAPI spec FastAPI generates is the machine-readable version of this document.

- `dileepa-dev` generates `lib/api-types.ts` from it, replacing the hand-maintained file.
- `admin-dileepa-dev` generates a typed client from it, replacing hand-written request shapes.

When they diverge, the spec wins and this document gets corrected.

Interactive docs stay **disabled in production**, enabled in development — the v1 posture,
kept. The reference is rendered by [Scalar](https://scalar.com/) at `/docs`, and the JSON is at
`/api-json`. Swagger UI and ReDoc are both switched off.

In production neither is registered, so the page cannot be reached *and* the spec it reads is
not served. Turning off only the page would leave the spec public, which is the part that
actually describes the admin write paths.

## 9. Cross-cutting

- **CORS allowlist:** `dileepa.dev`, `admin.dileepa.dev`, `links.dileepa.dev`, Vercel preview
  domains, `localhost`. Never `*`.
- **Rate limiting** on every public endpoint; tighter on `POST /contact`.
- **Security headers** replacing Helmet.
- **Never return a raw database document.** Map to a response model, so a schema change cannot
  silently become an API change.
- **Never log a secret, a token, or a request body containing credentials.**

## 10. Decisions closed during implementation

Four things this document did not say, decided when the code forced them. The implementation is
the contract; this section records what it settled on and why.

### `/users` — there is no such resource

Accounts are seeded with `scripts/create_user.py`, run against the database directly.

v1 never had a users endpoint either: `UsersService` only ever looked a user up by email. This
is a single-owner platform, so user CRUD would put an attack surface next to the password hashes
in exchange for nothing. `GET /auth/profile` covers "who am I", and role changes are rare enough
to be a script.

### Admin writes

`POST /{resource}` · `PATCH /{resource}/{id}` · `DELETE /{resource}/{id}`, with `PATCH` a
partial update. `DELETE` returns `{ "id": "...", "deleted": true }` rather than the deleted
record: a client that wanted the record had it before it asked.

### Reordering is bulk

`PATCH /{resource}/order` takes `{ "items": [{ "id": "...", "order": 10 }, ...] }` and returns
`{ "updated": n }`. One request per drag-and-drop commit rather than one `PATCH` per row, which
is what a list of any length would otherwise cost.

The route is declared before `/{id}` so `order` is not read as a record id.

### `draft` versus `published` on `BlogPost`

**`published` gates visibility**, on blogs exactly as on every other resource. `draft` is
front-matter provenance, carried through so the API can say where a post's state came from.

`POST /blogs/sync` maps `published = not draft` and **refuses** a `published` field in the body.
That keeps the front matter the single place an author decides whether a post is live — two
places to check would go out of sync the first time someone edited the wrong one.

## 11. Departures from v1 that consumers must adopt

v2.0.0 is a major release and both frontends are rebuilt in it, so these are adopted rather than
absorbed. `api-dileepa-dev/tests/contract/test_v1_parity.py` fails if anything departs from v1
that is not listed here or in that file.

| v1 | v2.0.0 | Why |
| --- | --- | --- |
| Collection endpoints return a bare array | `{ items, total, limit, offset }` | One shape on every resource |
| An empty collection returns `404` | `200` with an empty list | An empty section was indistinguishable from a broken endpoint |
| `{ statusCode, timestamp, path, message }` | `{ error: { code, message, details } }` | A stable machine-readable code, and a message written for a person |
| `_id`, `__v` | `id` | Responses are mapped through a model |
| `index` | `order` | Same meaning, one name |
| `POST /auth/sign-in` | `POST /auth/login` | Renamed. The old path is not aliased |
| `POST /upload` | `POST /uploads` | Renamed. The old path is not aliased |
| `GET /events` | `GET /events` | Same path, reshaped into the standard envelope |
| `GET /` returned `Hello World!` | `{ name, version, docs, website }` | Nothing consumed the string |

The sign-in **response body keeps v1's field names** — `access_token`, `refresh_token`,
`token_type`, `expires_in` — rather than the camelCase used everywhere else. `admin-dileepa-dev`
reads `access_token` today, and renaming it would sign the owner out at the moment of cutover.
