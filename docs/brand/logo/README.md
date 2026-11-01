# Logo assets

The logo is the handle, **`@dileepadev`** — the `@` one step muted (`--fg-muted`), the wordmark
at full contrast (`--fg`), both Manrope 500, set as one word with no gap. Black and white only.
Full specification in [`../brand-guide.md`](../brand-guide.md) §3.

> [!WARNING]
> **The files in this directory are out of date.** None of the SVGs here draw the current
> `@dileepadev` lockup. Do not hand them out or copy them into a site until they are
> redrawn. The table below is the redraw brief.

| File | Surface | `@` | Wordmark | State |
| --- | --- | --- | --- | --- |
| `lockup-dark.svg` | Carbon `#050505` | `ink-400` `#8D8D8D` | `ink-100` `#F1F1F1` | Stale - redraw |
| `lockup-light.svg` | Paper `#F7F7F7` | `paper-400` `#6A6A6A` | `paper-900` `#131313` | Stale - redraw |
| `lockup-dark-outlined.svg` | Carbon | as above | as above | Stale - redraw as paths |
| `lockup-light-outlined.svg` | Paper | as above | as above | Stale - redraw as paths |
| `mark-dark.svg` | Carbon | `ink-100` `#F1F1F1` | - | Stale - the reduced mark is now `@` |
| `mark-light.svg` | Paper | `paper-900` `#131313` | - | Stale - the reduced mark is now `@` |

The reduced mark is the `@` alone, at full contrast (it has no wordmark to step down from).
Upright, weight 500 - no italic, no oblique.

## Live text, not outlines

The live-text SVGs use `<text>` with a Manrope font stack. On a surface where Manrope is loaded
they render exactly right and stay a few hundred bytes. Anywhere the font is missing they fall
back to `system-ui`, and the wordmark's proportions go with it.

**Before sending the logo anywhere off-platform** — a conference speaker pack, a print vendor, a
third-party site — use the outlined version (Manrope converted to `<path>`, no font to load).
Manrope is under the SIL Open Font License 1.1; outlines are permitted.

Inside our own applications, prefer the CSS lockup over these files: it inherits the theme and
needs no light/dark file swap.

```html
<a class="lockup" href="/" aria-label="dileepadev - home">
  <span class="mark" aria-hidden="true">@</span><span class="wordmark">dileepadev</span>
</a>
```

`.lockup`, `.mark` and `.wordmark` are defined in [`../brand-tokens.css`](../brand-tokens.css).
The `@` is decorative to a screen reader — the accessible name comes from the link's
`aria-label`. `dileepa-dev` renders it from `components/ui/Lockup.tsx`.

## Rules

- Minimum width **120px** for the lockup.
- Clear space equal to the wordmark's cap-height on all four sides.
- The `@` is always the muted step; the wordmark is always full contrast. Never the reverse,
  never one colour for both, never a hue.
- Never outline it (as a stroke), gradient it, rotate it, or place it on a photograph without a
  solid backing shape.
- Use the reduced `@` only where the full handle will not fit — avatars, small square placements.

## Favicon

**The favicon is the portrait, not the mark** — see brand guide §3.2. The face is the
recognisable element across the platform. The icon set lives in `../favicon/`, generated from
`../profile-picture/`, and is current.

## Other assets

| Asset | Path | State |
| --- | --- | --- |
| Favicon and app icons | `../favicon/` | Current (the portrait) |
| Profile pictures | `../profile-picture/` | Current |
| Social covers | `../covers/` | Out of date - see its README |
| LinkedIn banner | `../banners/linkedin.png` | Stale |
| Open Graph image | `../og.png`, 1200 × 630 | Current |
| Pillar icons | `../icons/` | Out of date; unused by any surface |

This repo is the only home for brand assets — consuming repos copy what they need (a favicon
into `public/`, the token sheet into their styles) rather than linking back to it.
