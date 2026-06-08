---
draft: true
date: 2026-06-05
---
# Blog Viz Poster — 2026-06-05 (second of the day) · Attractive / Hair Part 2.0 — The Stack and the Routine

- **Source brief:** `concepts/Visualization Concept — Attractive - Hair Part 2.0 - The Stack and the Routine.md` (in the connected blog folder)
- **Article:** Attractive pillar · Hair track · **Part 2.0 of 3 — The Stack and the Routine** (the final Hair article; the execution payload of the 3-part series)
- **Note:** Today's *first* run already postered Hair Part 1.1 (recorded in `blog-viz-poster-2026-06-05.md`). Hair 2.0 was the most-recently-modified concept brief (05:38) and had no existing poster, so it was the next target. This record is suffixed to avoid overwriting the earlier 06-05 run.

## Visual concept used
Third Attractive-pillar poster, second on the Hair track — reuses the **locked Attractive "Architect's Elevation / Spec Sheet"** signature (bone paper `#F4F1EA`, graphite ink `#1E2024`, terracotta `#C2703D` = built/load-bearing/living, slate-blue `#5E7585` = measurement & schedule only, single alarm red `#D9483B` reserved for the breach interlock + the foundation-crack note, ghost-grey `#9A958C` for the fixed follicle substrate and the disconnected systemic mains). Sub-archetype is the natural sequel to 1.1's *condition survey*: **a build-up / assembly section read bottom-to-top for hierarchy and timed top-to-bottom on a phasing rail for the day's sequence.**

The hero is the assembly itself, seated on a ghosted follicle substrate (the 1.1 callback, "still left of the line"): a deliberately **enormous terracotta FOUNDATION SLAB — THE 90% (adherence + the diagnostic loop)** that dwarfs everything above it (the proportion *is* the argument), carrying the **TIER-1 PHARMACY SPINE** (four solid course-stones: oral minoxidil 2.5–5 mg · topical minoxidil 5% + tretinoin 0.025% · ketoconazole 2% · alpha-estradiol 0.025%, doses as cool dimension ticks), then a thin hatched **MECHANICAL MEMBRANE** (microneedling / scalp massage / LLLT) drawn as a multiplier interlayer with × glyph and up/down "amplifies both" gain arrows, then a lighter, dashed, inset **TIER-2 RESEARCH STACK** (RU58841 · MK-677 [cycle clock] · GHK-Cu · KPV) that reads as removable. Branching off to the left: the **LOCAL-LOOP detail** (closed warm loop at the scalp, systemic mains drawn ghosted + cut with a break symbol, protected "upstairs" room = allopregnanolone/mood/drive — the finasteride-exclusion reasoning in one architectural gesture), and above it the **single red BREACH INTERLOCK** (sealed-vs-needled pictogram, `MICRONEEDLE NIGHT = TOPICALS OFF · resume +24 h · RU58841 +48 h`, red leader to the membrane: "a needled scalp turns a LOCAL topical SYSTEMIC"). A full-height **PHASING RAIL** runs down the right margin with the **dry-time clearances drawn as literal dimensioned empty gaps** (RU58841 → dry 15–20 min → minoxidil → dry 10 min → tretinoin; M/W/F ketoconazole; weekly microneedle = topicals off) under an AM/PM-split bracket. Lower-third spec sheet = the impact/leverage ladder (early · adherence · Tier-1 · mechanical · Tier-2 · transplant) + a 90/10 proportion bar. Bottom lockup `GET THE 90% RIGHT, THEN LAYER THE 10%.` + three register-coded chips `STACK BY LOAD` (warm) · `APPLY IN SEQUENCE` (cool) · `NEVER BREACH THE LOOP` (red).

Headline = the brief's flagged-strongest option, `A STACK IS A BUILDING, NOT A LIST.` Orientation = **portrait** `viewBox 1200×1580` (opposite to 1.1's landscape survey — the hero is a vertical build-up, per §3). §7 avoided: no flat bottle/compound list, no circular routine clock; the 90% slab is visually dominant and the interlock is the single hardest mark on the page.

## Outputs (in `visualization/`)
- PNG: `visualization/Poster — Attractive - Hair Part 2.0 - The Stack and the Routine.png`
- SVG: `visualization/Poster — Attractive - Hair Part 2.0 - The Stack and the Routine.svg`

## Renderer & verification
- **Renderer:** CairoSVG (pip-installed in sandbox; rsvg-convert / Playwright not needed).
- **Verified:** PNG renders at 2400×3160, ~527 KB, non-empty; read back and visually inspected. One layout fix applied after first inspection — the AM/PM-split bracket on the phasing rail was overrunning the right drafting border, so the rail was shifted inward (axis x 1020 → 998) and the bracket label re-anchored inside the frame. No clipping or dead space in the final.
- No prior Hair 2.0 poster existed, so no delete was required (exactly one PNG + one SVG for this concept).

## Deviations / fallbacks
- None of substance. Fonts: brief/design.md specify Inter (display) + JetBrains Mono (labels); the render host has DejaVu substitutes (declared in the font stacks) — re-render on a host with Inter + JetBrains Mono for a 1:1 match.
- Path-reconciliation policy still applies: the scheduled-task file's hard-coded `local_*` outputs path is unreachable from the run session; the connected `blog viz daily - temporary/` folder is the live source of truth (concept read from `/concepts/`, outputs written to `/visualization/`, record here, tracker row appended).
