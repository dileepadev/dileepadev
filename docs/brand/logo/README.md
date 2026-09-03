# Logo assets

The lockup is **`dileepadev /.`** — a neutral wordmark followed by an italicised emerald
forward slash and a solid emerald dot at its base. Full specification in
[`../brand-guide.md`](../brand-guide.md) §3.

| File | Surface | Wordmark | Accent |
| --- | --- | --- | --- |
| `lockup-dark.svg` | Carbon | `ink-100` `#F2F2F2` | Emerald Bright `#23B888` |
| `lockup-light.svg` | Paper | `paper-900` `#141414` | Emerald Deep `#087F5B` |
| `mark-dark.svg` | Carbon | — | Emerald Bright `#23B888` |
| `mark-light.svg` | Paper | — | Emerald Deep `#087F5B` |

## Live text, not outlines

These SVGs use `<text>` with a Manrope font stack. On a surface where Manrope is loaded they
render exactly right and stay a few hundred bytes. Anywhere the font is missing they fall back
to `system-ui`, and the wordmark's proportions go with it.

**Before sending the lockup anywhere off-platform** — a conference speaker pack, a print
vendor, a third-party site — export an outlined version from the design tool. Live text is for
surfaces we control.

For the same reason, prefer the CSS lockup over these files inside our own applications: it
inherits the theme automatically and needs no light/dark file swap.

```html
<span class="wordmark">dileepadev</span><span class="mark" aria-hidden="true">/</span>
```

`.wordmark` and `.mark` are defined in [`../brand-tokens.css`](../brand-tokens.css). The mark is
decorative — the accessible name comes from the containing link's `aria-label`.

## Rules

- Minimum width **120px** for the lockup. The `/.` must stay legible as two distinct strokes.
- Clear space equal to the wordmark's cap-height on all four sides.
- The wordmark is **never** emerald. The `/.` is **never** the neutral text colour.
- Never outline it, gradient it, rotate it, or place it on a photograph without a solid backing
  shape.
- Use the reduced mark only where the full wordmark will not fit — favicons, avatars, small
  square placements.

## Favicon

**The favicon is the portrait, not the mark** — see brand guide §3.2. At 16px the `/.` reads as
a smudge, and the face is already the recognisable element across the platform. The icon set
lives in `../favicon/`, generated from `../profile-picture/`.

The reduced mark is still the answer for in-product square placements where a photograph would
be wrong. If one is ever needed against browser chrome, generate it from `mark-dark.svg`: the
bright stop holds up in both light and dark chrome, while the deep stop disappears into a dark
tab bar.

## Produced

These sit alongside this directory, under `docs/brand/`:

| Asset | Path |
| --- | --- |
| Favicon and app icons | `../favicon/` — the portrait: `.ico`, PNG 16/32/96, android 36–512, apple 57–180, ms-tile 70/150/310 |
| Web manifest | `../favicon/manifest.json`, `../favicon/browserconfig.xml` |
| LinkedIn banner | `../banners/linkedin.png`, 1584 × 396 |
| Open Graph image | `../og.png`, 1200 × 630 |

## Outlined lockups

`lockup-dark-outlined.svg` and `lockup-light-outlined.svg` are the off-platform versions —
Manrope converted to `<path>` data, so they render identically anywhere with no font to load.
The italic slash is a 14° synthetic oblique, matching what a browser generates from the live-text
version (Manrope ships no italic).

Send these to speaker packs, print vendors, and third-party sites. Keep using the CSS lockup on
our own surfaces, and the live-text SVGs where the file needs to stay small and the font is
loaded.

Both are generated from Manrope under the SIL Open Font License 1.1. Outlines are permitted; the
licence travels with the glyph shapes.

This repo is the only home for brand assets — consuming repos copy what they need (a favicon
into `public/`, the token sheet into their styles) rather than linking back to it.
