#!/usr/bin/env python3
"""github-readme.svg: the animated cover at the top of the profile README. Dark theme, brand v2.1.0.

    python3 docs/brand/github-readme.py

Needs: `pip install fonttools uharfbuzz`; Node and the site checked out beside this repo
(../dileepa-dev, with `npm install` run) for the Lucide icon data; Manrope and JetBrains Mono
installed as variable fonts.

Left: the lockup, "AI Engineer", "I develop" and a phrase that types itself a letter at a time,
with a caret that slides to each new letter, stays solid while it moves and blinks while it
waits; the line under it says what that part of the role involves. Right: a website chip and the
six pillars of the role, the lit one following the phrase. Text is outlined and the animation is
CSS only. Letters fade in on their own (no clip-path or mask is animated), and every change is
eased, so nothing snaps.
"""
import json
import pathlib
import subprocess

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[1]
SITE = ROOT.parent / "dileepa-dev"
OUT = HERE / "github-readme.svg"
T = dict(bg="#050505", surface="#0d0d0d", raised="#141414", rule="#1f1f1f", edge="#2e2e2e",
         input="#5b5b5b", body="#a8a8a8", muted="#8d8d8d", fg="#f1f1f1")
W, H = 1500, 540

# phrase, tile label, icon, what that part of the role involves
ROLE = [
    ("agentic AI systems.", "agents", "bot", "Agents that plan, call tools and finish multi-step tasks."),
    ("LLM applications.", "LLM apps", "sparkles", "Context design, structured outputs and streaming."),
    ("RAG pipelines.", "retrieval", "database", "Chunking, embeddings, hybrid search and reranking."),
    ("MCP servers and tools.", "MCP", "plug", "Tools agents can use, with permissions and approvals."),
    ("eval suites.", "evals", "flask-conical", "Golden datasets, LLM judges and regression tests."),
    ("production AI backends.", "production", "server", "Cloud services with tracing, guardrails and cost control."),
]
PERIOD = 5.0
LOOP = PERIOD * len(ROLE)
TYPE_AT, TYPE_STEP, LETTER_FADE = 0.55, 0.065, 0.09
HOLD_END, ERASE_STEP, ERASE_FADE = 3.9, 0.035, 0.06
EASE = "cubic-bezier(.4,0,.2,1)"

script = r"""
const fs=require('fs');const dir=process.argv[1]+'/node_modules/lucide-react/dist/esm/icons/';const out={};
for(const n of process.argv.slice(2)){const m=fs.readFileSync(dir+n+'.mjs','utf8').match(/const __iconNode = (\[[\s\S]*?\]);\s*\n/);
out[n]=new Function('return '+m[1])().map(([t,a])=>[t,Object.fromEntries(Object.entries(a).filter(([k])=>k!=='key'))]);}
console.log(JSON.stringify(out));"""
ICONS = json.loads(subprocess.run(["node", "-e", script, str(SITE), "globe", *[r[2] for r in ROLE]],
                                  capture_output=True, text=True, check=True).stdout)


def icon(name, x, y, size, color, sw=1.6):
    inner = "".join(f"<{t} " + " ".join(f'{k}="{v}"' for k, v in a.items()) + "/>" for t, a in ICONS[name])
    return (f'<g transform="translate({x - size / 2:.2f} {y - size / 2:.2f}) scale({size / 24:.4f})" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{inner}</g>')


