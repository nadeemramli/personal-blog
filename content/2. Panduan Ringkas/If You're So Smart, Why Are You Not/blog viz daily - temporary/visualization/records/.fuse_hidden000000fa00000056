---
draft: true
---
# Blog Viz Poster — 2026-06-02

**Date:** 2026-06-02
**Source brief:** `Visualization Concept — Healthy - Sleep Part 1.0 - The Architecture of Sleep.md`
(path: `…/blog viz daily - temporary/concepts/`) — the most recently modified concept (10:37), confirmed as today's freshest brief.
**Article:** Healthy pillar · Sleep track · **Part 1.0 — The Architecture of Sleep** (Part 1 of 5)

## Visual concept used
A **hypnogram drawn as the cross-section of a building at night** — the brief's non-negotiable hero object, rendered literally. The horizontal axis is TIME (LIGHTS OUT → WAKE, ~8 h with hour ticks); the vertical axis is DEPTH (AWAKE · REM · N1 · N2 · N3 DEEP on a left ruler). The sawtooth trace plunges into big N3 troughs in the first two cycles and shallows toward morning while the REM bands lengthen, so the night's **asymmetry** is obvious at a glance: warm **amber deep wedges crowd the left** (THE BODY · physical repair) and cool **violet REM ribbons stretch across the right** (THE BRAIN · cognitive repair). A left-to-right amber→violet under-curve gradient encodes the body→brain gradient before a word is read. The emotional payload sits as two red guillotine cuts — a solid right-hand cut with a hatched amputation zone (`WAKE EARLY → LOSE REM`) and a dashed left cut (`LATE TO BED → COMPRESS DEEP`) — beside the headline math `A 6-HOUR NIGHT ≠ 75% OF 8.` A two-room cutaway floorplan (THE BODY / THE BRAIN with their stage-specific jobs) is bolted under the curve, and the thesis lockup `YOU DON'T TAKE SLEEP. YOU BUILD IT.` closes the bottom. Style = the brief's proposed **"Clinical Nocturne"** — a sibling to the Fit pillar's Engineering Diagnostic Instrument style, same instrument-grade labeling and single-alarm-color (red) discipline, rendered after dark. Banned clichés (sleeping figure, moon, alarm clock, symmetric pie/stacked bars) all avoided.

**Palette (from §5 of the brief):** background ink `#0B0F1A`; body/deep amber `#E8A23D`; brain/REM violet `#8B7CF0`; text off-white `#E6E8EE` / slate `#A1A1AA`; the one alarm color, signal red `#FF5C5C`, reserved exclusively for the two cuts and the `6 ≠ 75%` math.

## Outputs
- SVG: `outputs/poster-2026-06-02-architecture-of-a-night.svg` (also copied to `…/blog viz daily - temporary/posters/`)
- PNG: `outputs/poster-2026-06-02-architecture-of-a-night.png` — 2400×3000, ~288 KB (also copied to the `posters/` folder for the downstream insert task)

## Renderer & verification
- **Renderer used: CairoSVG** (2× = 2400×3000). Playwright/Chromium and rsvg-convert were both unavailable in the sandbox (no apt/chromium); CairoSVG was installed via pip and used as the fallback.
- Verified: PNG is 2400×3000 as expected and ~288 KB (> 50 KB threshold); SVG parses as well-formed XML; layout/text visually inspected via a downscaled preview and corrected (label overflow, math box width, thesis sizing).
- **Font note:** CairoSVG has no Inter/JetBrains Mono and falls back to DejaVu Sans (wider metrics). Type sizes were tuned so all labels fit; on a Playwright/Inter render the layout would have slightly more breathing room.

## Deviations / notes
- **Headline:** used `A NIGHT HAS A SHAPE.` (the brief's "cleanest, most poster-like" option) with the provocation surfaced separately as the red math callout.
- **Two posters exist for today.** An earlier run (01:43) already produced `poster-2026-06-02-vo2-max-and-mitochondria` for Fit/Athletic Part 2.1 (the tracker's prior "next up") and its record `blog-viz-poster-2026-06-02.md`. This run targets the **newer** Sleep Part 1.0 brief (modified 10:37), so this record is filenamed with a slug suffix to avoid overwriting the earlier VO2 record.
- Path-reconciliation policy (from prior runs) still applies: the live workflow folder is `…/blog viz daily - temporary/`; the scheduled-task file's hard-coded `local_dbaa9cdd` outputs path is not mounted in run sessions, so outputs are saved to the session outputs folder and copied into the connected `posters/` folder.
