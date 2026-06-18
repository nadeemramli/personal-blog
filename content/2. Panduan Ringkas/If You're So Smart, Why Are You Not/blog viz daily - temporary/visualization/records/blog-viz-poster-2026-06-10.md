---
title: "Blog Viz Poster Record — 2026-06-10"
date: 2026-06-10
---
# Blog Viz Poster — 2026-06-10

- **Source brief:** `concepts/Visualization Concept — Fit - Part 3.2 (Performance Enhancement) - Cycle Design.md`
- **Article:** Fit pillar → Performance Enhancement track → **Part 3.2 — Cycle Design** (closes the 3-part "Optimize" sub-arc: 3.0 mechanism → 3.1 lineage → 3.2 time)
- **Style:** Engineering Diagnostic Instrument (locked, Fit pillar)
- **Sub-archetype:** **Annual Operating Schedule / forward mission-plan** — landscape Gantt with a body-fat gate trace. New within the PE set (after 1.0 authorization console, 2.0 calibration bench, 2.1 telemetry strip-chart, 3.0 mixing console, 3.1 derivation tree).

## Visual concept used

A landscape (1680×1060) annual operating schedule. A single bold horizontal **year axis** (Month 0 → Month 12, M3/M6/M9/M12 majors) carries two vertically-aligned coupled lanes. The **PHARMACOLOGY lane** (above) runs the four-phase loop at honest proportional widths — PREP (1 mo, narrow) → BLAST off-season (the long "ON" ~8 mo, widest, violet gradient with an amber "→ calculated unhealthiness = cue to CRUISE" cue) → CUT (dry compounds) → **CRUISE/DOWN-PERIOD drawn as a TRUE ~quarter** (3.5 mo) with a ghosted amber-dashed "4-wk token break ≠ recovery" stub beside it to make "clearing ≠ restoring" a length difference. The **FOOD lane** (below) shows lean-bulk ~75% / cut ~20% / maintenance ~5% with an 8-week continuation check and refeed ticks; a coupling note ("food is the lever you pull most — drug lever only when extra food turns to FAT") sits between the lanes.

The **load-bearing device** is the body-fat gate trace threaded across the top: a continuous line caged between a green 8–12% push band and a hard red ~15% ceiling. The single red object on the poster is the trace **breaching the ceiling into the MICHELIN-MAN zone**, with a green dashed pull-back arrow dragging it back under the line ("cut at ~15–17%"). A green dashed **return-arrow loop** closes the cycle beneath the food lane ("push to calculated unhealthiness → pull all the way back → repeat").

Docked right: the **adjustment ladder** (read bottom→top, drugs LAST, crowned "MILK THE DOSE"), the **q3-month blood-checkpoint plate** (Cystatin C / ALT-AST 7-day rule / thyroid triad / SHBG / prolactin+cortisol, with the "a marker deviates → the cycle bends or stops" law), a **wet/dry tuning dial** grace-note, and the **80% retention** chip. Three-state color discipline: green gate band, one red breach, amber for every other caution.

## Outputs

- SVG: `visualization/Poster — Fit - Part 3.2 (Performance Enhancement) - Cycle Design.svg`
- PNG: `visualization/Poster — Fit - Part 3.2 (Performance Enhancement) - Cycle Design.png`

## Render & verification

- **Renderer:** CairoSVG (rsvg-convert / Playwright unavailable in sandbox; CairoSVG installed via pip).
- **PNG:** 3360×2120 px (2× of the 1680×1060 viewBox), ~493 KB — passes the non-empty / >50 KB / correct-dimension checks.
- Visually inspected full poster + zoomed crops (trace band, lane region, right dock). Fixed in iteration: title/subtitle overlap on the trace band, a redundant truncated "coupling" stub, repeated gate-note overlap in the ladder, and excess bottom whitespace (panel height tightened).

## Deviations / notes

- No prior poster existed for this concept → clean write, no delete needed.
- Landscape orientation per the brief (year axis is horizontal); distinct from 2.1's landscape strip-chart by being a planned segmented Gantt, not a recorded signal.
- Path-reconciliation policy holds: the scheduled-task file's hard-coded `local_dbaa9cdd` outputs path is unreachable from the run session; the connected `blog viz daily - temporary/` folder is the source of truth.