class Face:
    def __init__(self, family, weight):
        path = subprocess.run(["fc-match", "-f", "%{file}", family], capture_output=True, text=True).stdout
        self.hb_font = hb.Font(hb.Face(hb.Blob.from_file_path(path)))
        self.hb_font.set_variations({"wght": weight})
        font = instancer.instantiateVariableFont(TTFont(path), {"wght": weight})
        self.upem, self.order, self.glyphs = font["head"].unitsPerEm, font.getGlyphOrder(), font.getGlyphSet()

    def _shape(self, s):
        buf = hb.Buffer()
        buf.add_str(s)
        buf.guess_segment_properties()
        hb.shape(self.hb_font, buf, {"kern": True, "liga": False})
        return buf

    def _glyph(self, info, pos, scale, x, y):
        pen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
        self.glyphs[self.order[info.codepoint]].draw(
            TransformPen(pen, (scale, 0, 0, -scale, x + pos.x_offset * scale, y - pos.y_offset * scale)))
        return pen.getCommands()

    def text(self, s, size, x, y, fill, track=0.0, anchor="start"):
        buf = self._shape(s)
        scale = size / self.upem
        total = sum(p.x_advance for p in buf.glyph_positions) * scale + track * size * (len(s) - 1)
        cursor = x - total / 2 if anchor == "middle" else x - total if anchor == "end" else x
        d = ""
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            d += self._glyph(info, pos, scale, cursor, y)
            cursor += pos.x_advance * scale + track * size
        return f'<path fill="{fill}" d="{d}"/>', total

    def letters(self, s, size, x, y, track=0.0):
        """One outline per character, and where each one ends: what the typing is built from."""
        buf = self._shape(s)
        scale = size / self.upem
        out, cursor = [], x
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            out.append(self._glyph(info, pos, scale, cursor, y))
            cursor += pos.x_advance * scale + track * size
        return out, cursor - x - track * size


MAN, MAN4 = Face("Manrope", 500), Face("Manrope", 400)
MONO = Face("JetBrains Mono", 500)


def pct(t):
    return f"{max(0.0, min(100.0, t / LOOP * 100)):.4f}%"


def kf(name, stops):
    """Keyframes from (seconds, declarations); times must rise, so any that do not are nudged."""
    body, last = "", -1.0
    for t, d in stops:
        t = max(t, last + 0.0004 * LOOP / 100)
        last = t
        body += f"{pct(t)}{{{d}}}"
    return f"@keyframes {name}{{{body}}}"


def window(cls, i, on, off, rest, lit, fade_in=0.4, fade_out=0.4, delay=0.0):
    """Lit while pillar i is on screen, eased in and out, then at rest for the rest of the loop."""
    a, b = i * PERIOD + on, i * PERIOD + off
    return (f".{cls}{{animation:{cls}k {LOOP}s linear infinite both}}"
            + kf(f"{cls}k", [(0, rest), (max(a - fade_in, 0.001), f"{rest};animation-timing-function:{EASE}"),
                             (a, lit), (b, f"{lit};animation-timing-function:{EASE}"), (b + fade_out, rest), (LOOP, rest)]))


CSS, parts = [], []
parts.append(f'<rect width="{W}" height="{H}" rx="32" fill="{T["bg"]}"/><rect width="{W}" height="{H}" rx="32" fill="url(#dots)" mask="url(#fade)"/>')
src = (ROOT / "docs/brand/logo/lockup-dark-outlined.svg").read_text()
paths = "".join(l.strip() for l in src.splitlines() if l.strip().startswith("<path"))
parts.append(f'<g transform="translate(62 38) scale(1.25)">{paths}</g><path d="M64 122H1436" stroke="{T["rule"]}" stroke-width="2"/>')

# top right: the website, with a website icon (the handle is already the logo, top left)
d_site, w_site = MONO.text("dileepa.dev", 24, 0, 0, T["fg"])
chip_w, chip_h = 12 + 44 + 14 + w_site + 14 + 24 + 22, 56
cx0, cy0 = 1436 - chip_w, 38
mx, my = cx0 + 12, cy0 + 6
ax = cx0 + chip_w - 22 - 24
parts.append(f'<rect x="{cx0}" y="{cy0}" width="{chip_w}" height="{chip_h}" rx="{chip_h / 2}" fill="{T["surface"]}" stroke="{T["edge"]}" stroke-width="2"/>'
             f'<circle class="halo" cx="{mx + 22}" cy="{my + 22}" r="22" fill="none" stroke="{T["fg"]}" stroke-width="2"/>'
             f'<circle cx="{mx + 22}" cy="{my + 22}" r="22" fill="{T["bg"]}" stroke="{T["edge"]}" stroke-width="2"/>'
             f'{icon("globe", mx + 22, my + 22, 24, T["fg"], 1.8)}'
             f'<g transform="translate({mx + 58} {cy0 + 37})">{d_site}</g>'
             f'<g class="nudge"><path d="M{ax + 6} {cy0 + 38}l12 -12M{ax + 8} {cy0 + 26}h10v10" fill="none" stroke="{T["body"]}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></g>')
