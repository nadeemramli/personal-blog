---
title: Blog Viz Poster — 2026-06-21 — Productivity Enhancement Part 6.0 (Just-in-Time Project Management)
draft: true
date: 2026-06-21
---
# Poster run — 2026-06-21

- **Date:** 2026-06-21
- **Source brief:** `concepts/Visualization Concept — Productive - Productivity Enhancement Part 6.0 - Just-in-Time Project Management.md` (most-recently-modified concept, created 2026-06-21 00:40; confirmed today's run against `concepts/blog-viz-tracker.md`).
- **Article:** Productive pillar → Productivity Enhancement track → **Part 6.0 — Just-in-Time Project Management** (opens and completes "Part 6: JIT Project Management", the capstone discipline that fixes overwhelm).
- **Design tokens:** `aether-call-to-action-DESIGN.md` (near-black `#0B0F14` ground, Inter display, JetBrains Mono labels, semantic status colours).

## Visual concept used
The locked Productive-pillar **"Neural Signal Schematic"** house style, rendered as a **power-distribution / load-management schematic** — a NEW, distinct sub-archetype: the **PULL-DEMAND CAPACITY GOVERNOR**. A finite RATED SUPPLY feeds a long PROJECT MANIFOLD. Left ~40% is a vast, calm **DORMANT / PARKED FIELD** of ~36 dark cells (open switches, drawing zero current, tagged "inventory waiting for demand · costs you nothing"). A central **CURRENT LIMITER stamped `ACTIVE CAP · 3–5`** gates the path to a 5-socket **ACTIVE BAY** where 4 projects run at full cyan brightness and one sits **DONE**. A top **DEMAND TIMELINE** (deadline clock + opportunity spark) drops a cyan pull-arrow that closes one dormant cell's switch and pulls it into the bay; a bottom-up **amber "I feel bad about it" anxiety-push** is **BLOCKED** at the gate (pull, not push). Beneath the bay, a **KIT-FEED bus** assembles each project from `RESOURCES → 4.0 PARA · MAPS → 4.1 · NEXT ACTION → 3.0`, with an **×AI KIT-ASSEMBLER** arm collapsing "blank page → 0" (lit only because the lower feeds are live — the fundamental-before-multiplier law). The DONE socket **sweeps one-way to a dark ARCHIVE SINK** ("finish ⇒ free a slot · completion > open"). The prominent lower-centre **OVERLOAD PARADOX A/B** proves the thesis: EVERYTHING ON → all loads brown out → completion ≈ 0 (the ONE RED: limiter TRIPPED, a hand cramming a 6th switch) vs A FEW ON → full power → completion HIGH. A lower-left **learning twin** mirrors the pull logic (just-in-case capacitor-bank stockpile, self-discharging/amber, vs a just-in-time skill-tap off a live project, cyan), and a lower-right **→ Part 7 autonomous-runner** badge carries forward continuity. Headline: **"PULL. DON'T STOCKPILE."**

Colour discipline held to the locked palette: cyan `#2DD4BF` = live/load-bearing (active bay, demand pull, kit feeds, ×AI, high-completion meter, JIT skill-tap); amber `#E8A23D` = ordinary caution (blocked anxiety-push, self-discharging stockpile, weekly-review prompt); **one** red `#FF5C5C`, used only at the overload trip; dim grey = the calm dormant field, the archive sink, the done/swept loads. The largest region of the poster is deliberately calm grey — the article's payoff (parked = guilt-free).

## Outputs (authoritative copies in `visualization/`)
- **SVG:** `visualization/Poster — Productive - Productivity Enhancement Part 6.0 - Just-in-Time Project Management.svg` (~43 KB, editable raw source)
- **PNG:** `visualization/Poster — Productive - Productivity Enhancement Part 6.0 - Just-in-Time Project Management.png` (~472 KB, 3000×2400)
- Build script (scratch): session outputs `build_poster.py` (hand-coded SVG generator with Python loops for the dormant field, paradox switch grid, and socket rack).

## Renderer & verification
- **Renderer:** CairoSVG (`output_width=3000`). Playwright + Chromium and rsvg-convert were not available in the sandbox; CairoSVG is the established fallback for this series.
- **Verification:** PNG is 3000×2400 (= 2× the 1500×1200 landscape viewBox) and ~472 KB (> 50 KB threshold), non-empty. Rendered PNG was read back and inspected at full size plus four zoom crops (top demand-timeline/active-bay header, kit-feed + archive, overload-paradox inset, learning panel). Two issues found and fixed on a second pass: (1) the DEMAND TIMELINE label collided with the ACTIVE BAY header — separated onto distinct positions; (2) a double-escaped `&` in the learning-panel header and overlapping caption text in the ×AI assembler box — corrected. Final inspection clean: no clipping, no dead space, all labels legible.

## Deviations / notes
- **Orientation:** landscape 1500×1200 (per the brief's explicit LANDSCAPE call — the supply → manifold → archive flow reads wide and the dormant field needs room to feel vast/calm), consistent with the recent Productive-pillar posters.
- **Selection convention:** followed the established finish-the-active-track hand-off (Part 5.0's named next-up was Part 6.0), matching the brief's own selection note, rather than the scheduled task's strict glob-order rule.
- **No prior poster** existed for this concept, so no delete-before-write was needed; confirmed exactly one PNG + one SVG for the concept after writing.
- **Tracker:** appended a row to `Tracker — Blog Viz Poster.md`.
