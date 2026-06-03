---
title: "Blog Viz Poster — 2026-06-02"
date: 2026-06-02
---
# Blog Viz Poster Record — 2026-06-02

- **Date:** 2026-06-02
- **Source brief:** `Visualization Concept — Fit - Part 2.1 - VO2 Max and Mitochondria.md`
  - Path: `…/blog viz daily - temporary/concepts/Visualization Concept — Fit - Part 2.1 - VO2 Max and Mitochondria.md` (modified 2026-06-02, most recent in folder)
  - Cross-checked against `blog-viz-tracker.md` in the same folder — Part 2.1 (Athletic track) is the latest logged entry. Confirmed.
- **Article:** Fit pillar → Athletic track → **Part 2.1 — VO2 Max & Mitochondria**
- **Style lock:** Engineering Diagnostic Instrument (Fit-series locked style). Sub-archetype: **P&ID of the oxygen delivery chain** — a control-room flow schematic with the Fick equation as the master bus and two wired protocol feeds.

## Visual concept used

A portrait (1200×1500, 4:5) process-and-instrumentation diagram of the aerobic engine. The Fick equation runs across the top as the master readout, colour-coded into its three terms: `HRmax` rendered LOCKED (desaturated, hatched dial, padlock glyph), and `SVmax` + `(a-vO₂ diff)` rendered as active/trainable. Below it, a left→right delivery pipeline — LUNGS → HEART → BLOOD → MUSCLE → MITOCHONDRIA — carries two illuminated "gain dials" as the visual anchors: the heart's STROKE VOLUME dial (the ceiling) and the muscle's a-vO₂ DIFFERENCE dial (the floor), both glowing in the single rationed active accent (teal). The locked HRmax dial sits beside them deliberately dimmed. An LV-chamber-expansion inset hangs off the heart; a PGC-1α biogenesis cascade chip terminates the chain at the mitochondria.

Beneath the pipeline, two protocol feeds physically wire UP into their respective organs — INTERVALS (4×4) into the heart's SV dial, ZONE 2 into the muscle's a-vO₂ dial — meeting at the centered `80/20 POLARIZED` junction. Four quieter auxiliary gauges fill the lower zone: the LACTATE-IS-FUEL myth strip (full width), then a 3-across row of RESPONDER SLOPE (genetics), AGE-DECLINE (central fades faster), and MORTALITY COMPOSITE (the sober amber gravity panel, Mandsager 2018). Footer carries the legend, sources, and the `Fit — Athletic` series mark.

Semantic colour was rationed to three states exactly as the brief required: teal = the two trainable gains + their feeds; desaturated grey = the locked HRmax term; sober amber = the mortality panel (gravity, not alarm). No rainbow plumbing, no anatomical heart/lungs illustration — the chain stays an abstract instrument schematic.

## Outputs

- **SVG:** `poster-2026-06-02-vo2-max-and-mitochondria.svg`
- **PNG:** `poster-2026-06-02-vo2-max-and-mitochondria.png` (2400×3000, 2× the viewBox)
- **Generator:** `gen_poster.py` (hand-coded SVG, no external design service)
- Copies also written to the blog folder `…/blog viz daily - temporary/posters/` for the downstream insert task and direct review.

## Render notes

- Renderer used: **CairoSVG** (2.9.0), output_width=2400 × output_height=3000.
- Playwright + Chromium (1st preference) and rsvg-convert (2nd) were both unavailable in this run — the Chromium download was network-blocked and `apt-get install librsvg2-bin` could not reach the package mirror. Fell back to CairoSVG per the task's renderer order.
- Verification: PNG is 2400×3000, ~490 KB (well above the ~50 KB floor); SVG passed an XML well-formedness check; the hero zone, dials, equation, feeds and auxiliary gauges were visually inspected on a rendered crop.
- One render-fidelity note: CairoSVG resolves the `system-ui`/`Inter`/`JetBrains Mono` stacks to local fallbacks (Liberation/DejaVu). The Fick equation was rebuilt with native `<tspan>` segments so spacing is renderer-measured rather than estimated, which keeps it clean under any fallback font.

## Deviations / fallbacks

- Renderer fallback to CairoSVG (above) — the only deviation. No fallback to transcript recovery was needed; the brief was found directly in the connected blog folder.
- Colours were not specified by the brief (it defers to the Aether design tokens); I used the Aether dark ground + a single teal active accent and a sober amber for the mortality panel, consistent with the "rationed semantic colour, three states max" instruction.
