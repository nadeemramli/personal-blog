---
date: 2026-06-11
pillar: Fit
track: Performance Enhancement
part: "4.2"
title: Choosing Your Ancillaries
---

# Poster record — Fit / Part 4.2: Choosing Your Ancillaries

- **Date:** 2026-06-11
- **Source brief:** `concepts/Visualization Concept — Fit - Part 4.2 (Performance Enhancement) - Choosing Your Ancillaries.md`
  (path: `…/blog viz daily - temporary/concepts/`)
- **Article:** Fit pillar → Performance Enhancement track → Part 4.2 — Choosing Your Ancillaries (9th PE concept; "the missing middle" of the Protection & toolbox arc)
- **Tracker cross-check:** confirmed against `concepts/blog-viz-tracker.md` — the 2026-06-11 entry logs Part 4.2 as today's run (Part 4.1 was the earlier 00:39 run, already postered).

## Visual concept used

Built the locked sub-archetype from the brief: a tall, black-ground **Engineering Diagnostic Instrument** rendered as a **specification selector / interchangeable-part fitment rack**. Each drug class is a pull-out **member tray**; candidates share an **identical mounting flange** (the shared job: "LDL ↓", etc.) but diverge by a **spec-fingerprint skirt**, so the eye reads "same socket, different skirt." Exactly one member per tray is **seated & lit** (cool instrument-green) with a reason chip; rejects sit **dimmed-but-present** with a one-line disqualifier. The **statin tray is the hero** (drawn largest, docked as the legend): rosuvastatin water-drop / HYDROPHILIC / low ache-gauge / SEATED vs simvastatin-80 oil-drop / LIPOPHILIC / high ache-gauge / dimmed, with the myth-buster flag ("water-soluble = gentler on muscle") and the ezetimibe "second door." Below it, eight class trays (ARBs, MRAs, BP adjuncts, glucose/insulin, thyroid, organ/antioxidant, prolactin & gyno, hair) each in left-load→right-seat reading order, inheriting the ecosystem rail (FAMILY → LOADS → BIOMARKER → ANCILLARY). The **redundancy dimmer** is shown as the ARB note (GLP-1 seated → telmisartan's PPAR-γ greys to nice-to-have); **cross-tie buses** (one part → several jobs) appear in the hero fan and the footer "PARTS COUNT" mini-diagram. The **single red object** is spironolactone in the MRA tray — a barbed reverse-flange that won't seat plus a red REJECT stamp ("blocks androgen receptors → gyno → sabotages your cycle"); every other caution (TZD AVOID, amlodipine/indapamide misuse, oral-minoxidil interlock, MRA+ARB+thiazide interlock) is amber. The footer carries the over-stack thesis ("DEFEND THE SYSTEM, NOT THE DRUG … the number is still the boss"), a forward chip to 4.3, and the prescription/physician framing footnote.

## Outputs (in `visualization/`)

- **SVG:** `Poster — Fit - Part 4.2 (Performance Enhancement) - Choosing Your Ancillaries.svg`
- **PNG:** `Poster — Fit - Part 4.2 (Performance Enhancement) - Choosing Your Ancillaries.png`
- Generator script: `gen_poster.py` (session scratch) — hand-coded SVG, no external design service.

## Renderer & verification

- **Renderer:** CairoSVG (rsvg-convert / Playwright unavailable in sandbox — no root for apt; CairoSVG was the available path per the SKILL fallback note).
- **Resolution:** viewBox 1200×1720 rendered at 2× → **2400×3440 px**, 676 KB (well over the 50 KB floor).
- **Verification:** PNG re-opened (size 2400×3440, RGB confirmed). Visually inspected full poster + zoomed crops of the hero statin tray, the ARBs/MRAs tray row, and the footer; corrected member-row overlap (lengthened the cabinet to a taller portrait, 1200×1720), repositioned the rosuvastatin ache-gauge off the reason text, un-clipped the ezetimibe chip, shortened the MRA tray title, and re-rendered until clean.

## Deviations / notes (autonomous run)

- **Canvas height:** went **portrait 1200×1720** instead of the default 1200×1500 (4:5). The brief explicitly calls for a *tall parts cabinet* of eight stacked class trays under a dominant statin tray; 1500 px forced member rows to overlap, so the taller portrait was the faithful choice. Still portrait, still "spec binder," distinct from 4.1's landscape.
- **Fonts:** only DejaVu available in sandbox (no Inter / JetBrains Mono, apt blocked). Used DejaVu Sans for display/body and DejaVu Sans Mono for technical labels — the brief's sanctioned fallback. Visual register (clinical, mono labels, display headline) is preserved.
- **Em-dashes:** per the house style (parentheses/colons over em-dashes in flowing prose), the two prose em-dashes were changed to a comma and a colon; em-dashes kept only as label/heading separators (e.g. the grammar strip).
- **Source truncation:** the article file is still truncated on disk at Neuroprotection (per the brief's source note); the poster was built from the intact thesis + ecosystem table + within-class logic, and the over-stack base course already carries the (truncated) "selection principles & over-stacking trap." No change needed if the tail is finished later.
