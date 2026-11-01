# Pillar marks

Brand v2.1.0. These six marks are retained from the former About cards. The current site uses
Lucide for its section icons; these assets are a separate set, available when a pillar mark is
needed. Their geometry is unchanged and their exports now use neutral ink.

| Mark | Plain SVG | Badge SVG | Inline symbol | PNG | Badge PNG |
| --- | --- | --- | --- | --- | --- |
| AI engineering | [SVG](ai-engineering.svg) | [SVG](ai-engineering-badge.svg) | [SVG](ai-engineering-symbol.svg) | [PNG](ai-engineering.png) | [PNG](ai-engineering-badge.png) |
| Open source | [SVG](open-source.svg) | [SVG](open-source-badge.svg) | [SVG](open-source-symbol.svg) | [PNG](open-source.png) | [PNG](open-source-badge.png) |
| Public speaking | [SVG](public-speaking.svg) | [SVG](public-speaking-badge.svg) | [SVG](public-speaking-symbol.svg) | [PNG](public-speaking.png) | [PNG](public-speaking-badge.png) |
| Technical writing | [SVG](technical-writing.svg) | [SVG](technical-writing-badge.svg) | [SVG](technical-writing-symbol.svg) | [PNG](technical-writing.png) | [PNG](technical-writing-badge.png) |
| Technical videos | [SVG](technical-videos.svg) | [SVG](technical-videos-badge.svg) | [SVG](technical-videos-symbol.svg) | [PNG](technical-videos.png) | [PNG](technical-videos-badge.png) |
| Community building | [SVG](community-building.svg) | [SVG](community-building-badge.svg) | [SVG](community-building-symbol.svg) | [PNG](community-building.png) | [PNG](community-building-badge.png) |

## Variants

- **Plain:** a 24 × 24 SVG, transparent, with Ink 100 (`#F1F1F1`) strokes. Use on Carbon.
- **Badge:** a 60 × 60 SVG with the same mark on a Carbon surface (`#0D0D0D`) and a neutral
  `#2E2E2E` perimeter. It is exported artwork, not an interactive badge component.
- **Symbol:** a 24 × 24 SVG using `currentColor` for every stroke and filled detail. Inline its
  shapes in an application and inherit a semantic colour; do not copy the fixed export colours
  into component styles. A standalone symbol takes the SVG renderer's default colour.
- **PNG:** 512 × 512 RGB, Ink 100 on Carbon (`#050505`). Both plain and badge variants are
  provided. These are fixed dark-surface exports; use the inline symbol for a theme-aware UI.

The former HTML preview catalogue is retired. This Markdown index replaces its duplicated
palette and embedded copies of the marks; the SVG files are the geometry sources.

## Regenerating PNGs

After changing a plain or badge SVG, render it at 512 × 512 with Carbon as the background.
For example, from the repository root, using an optional temporary export environment:

```bash
uv run --no-project --with cairosvg --with pillow python - <<'PY'
from pathlib import Path
import cairosvg
from PIL import Image

for path in Path("docs/brand/icons").glob("*.svg"):
    if path.stem.endswith("-symbol"):
        continue
    target = path.with_suffix(".png")
    cairosvg.svg2png(url=str(path), write_to=str(target),
                    output_width=512, output_height=512, background_color="#050505")
    Image.open(target).convert("RGB").save(target)
PY
```

The symbols retain `currentColor`; verify them on both Carbon and Paper before embedding them
in an application. Decorative instances use `aria-hidden="true"`, with the accessible name
supplied by the surrounding text or control.
