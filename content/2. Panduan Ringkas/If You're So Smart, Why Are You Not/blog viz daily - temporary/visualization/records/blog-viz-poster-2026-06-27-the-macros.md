---
title: "Poster Record — Healthy / Nutrition Part 2.0: The Macros"
date: 2026-06-27
---
# Blog Viz Poster — 2026-06-27 — Healthy / Nutrition Part 2.0: The Macros

- **Date:** 2026-06-27
- **Source brief:** `Visualization Concept — Healthy - Nutrition Part 2.0 - The Macros.md` (dated alias `blog-viz-2026-06-27-part-2-0-the-macros.md`), in the connected blog folder `…/blog viz daily - temporary/concepts/`.
- **Article:** Healthy pillar · Nutrition track · **Part 2.0 — The Macros** (Part 2 of 5; the article that puts real numbers on the four levers named in Nutrition 1.0).
- **Selection:** Today's most-recently-modified concept brief (mtime 10:40, 2026-06-27) that did **not** already have a poster. Nutrition 1.0 was postered earlier today; Part 2.0 — The Macros was the open one. Cross-checked against the Daily tracker (Nutrition was the pre-planned next track; 2.0 is 1.0's named next-up).

## Visual concept used

A landscape **"Clinical Nocturne" CALIBRATION BENCH** — the direct sequel to Nutrition 1.0's control console, advancing the verb from *operate* to *calibrate*. The four macros are drawn as **four deliberately-different lever gauges** so their *difference in constraint shape* (the whole article) reads in one glance: **① PROTEIN** = a hard-floor gauge with the engraved cyan `1.6–2.2 g/kg` SET band, a machined hard-stop detent at the floor, a hatched dim-red `>2.5 = just digestion` dead-zone above, the side distribution comb (`0.3–0.4 g/kg × 3–5 feeds`), and **the poster's one scarce saturated-red zone** below the floor (`↓ below for weeks = lost tissue`); **② CALORIES** = the tallest three-position direction gate (SURPLUS +250 / MAINTENANCE 0 (lit) / DEFICIT −300); **③ FAT** = a floor-and-ceiling band gauge (bright cyan `0.8–1.0` floor + an **amber** `9 kcal/g` ceiling-overshoot marker, safe travel lit between); **④ CARBS** = a detent-free remainder window whose `378 g` value is *computed*, fed by a literal subtraction strip (`2,800 − 640 − 648 = 1,512 ÷ 4`). A top **calculation chain** rail engraves the order (`SET PROTEIN → SET CALORIES → HOLD FAT FLOOR → CARBS = WHAT'S LEFT`); a docked **DAY TICKET** prints the 80 kg lean-recomp proof (P 160 / F 72 / C 378 / ≈2,800 kcal) with the `±5% protein · ±10% the rest` tolerance stamp, a Malaysian affordability readout (`protein floor ≈ < RM 15/day`), and a Part-1 trend-wire callback. A dim bottom **fad-diet shelf** shows KETO / IF / CARNIVORE as amber levers jammed past their own rule. Single-alarm-color discipline held: cyan = the calibrated instrument you trust, amber = the warm thing that misleads, exactly one saturated red on the protein below-floor zone. Avoided the macro pie/donut and four-identical-dials traps per §7.

## Outputs (authoritative copies in `visualization/`)

- **SVG (editable source):** `visualization/Poster — Healthy - Nutrition Part 2.0 - The Macros.svg`
- **PNG (2× = 3200×2080):** `visualization/Poster — Healthy - Nutrition Part 2.0 - The Macros.png`
- Hand-coded SVG, landscape `viewBox 0 0 1600 1040` (~3:2). Exactly one PNG + one SVG for this concept (clean first build — no prior poster to delete).

## Renderer & verification

- **Renderer:** CairoSVG (rsvg-convert/librsvg unavailable in sandbox; Playwright not needed). Rendered at 3200×2080 (2× the 1600×1040 viewBox).
- **Verified:** PNG non-empty (~360 KB), correct dimensions 3200×2080, valid XML in the copied SVG. Visually inspected full poster + zoom crops of the lever cluster, calc chain, thesis, and day ticket.
- **Fixes during build:** CairoSVG mis-positions inline coloured `<tspan>` under `text-anchor="middle"` (jammed the cyan `→` arrows into adjacent words). Resolved by switching the calc-chain and thesis lines to start-anchor at a computed x (start-anchored mid-line tspans render correctly, as the header/day-ticket proved) and padding the arrows with non-breaking spaces. Also stripped stray trailing NUL bytes the editor appended before each render. Trimmed the CALORIES subtitle (`· LARGEST THROW`) to avoid crowding the FAT header (the tallest slot already conveys "largest throw").

## Deviations / notes

- **Malaysian readout placement:** the brief suggests clipping the affordability gauge to the protein lever; to keep the protein column legible it was docked instead in the right-hand instrument cluster under the tolerance stamp (still a small grace note, not a co-star). Minor placement choice only.
- **Path reconciliation:** the scheduled task's hard-coded `local_…/outputs` path is unreachable from this run; per established policy the authoritative copies live in the connected-folder `visualization/`, with build/scratch copies in the run-session outputs folder.
- **Next up (Daily):** Nutrition Part 3.0 — Omega-3, Fiber, and the Gut.
