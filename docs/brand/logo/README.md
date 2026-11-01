# Logo assets

Brand v2.1.0. The logo is **`@dileepadev`**: the `@` in `--fg-muted`, the wordmark in `--fg`,
both Manrope Medium (500), with no gap and `-0.02em` tracking. The full contract is in
[`../brand-guide.md`](../brand-guide.md) §3.

| File | Placement | `@` | Wordmark | Font dependency |
| --- | --- | --- | --- | --- |
| [`lockup-dark.svg`](lockup-dark.svg) | Carbon | `#8D8D8D` | `#F1F1F1` | Manrope 500 |
| [`lockup-light.svg`](lockup-light.svg) | Paper | `#6A6A6A` | `#131313` | Manrope 500 |
| [`lockup-dark-outlined.svg`](lockup-dark-outlined.svg) | Carbon | `#8D8D8D` | `#F1F1F1` | None; filled paths |
| [`lockup-light-outlined.svg`](lockup-light-outlined.svg) | Paper | `#6A6A6A` | `#131313` | None; filled paths |
| [`mark-dark.svg`](mark-dark.svg) | Carbon field | `#F1F1F1` | — | None; filled paths |
| [`mark-light.svg`](mark-light.svg) | Paper field | `#131313` | — | None; filled paths |

The lockups have a transparent background and include 24px of clear space around the type at
the native size, approximately its cap height. They share a 235 × 80 viewBox. The reduced marks
are 48 × 48, with the `@` centred on a solid field. They are upright, weight 500.

## Which file to use

Use an outlined version for a speaker pack, print vendor, third-party page, or any image context
where Manrope cannot be guaranteed. The glyphs are converted from Manrope 4.505 at weight 500;
no font is embedded and no network request is needed. “Outlined” means filled glyph paths,
never a stroke around the letters.

Live-text SVGs are for an inline context where Manrope is loaded. A surrounding page's font does
not automatically load inside an SVG used through an `<img>`, so use the outlined file there
too. The fallback keeps the words readable, but changes their proportions.

Inside an application, prefer the CSS lockup so its semantic colours follow the theme:

```html
<a class="lockup" href="/" aria-label="dileepadev - home">
  <span class="mark" aria-hidden="true">@</span><span class="wordmark">dileepadev</span>
</a>
```

Those classes are defined in [`../brand-tokens.css`](../brand-tokens.css).

## Rules

- Minimum width: 120px for the full lockup, keeping the `@` legible.
- Clear space: at least the wordmark's cap height on every side, including after scaling.
- The `@` is muted when it leads the wordmark. The reduced `@` is full contrast because it has
  no wordmark beside it.
- Keep the handle lowercase, upright, at weight 500. No hue, gradient, shadow, rotation, or
  outline stroke. A photograph behind it needs a solid backing field.

## Favicon

The favicon and app icons are the portrait, not the reduced mark. The current set is in
[`../favicon/`](../favicon/), derived from [`../profile-picture/`](../profile-picture/).

## Other assets

| Asset | Source |
| --- | --- |
| Social covers and their exports | [`../covers/README.md`](../covers/README.md) |
| LinkedIn banner | [`../banners/linkedin.png`](../banners/linkedin.png), identical to the cover export |
| Standard OG card | [`../og.png`](../og.png), 1200 × 630 |
| Wide OG card | [`../covers/og-wide.png`](../covers/og-wide.png), 1600 × 900 |
| Retained neutral pillar marks | [`../icons/README.md`](../icons/README.md) |

This repository is the canonical home. Consuming applications copy the assets they need and
record the source tag; they do not link back to a runtime asset host.
