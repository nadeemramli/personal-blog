---
date: 2026-06-23
type: blog-viz-poster-record
---
# Blog Viz Poster — 2026-06-23

- **Source brief:** `concepts/Visualization Concept — Attractive - Appearance Part 3.0 - Hair Biomechanics & The Blueprint Cut.md` (dated alias: `concepts/blog-viz-2026-06-23-part-3-0-hair-biomechanics-and-the-blueprint-cut.md`)
- **Article:** Attractive pillar · Appearance track · **Part 3.0 — Hair Biomechanics & The Blueprint Cut** (Part 3 of 7)
- **Confirmed via:** `Tracker — Blog Viz Daily.md` named-next-up after Appearance Part 2.0 ("Next up = Part 3.0 — Hair Biomechanics & The Blueprint Cut"). Brief is today's most-recent concept file.

## Visual concept used

The locked Attractive-pillar style ("Architect's Elevation / Spec Sheet") in its **SURVEY-DRAWING variant** — a barber's "Blueprint Cut" working drawing of *the reader's own head*, drawn the way a mechanical part is drawn. Portrait 1200×1500 on bone drafting-paper with a faint dot grid and drafting border. **VIEW 1 · PLAN — THE SITE SURVEY** is a top-down crown circle carrying the measurable biology in terracotta: the clockwise whorl spiral (`94% clockwise`), a radiating growth-direction flow field, cowlick carets (`won't lie = biology, not failure`), the front growth angle that sets the part, and a flat-occiput note for the Malaysian-male case. A dashed leader carries the eye **survey → spec** down to **VIEW 2 · ELEVATION — THE SPEC**: the face drawn as pure geometry (ellipse + centre-line + faint mirror-flip asymmetry ghost), with a hatched `+WEIGHT` wedge on the softer side, a combed `CLEAN / TIGHT` stronger side, a `≤ 1–2 cm · counter-balance, NOT concealment` dimension tick, guard-number callouts, and the face-shape glyph row flagged in slate-blue as `a strong default, not a law` (the article's "convention, not law"). Bottom-right docks the **5-line barber-script title-block**; a rakish terracotta **7-DAY MIRROR TEST · NO product = PASS** inspection stamp overprints its corner (the article's only KPI). The single restrained red is reserved for the ghosted **REJECTED** phone showing someone else's head ("not your biomechanics · it worked on their head — yours is a different drawing"). Left rail = the warm-biology / cool-convention epistemic key; right rail demotes the Andre Walker chart to a thin `STOCK — WALKER TYPE · most MY men 1A–2B` materials note. Headline **"CUT THE HEAD YOU HAVE."**; thesis lockup **"SURVEY FIRST. CUT SECOND."**

Sits as the deliberate sibling to Appearance Part 1.0 (which used the *elevation* half of the family); 3.0 uses the *survey/spec* half — same bone palette, same warm/cool coding, same single-alarm-red discipline, new hero object. All §7 traps avoided: no grooming portrait (the only face is the rejected phone), no Walker-chart hero, skull rendered as engineering survey not phrenology, and the blueprint is annotated to the reader's own head rather than decorative wallpaper.

## Outputs (in `visualization/`)

- SVG: `visualization/Poster — Attractive - Appearance Part 3.0 - Hair Biomechanics & The Blueprint Cut.svg`
- PNG: `visualization/Poster — Attractive - Appearance Part 3.0 - Hair Biomechanics & The Blueprint Cut.png`

## Render notes

- **Renderer:** CairoSVG 2.x (Playwright + rsvg-convert unavailable in sandbox). Generator: `gen_poster_hair.py` (code → SVG → PNG, no external design tools).
- **Dimensions:** portrait viewBox 1200×1500, rendered @2× → **2400×3000**, ~497 KB. Verified non-empty, correct dimensions, visually inspected.
- **Fonts:** Inter/JetBrains-Mono stacks with DejaVu Sans / DejaVu Sans Mono fallback (sandbox fonts).
- **Build fix after first render:** lower ELEVATION view + face-shape convention strip were colliding with the footer band; moved the face ellipse up (center 1040→998, ry 160→150) and pinned the face-shape glyph strip at y≈1206 to clear the divider.
- **Deviations / fallbacks:** none. Fresh build — no prior poster existed for this concept (no deletes needed; exactly one PNG + one SVG kept). The `aether-call-to-action-DESIGN.md` token file is a generic dark-UI template, so the brief's own §5 palette was used as the authoritative source (bone `#F4F1EA`, ink `#1E2024`, terracotta `#C2703D` = biology, slate `#5E7585` = convention, red `#D9483B` = the rejected phone only).

**Next up (per Daily tracker):** Part 4.0 opens the next Appearance node; keep distinct from this survey/spec drawing.