CSS.append(".halo{transform-box:fill-box;transform-origin:center;animation:halo 3.2s ease-out infinite}"
           "@keyframes halo{0%{opacity:.7;transform:scale(1)}70%,100%{opacity:0;transform:scale(1.45)}}"
           f".nudge{{animation:nudge 3.2s {EASE} infinite}}"
           "@keyframes nudge{0%,55%,100%{transform:translate(0,0)}70%{transform:translate(3px,-3px)}85%{transform:translate(0,0)}}")

# left: role, I develop, the typed phrase
parts.append(MAN.text("AI Engineer", 28, 64, 196, T["muted"])[0])
parts.append(MAN.text("I develop", 58, 64, 278, T["fg"], track=-0.02)[0])
SIZE, BASE, X0 = 66, 370, 64
widest, first_end, first_n = 0, 0.0, 0
for i, (phrase, *_r) in enumerate(ROLE):
    glyphs, total = MAN.letters(phrase, SIZE, X0, BASE, track=-0.02)
    ends = []
    run = 0.0
    buf = MAN._shape(phrase)
    scale = SIZE / MAN.upem
    for pos in buf.glyph_positions:
        run += pos.x_advance * scale - 0.02 * SIZE
        ends.append(run)
    n = len(glyphs)
    widest = max(widest, total)
    if i == 0:
        first_end, first_n = ends[-1], n
    delay = i * PERIOD
    t_in = [TYPE_AT + TYPE_STEP * k for k in range(n)]
    t_out = [HOLD_END + ERASE_STEP * r for r in range(n)]        # r = how many letters have gone
    for k, d in enumerate(glyphs):
        if not d:
            continue
        erase = t_out[n - 1 - k]
        parts.append(f'<path class="g g{i}_{k}" fill="{T["fg"]}" d="{d}"/>')
        CSS.append(f".g{i}_{k}{{animation:g{i}_{k}k {LOOP}s linear {delay}s infinite both}}"
                   + kf(f"g{i}_{k}k", [(0, "opacity:0"), (t_in[k], "opacity:0"), (t_in[k] + LETTER_FADE, "opacity:1"),
                                       (erase, "opacity:1"), (erase + ERASE_FADE, "opacity:0"), (LOOP, "opacity:0")]))
    # the caret: it slides to each letter, is solid while it moves, blinks while it waits
    x = lambda k: f"transform:translateX({(ends[k] if k >= 0 else 0):.2f}px)"
    caret = [(0, "transform:translateX(0);opacity:0"), (0.01, "transform:translateX(0);opacity:1")]
    for k in range(n):
        caret += [(t_in[k], x(k - 1) + ";opacity:1"), (t_in[k] + 0.05, x(k) + ";opacity:1")]
    t = t_in[-1] + 0.4
    while t + 1.0 < HOLD_END - 0.1:
        caret += [(t, x(n - 1) + ";opacity:1"), (t + 0.45, x(n - 1) + ";opacity:1"), (t + 0.5, x(n - 1) + ";opacity:0"),
                  (t + 0.95, x(n - 1) + ";opacity:0"), (t + 1.0, x(n - 1) + ";opacity:1")]
        t += 1.0
    caret += [(HOLD_END - 0.05, x(n - 1) + ";opacity:1")]
    for r in range(n):
        caret += [(t_out[r], x(n - 1 - r) + ";opacity:1"), (t_out[r] + 0.03, x(n - 2 - r) + ";opacity:1")]
    caret += [(PERIOD + 0.05, "transform:translateX(0);opacity:1"), (PERIOD + 0.1, "transform:translateX(0);opacity:0"), (LOOP, "transform:translateX(0);opacity:0")]
    CSS.append(f".k{i}{{animation:caret{i} {LOOP}s linear {delay}s infinite both}}" + kf(f"caret{i}", caret))
    parts.append(f'<g transform="translate({X0} {BASE})"><g class="k k{i}"><rect x="3" y="-62" width="4" height="70" rx="2" fill="{T["fg"]}"/></g></g>')
    on, off = TYPE_AT, HOLD_END + 0.1
    CSS.append(window(f"a{i}", i, on, off, "opacity:0", "opacity:1"))
    CSS.append(window(f"l{i}", i, on, off, "transform:translateY(0)", "transform:translateY(-6px)"))
