# Blog Viz Poster — 2026-06-28 · Nutrition Part 4.0 (Calorie Management: Bulk, Cut, Reverse)

**Date:** 2026-06-28
**Source brief:** `concepts/Visualization Concept — Healthy - Nutrition Part 4.0 - Calorie Management - Bulk, Cut, Reverse.md`
(most-recently-modified concept on disk @ 05:39; cross-checked against the Poster tracker, whose prior entry — Nutrition 3.0 — names "Next up = Nutrition Part 4.0", confirming the pick.)
**Article:** Healthy · Nutrition · Part 4 of 5 — *Calorie Management: Bulk, Cut, Reverse*

## Visual concept used
Locked Healthy **"Clinical Nocturne"** ground; NEW Nutrition sub-archetype = **"The Transition Recorder / Slew-Limited Glide-Path"** — the first Nutrition instrument whose hero is *change-over-time* rather than a lever (1.0 control console), a scale (2.0 calibration bench), or a depth (3.0 waterline assay). **Landscape** (flips 3.0's portrait), because time runs left→right.

A wide chart-recorder plots one continuous intake **trace** drifting between three stacked energy bands — **SURPLUS · MAINTENANCE · DEFICIT** — across a weeks→months axis. The signature device is a **dashed cyan TRUE-MAINTENANCE setpoint that MOVES**: it holds level through the bulk, **sags down** across the deficit (`adapts down · NEAT drops · 2,800 → 2,550`), then **recovers** under the reverse, with a `lands back near start` bracket — and a ghosted, **struck-through** high line above it (`PROMISED maintenance — "reverse lets you eat WAY more"`, the myth the article debunks). The trace runs a flat **BULK** run → a rate-limited ramp **DOWN** (a clamp/governor glyph asserts *the slope is the controlled variable*) → a flat **CUT** run → then **FORKS** at the end of the cut: **PATH A — the violent switch** (amber dashed vertical slam → **the one saturated red** overshoot that rings into `FAT REBOUND +5 kg in a month`, stamped **"THE SWITCH, NOT THE DIET"**) vs **PATH B — the reverse glide** (lit-cyan **+50–100 kcal/wk staircase** hugging the recovering setpoint, parallel CARDIO↑ arrows then a taper↓, settling clean).

Margins: **Panel A — Phase Selector** (left: body-fat / training-age / goal dials lighting one of CUT/BULK/RECOMP, "PICK ONE DIRECTION · RUN IT 8–12 WEEKS", Fit 1.2 cross-ref). **Panel C — Trend Reader** (right-upper: noisy raw daily trace under a smoothed 7-day average, `THE DAY IS NOISE · TWO WEEKS IS SIGNAL`, TAPE/MIRROR/LIFTS cross-check). **Panel D — Rate Governor + Autopilot** (right-lower: slew dial with BULK/CUT/REVERSE rate arcs + a subordinate MacroFactor autopilot note, explicitly *"the closed loop lives in Part 1.0; here it just holds the glide"*). **Bottom rail — the ramps are made of macros** (CUT = protein↑/fat=floor/carbs↓ · BULK/REVERSE = carbs↑; "carbs are the lever you move; protein & fat are the rails you don't break"). Takeaway lockup: **"DON'T STOP A DIET — GLIDE OFF IT."** / *a hard step rings · a rate-limited ramp settles.*

**Headline:** `THE SWITCH, NOT THE DIET.` · **Thesis:** *the damage isn't the diet; it's how violently you switch — ramp slow, the target already moved.*

§7 traps avoided: **no literal steering wheel** (1.0 owns it; steering rendered as the glide-vs-slam trajectory), **no flat fixed maintenance line** (the sag/recover IS the thesis), **no magic-rebuild reverse curve** (recovered line lands at/near the original; the high "promised" line is ghosted + struck), **no single trace without the A/B fork**, no diet/fitness cliché kit (before/after bodies, scale-with-arrow, macro pie, biceps, journey-mountain, checkmark calendar), no pastel Excel chart (reads as a clinical chart-recorder), no red-flooding (flat phases + clean glide carry no alarm; only the one ring is red), no wrong-pillar surfacing.

## Outputs (authoritative copies in `visualization/`)
- SVG: `visualization/Poster — Healthy - Nutrition Part 4.0 - Calorie Management - Bulk, Cut, Reverse.svg`
- PNG: `visualization/Poster — Healthy - Nutrition Part 4.0 - Calorie Management - Bulk, Cut, Reverse.png`
- Fresh build — no prior poster existed for this concept, so no delete needed (exactly one PNG + one SVG).

## Renderer & verification
- **Renderer:** CairoSVG (Playwright + rsvg-convert unavailable in sandbox; Inter / JetBrains Mono → DejaVu fallback). Rendered **landscape 1600×1040 @2× → 3200×2080**, ~452 KB (> 50 KB threshold; dimensions match the viewBox).
- **Verification:** XML well-formedness asserted via `xml.dom.minidom`; full poster + two zoom crops (fork region, bottom rail) read back and visually inspected — unicode arrows (↑ ↓ →) and the red/cyan fork render correctly.
- **Build fix:** after two label edits the on-disk file lost its closing `</g></svg>` (mount/edit truncation; text-tag balance stayed 94/94 but the root never closed → CairoSVG `no element found`). Detected via tag-balance check, re-appended the two closers, re-validated XML OK, re-rendered, and re-copied the fresh pair to `visualization/` (so the authoritative PNG is the fixed render, not the stale first pass). Also right-anchored/tightened the Path A red annotation so it stays inside the hero panel.

## Deviations / fallbacks
- Record filename suffixed with the concept slug (`...-calorie-management-bulk-cut-reverse.md`) because `blog-viz-poster-2026-06-28.md` already exists from today's earlier Nutrition 3.0 poster run — per Step 5, no overwrite.
- Scheduled-task's hard-coded `local_dbaa9cdd` outputs path not used; built in the run-session outputs scratch, authoritative copies kept in the connected-folder `visualization/`. Connected-folder `concepts/` + the trackers remain the source of truth.

**Next up = Nutrition Part 5.0 — the Nutrition track CAPSTONE** (closes the 5-part Nutrition track and the Healthy pillar's last open track).
