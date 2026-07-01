---
title: "Poster Record — Healthy / Nutrition Part 3.0: Omega-3, Fiber, and the Gut"
date: 2026-06-28
---
# Blog Viz Poster — 2026-06-28 — Healthy / Nutrition Part 3.0: Omega-3, Fiber, and the Gut

- **Date:** 2026-06-28
- **Source brief:** `Visualization Concept — Healthy - Nutrition Part 3.0 - Omega-3, Fiber, and the Gut.md` (dated alias `blog-viz-2026-06-28-part-3-0-omega-3-fiber-and-the-gut.md`), in the connected blog folder `…/blog viz daily - temporary/concepts/`.
- **Article:** Healthy pillar · Nutrition track · **Part 3.0 — Omega-3, Fiber, and the Gut** (Part 3 of 5; the two nourishing inputs a macro tracker is structurally blind to, plus the gut microbiome they feed).
- **Selection:** Today's most-recently-modified concept brief (mtime 00:39, 2026-06-28) with no existing poster. Cross-checked against the Daily tracker, which logged Nutrition 3.0 as today's run and named it the next-up after Part 2.0 (The Macros).

## Visual concept used

A portrait **"Clinical Nocturne" DEPTH-ASSAY** — a brand-new Nutrition sub-archetype the brief names *"The Assay Below the Waterline / what the tracker can't see,"* distinct from 1.0's control console and 2.0's calibration bench. The hero is **invisibility, not a lever**. A lit, smug **MACRO TRACKER** sits at the top (`PROTEIN ✓ 180 g · FAT ✓ 70 g · CARBS ✓ 230 g` + a rotated **DAY COMPLETE** stamp), its ticks deliberately **amber, not cyan** — seductive-but-incomplete. Three sensor probes drop from it and stop dead at a hard horizontal **SENSOR LINE** engraved `LIMIT OF WHAT THE TRACKER SEES` (above = MONITORED, below = UNSENSED) — the single most important compositional element, the line the eye is meant to cross and feel the drop. Below it, the dim field wakes to cyan only where it's fed: **left = the OMEGA-3 GANTRY** (food-vehicle intake rows salmon / ikan kembung-mackerel / sardines / tamago-roe with the phospholipid-uptake flag; two cyan output nodes DHA (brain ≈ 60% fat, retina) and EPA (TG ↓ 25–30%, BP↓, recovery); a near-shut amber **ALA BYPASS** stamped `~5–10% → EPA · <1% → DHA`; an amber supplement port `count EPA+DHA grams, NOT fish-oil · 6–7 caps = 2 g`; target `FLOOR 2 g/day · 3–4 g rx`); **right = the FIBER TANK** drawn HALF-FULL (amber-hatched `MOST UNDERSHOOT BY HALF` upper zone, cyan fill below, target band `30–40 g` + `~25–30 g plateau`), splitting into a cyan **SOLUBLE** pipe (→ SCFA → **butyrate**, dropping down) and a grey **INSOLUBLE** "plumbing" pipe. **Bottom register = the GUT CULTURE BED**, a bioreactor split **sparse (≤10 plants/week, pale, hatched)** vs **dense thriving cyan (30+ plants/week)** across a `DIVERSITY > ANY SINGLE STRAIN` dial, fed by FERMENTED + POLYPHENOL inlets, with a ghosted struck-through **PROBIOTIC PILL** that never reaches the bed (`doesn't survive acid · doesn't colonise · mostly placebo`). The resolution band docks the **PREBIOTIC BOWL CARTRIDGE** (`~50 g protein · ~25–30 g fiber · ~10 plants` + tagline **ONE BOWL FILLS THE BLIND SPOT**), a **SAVOURY FIBER PLATE**, and a separately-docked amber **PSYLLIUM — DOCK ALONE** caution. The **single scarce red object** is THE ONE TRAP: the lifter's `200 g PROTEIN, 12 g FIBER` day — maxed protein above the line, a 12 g near-empty fiber tank and a dark/sparse gut below, captioned `THE TRACKER SAID YOU WON. THE GUT STARVED.` Red appears nowhere else.

## Outputs (authoritative copies in `visualization/`)

- **SVG (editable source):** `visualization/Poster — Healthy - Nutrition Part 3.0 - Omega-3, Fiber, and the Gut.svg`
- **PNG (2× = 2400×3120):** `visualization/Poster — Healthy - Nutrition Part 3.0 - Omega-3, Fiber, and the Gut.png`
- Hand-coded SVG, **portrait** `viewBox 0 0 1200 1560` (~4:5; first Nutrition poster built portrait, the depth axis is vertical so it breaks cleanly from the landscape console/bench siblings). Exactly one PNG + one SVG for this concept (clean first build — no prior poster to delete).

## Renderer & verification

- **Renderer:** CairoSVG (rsvg-convert/librsvg and Playwright unavailable in sandbox). Rendered at 2400×3120 (2× the 1200×1560 viewBox).
- **Verified:** PNG non-empty (~480 KB), correct dimensions 2400×3120, valid XML in the copied SVG. Visually inspected the full poster + zoom crops of the macro-tracker header, the sensor line + probes, both channels, the gut bed, and the bottom trap/resolution band; checkmark and arrow glyphs render.
- **Build fixes:** stray invalid hex tokens accidentally introduced while drafting (`#5d6party`, `#3a4considerbe`, etc.) were corrected; XML comment dividers using `----------` were invalid (XML forbids `--` inside comments) and were shortened; the editor/mount kept appending trailing NUL bytes that broke the parse, so the authoritative SVG was cleaned and rendered from a sandbox `/tmp` copy and then `cp`'d into `visualization/` (the file tools' Edit + mount sync corrupted the saved copy mid-run). One cosmetic pass: nudged the `· CALORIES · PROTEIN · FAT · CARBS` subtitle right so it no longer touched the bold `MACRO TRACKER` label.

## Deviations / notes

- **Palette source:** the brief's verbatim "Clinical Nocturne" palette is authoritative (ink `#0B0F14`, cyan `#2DD4BF` = nourishing/fed/alive, amber `#E8A23D` = seductive-but-incomplete, one red `#FF5C5C` = the single trap, dim grey = unsensed). `aether-call-to-action-DESIGN.md` is a generic dark-UI token template; only its type intent (Inter display / JetBrains Mono labels) was used.
- **§7 traps avoided:** no gut-health cartoon kit (smiling stomach, good-vs-bad-bacteria army, fiber-broom, yoghurt splash); the bowl is an instrument **cartridge**, not a food-blog flat-lay; "30 plants" rendered as **bed density**, not a 30-icon sticker grid; the top panel kept **amber** (the green tick is the trap, never coded as the good colour); no sibling redraw (new depth/visibility axis + living substrate + resolution cartridge); exactly one red object, no red-flooding.
- **Malaysian context kept on-brand:** ikan kembung / sardines / tamago for omega-3; beans/lentils + roasted sayur in the savoury plate.
- **Path reconciliation:** the scheduled task's hard-coded `local_…/outputs` tracker path is unreachable from run sessions (verified again this run); the connected-folder `concepts/` + the two trackers are the source of truth, with build/scratch copies in the run-session outputs folder.
- **Next up (Daily):** **Nutrition Part 4.0 — Calorie Management: Bulk, Cut, Reverse** (the steering article — when to bulk / cut / reverse; keep locked Clinical Nocturne, new instrument distinct from this depth-assay, likely a state-selector / energy-balance directional device, not a waterline). Then Part 5.0 — The Weekly System closes the Nutrition track and the Healthy pillar.