assert X0 + widest < 800, f"a phrase ends at {X0 + widest:.0f}px"

# the line under the phrase: what that part of the role involves
for i, row in enumerate(ROLE):
    t, w = MAN4.text(row[3], 28, 64, 440, T["body"])
    assert 64 + w < 830, f"detail line {i} is {w:.0f}px wide"
    parts.append(f'<g class="d d{i}">{t}</g>')
    CSS.append(window(f"d{i}", i, TYPE_AT + 0.7, HOLD_END, "opacity:0", "opacity:1", fade_in=0.5, fade_out=0.35))

# the six pillars
cols, rows = [926, 1146, 1366], [206, 386]
for i, (_, label, ic, _d) in enumerate(ROLE):
    cx, cy = cols[i % 3], rows[i // 3]
    s, r = 112, 112 * 0.27
    base = (f'<rect x="{cx - s / 2}" y="{cy - s / 2}" width="{s}" height="{s}" rx="{r}" fill="url(#tg)" stroke="{T["edge"]}"/>'
            f'<rect x="{cx - s / 2 + 1}" y="{cy - s / 2 + 1}" width="{s - 2}" height="{s * .5}" rx="{r}" fill="url(#th)"/>'
            f'{icon(ic, cx, cy, s * 0.46, T["body"])}')
    lit = (f'<rect x="{cx - s / 2}" y="{cy - s / 2}" width="{s}" height="{s}" rx="{r}" fill="url(#tg)" stroke="{T["body"]}" stroke-width="1.5"/>'
           f'<rect x="{cx - s / 2 - 6}" y="{cy - s / 2 - 6}" width="{s + 12}" height="{s + 12}" rx="{r + 5}" fill="none" stroke="{T["fg"]}" stroke-dasharray="3 4" opacity=".7"/>'
           f'{icon(ic, cx, cy, s * 0.46, T["fg"], 1.8)}')
    ly = cy + s / 2 + 38
    parts.append(f'<g class="l{i}">{base}{MONO.text(label, 24, cx, ly, T["muted"], anchor="middle")[0]}'
                 f'<g class="a a{i}">{lit}{MONO.text(label, 24, cx, ly, T["fg"], anchor="middle")[0]}</g></g>')

style = f"""
    {"".join(CSS)}
    @media (prefers-reduced-motion:reduce){{
      *{{animation:none!important}}
      .g{{opacity:0}} {" ".join(f".g0_{k}{{opacity:1}}" for k in range(first_n))}
      .k{{opacity:0}} .k0{{opacity:1;transform:translateX({first_end:.2f}px)}}
      .a,.d{{opacity:0}} .a0,.d0{{opacity:1}} .l0{{transform:translateY(-6px)}} .halo{{opacity:0}}
    }}
"""
desc = ("The @dileepadev lockup, AI Engineer, and the line I develop followed by "
        + ", ".join(r[0].rstrip(".") for r in ROLE) + ", typed one at a time with a line under each saying what it involves. "
        "On the right, a link to dileepa.dev and six pillars for " + ", ".join(r[1] for r in ROLE)
        + ", each lit while its phrase is on screen.")
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
  <title id="t">@dileepadev - AI engineer</title>
  <desc id="d">{desc}</desc>
  <!-- Generated by docs/brand/github-readme.py. Text is outlined; the animation is CSS only. Manrope and JetBrains Mono are SIL OFL 1.1. -->
  <defs>
    <linearGradient id="tg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#232323"/><stop offset="1" stop-color="#101010"/></linearGradient>
    <linearGradient id="th" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="14" cy="14" r="1.2" fill="{T["rule"]}"/></pattern>
    <linearGradient id="fg2" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".2"/><stop offset=".55" stop-color="#fff"/></linearGradient>
    <mask id="fade"><rect width="{W}" height="{H}" fill="url(#fg2)"/></mask>
    <style>{style}</style>
  </defs>
  {chr(10).join("  " + p for p in parts)}
</svg>
"""
OUT.write_text(svg)
print(f"wrote {OUT.name} ({len(svg) / 1024:.0f} KB), widest phrase {widest:.0f}px")
