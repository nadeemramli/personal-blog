---
draft: true
---
# Blog Viz Poster — 2026-06-01

- **Date:** 2026-06-01
- **Source brief:** `Visualization Concept — Fit - Part 4.0 - Pharmacology.md`
  - Path: `…/blog viz daily - temporary/concepts/Visualization Concept — Fit - Part 4.0 - Pharmacology.md` (most recently modified, mod-time Jun 1 00:38)
  - Cross-checked against `blog-viz-tracker.md` → matches the logged "Part 4.0 - Pharmacology.md" run. (Note: the tracker in this folder is the reachable source of truth; the original scheduled-task `Tracker — Blog Viz Daily.md` path is not mounted in run sessions.)
- **Article:** Fit pillar / Part 4.0 — Pharmacology ("The Margin"), the capstone closing the Aesthetic & Strength sub-series (4 of 4).

## Visual concept used

Hand-coded SVG in the locked Fit "Engineering Diagnostic Instrument" style, sub-archetype: a **margin / trim-gain panel on a foundation block, feeding a two-tier gated compound catalog with a hardware safety interlock.** Five zones top-to-bottom: (1) a **90/10 proportion bar** drawn true-to-scale — `THE WORK · 90%` as a massive green foundation block annotated with Parts 1–3, and `THE MARGIN · 10%` as a thin amber terminal slice with explode-rails descending into the catalog; (2) **Tier 1 — Natty**, an open green-keyed 2×2 shelf of four mechanism buckets (Energy/Cardio, Pre-workout Cognition, Fat-loss cut-only, Pump/Recovery) with compound spec rows and `year-round / cut-only / cycle-it` state chips; (3) a heavy full-width **safety interlock gate** in danger chrome with three required keys (bloodwork · a doctor · a structured plan) and the stamp "NOT A RECOMMENDATION GATE — A TRANSPARENCY GATE"; (4) **Tier 2 — Half-Natty**, a hatched, cordoned quarantine zone of four compound cards (Retatrutide, CJC-1295+Ipamorelin, MK-677, Clen/Cardarine) each carrying mechanism · use · ⚠ caveat, watermarked "Shown for transparency — not endorsement"; (5) the **hierarchy-of-impact ladder**, drawn upright and tapering (training → calories → sleep → Tier 1 → Tier 2) beside a ghosted, struck-through "what most people optimize first" inversion with a single correction arrow flipping it. Footer carries the Tier-1 starter rail, the arc-close line, disclaimer, sources, and the `Fit — Aesthetic & Strength` series mark. Semantic color rationed per brief: green = go/foundation, amber = warning/cut-only chips, red = the interlock and the entire Tier-2 lower register (the open-above / locked-below contrast is the argument). No pill-bottle/product/anatomy aesthetic; no S/A/B tier-list.

## Outputs

- **SVG:** `poster-2026-06-01-pharmacology.svg` (1200×2440 viewBox, portrait/tall)
- **PNG:** `poster-2026-06-01-pharmacology.png` (2400×4880, ~726 KB)
- Both also copied to the blog folder: `…/blog viz daily - temporary/posters/`

## Renderer & verification

- **Renderer:** CairoSVG (last-resort fallback in the task's preferred order). Playwright/Chromium download failed (sandbox network restriction) and `rsvg-convert` was unavailable (no `apt`/`sudo` in sandbox), so the pipeline fell back to CairoSVG, which rendered all patterns (background grid, danger hatch, gate warning-stripe) and markers correctly.
- **Verification:** PNG is non-empty (~726 KB > 50 KB) and exact-dimension 2400×4880 = 2× the 1200×2440 viewBox. Spot-checked top region (90/10 bar true-to-scale, headline + subhead legible) and bottom region (impact ladder upright with struck-through inversion, footer legible).

## Deviations / notes (autonomous run)

- **Canvas height:** used 1200×**2440** (taller than the default 1200×1500) because the brief specifies five dense zones plus a multi-line footer; a 4:5 frame would have crushed legibility. Orientation stays portrait/tall as the brief requires.
- **Fonts:** Inter / JetBrains Mono are not installed in the sandbox, so the SVG's documented fallback stack rendered (DejaVu Sans for display, DejaVu Sans Mono for labels). Layout and hierarchy are unaffected; on a machine with Inter/JetBrains Mono installed the SVG will render in the intended faces.
- **Strikethrough:** CairoSVG ignores `text-decoration: line-through`, so explicit strikethrough lines were drawn over the inverted "what most people optimize" ladder to preserve the brief's "visibly struck-through" requirement.
