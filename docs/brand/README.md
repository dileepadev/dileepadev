# Brand assets

The platform's brand, **design system v2.1.0**: a black-and-white system in which the accent is
the text colour, the logo is the handle `@dileepadev`, and colour appears only to report a state.

Two kinds of file live here. **Imported** files are exact copies from the website, which is where
the design was built and settled. **Drawn here** files are the logo, the pillar icons and the social
covers; each has a generator, so it can be rebuilt rather than edited by hand.

## Imported from the website

Source: [`dileepadev/dileepa-dev`](https://github.com/dileepadev/dileepa-dev), tag
[`v2.1.0`](https://github.com/dileepadev/dileepa-dev/releases/tag/v2.1.0), commit
[`7c484f3ee5cdce19b5b583aae781f0487b510c79`](https://github.com/dileepadev/dileepa-dev/commit/7c484f3ee5cdce19b5b583aae781f0487b510c79).
Imported on 2026-11-02. Each file is byte-for-byte identical to its source; nothing was fixed,
reformatted or re-valued in the copy.

| Source in `dileepa-dev`                                                                | Here                                     | What                                                     |
| -------------------------------------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------- |
| `docs/brand-guide.md`                                                                  | [`brand-guide.md`](brand-guide.md)       | Colour, type, logo, voice, portrait                      |
| `docs/design-system.md`                                                                | [`design-system.md`](design-system.md)   | The component and token contract                         |
| `docs/brand-tokens.css`                                                                | [`brand-tokens.css`](brand-tokens.css)   | The canonical token sheet; applications vendor it        |
| `DESIGN.md`                                                                            | [`../../DESIGN.md`](../../DESIGN.md)     | The agent-facing synthesis, with machine-readable tokens |
| `public/og.png`, `public/og2.png`                                                      | [`og.png`](og.png), [`og2.png`](og2.png) | The link-preview cards, 1200×630 and 1600×900            |
| `app/favicon.ico`, the favicon and app-icon PNGs, `manifest.json`, `browserconfig.xml` | [`favicon/`](favicon/)                   | The portrait as every icon, and the web-app manifest     |
| `public/profile/*`                                                                     | [`profile-picture/`](profile-picture/)   | The portrait: JPG, PNG, WebP and a transparent PNG       |

Verify all 38 files from the repository root:

```sh
sha256sum -c docs/brand/SHA256SUMS
```

`DESIGN.md` is copied exactly, so its relative links to `docs/brand-guide.md`, `docs/brand-tokens.css`,
`docs/design-system.md`, `public/og.png` and `public/og2.png` follow the website's layout. Here those
files are under `docs/brand/`.

The site's runtime sheet, `app/brand-tokens.css`, adds a vendor header and drops the Google Fonts
import because `next/font` supplies the faces; it is not copied here. `brand-tokens.css` above is the
full canonical sheet, and applications vendor it from this repository's tag.

## Drawn here

| Folder                        | What                                                                               | Rebuild                               |
| ----------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------- |
| [`logo/`](logo/README.md)     | The `@dileepadev` lockup, live-text and outlined, and the `@` mark, in both themes | `python3 docs/brand/logo/generate.py` |
| [`icons/`](icons/README.md)   | The six pillar marks: symbol, standalone, badge and PNGs                           | `node docs/brand/icons/generate.mjs`  |
| [`covers/`](covers/README.md) | The social covers for eight platforms                                              | `node docs/brand/covers/generate.mjs` |

All three use the semantic palette from `brand-tokens.css`, and none carries a hue. Each folder's
README lists what its generator needs.

## The decision

Issue [#4](https://github.com/dileepadev/dileepadev/issues/4) chose **option B**: change a brand
rule and adopt the website's completed monochrome design, rather than refine the emerald system.
The owner keeps the brand and `DESIGN.md` at **2.1.0**, so the issue's proposed correction to 2.0.0
is cancelled. The imported design-system document is not edited to record this; this README and
issue #4 do.

## Updating

When the website ships a new tag, copy the files in the table above from it, regenerate the
checksums, and update the commit and date here. Do not edit an imported file in place. Then
publish this repository's tag, and have each application re-vendor `brand-tokens.css` from it.
Release progress is tracked in issue #4, not in a file.
