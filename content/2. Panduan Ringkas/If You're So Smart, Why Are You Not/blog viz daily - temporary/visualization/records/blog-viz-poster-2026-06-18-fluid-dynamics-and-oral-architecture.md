# Blog Viz Poster — Run Record

- **Date:** 2026-06-18 (third poster run of the day)
- **Source brief:** `concepts/blog-viz-2026-06-18-part-2-0-fluid-dynamics-and-oral-architecture.md` (written 10:39 — the most recently modified brief in `concepts/`, newer than that day's "The Machine and the Room" brief which was already postered at 06:53). The brief carries the full "Visualization Concept — Appearance Part 2.0: Fluid Dynamics & Oral Architecture" inside the dated `blog-viz-*` filename rather than a separate `Visualization Concept —` file.
- **Article:** Attractive · Appearance · Part 2.0 — Fluid Dynamics & Oral Architecture (Part 2 of 7). Source article: `…/Attractive/Appearance/Part 2.0 - Fluid Dynamics & Oral Architecture.md`.
- **Brief selection note:** The Daily tracker's latest *logged* run was Part 2.0 "The Machine and the Room" (Productive), but that poster already existed (PNG+SVG from 06:53, record saved). The Appearance 2.0 brief at 10:39 was the newest brief and had no poster, so it was the correct target for this run.

## Visual concept used

The **Drawdown Schematic** — a new sub-archetype inside the locked Attractive "Architect's Elevation / Spec Sheet" style (established by Appearance 1.0, where 2.0 is the engineered *section through* the substrate floor 1.0 named as load-bearing). Portrait 4:5 on bone-paper (`#F4F1EA`) with a faint blueprint grid + drafting dots and a thin drafting border with corner ticks, matching 1.0 so the two read as a set.

Hero = a strict **side-profile head-and-neck section** (right-facing, stylised as a hydraulic drawing, never a portrait) with a hatched **interstitial reservoir** ("the puff") under cheek/jaw/eye, and terracotta drainage **channels** sweeping down the neck (flow chevrons + a rotated `DOWN THE NECK · NEVER UP` annotation) into a labelled **supraclavicular DOCK** at the collarbone (`open first · close last → subclavian vein`). The four article mechanisms dock in as escalating control inputs: **A · Electrolyte Flush** (master valve, 70–80%, three-slider `Na⁺↓ K⁺↑ Mg²⁺↑` + a sectioned-coconut supply tank `air kelapa muda ~600 mg K⁺/330 ml`), **B · Diuretic + Thermal** (relief valve, 20–30%, sauna→cold + dandelion/hibiscus), the lone-red **SEALED** pharmacological-diuretic valve ("where lifters die"), **C · Lymphatic Sweep** (the manual pump; `LYMPH HAS NO PUMP — YOU ARE THE PUMP`, on-face outward-and-down sweep arrows + a graphite crossed `NEVER UP`), and **D · Oral Architecture** (a cool slate service panel at the mouth: BASELINE/DAILY/STRUCTURAL). Left rail = the **48-hour countdown dial** (T-48h→T-0, eight protocol beats ending at the dock aligned `walk in · sharpest in 48h`, + "not on a Tuesday" use-sparingly note). Top-right = the **ACUTE (lit) / CHRONIC (ghosted, "built elsewhere · Pt 1.1")** timescale toggle with the `puffy + lean = ACUTE · soft + not-lean = chronic` diagnostic. Right rail = three KPI **READOUT** gauges (AM/PM Face Δ, Waking Weight Δ "2+ kg = Na⁺ event", BOP `<10%`). Headline `SHARPEN IN 48 HOURS — NOT 48 DAYS.`; thesis lockup `DRAIN THE FACE — DON'T DRENCH IT.`; footer caption + `a puffy face on a lean person is plumbing — solved in hours, not seasons.`

Colour teaches the argument per the brief: warm terracotta (`#C2703D`) dominant = fast reversible fluid work; cool slate (`#5E7585`) = the slow structural oral layer; signal red (`#D9483B`) used **exactly once** on the SEALED valve (the cheek "NEVER UP" slash was recoloured graphite to preserve the one-red discipline; the only other red is the legend swatch that explains the convention). §7 respected: no photoreal/groomed-man face, no before/after, no glossy coconut/Waterpik/mouthwash product shot, no spa-wellness imagery, no generic timeline/"5 tips" list — directionality (down-and-out, never up) and the system-on-a-clock coupling are both load-bearing in the drawing; the pharmacological extreme is sealed in red, never glamorised.

## Output

- **Poster PNG:** `visualization/Poster — Attractive - Appearance Part 2.0 - Fluid Dynamics and Oral Architecture.png` (2400×3000, ~540 KB)
- **Raw SVG:** `visualization/Poster — Attractive - Appearance Part 2.0 - Fluid Dynamics and Oral Architecture.svg` (~26 KB)
- Poster name derived from the in-brief concept title; "&" rendered as "and" to match the established Appearance/Attractive poster naming (e.g. Part 1.0 "What Actually Matters", Hair "Body, Neck and Hands").
- No prior poster existed for this concept → no deletes (exactly one PNG + one SVG).

## Renderer & verification

- **Renderer:** CairoSVG (rsvg-convert + Playwright unavailable in the sandbox), 2× the 1200×1500 viewBox → 2400×3000.
- **Verified:** PNG non-empty (~540 KB), correct 2400×3000 dims, read back and visually inspected twice (layout balanced, no clipping, single red confined to the SEALED valve). Red-occurrence grep = SEALED-valve instrument + the legend swatch only.

## Build notes / deviations

- **Mount-sync truncation recurred** (the persistent file-tool-vs-render-mount issue): file-tool Edits/overwrites left the SVG with a lost tail and trailing NUL padding on the render mount, breaking XML parse. Fixed by writing the complete final SVG and stripping NULs in the sandbox (`tr -d '\\000'`) before the final render; the one small colour tweak (NEVER-UP slash → graphite) was applied via `sed` on the mounted file, then re-rendered.
- Layout fix during build: the coconut supply tank initially overflowed Input A into Input B → Input A box was made taller to contain the tank, B/SEALED/C re-stacked; the legend was moved off the crowded left column into the empty lower band as a horizontal "THE COLOUR IS THE ARGUMENT" strip, and a rotated neck annotation was added to use the neck's negative space and reinforce directionality.
- Path-reconciliation policy unchanged (the scheduled-task's hard-coded `local_dbaa9cdd` outputs path is unmounted; this `blog viz daily - temporary/` folder is the source of truth).
