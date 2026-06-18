---
draft: true
date: 2026-06-08
pillar: Fit
track: Performance Enhancement
part: "3.0"
title: The Eight Anabolic Pathways
---

# Blog Viz Poster — 2026-06-08 — Fit / PE Part 3.0: The Eight Anabolic Pathways

- **Source brief:** `concepts/Visualization Concept — Fit - Part 3.0 - The Eight Anabolic Pathways.md` (in the blog folder; modified today 05:38, most recent concept — confirmed not yet postered before this run).
- **Article:** Fit pillar · Performance Enhancement track · Part 3.0 — opens the "Optimize" sub-arc (4 of 15 in the PE track).
- **Outputs:**
  - PNG → `visualization/Poster — Fit - Part 3.0 - The Eight Anabolic Pathways.png`
  - SVG → `visualization/Poster — Fit - Part 3.0 - The Eight Anabolic Pathways.svg`
- **Renderer:** CairoSVG (pip-installed; rsvg-convert unavailable in sandbox). Rendered at 3840×2720 (2× the 1920×1360 viewBox), ~445 KB. Read back full + two region crops (channels L, channels R + master) and inspected; one revision pass applied.

## Visual concept used

Locked Fit **"Engineering Diagnostic Instrument"** style; **new sub-archetype = a multi-channel mixing console / mixing desk** — deliberately distinct from the prior PE instruments (1.0 authorization console, 2.0 calibration bench, 2.1 telemetry strip-chart). **Landscape `viewBox 1920×1360`** (a console is natively horizontal; also the deliberate flip back to landscape after 2.0's portrait certificate, giving the PE set rhythm).

The poster renders the article's controlling thesis — *building muscle on enhancement is a mixing job, not a power-lifting job* — as a control surface. Left spine = the **90/10 POWER RAIL**: a labelled ON power switch fed by `BASELINE SIGNAL IN — training · calories · protein · sleep`, feeding a green **MASTER BUS** that runs under all channels, so the eight faders visibly do nothing without the baseline signal (the prerequisite made structural, "the pathways are the MARGIN"). Centre hero = **six channel strips** (the eight pathways, with ⑤+⑥ cortisol combined and ⑦+⑧ GH·IGF-1·Insulin combined into one wider *fenced/gated* strip). Each strip carries: channel number + pathway + receptor, a **direction glyph** (RAISE / HOLD in window / BLOCK / POWERFUL), a **fader parked inside a green target window** (HOLD channels — SHBG, ER — get amber caution zones at *both* extremes so "crush it" and "overdo it" both read wrong), a family tag chip (T / DHT / E2 / 19 / gated), the by-the-job compound, and the OTC **TRIM** knob (the only place doses appear). The eight direction glyphs deliberately point different ways — the teaching object that corrects "more = better." Right = the **MASTER · NET MUSCLE** payoff: two comparison meters, `EIGHT, NUDGED` (tall, green, clean) vs `ONE, SLAMMED` (shorter + a red **CLIP** cap), the counter-intuitive height inversion landing pre-attentively, plus the `CHOOSE BY JOB, NOT HYPE` routing plate.

**Failure state** integrated on the same board (not a separate panel): faint dashed ghost caps show ① railed to the top (red) and ②–⑧ dead at the bottom (grey), the PR/ER **over-drive LEDs** ("OD", amber) lit, and the master clipping red — captioned at the footer.

**Color discipline (per §5/§7):** red rationed to exactly the one master clip; **amber** carries all caution (HOLD-channel extremes, the two OD LEDs, the gated fence, the routing plate); green = in-window + baseline signal + the clean master. Shape/position encode RAISE/HOLD/BLOCK independent of hue, so the board survives grayscale. §7 respected: no receptor/biology diagram, no flat drug-list grid, no uniform all-up equaliser, failure state is a faint overlay on the same console rather than a red-flooded "bad" panel.

## Verification notes

- Parse-checked the generator (`ast.parse` OK) and verified PNG dimensions/size programmatically.
- **Revision pass:** initial render had the fader tracks starting too high (running through the direction-pill text) and the over-drive LEDs colliding with the pills. Fixed by dropping the track top to below the pills and relocating the OD LEDs to the top-right of each fader region with an "OD" label. Re-rendered and re-inspected — clean.
- Minor copy fix: "AIs" → "AI sparingly + SERMs" (capital-I/lowercase-l ambiguity in Inter rendered "AIs" as "Als").

## Deviations / fallbacks

- None on content. The `aether-call-to-action-DESIGN.md` tokens file is a generic web-component spec, so (as with all prior Fit posters) the palette was taken from the locked Fit "Engineering Diagnostic Instrument" precedent (dark console ground; green/amber/red semantic roles), with the design tokens supplying the type roles (Inter display + JetBrains Mono labels) and semantic success/caution/danger mapping.
- **Sandbox/mount sync hiccup (noted, not a content issue):** mid-edit, the connected-folder mount truncated the generator file at line 335 (an em-dash byte boundary); the missing tail was re-appended via bash and the file re-parsed clean before final render.
- No prior poster existed for this concept, so no delete was required (only one PNG + one SVG now present).
