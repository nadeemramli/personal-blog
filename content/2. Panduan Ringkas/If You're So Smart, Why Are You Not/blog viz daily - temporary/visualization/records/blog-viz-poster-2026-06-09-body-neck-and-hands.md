---
date: 2026-06-09
pillar: Attractive
track: Skin
part: 3.0
title: Body, Neck and Hands
renderer: CairoSVG
---

# Blog Viz Poster — 2026-06-09 — Attractive / Skin Part 3.0: Body, Neck and Hands

- **Date:** 2026-06-09
- **Source brief:** `concepts/Visualization Concept — Attractive - Skin Part 3.0 - Body, Neck and Hands.md`
  (in the blog folder `2. Panduan Ringkas/If You're So Smart, Why Are You Not/blog viz daily - temporary/`)
- **Article:** If You're So Smart, Why Are You Not → **Attractive** pillar, **Skin** track, **Part 3.0 of 4 — the capstone** ("Below the Jaw"). Fifth Skin concept postered, seventh Attractive-pillar poster.

## Visual concept used

Implemented the brief's hero verbatim: a **full-body architectural SITE ELEVATION** of a standing structure (a drawing, never a body), with the **camera pulled all the way back** from 1.1's wall section to the whole site. The single highest-contrast horizontal in the frame is the **`FACE ROUTINE TERMINATES HERE` coverage line across the jaw** — the hero device and register boundary. Above it the head is a warm **FINISHED FAÇADE** (terracotta cladding hatch, dimensioned, crisp); below it the structure is bare, washed-out, weathered graphite hatch. The same **UV weather from 1.1 rakes the ENTIRE elevation in alarm red** (eight diagonal arrows over face, neck, torso, hands, legs) under the label `PHOTOAGING · UV · ~80% · does not stop at the jaw.` The **three age-tell corners** — NECK, DÉCOLLETAGE, BACK OF HANDS — are the only saturated-red objects besides the UV field, each red-dotted with a leader-line callout. A warm **`EXTEND THE LINE DOWN`** repair arrow drags the cladding past the jaw onto neck + décolletage + hand (captioned "almost free"). A **material-zoning overlay** maps the lower structure into its different-organ zones (OILY → acne, STRETCH → manage, TEXTURE → KP, DRY → flaking) with slate zone-hatch, paying off "one building, many materials — not a bigger face." The structure stands on the reused **finite collagen-scaffold ground line** below grade (`thicker · slower turnover · slower healing · built, not bought`).

Lower third = the **zoning spec sheet** as slate instrument docks: the **BACNE FORK** two-way split (bacterial/hormonal → BP + salicylic **vs** fungal/Malassezia → ANTIFUNGAL, 90% = sweat hygiene), a **KP** card + a warm→grey **stretch-mark honesty gauge** (rubrae → some · albae → permanent, drawn grey not red per §5), and the five-chip **MINIMUM BODY ROUTINE** strip ("90% = sun + sweat hygiene + moisturize · don't over-build"). Bottom band carries the thesis lockup `THE WEATHER NEVER STOPPED AT YOUR JAW.` plus the leverage punch `NECK + BACK OF HANDS = HIGHEST LEVERAGE`.

Locked Attractive "Architect's Elevation / Spec Sheet" signature carried over verbatim: bone `#F4F1EA`, graphite `#1E2024`, terracotta `#C2703D` (living/buildable + the extend-down arrow + striae rubrae), slate `#5E7585` (instruments + datum label + zoning tags), single alarm red `#D9483B` reserved exclusively for the UV field and the three exposed corners. New sub-archetype = the **"SITE ELEVATION / ZONING PLAN" pull-back**. Headline chosen: `YOUR ROUTINE STOPS AT THE JAW. THE SUN DOESN'T.` (the brief's flagged-strongest option).

## §7 avoidances respected

No real torso / before-after / "flawless body" model — the hero is a diagrammatic elevation. The body is visibly **zoned** (not the 1.1 face section re-drawn uniformly). The UV field rakes the **whole** elevation (not stopping at the jaw); stretch marks/KP/acne are **not** red-coded; striae albae read grey/permanent; the `extend the line down` cheap-fix arrow is present.

## Output

- **SVG:** `visualization/Poster — Attractive - Skin Part 3.0 - Body, Neck and Hands.svg`
- **PNG:** `visualization/Poster — Attractive - Skin Part 3.0 - Body, Neck and Hands.png`
- Portrait `viewBox 1200×1500`.

## Renderer & verification

- **Renderer:** CairoSVG @2× (rsvg-convert unavailable in sandbox; pip-installed cairosvg). Output **2400×3000**, ~768 KB. XML validated well-formed before render.
- Read the PNG back and inspected the full view: coverage line is the dominant horizontal and survives at thumbnail; UV field clearly covers the whole figure; three red tells legible; zoning overlay, extend-down arrow, scaffold line, and spec sheet all clean. No clipping or dead-space issues. First-pass render accepted (one cleanup edit removed two stray empty `<text>` nodes in the hands callout before final render).
- No prior poster for this concept → **no deletes** required (verified `visualization/` had no `Poster — ... Body, Neck and Hands.*`).

## Deviations / fallbacks

- The `aether-call-to-action-DESIGN.md` token file is the generic Aether CTA template (black/white SaaS palette), not the Attractive-pillar palette — so the **locked palette was taken from the brief's §5/§6** (the authoritative source for this pillar), consistent with all prior Attractive posters. No other deviations.
