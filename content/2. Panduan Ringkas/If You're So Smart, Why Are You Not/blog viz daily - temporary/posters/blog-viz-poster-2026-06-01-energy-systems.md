# Blog Viz Poster — 2026-06-01

- **Date:** 2026-06-01
- **Source brief:** `Visualization Concept — Fit - Part 2.0 (Athletic) - Energy Systems and the Aerobic Base.md`
  - Path: `…/blog viz daily - temporary/concepts/` (connected-folder source of truth; selected as the most recently modified brief, mtime 10:37)
- **Article:** Fit / Athletic / Part 2.0 — Energy Systems & the Aerobic Base (2 of 5, first "Engine" chapter)
- **Locked pillar style:** Engineering Diagnostic Instrument (new sub-archetype: the vertical capacity gauge)

## Visual concept used

A diagnostic instrument panel built around **"The Capacity Column"** — a tall floor-and-ceiling gauge. A near-fixed **CEILING (VO₂ max, genetic cap)** sits at the top with a tiny stubborn arrow; a **FLOOR (lactate threshold)** rises far up the chamber on a thick green arrow from its ghosted week-1 position, claiming the bright green **USABLE PERFORMANCE** band beneath it — literalizing "build the floor first, the room grows from the bottom up," plus the "sports car with a 2-litre tank" caution as an amber margin note. Paired to its right is the **Zone Map ladder** (Z1–Z5) with Zone 2 highlighted green as the operating band, Zone 3 flagged amber as the grey-zone trap, and a **polarized 80/20** bar below it, visually rhymed to the hero's floor via a dashed leader. A full-width **fuel-mix crossfade** (phosphagen → glycolytic → oxidative stacked areas over an effort-duration axis, none hitting zero) acts as the structural ground. Below: the **Two Protocols, Two Jobs** datasheet (FLOOR = steady Zone 2 / CEILING = Norwegian 4×4) with an amber interference-cost bridge to Part 4.0, then a four-gauge **convergence readout** (resting HR ↓, pace@HR ↑, decoupling <5%, VO₂ est ↑) and a Zone-2-by-feel chip.

Color discipline per the brief: **green = the working/growing things** (usable band, Zone 2, 80% easy, convergence gauges); **amber = the cautions** (Zone 3 trap, interference cost, the low-floor warning); **red deliberately withheld** (no catastrophic payload in this chapter), so its meaning is preserved across the pillar. Everything structural stays in the neutral ink ramp.

## Outputs

- **SVG:** `poster-2026-06-01-energy-systems.svg`
- **PNG:** `poster-2026-06-01-energy-systems.png` (2400×3440, ~425 KB)
- Both copied to the blog folder: `…/blog viz daily - temporary/posters/`

## Render notes

- **Renderer used:** CairoSVG (`output_width=2400 output_height=3440`, exact 2× of the 1200×1720 viewBox).
- rsvg-convert and `apt-get` were **unavailable** in the run sandbox (no install), and Playwright was not needed; CairoSVG (pip, `--break-system-packages`) succeeded on the first attempt.
- **Verification:** PNG is non-empty (~425 KB > 50 KB), dimensions match the expected 2400×3440, and a visual read confirmed all regions render (headline, hero gauge with both arrows, zone ladder, fuel crossfade, protocol cards, convergence gauges, footer). A first-pass legibility issue (fuel-band labels rendered near-black on dark bands) was fixed by lightening those labels and re-rendering.

## Deviations / decisions (autonomous run)

- **Brief selection:** A pharmacology poster (`poster-2026-06-01-pharmacology.*`) already existed from an earlier run today; the Energy Systems brief was the most recently modified concept with no poster yet, so it was the correct target. Slug `energy-systems` used to avoid filename collision on the shared date.
- **Metaphor reconciliation:** The brief's "USABLE PERFORMANCE band between floor and ceiling" + "room grows from the bottom up" + "floor rises far, ceiling barely" are slightly in tension geometrically. Resolved by rendering the green USABLE band as the floor's claimed territory growing *upward* from baseline (which unambiguously grows as the floor lifts), with a thin neutral "HEADROOM" strip above it up to the ceiling — this keeps every literal label and the unequal-arrow argument intact and legible.
- Tracker note: the scheduled-task's hard-coded `local_dbaa9cdd … outputs` path remains unmounted in run sessions; the connected `posters/` folder is the reachable destination (consistent with prior runs).
