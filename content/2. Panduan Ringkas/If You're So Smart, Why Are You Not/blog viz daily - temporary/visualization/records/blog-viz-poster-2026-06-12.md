---
date: 2026-06-12
draft: true
---
# Blog Viz Poster — 2026-06-12

- **Source brief:** `concepts/Visualization Concept — Fit - Part 4.4 (Performance Enhancement) - Electrolyte Management.md` (dated 2026-06-12; cross-checked against Tracker — Blog Viz Daily, which logs Part 4.4 as today's run)
- **Article:** Fit pillar / Performance Enhancement track / Part 4.4 — Electrolyte Management (5th article of the "Protection & the toolbox" sub-arc)
- **Outputs:**
  - `visualization/Poster — Fit - Part 4.4 (Performance Enhancement) - Electrolyte Management.png` (3840×3080, ~713 KB)
  - `visualization/Poster — Fit - Part 4.4 (Performance Enhancement) - Electrolyte Management.svg` (raw source, landscape viewBox 1920×1540)
- **Renderer:** CairoSVG @2× (Playwright and rsvg-convert unavailable in sandbox); XML validated; full view + 5 crops read back visually before finalizing.

## Visual concept used

The locked Fit "Engineering Diagnostic Instrument" style, new sub-archetype = **FLUID-BALANCE REGULATION STAND / two-compartment hydraulic bench** (the first and only hydraulic instrument in the PE set). Center-left hero = the two-compartment vessel: a bright teal INTRACELLULAR core (`KEEP FULL · fullness · pump · hard muscle`, with a FULL→FLAT level gauge) inside a dim EXTRACELLULAR shell (`KEEP LOW · bloat · BP water`), fed by a consistency-governed inlet (`sip steadily` vs a ghosted, crossed-out amber `chug-and-starve → vasopressin pauses filtration`) and drained through the SODIUM aldosterone float valve, drawn in its good state (open, flushing, green). Upper-center = the loud COUNTERINTUITION inset: two paradox vessels side by side (CUT SALT → float low → ALDOSTERONE HIGH → drain CLAMPED → shell puffy, all amber; CONSISTENT SLIGHT SURPLUS → ALDOSTERONE LOW → drain open, continuously flushing, cheat/refeed passes through, green) under the hero lockup banner `CUT SALT → ALDOSTERONE HIGH → YOU HOLD WATER. / STEADY SURPLUS → ALDOSTERONE LOW → YOU FLUSH.` Right column = POTASSIUM as a glycogen-geared fill valve (gear ratio plate `≈10 mg K per 1 g carb`, food-source dial white rice ~1 vs sweet potato ~20 mg/g) terminating in the page's ONE red object, the HYPERKALEMIA INTERLOCK (ARB/MRA in stack → DO NOT mega-dose K). Right-center = the MAGNESIUM⇄CALCIUM antagonist balance beam (relax/eccentric vs contract/concentric, Mg self-limiting bowel-tolerance dial, Ca timed-release rule). Left flank = the CONVERGENCE MANIFOLD (aromatizing+GH, dry vs wet, diuretics, clen, carb↔keto, Malaysian heat) under the law plate `SET LAST · REVISIT OFTEN`. Foot = full-width FORMULA PLATE (five per-bodyweight setpoint cells), RATIO SELECTOR (CARB vs KETO bar presets re-proportioning Na:K:Mg:Ca), and WORKED EXAMPLE chip with the Malaysian-tax callout. Footer law: `YOU DON'T CHASE WATER OR STARVE IT — YOU REGULATE THE BALANCE.`

Three-state semantic palette per the brief: teal `#36C9C0` water through-line, warm amber `#E3B23C` sodium/setpoint + all cautions, green `#58B368` rationed to the flushing/open state, cool/warm `#4F8FC9`/`#C97B3E` for the Mg/Ca antagonism, red `#E5484D` on exactly one object (the K×ARB interlock). §7 respected: no pill grid, no single tank, no "less salt = drier" arrow, red not flooded, no hydration-photo, formulas live inside the instrument as dials/cells.

## Deviations / notes

- Fonts fall back to DejaVu Sans / DejaVu Sans Mono in the sandbox (Inter/JetBrains Mono unavailable) — sanctioned fallback.
- The brief's `⇄` glyphs were rendered as `↔` / `/` in mono labels for glyph-coverage safety.
- The outputs-folder SVG was twice truncated at the tail by mount sync after edits; tail re-appended via bash and XML re-validated before each render (same known issue as prior runs).
- Iteration fixes after visual inspection: ghost chug-and-starve label moved off the deck line, CHEAT/REFEED tag un-clipped and moved inside the inset panel, `shell dry` label moved out of the core into the shell band, CARB ratio bars rescaled to stop poking through the panel title, core level gauge added to fill dead space.
- No prior poster existed for this concept → no deletes needed (one PNG + one SVG rule holds).
