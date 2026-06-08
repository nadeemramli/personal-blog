---
draft: true
title: "Blog Viz Poster — 2026-06-03"
date: 2026-06-03
task: blog-viz-poster-daily
---

# Blog Viz Poster — 2026-06-03

**Date:** 2026-06-03

**Source brief:** `Visualization Concept — Fit - Part 4.0 (Athletic) - Concurrent Training.md`
Path: `…/blog viz daily - temporary/concepts/Visualization Concept — Fit - Part 4.0 (Athletic) - Concurrent Training.md` (modified 10:38 local today; confirmed against `blog-viz-tracker.md`, which logs this article as the 2026-06-03 run — "dual-trace interference scope + 5-control de-confliction console sub-archetype").

**Article:** Fit pillar → Athletic track → **Part 4.0 — Concurrent Training** (the integration chapter).

## Visual concept used

A portrait (1200×1500, 4:5) **"Engineering Diagnostic Instrument"** poster built directly from the brief's native geometry — a *timing / interference* problem, not a split or a tug-of-war. Five stacked instrument zones, read top→down:

1. **Master headline** — `TWO SIGNALS. ONE BODY.` with the subhead framing the whole argument (strength = mTOR, endurance = AMPK, they fight only when they peak at once).
2. **Interference scope** — a dual-trace oscilloscope on a shared time axis, split into **State A · SEPARATED** (mTOR and AMPK pulses peak in turn, both complete, green ✓) and **State B · OVERLAPPED** (forced onto the same instant; the mTOR trace is clipped flat against a red ceiling with a dashed "ghost" of the lost signal and a `⚠ SIGNAL LOST` flag). Carries the sprint-15-min-before-the-lift citation and the `INTENSITY, NOT DURATION, FIRES AMPK HARDEST` caption.
3. **The asymmetry valve** — a one-way `AMPK ▶ suppresses ▶ mTOR` arrow (live/red) with the reverse path greyed and blocked, encoding "cardio hurts strength more than strength hurts cardio → almost every rule protects the lift."
4. **Five-control de-confliction console** — Phase Separation (slider), Intensity Cap (capped limiter), **Modality Selector** (full-width big lever, three-state ride/row ✓ · easy run mod · hard run ✕, Wilson 2012 cite), Fuel/Glycogen (gauge), and **Block Bias** (emphasised mode switch — the single most effective control).
5. **Weekly scheduler + dual dashboard** — three selectable 7-cell template rows (Lifter-priority / Engine-priority / Balanced) with the leg-day-vs-running warning chip, then twin Chassis ▲ / Engine ▲ dashboards, the three-line verdict logic, and the closing enhanced-lifter note.

**Palette / type (Aether tokens):** black ground (#000000), surface panels (#0B0B0D) with #27272A / #3F3F46 hairline borders, Inter for display/body and JetBrains Mono for technical labels. Two signal identities locked across the whole poster — **mTOR = cyan #38BDF8** (build), **AMPK = amber #F59E0B** (endure) — with **red #EF4444** reserved exclusively for the fault/collision state and the one-way valve, and **green #22C55E** for the "preferred / both-complete" cues. Clinical control-room mood; drama carried entirely by the separated-vs-overlapped contrast, not saturation. Avoided the tug-of-war and runner-vs-lifter clichés per the brief's §7.

## Outputs

- **SVG:** `poster-2026-06-03-concurrent-training.svg`
- **PNG:** `poster-2026-06-03-concurrent-training.png` (2400×3000, ~0.5 MB)
- Both also copied into the blog folder root: `…/blog viz daily - temporary/`

## Renderer & verification

- **Renderer used: CairoSVG** (last-resort fallback). Playwright/Chromium was attempted first for font fidelity but the Chromium download exceeded the sandbox time limit; `librsvg2-bin` (rsvg-convert) was unavailable and could not be installed. CairoSVG produced a clean 2400×3000 raster.
- **Verification:** PNG confirmed non-empty (510,887 bytes > 50 KB) and dimensions exactly 2400×3000 via PIL. Poster also visually reviewed (Read on the PNG) — all five zones render correctly; the scope clip, one-way valve, five controls, scheduler rows, and dual dashboards are all legible.

## Deviations / notes

- **Fonts:** CairoSVG has no Inter / JetBrains Mono installed in the sandbox, so it falls back to DejaVu/Liberation sans + mono. Visual hierarchy and the mono "instrument" feel are preserved; exact letterforms differ slightly from the Aether spec. (Re-rendering with Chromium + the real font files would tighten fidelity if desired.)
- **SVG hygiene fix:** initial render failed twice — first on `--` sequences inside XML comments (illegal in strict XML), then on trailing NUL bytes left after an edit. Both were corrected; the final SVG is well-formed.
- One cosmetic adjustment: the scheduler section title was shortened from "WEEKLY SCHEDULER — SELECT A TEMPLATE" to "WEEKLY SCHEDULER" to stop it colliding with the Mon–Sun day-letter header.
- Downstream: the `blog-viz-insert-daily` task (10:30) can pick up `poster-2026-06-03-concurrent-training.png` for embedding.
