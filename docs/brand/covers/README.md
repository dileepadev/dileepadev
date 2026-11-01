# Social covers

Brand v2.1.0. The wide covers follow the completed site's flat split card: `@dileepadev`, the
name, `AI Engineer` and `dileepa.dev` beside the colour portrait. Type and framing are neutral.
The portrait is content, not an accent colour.

[`source-1584x396.svg`](source-1584x396.svg) is the wide master. Its type is filled paths from
Manrope 4.505 at weight 500 and JetBrains Mono 2.211 at weight 400. The portrait is embedded
from [`../profile-picture/v2.jpg`](../profile-picture/v2.jpg). Rendering needs neither an
installed font nor a network connection. The `data-text` attributes identify each outlined line
for an editor; change text in a vector editor with those fonts, then convert it back to paths.

## Exports

Every target has an SVG, PNG and JPG. Use PNG for uploads. The wide artwork scales uniformly and
is centred on Carbon (`#050505`); it is never stretched. The surrounding space changes to fit
each platform.

| File stem | Size | Use | Scale of wide master |
| --- | --- | --- | --- |
| `linkedin-cover` | 1584 × 396 | LinkedIn profile | 1 |
| `reddit-banner` | 1920 × 384 | Reddit profile | 384 / 396 |
| `x-header` | 1500 × 500 | X profile; this repository's profile README | 0.91 |
| `youtube-banner` | 2560 × 1440 | YouTube channel | 1546 / 1584 |
| `facebook-cover` | 1640 × 624 | Facebook page | 0.98 |
| `github-social` | 1280 × 640 | Repository social preview | 0.76 |
| `twitch-banner` | 1200 × 480 | Twitch profile | 0.72 |
| `discord-banner` | 600 × 240 | Discord profile | 0.36 |
| `og` | 1200 × 630 | Standard social card | Approved website PNG, unchanged |
| `og-wide` | 1600 × 900 | 16:9 social card | Approved website PNG, unchanged |

**YouTube:** the whole artwork fits inside the central 1546 × 423 safe area, at
`x = 507..2053`, `y = 508.5..931.5`. Only that centre is guaranteed to survive a phone crop.

**Discord:** the smallest type in the wide source is 38px. At 0.36 it becomes 13.68px; the
handle is 14.4px and the name is 31.68px. There is no miniature code block to become illegible.

`x-header-animated.svg` is retained as a **static compatibility copy** of `x-header.svg`.
The profile README uses `x-header.png`. No cover contains a looping animation.

`../banners/linkedin.png` is a byte-identical copy of `linkedin-cover.png`.

## Approved OG cards

`og.png` and `og-wide.png` were copied unchanged from `dileepa-dev/public/og.png` and
`dileepa-dev/public/og2.png` at commit `d5fb116`. `../og.png` is identical to `og.png`.
Their SVG counterparts are lossless wrappers around those approved raster files, not editable
vector masters. This preserves the approved cards exactly rather than drawing a second version.
The JPGs are upload alternatives.

The intended per-record card follows the same flat split design, with the record title and
metadata in place of the profile name. **The current `dileepa-dev/lib/og/card.tsx` still draws a
terminal window.** That mismatch is tracked in the platform [roadmap](../../../TODO.md); this
asset release does not claim that component already matches.

## Regenerating

Edit the wide master first. This optional export command refreshes each SVG wrapper from the
master and renders the raster files. It adds no manifest, dependency tree or build step to this
repository. Run from the repository root with `uv` available; the temporary environment supplies
CairoSVG and Pillow. CairoSVG also needs the system Cairo library.

```bash
uv run --no-project --with cairosvg --with pillow python - <<'PY'
import base64
import copy
import shutil
from pathlib import Path
import xml.etree.ElementTree as ET
import cairosvg
from PIL import Image

ns = "http://www.w3.org/2000/svg"
ET.register_namespace("", ns)
folder = Path("docs/brand/covers")
source = ET.parse(folder / "source-1584x396.svg").getroot()
variants = {
    "linkedin-cover": (1584, 396, 1),
    "reddit-banner": (1920, 384, 384 / 396),
    "x-header": (1500, 500, 0.91),
    "youtube-banner": (2560, 1440, 1546 / 1584),
    "facebook-cover": (1640, 624, 0.98),
    "github-social": (1280, 640, 0.76),
    "twitch-banner": (1200, 480, 0.72),
    "discord-banner": (600, 240, 0.36),
}
for stem, (width, height, scale) in variants.items():
    path = folder / f"{stem}.svg"
    root = ET.parse(path).getroot()
    root.remove(root.find(f"{{{ns}}}svg"))
    artwork = copy.deepcopy(source)
    artwork.attrib.pop("role", None)
    artwork.attrib.pop("aria-labelledby", None)
    for node in list(artwork):
        if node.tag in (f"{{{ns}}}title", f"{{{ns}}}desc"):
            artwork.remove(node)
    artwork.set("x", str((width - 1584 * scale) / 2))
    artwork.set("y", str((height - 396 * scale) / 2))
    artwork.set("width", str(1584 * scale))
    artwork.set("height", str(396 * scale))
    root.append(artwork)
    path.write_text(ET.tostring(root, encoding="unicode") + "\n")
    cairosvg.svg2png(url=str(path), write_to=str(path.with_suffix(".png")))
for stem in (*variants, "og", "og-wide"):
    path = folder / f"{stem}.png"
    Image.open(path).convert("RGB").save(path.with_suffix(".jpg"), quality=95, subsampling=0)
for stem in ("og", "og-wide"):
    path = folder / f"{stem}.png"
    root = ET.parse(folder / f"{stem}.svg").getroot()
    root.find(f"{{{ns}}}image").set("href", "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode())
    (folder / f"{stem}.svg").write_text(ET.tostring(root, encoding="unicode") + "\n")
shutil.copyfile(folder / "linkedin-cover.png", folder.parent / "banners/linkedin.png")
shutil.copyfile(folder / "x-header.svg", folder / "x-header-animated.svg")
shutil.copyfile(folder / "og.png", folder.parent / "og.png")
PY
```

If an approved website card changes, copy the new PNG into `og.png` or `og-wide.png` here before
running the command. Confirm every export's dimensions and view the YouTube safe-area crop and
Discord card at actual size.
