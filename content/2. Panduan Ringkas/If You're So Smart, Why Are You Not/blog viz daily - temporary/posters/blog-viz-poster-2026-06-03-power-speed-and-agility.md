---
title: "Blog Viz Poster — 2026-06-03 — Fit / Part 3.1 (Athletic): Power, Speed & Agility"
date: 2026-06-03
---
# Blog Viz Poster — 2026-06-03

- **Date:** 2026-06-03
- **Source brief:** `concepts/Visualization Concept — Fit - Part 3.1 (Athletic) - Power, Speed and Agility.md`
  (in `…/blog viz daily - temporary/concepts/`)
- **Article:** Fit pillar · Athletic track · **Part 3.1 — Power, Speed & Agility**
- **Series style lock:** Engineering Diagnostic Instrument (Fit-pillar). Sub-archetype this run: **oscilloscope / signal-tuning bench.**
- **Cross-checked:** matches `Tracker — Blog Viz Daily.md` line 30 — the article logged as today's (2026-06-03) run.

## Visual concept used

A wall-mountable signal-analysis bench. The **hero** is an RFD oscilloscope — **FORCE vs TIME in milliseconds** (0–400 ms) — carrying two traces: a grey STRENGTH curve (tall peak, but lazy, crossing its max after the window) and a bright-green EXPLOSIVE curve (steep, early, lower peak). A shaded green **CONTACT WINDOW (0.1–0.3 s)** gate frames where the explosive trace sits *above* the strength trace, making the article's whole thesis — *rate, not peak* — a literal visible slope (stamped `RFD = ΔForce ÷ Δtime = the SLOPE`). The paired instrument is a **force–velocity tuning chart** with two training zones and a ghost/solid raised-ceiling pair (`max strength raises the WHOLE curve`). Below, **three tuned output channels** hang off one `phosphagen + Type IIx` input rail: POWER (spec chip + accessible→advanced toolkit ladder), SPEED (two sub-tracks — acceleration vs max-velocity), AGILITY (brakes-first 3-rung ladder decelerate → pre-planned COD → reactive, plus the `5-10-5 = COD test, not agility` fault chip). The **elastic engine** renders the stretch-shortening cycle as a three-beat timing strip with a deliberately narrow amber AMORTIZATION gap, beside an **RSI gauge** (strength-dominant ↔ elastic-dominant, `RSI = jump ht ÷ contact time`) and a neural-drive note. A hard red **safety interlock** gates high-intensity plyos behind `1.5× BW squat · 30 s SL balance · 30 s SL half-squat`, with a free green bypass lane for low-intensity plyos and an `earn the right` warning. Footer = benchmark scoreboard (`THE NUMBER IS THE BOSS`) + the law `POWER = STRENGTH EXPRESSED FAST`. Per §5, this is the first Athletic poster to *use* the danger state — rationed strictly to the safety interlock (highest-injury-ceiling chapter). §7 avoidances honoured: no explosive-athlete hero photo, no bare textbook F-V curve, no agility-ladder/cone clipart.

## Outputs

- **SVG (working source, scratch):** `outputs/poster-2026-06-03-power-speed-and-agility.svg` (also copied to `…/posters/`)
- **PNG (published):** `…/blog viz daily - temporary/visualization/Poster — Fit - Part 3.1 (Athletic) - Power, Speed and Agility.png`
- **PNG (working copy):** `…/blog viz daily - temporary/posters/poster-2026-06-03-power-speed-and-agility.png`
- Canvas: portrait `viewBox 1200×1860`, rendered at 2× → **2400×3720**, ~602 KB.

## Renderer & verification

- **Renderer:** CairoSVG 2.x (pip-installed this run; cairo system libs present, no sudo needed). rsvg-convert/Playwright not required.
- **Verification:** PNG non-empty (602 KB > 50 KB) and dimensions exactly 2400×3720 (2× the viewBox). XML validated via minidom before final render. Visual QA by cropping and viewing the hero/F-V region, the elastic-engine + RSI region, and the section-label band.
- **Fixes after first render:** (1) shortened the hero section label to `THE RFD OSCILLOSCOPE — force vs time (ms)` so it no longer overran the F-V chart label; (2) shrank and re-centred the RSI dial (radius 84, centre 927,1400, formula chip moved above the arc) so the gauge sits cleanly inside its card. Re-rendered and re-verified both.

## Deviations / notes

- One transient hiccup: the on-disk SVG lost its final `</text></svg>` (a write/sync truncation between the editor and the render mount); detected via an XML parse error, repaired by appending the closing tags directly, then re-validated. No content lost.
- The scheduled-task file's hard-coded outputs path remains unreachable from the run session (long-standing); the connected blog folder was the working source of truth, consistent with prior runs.
- Downstream `blog-viz-insert-daily` (10:30) should pick up the published PNG by its convention name in `/visualization/`.
