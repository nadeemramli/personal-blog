---
date: 2026-06-24
type: blog-viz-poster-record
---

# Poster Record — Attractive · Appearance Part 7.0 (the CAPSTONE)

**Date:** 2026-06-24 (2nd poster of the day — Part 6.0 was built earlier; this record is suffixed so it does not overwrite `blog-viz-poster-2026-06-24.md`).

**Source brief:** `concepts/Visualization Concept — Attractive - Appearance Part 7.0 - The 1% Cleanliness Audit and The Foundation Gate.md` (canonical) — also aliased as `concepts/blog-viz-2026-06-24-part-7-0-the-1-percent-cleanliness-audit-and-the-foundation-gate.md`. Located in the connected blog folder. Confirmed as today's brief: most-recently-modified concept file, and logged in `Tracker — Blog Viz Daily.md` as the named next-up after the 2026-06-24 Part 6.0 run.

**Article:** Attractive · Appearance — **Part 7 of 7, the CAPSTONE that completes the Appearance track.** `Part 7.0 - The 1% Cleanliness Audit & The Foundation Gate.md`.

## Visual concept used

A **landscape Commissioning & Run Schematic** — the seventh and final sub-archetype of the locked "Architect's Elevation / Spec Sheet" pillar style. Where Part 5.0 owns the *static* QC audit-sheet, 7.0 is the *dynamic run/commission diagram*: a plant run-diagram of the assembled "Appearance machine" governed by an upstream pass/fail intake **GATE** and wrapped by a recurring maintenance **LOOP**, with a ghosted **decay-shadow** below.

Left-to-right the plate reads: a far-left **epistemic key** (warm = measurable & yours · cool = convention/benchmark · grey = decayed · amber = grace-note caution · one red = the single alarm); a left-third **GATE — the prerequisite** rendered as a descending **surplus subtraction manifold** (MONTHLY INCOME draining through five slate-tagged tap-offs — health, rent ≤30%, bills/transport/insurance, emergency 3–6 mo, retirement ≥10–15% — into a warm **= SURPLUS** reservoir), a **comparator** weighing surplus against the machine RUN-COST (RM 500–1,500/mo), and a **gate valve** with two outcomes (OPEN warm → full fuel + the dating outlet; HELD grey → thin substrate-bypass trickle), beside a numbered 1–7 **commissioning-order ladder**; a centre **MACHINE + FLOOR** = a small sealed two-tier core (SIGNAL tier over SUBSTRATE slab, "PARTS 1–6 · SEALED") on a baseplate "THE FLOOR", wrapped by a warm clockwise **maintenance LOOP** carrying the six Sunday-reset stations (shoes · wardrobe scan · vehicle/bag · wallet · nails/grooming · screens & crystals), a **× multiplier** glyph at the top, a **levelling bar** ("UPGRADE EVENLY"), the cadence stamp "30 MIN · SAME DAY EACH WEEK", and a 4-zone **1% detail rail** (FACE · HAND · CLOTHING · METAL & LEATHER) hanging off the loop under the output; a right-edge **OUTPUT terminal** "RUNS FROM STRENGTH, NOT COMPENSATION" lit only when GATE OPEN ∧ LOOP INTACT; a lower **ghosted decay-shadow** band (the same machine with the loop severed, grey within 6 months — scuffed shoe, frayed strap, greyed sneaker, stained lapel, overgrown neckline, "BUILT-AND-DECAYING"); and a full-width bottom lockup **"BUILD THE MACHINE FIRST."** + thesis **"MAINTENANCE IS THE MULTIPLIER · THE GATE IS THE PREREQUISITE."**

**The ONE red** (the only alarm): a failure-mode inset at the gate — a hand cranking the valve **FORCED OPEN** on a LOW surplus reading, blowing out the red **DATING (7)** outlet while the financial footing erodes grey beneath: *"STRETCHED BALANCE SHEET — romance bought without a buffer is a liability."* Everything else stays calm: the held gate is neutral, the decay-shadow is grey (neglect, not alarm), and the two grace-notes (CONSPICUOUS ≠ SOLVENT; the RM 8,000-watch / RM 30-frayed-wallet mismatch) are amber. Exactly one red, located at the prerequisite half — the maintenance half's failure is the grey decay-shadow, keeping palette discipline.

Palette used verbatim from the brief §5: bone `#F4F1EA` · graphite `#1E2024` · terracotta `#C2703D` (measurable & yours) · slate `#5E7585` (convention) · dim grey `#A39D92` (decayed) · one red `#D9483B` · amber `#C9912E` (grace-note). §7 traps avoided: no Sunday-cleaning flat-lay / grooming still-life (maintenance is a recurring run-loop operator, not a product shot); no redraw of 5.0's QC audit-sheet (verb = RUN, not INSPECT — gate + recirculation loop + decay-shadow); no finance cliché (the gate is an intake valve + surplus comparator + subtraction manifold, the %-targets read as cool convention, not law); no red-flooding or mislocated red.

## Outputs

- **SVG (editable source):** `visualization/Poster — Attractive - Appearance Part 7.0 - The 1% Cleanliness Audit and The Foundation Gate.svg`
- **PNG (deliverable):** `visualization/Poster — Attractive - Appearance Part 7.0 - The 1% Cleanliness Audit and The Foundation Gate.png`
- Generator script: `gen_poster_70.py` (kept in the run-session outputs scratch folder).

## Renderer & verification

- **Renderer:** CairoSVG 2.9.0 (Playwright + rsvg-convert unavailable in the sandbox this run; installed CairoSVG via pip). Fonts: Inter / JetBrains Mono fall back to DejaVu Sans / DejaVu Sans Mono — consistent with every prior sibling in this set.
- **Canvas:** landscape `viewBox 0 0 1600 1000` (16:10), rendered at 2× → **3200 × 2000 px**, ~438 KB. Verified non-empty, correct dimensions, well above the ~50 KB floor.
- **Visual inspection:** read back the full preview plus three zoom crops (gate, machine, right/decay). Fixes applied during iteration: switched arrow markers to `userSpaceOnUse` (arrowheads were scaling with stroke-width and rendering oversized); replaced ①②③ header glyphs (tofu in DejaVu) with hand-drawn circled numbers; separated the × multiplier glyph from the SHOES station node at the loop top; relocated the 1% detail rail to a panel under the output to clear the right-side station labels; moved the loop direction arrows into the gaps between stations. Repaired a truncated final line in the generator before the final render.

## Deviations / fallbacks

- Brief's §5 locked palette treated as authoritative; the `aether-call-to-action-DESIGN.md` token file is a generic dark-UI template and was not used for colour (same convention as all prior Appearance siblings).
- Record filename suffixed with the concept slug because `blog-viz-poster-2026-06-24.md` already exists (Part 6.0 was produced earlier the same day).
- Fresh build — no prior Part 7.0 poster existed, so no delete was required; exactly one PNG + one SVG kept in `visualization/`.

**This completes the 7-part Appearance track.**
