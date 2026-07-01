---
title: "Blog Viz Poster — 2026-06-24 — Scent and Social Leverage"
date: 2026-06-24
---
# Blog Viz Poster Run — 2026-06-24

- **Source brief:** `concepts/Visualization Concept — Attractive - Appearance Part 6.0 - Scent and Social Leverage.md` (dated alias: `concepts/blog-viz-2026-06-24-part-6-0-scent-and-social-leverage.md`)
- **Article:** Attractive pillar / Appearance track / **Part 6.0 — Scent and Social Leverage** (6 of 7)
- **Pillar style:** "Architect's Elevation / Spec Sheet" (locked) — this is the **RADIATED-FIELD / THRESHOLD-PLAN diptych** sub-archetype, the pillar's first *non-object* drawing (a field + a room).

## Visual concept used

A vertical **diptych on one drafting sheet**, hinged across the middle by the refresh-kit **airlock** — the single shared object that proves the two topics are one idea. **TOP HERO = the climate-derated sillage field:** a graphite torso tech-flat with two marked pulse points, surrounded by concentric terracotta **isobars** (top / heart / base) rendered as an honest projection field (not perfume-ad swirls); a ghosted **HUMIDITY** ring balloons the base while an amber **HEAT** arrow burns off the top notes, resolving into a **50% dose dial** ("apply 50% of the European dose — the humidity does the projecting"). A cool **DAY/EVENING family selector** ("pick one, any one"), a struck "past 3 = collection" bottle shelf, and a warm **skin-chemistry decant gate** dock to either side. **MIDDLE = the refresh-kit airlock** (atomiser · mints · sanitiser) with a figure passing through, captioned "the kit that lets you cross without resetting." **BOTTOM HERO = the third-space floor plan:** a top-down plan with a cool enclosed **INSIDE / formal meeting room** ("decisions get RATIFIED") and a warm **DOORWAY / third space** ("decisions get SOCIALISED"), a numbered **DOORWAY PROTOCOL**, and a clean dashed figure-path looping out and back. The lone **signal-red** object is a single **cigarette** with a quiet CV micro-trace and a warm **bypass** arc routing around it; the largest non-headline line reads **"THE LEVERAGE IS THE DOORWAY, NOT THE CIGARETTE."** Left rail carries the epistemic key with warm large / cool small / red smallest — the proportions *are* the §0 argument. Headline: **"THE SIGNAL YOU CAN'T SEE."**; footer thesis: **"BUILD THE FIELD. WORK THE ROOM. SKIP THE SMOKE."**

§7 traps avoided: no perfume-bottle/luxury hero (bottles appear only as the struck "collection" ghost), no fragrance-wheel hero (the family selector is small and cool), projection drawn as technical isobars not cartoon swirls, the cigarette kept as one restrained red object (not smoking-glamour, not a gory PSA), and the warm doorway clearly out-weighs the red. Exactly one red object on the sheet; all other cautions (over-spray cloud, lingering tell, pouch caveat) are amber/grey.

## Outputs (authoritative copies in `visualization/`)

- **PNG:** `visualization/Poster — Attractive - Appearance Part 6.0 - Scent and Social Leverage.png`
- **SVG:** `visualization/Poster — Attractive - Appearance Part 6.0 - Scent and Social Leverage.svg`
- Portrait **1200×1500 viewBox → rendered 2400×3400** (canvas 1200×1700), ~566 KB.

## Renderer & verification

- **Renderer:** CairoSVG 2.9.0 (installed this run; Playwright + rsvg-convert unavailable in sandbox). Fonts: Inter / JetBrains Mono requested, DejaVu fallback at render time — consistent with prior Attractive siblings.
- **Verified:** PNG non-empty (~566 KB > 50 KB), dimensions 2400×3400 as expected. Visually inspected full sheet + zoomed crops (dial/airlock seam, floor plan, top hero/left rail). Two build fixes applied after first render: (1) moved the field centre + dose-dial cluster up so the "TWO SPRAYS…" stamp no longer clipped the airlock band; (2) replaced the numbered-waypoints-on-path (which collided with the protocol legend) with a clean dashed direction-loop + a readable numbered legend, and nudged the cigarette CV labels off the loop line.
- **Palette source:** the brief's §5 (bone `#F4F1EA`, graphite `#1E2024`, terracotta `#C2703D`, slate `#5E7585`, single red `#D9483B`) was used as authoritative; the `aether-call-to-action-DESIGN.md` token file is a generic dark-UI web template and does not describe the Attractive drafting-paper style.

## Deviations / notes

- Fresh build — no prior poster existed for this concept, so exactly one PNG + one SVG written, no deletion needed.
- The hard-coded session outputs path in the task file is not the live path this run; the connected `blog viz daily - temporary/` folder (concepts + trackers) was the source of truth, and the brief was found directly via Glob (no transcript fallback needed). The article logged as today's run in `Tracker — Blog Viz Daily.md` ("Next up = Part 6.0 — Scent and Social Leverage") matches the brief used.
