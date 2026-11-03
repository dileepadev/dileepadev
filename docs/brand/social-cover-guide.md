# Social cover guide

How to make a profile cover or banner for a social platform in the brand. The covers themselves
are not kept in this repository: they change with the platforms and with the work, so each one is
made, exported and uploaded when it is needed. The one exception is the animated cover at the top
of the profile README, [`github-readme.svg`](github-readme.svg), which belongs to this
repository and is rebuilt with `python3 docs/brand/github-readme.py`.

## Rules

- **Theme:** dark. The field is Carbon `#050505`; ink is `--fg` `#F1F1F1` for the handle and
  `--fg-muted` `#8D8D8D` for secondary text. No hue: colour is only ever a state.
- **Text:** the handle `@dileepadev` (the lockup from [`logo/`](logo/README.md), never
  retyped) and the domain `dileepa.dev` in JetBrains Mono. Nothing else is required.
- **No photograph and no name.** The platform already shows both beside the cover.
- **Brand parts only:** app-icon tiles, capsules, hairlines, Lucide icons and the dot grid, in the
  semantic palette from [`brand-tokens.css`](brand-tokens.css). Corners follow the
  fixed, capsule and concentric radius rules.
- **Voice:** sentence case and the banned-word list in `DESIGN.md` §17 apply to any copy.
- **Safe areas:** keep text and key artwork inside each platform's safe area (below). Avatars and
  mobile crops cover the rest, so let the dot grid run to the edges there.
- **Files:** export a PNG for upload and a JPG (quality around 90) for platforms that re-encode or
  cap file size. Never stretch artwork to fit a ratio; scale it and extend the background.

## Sizes

Upload sizes as the platforms state them at the time of writing. Check the platform's own help
page before exporting, because these change.

| Platform                  | Upload size | Keep content inside                                                   |
| ------------------------- | ----------- | --------------------------------------------------------------------- |
| LinkedIn profile          | 1584x396    | The right two-thirds; the profile photo covers the bottom-left        |
| X header                  | 1500x500    | The central band; the avatar overlaps the bottom-left on every screen |
| YouTube channel           | 2560x1440   | The central 1546x423, which is all a phone shows                      |
| Facebook page             | 1640x624    | The central area that desktop and mobile both keep, about 68% wide    |
| Reddit profile            | 1920x384    | Clear of the avatar on the left                                       |
| GitHub repository preview | 1280x640    | Everything; it is shown whole as a link card (40px margin all round)  |
| Twitch profile            | 1200x480    | The central band                                                      |
| Discord profile (Nitro)   | 600x240     | Clear of the avatar on the bottom-left; use larger type at this size  |

Link-preview cards for the website are not covers; they are [`og.png`](og.png) and
[`og2.png`](og2.png), exact copies of the website's.
