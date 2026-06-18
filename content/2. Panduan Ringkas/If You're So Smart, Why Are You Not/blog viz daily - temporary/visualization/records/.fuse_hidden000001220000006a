---
title: "Blog Viz Poster Record — 2026-06-10 (re-render · Cycle Design)"
date: 2026-06-10
---
# Blog Viz Poster — 2026-06-10 (second run of the day · re-render)

> **Supersedes** the 01:42 Cycle Design poster logged in `blog-viz-poster-2026-06-10.md`. Same concept, re-rendered cleaner; the PNG + SVG in `visualization/` were overwritten in place (one PNG + one SVG per concept — no orphaned variants).

- **Source brief:** `concepts/Visualization Concept — Fit - Part 3.2 (Performance Enhancement) - Cycle Design.md`
- **Article:** Fit pillar -> Performance Enhancement track -> **Part 3.2 — Cycle Design** (closes the 3-part "Optimize" sub-arc: 3.0 mechanism -> 3.1 lineage -> 3.2 time)
- **Style:** Engineering Diagnostic Instrument (locked, Fit pillar)
- **Sub-archetype:** Annual Operating Schedule / forward mission-plan — landscape Gantt with a body-fat gate trace. New within the PE set (after 1.0 authorization console, 2.0 calibration bench, 2.1 telemetry strip-chart, 3.0 mixing console, 3.1 derivation tree).

## What changed vs the 01:42 version
- **Canvas:** 1920x1200 viewBox @2x -> 3840x2400 (was 1680x1060 -> 3360x2120). Larger, more breathing room.
- **Palette discipline:** locked strictly to the design-token semantics — dark ground `#0A0D12`, green `#4FBE7B` for the gate band + in-range trace, red `#E5484D` for the ONE breach, amber `#E3B23C` for every other caution, plus a quiet instrument-blue `#5AB6D6` for the blood-checkpoint family. Dropped the earlier version's violet/blue phase accents so the three-state status logic (green = the envelope you keep, red = the one rule, amber = the judgement calls) reads cleanly per the brief's §5.
- **Mono/display roles** per design.md: Inter display for the headline + phase names, JetBrains Mono for every technical label/tick.

## Visual concept used
A landscape annual operating schedule. A single bold horizontal **year axis** (M0 -> M12, M3/M6/M9/M12 majors) carries two vertically-aligned coupled lanes. The **PHARMACOLOGY lane** (above) runs the four-phase loop at honest proportional widths — PREP (narrow) -> BLAST off-season (the long "ON" ~8 mo, widest, with an amber "-> calculated unhealthiness = cue to CRUISE, not push harder" cue) -> CUT (dry compounds) -> **CRUISE/DOWN-PERIOD drawn as a TRUE ~quarter (3-4 mo)** with a ghosted amber-dashed "4-wk break = a clean-out, not recovery" stub beside it so "clearing != restoring" reads as a length difference, captioned "~4-6 wks just to CLEAR; months to NORMALISE." The **FOOD lane** (below) shows lean-bulk ~75% / cut ~20% / maintenance ~5% with an 8-week continuation check + refeed ticks; the coupling note "food is the lever you pull most — the drug lever only when extra food turns to FAT" sits between the lanes.

The **load-bearing device** is the body-fat gate trace threaded across the top: a continuous green line caged between a green 8-12% push band and a hard red ~15% ceiling. The single red object is a dashed branch **breaching the ceiling into the MICHELIN-MAN zone** ("insulin sensitivity craters - the surplus now HINDERS the muscle the drugs are paying for"), while the recommended solid trace is pulled back under the line by a green "cut at ~15-17%" arrow. A green/amber dashed **return-arrow loop** ("push -> pull back -> repeat") closes the cycle beneath the food lane. q3-month **blood-checkpoint flags** are pinned on the year axis.

Docked right: the **adjustment ladder** (read bottom->top — 1 ADD FOOD -> 2 ADJUST TRAINING -> 3 RAISE THE DOSE last; drugs at the top rung, crowned "MILK THE DOSE"; gate notes "only when extra food makes FAT, not size"; "add ONE compound at a time - bloods 4 wks in - bioidentical-first Test->GH->Insulin - exotics last"), the **q3-month blood-checkpoint plate** (Cystatin C / ALT-AST 7-day rule / thyroid triad / SHBG / prolactin+cortisol + "a marker deviates -> the cycle bends or stops, regardless of the mirror" law). Bottom band grace-notes: a **wet/dry tuning dial** ("a SETTING, not a property — a DHT derivative is the dial"), the **80% retention** step-down chip, and a "what the whole schedule says" recap. Footer bridges forward: protection stack always-on (Part 4), full week-by-week build -> Part 5.1.

## Outputs
- SVG: `visualization/Poster — Fit - Part 3.2 (Performance Enhancement) - Cycle Design.svg`
- PNG: `visualization/Poster — Fit - Part 3.2 (Performance Enhancement) - Cycle Design.png`

## Render & verification
- **Renderer:** CairoSVG (rsvg-convert / Playwright unavailable in sandbox; CairoSVG installed via pip).
- **PNG:** 3840x2400 px (2x of the 1920x1200 viewBox), ~635 KB — passes non-empty / >50 KB / correct-dimension checks. XML validated well-formed before render.
- Visually inspected full poster + two zoomed crops (body-fat envelope/breach and the right-rail ladder + blood plate). Both densest regions legible; trace reads as caged with the single red breach piercing the ceiling, ladder reads bottom->top with drugs last.
- **Mid-edit truncation:** the connected-folder/scratch mount truncated the SVG tail at an em-dash byte boundary during one Edit (the same failure flagged on the 06-08 run); the footer tail was re-appended via bash and re-validated well-formed before the final render.

## Deviations / notes
- This is the SECOND run of 2026-06-10 for the same brief — a re-render that overwrote the earlier (01:42) poster's PNG + SVG using the identical proper names, leaving exactly one PNG + one SVG (delete-first rule satisfied by in-place overwrite).
- `aether-call-to-action-DESIGN.md` is the generic Aether CTA template; the Fit "Engineering Diagnostic Instrument" semantics were taken from the design tokens (ground/Inter/JetBrains Mono/semantic states) + the locked PE-set conventions, as on prior Fit runs.
- Landscape orientation per the brief (year axis is horizontal); distinct from 2.1's landscape strip-chart by being a planned segmented Gantt, not a recorded signal.
- Path-reconciliation policy holds: the scheduled-task file's hard-coded `local_dbaa9cdd` outputs path is unreachable from the run session; the connected `blog viz daily - temporary/` folder is the source of truth.
