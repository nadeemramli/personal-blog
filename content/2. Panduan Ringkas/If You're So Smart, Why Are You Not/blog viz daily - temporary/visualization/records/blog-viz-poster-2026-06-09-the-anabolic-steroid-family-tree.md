---
date: 2026-06-09
pillar: Fit
track: Performance Enhancement
part: 3.1
title: The Anabolic Steroid Family Tree
renderer: CairoSVG
---

# Blog Viz Poster — 2026-06-09 — Fit / Performance Enhancement Part 3.1: The Anabolic Steroid Family Tree

- **Date:** 2026-06-09
- **Source brief:** `concepts/Visualization Concept — Fit - Part 3.1 (Performance Enhancement) - The Anabolic Steroid Family Tree.md`
  (in the blog folder `2. Panduan Ringkas/If You're So Smart, Why Are You Not/blog viz daily - temporary/`)
- **Article:** If You're So Smart, Why Are You Not → **Fit** pillar, **Performance Enhancement** track, **Part 3.1 of 5** — the middle article of the "Optimize" sub-arc (3.0 pathways → **3.1 families** → 3.2 cycle design). Fifth PE-track poster (5 of 15), the natural visual sibling to 3.0.

## Visual concept used

Implemented the brief's hero device verbatim: a **derivation / parts-genealogy tree drawn over a shared OUTPUT DATUM**. The load-bearing object is a single **bold white horizontal rail** (`NITROGEN RETAINED ≈ 60–75 g LBM / day — ROUGHLY EQUAL ACROSS ALL THREE FAMILIES`) cutting the full panel width in the lower-middle, with the caption `Same muscle. The difference is everything above this line.` **Every family lane connects down to this rail at the same height** via a bold colour-coded drop-line + node, so "the muscle built is comparable" reads pre-attentively.

Above the datum stand **three family racks** in left→right learning-ladder order — **TESTOSTERONE FAMILY** (green), **DHT FAMILY** (blue), **19-NOR / NANDROLONE FAMILY** (amber) — each a rack of engineering part cards. The **divergence is encoded as a side-effect "plume" rising above each rack**: plume height + density = side-effect cost, so the **19-nor plume is tallest and densest**, the **DHT plume shortest and sparsest** ("‘weak’ = few sides"), Test medium. This survives grayscale (position/height carry the meaning, not just hue).

Teaching beats implemented:
- **BASE / ANCHOR badge** — a distinct repeated green glyph on exactly four cards (Testosterone, Boldenone/EQ, Dianabol, Trestolone/MENT) and nowhere else.
- **Three misfit cards, filed in the wrong drawer** — Halotestin* & Turinabol* sit in the Test lane wearing DHT-blue cross-tags; Anadrol* sits in the DHT lane wearing a 19-nor-amber tag; Trestolone* sits in the 19-nor lane wearing a Test-green tag (+ BASE badge). Each carries a thin dashed **cross-link arrow** to the family it actually behaves like, plus the legend `* behaves UNLIKE its family — the family is a strong default, not a law.`
- **The single RED object** — the **SUPPRESSION INTERLOCK** latched across the top of the 19-nor crown (`MOST SUPPRESSIVE FAMILY OF THE TREE` / `ONE NANDROLONE SHOT = MONTHS OF HPTA SHUTDOWN` / `Reserve 19-nors until you've accepted blast-and-cruise (→ Part 1, The Decision).`). Everything else cautionary stays amber.
- **Root + transform-valves** — a `TESTOSTERONE` parent node below the datum, with three branches fanning up through labelled valves (`↳ direct → TEST`, `↳ 5α-REDUCTION → DHT`, `↳ 19-DEMETHYLATION → 19-nor`), making derivation structural rather than captioned.
- **Climb-order rail** down the right edge (rung 1 MASTER TESTOSTERONE at the bottom → 2 ADD DHT DERIVATIVES → 3 REACH FOR 19-NORS LAST at the top, with `exhaust before ascending` gate glyphs), so the tree's height = the order of use and the red crown sits at the top of the climb.
- **Two-maps chip** (`3.0 = WHAT IT DOES (pathways) · 3.1 = WHAT TO EXPECT (family)` / law `THE FAMILY PREDICTS — THE PATHWAY EXPLAINS`) and a **footer family→pathway bridge** tying the lineage map back to 3.0's mechanism console.

Headline: `Same muscle. Wildly different rent.` (brief §4 verbatim).

## Style
Locked Fit **"Engineering Diagnostic Instrument"** language carried over from the prior PE posters: dark instrument ground `#0A0A0C`, hairline grid, JetBrains-Mono technical labels + tick-marks, Inter display for the headline, status-indicator colour logic (green = safe base, amber = caution/19-nor, **red rationed to exactly one object**). New sub-archetype within that language: a **derivation / parts-genealogy tree over a shared output datum** — distinct from 1.0's authorization console, 2.0's calibration bench, 2.1's telemetry strip-chart and 3.0's mixing console. Portrait `viewBox 1280×1648` (deliberate flip back to portrait after 3.0's landscape console — the climb reads as one upward column with the datum cutting across the lower-middle). No doses appear on any named anabolic (house rule); no potency ranking (the article exists to destroy "which is strongest?").

## §7 avoidances respected
- Not a botanical/pretty family tree — the **shared OUTPUT DATUM** is the hero and makes the equal-floor / unequal-ceiling split explicit.
- No "which is strongest?" ranking, podium, or potency bar chart — the three families read as **equal at the muscle line**, differing only in the cost-plume above it.
- Misfits are **not** footnotes — they visibly sit in one lane wearing another family's tag with a cross-link arrow.
- Red is **one object only** (the 19-nor suppression interlock); progestogenic/misfit warnings are amber. No doses on named anabolics.

## Outputs
- **Poster PNG:** `visualization/Poster — Fit - Part 3.1 (Performance Enhancement) - The Anabolic Steroid Family Tree.png`
- **Raw SVG:** `visualization/Poster — Fit - Part 3.1 (Performance Enhancement) - The Anabolic Steroid Family Tree.svg`
- No prior poster existed for this concept → no deletes.

## Renderer & verification
Renderer = **CairoSVG @2×** (rsvg/librsvg and Playwright unavailable in the sandbox; cairosvg pip-installed with `--break-system-packages`). Output **2560×3296 px, ~486 KB** (> 50 KB and matches the 1280×1648 viewBox at 2×). Read back the full PNG and inspected: datum reads as the dominant horizontal, three plumes clearly differentiated (19-nor tallest/densest, DHT cleanest), four BASE badges and three cross-tagged misfits with arrows present, single red crown legible. One revision pass after first render: shrank canvas/panel to remove ~110 px of bottom dead space and strengthened plume stroke/opacity so the cost-divergence reads. Fonts fall back to the sandbox default (no Inter/JetBrains installed locally), but the SVG references the correct Inter / JetBrains-Mono stacks for rendering where the fonts exist.

## Notes / deviations
- The brief logs the article as "Part 3.1 of 5"; the kicker uses the PE-track running count `article 5 of 15` consistent with the prior PE posters' tier labelling.
- Light house-style touch: converted the subhead's prose em-dash to a comma/colon per Nadeem's standing preference (em-dashes kept only in label/group-label strings such as the datum plate).
