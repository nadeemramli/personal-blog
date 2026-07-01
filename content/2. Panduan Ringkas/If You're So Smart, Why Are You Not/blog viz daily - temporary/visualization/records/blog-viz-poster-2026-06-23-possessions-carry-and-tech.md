---
title: "Blog Viz Poster — 2026-06-23 · Possessions, Carry and Tech"
draft: true
tags:
date: 2026-06-23
---
# Blog Viz Poster Record — 2026-06-23 (Part 5.0)

- **Date:** 2026-06-23 (run executed ~11:34 local; scheduled 09:30 slot)
- **Source brief:** `concepts/Visualization Concept — Attractive - Appearance Part 5.0 - Possessions, Carry and Tech.md` (dated twin: `concepts/blog-viz-2026-06-23-part-5-0-possessions-carry-and-tech.md`)
- **Article:** Attractive pillar · Appearance track · **Part 5.0 — Possessions, Carry and Tech** (Part 5 of 7)
- **Poster stem:** `Poster — Attractive - Appearance Part 5.0 - Possessions, Carry and Tech`

## Which brief / target selection

Three briefs carry today's date: Part 3.0 (Hair Biomechanics, 00:40), Part 4.0 (Clothing/Color/Footwear, 05:40), and Part 5.0 (Possessions/Carry/Tech, 10:44). Posters for 3.0 and 4.0 were already built earlier today (01:40 and 06:53), and the Daily tracker's run-note + the Poster tracker's "Next up = Part 5.0" both point to 5.0 as the uncovered article. Part 5.0's brief is also the most-recently-modified concept. So Part 5.0 was the correct target. Fresh build — no prior 5.0 poster existed (one PNG + one SVG written).

## Visual concept used

Fifth sibling in the locked **"Architect's Elevation / Spec Sheet"** pillar family, introducing the new **INSPECTION / QC AUDIT-SHEET** variant (verb = *audit what you already carry on the maintenance axis*, distinct from 4.0's *choose-what-to-wear* loadout catalog). Landscape **1680×1120 (3:2)**, matching sibling 4.0. The board re-tilts **warm** (inverting 4.0's cool hinge) because carry has a measurable truth — maintenance & coherence — that clothing-colour lacked; the enlarged warm / shrunken cool epistemic key in the left rail states this before any label.

Reading path implemented top→down: **continuity banner** ("still signaling, not biology — but carry has a measurable truth again") → **01 the hero inversion** (a clean 8-yr Civic vs a filthy 2-yr BMW, each wearing a small value tag *and* a maintenance gauge; the Civic's signal bar out-reads the BMW's; hero callout "THE SIGNAL IS MAINTENANCE, NOT VALUE") → **02 the four inspection stations** (Mobility = 3-detent pick-one-lane selector with a struck all-three ghost; Wallet = slim cardholder + eWallet stack + capped cash dial + "credit = infrastructure, not status"; Tech = one coherent device ring vs a ghosted fragmented set; Watches = two matched flats "two cover 95%", Seiko 5 + Orient ≈ <RM 2,500, struck one-piece-flagship trap) → **the COHERENCE TOLERANCE BAND** (a dashed terracotta corridor threading under all four stations; three station pins sit in-tolerance, the three warm coherence ties — METAL→METAL · LEATHER→LEATHER · MAINTENANCE UNIFORM — stitch across) → **the MASTER READOUT** at the band's right end, an arc gauge whose needle is **dragged into the NEGLECTED/low end** ("reads at the weakest pin, not the best") → **the ONE RED**: the phone in the tech ring is drawn with a cracked screen, its pin alone dropped **below** the corridor as "OUT OF TOL — cracked screen", and a red leader runs from it into the master needle and drags the whole read down → **the FOUNDATION GATE** (pass/fail threshold: if monthly cost erodes health · gym · nutrition · rent · savings, you can't afford the signal; amber leverage-trap note; "→ Part 7.0 makes this a weekly gate"). Footer thesis lockup: **"MAINTAINED BEATS EXPENSIVE. COHERENT BEATS FLAGSHIP."**

Single-alarm-red discipline strictly enforced per §7: **red appears only** on the cracked-screen glyph, its out-of-tolerance pin, the red leader, and the master needle it drags down. Every other failure mode (all-three-lanes indecision, the fragmented ecosystem, the one-piece-flagship trap, the neglected BMW gauge, the APR-balance / mismatched-metal cautions, the leverage trap) is rendered in **grey or amber**, never red. Price tags appear only in the Civic/BMW pair, only to be out-voted by the maintenance gauge.

## Palette (brief §5 = authoritative)

Bone paper `#F4F1EA` + drafting-dot texture; graphite ink `#1E2024`; **terracotta `#C2703D`** = MEASURABLE/grounded (dominant — gauges at immaculate, coherence band + ties, foundation gate); slate-blue `#5E7585` = CONVENTION (shrunk — which lane / ecosystem / tier); **signal-red `#D9483B`** = the cracked screen only; amber `#C8902E` for calm cautions; grey `#9A958C`/`#6E6A62` for neglected/ghosted/struck. The aether-call-to-action-DESIGN.md token file is a generic dark-UI template (primary #000 / bg #000), so the brief's §5 light-first drafting-paper palette was used as authoritative — consistent with the 3.0 and 4.0 records.

## Outputs

- SVG: `visualization/Poster — Attractive - Appearance Part 5.0 - Possessions, Carry and Tech.svg` (~40 KB, editable raw source)
- PNG: `visualization/Poster — Attractive - Appearance Part 5.0 - Possessions, Carry and Tech.png` (~487 KB, 3360×2240)
- Generator (scratch): `outputs/gen_poster_5_0.py`

## Renderer & verification

- **Renderer: CairoSVG** (Playwright + rsvg not installed in sandbox this run — same as 3.0/4.0). Inter/JetBrains Mono → DejaVu Sans / DejaVu Sans Mono fallback at render time.
- Rendered at **2× the 1680×1120 viewBox → 3360×2240**; PNG verified non-empty (~487 KB > 50 KB threshold) and exact 3360×2240 dimensions.
- **Visual inspection:** read back the full PNG plus zoom crops of (a) the four stations, (b) the coherence band + out-of-tolerance red pin + master readout. **Build fix applied:** first pass had station panels too short (182 px) → text overlap in the Wallet/Tech/Watches stations and a stray red on the struck "all three lanes" mark. Stations were enlarged to 240 px, the band/master/bottom zones shifted down, and the stray red recolored to grey (red reserved for the cracked screen). Re-rendered and re-inspected clean — no overlaps, no clipping, mechanism legible.

## Deviations / notes

- Em-dash use minimized in prose-style lines per house style (continuity banner sentence-split; "open the passenger door:" uses a colon). Em-dashes retained only in title/group-label lines (headline, big red callout, band rule) where the convention permits.
- Scheduled-task's hard-coded `local_…/outputs` path is not this run's session path; the connected `visualization/` folder + trackers were used as the source of truth and authoritative output home (same as recent runs). Deliverables also kept in the run-session scratch `outputs/`.
- One PNG + one SVG only; no prior 5.0 variant to delete.
