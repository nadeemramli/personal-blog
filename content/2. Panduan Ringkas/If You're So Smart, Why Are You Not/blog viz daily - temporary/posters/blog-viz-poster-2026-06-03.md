# Blog Viz Poster — 2026-06-03

- **Date:** 2026-06-03
- **Source brief:** `Visualization Concept — Fit - Part 3.1 (Athletic) - Power, Speed and Agility.md`
  - Path: `…/blog viz daily - temporary/concepts/`
  - Modified 2026-06-03 00:37 (today's brief; cross-checked against `blog-viz-tracker.md`, which logs "Part 3.1 - Power, Speed and Agility.md (Athletic track)").
- **Article:** If You're So Smart, Why Are You Not → **Fit** pillar / **Athletic** track / **Part 3.1 — Power, Speed & Agility**
- **Design tokens:** `aether-call-to-action-DESIGN.md` (Aether — near-black surface #050507/#0A0A0D, text #FFFFFF / #A1A1AA, border #71717A; Inter display+body, JetBrains Mono labels).

## Visual concept used

Hand-coded **oscilloscope / signal-tuning bench** (the locked "Engineering Diagnostic Instrument" Fit style, in a sub-archetype no prior Fit poster has used: force plotted against *time in milliseconds*, plus a hard safety interlock). The hero is an **RFD oscilloscope** — a force-vs-time trace where a steep, early **EXPLOSIVE** curve (phosphor-green live signal) sits *above* a tall-but-lazy **STRENGTH** curve (muted steel-blue) inside a shaded **0.1–0.3 s contact window**, carrying RFD = ΔForce ÷ Δtime = the slope, not the peak. Paired with a **force-velocity tuning chart** (ghosted "before" curve, raised solid "after" curve, green raise-arrow + velocity-shift arrow, two training zones). Below: the **three output channels** (POWER / SPEED-as-two-skills / AGILITY-as-brakes-first-3-rung-ladder) sharing one "phosphagen + Type IIx" input rail, each with prescription chip and benchmark tag; the **elastic engine** (SSC three-beat timing diagram with a hazard-hatched short amortization gap + an RSI dial gauge reading strength-dominant ↔ elastic-dominant); a hard amber **safety interlock** gating high-intensity plyos behind the 1.5× BW squat + balance prerequisites, with a green bypass lane for low-intensity plyos; and a footer scoreboard strip + the closing law "POWER = STRENGTH EXPRESSED FAST." Warning/danger color (amber) rationed to the interlock only, per the brief.

## Outputs

- **SVG:** `poster-2026-06-03-power-speed-agility.svg`
- **PNG:** `poster-2026-06-03-power-speed-agility.png`
- Both saved to the session outputs folder and copied to `…/blog viz daily - temporary/posters/` for persistence and downstream pickup.

## Render & verification

- **Renderer:** CairoSVG (preferred Playwright/Chromium and rsvg-convert were both unavailable — `librsvg2-bin` could not be installed in the sandbox and Chromium download was skipped; CairoSVG was the working fallback in the preferred order).
- **Dimensions:** 2400 × 3000 px (2× the 1200 × 1500 / 4:5 portrait viewBox). **Size:** ~513 KB (> 50 KB threshold). Verified non-empty and correct dimensions via PIL.
- **Fonts:** Inter / JetBrains Mono are not installed in the render sandbox, so the SVG's declared fallbacks resolved to DejaVu Sans / DejaVu Sans Mono. The SVG keeps the Inter + JetBrains Mono stacks, so it will render with the correct faces on any machine that has them.
- **Visual QA:** inspected hero, F-V chart, three channels, elastic engine, interlock, and footer at full res. Fixed a duplicate FORCE axis label, F-V caption/axis collisions, and an oversized RSI dial that overran its panel; re-rendered clean.

## Deviations / notes

- **Accent color choice:** the Aether palette is essentially monochrome (primary/accent both #000000). To satisfy the brief's required "brightest live signal" / "success inside the window" reading and a "reserved warning state," I introduced a phosphor-green (#2EE6A6) live-signal accent and an amber (#F5A524) warning, both consistent with a signal-analysis bench. All neutral surfaces/type stay within the Aether tokens.
- **Duplicate output for today:** an earlier run at 01:41 today already produced a poster for this same article under the slug `power-speed-and-agility` (`poster-2026-06-03-power-speed-and-agility.{svg,png}` + its record). This 09:30 run produced `power-speed-agility` (no "and"). Both now sit in `posters/`. Left the older pair in place (non-destructive); recommend Nadeem keep one slug to avoid the downstream `blog-viz-insert-daily` task picking the wrong file.
