---
title: "Blog Viz Poster — 2026-06-04"
draft: true
date: 2026-06-04
---
# Blog Viz Poster — 2026-06-04

- **Date:** 2026-06-04
- **Source brief:** `concepts/Visualization Concept — Attractive - Appearance Part 1.0 - What Actually Matters.md` (modified 2026-06-04 00:37 — confirmed today's run; most-recently-modified concept in `/concepts/`).
- **Article:** Attractive pillar → Appearance track, **Part 1.0 — What Actually Matters For Your Appearance** (Part 1 of 7). This is the **first Attractive-pillar poster** in the run.

## Visual concept used

A hand-coded **architect's elevation** of "the appearance stack" — a four-storey structure drawn bottom-to-top, where **width encodes leverage** (widest, heaviest at the base). Read from the ground up: a ghosted, below-grade **foundation slab** (`THE CHRONIC BASE — built elsewhere, never claimed here`, with four footing piles: LEANNESS·Fit / SKIN·Skin / RETENTION·Hair / RECOVERY·Sleep), then **SUBSTRATE** (Layer 1, physiology), **FRAME** (the cut) — both below a hard horizontal **epistemic line** (`← MEASURABLE MECHANISM` / `HONEST CONVENTION →`) — then **SIGNAL** (Layer 2, presentation) and **FLOOR** (Layer 3, the maintenance multiplier) above it. The surface carries two registers per the brief: engineering hatching + dimension ticks below the line (warm terracotta), cleaner editorial linework above (cool slate-blue). A left-margin **leverage gauge** wedges downward (`LEVERAGE — HIGHEST AT THE BASE`). In the upper-right negative space, a ghosted, rotated **failure overlay** shows the same building attempted top-down — an oversized `WATCH · FIT · FRAGRANCE` crown balanced on a hollow, cracking substrate, toppling, with the single alarm-red caption `built top-down → it topples.` Headline `THE WATCH DOESN'T FIX THE FACE.`; thesis lockup `THE ORDER IS THE LEVERAGE.` All §4 copy verbatim.

This establishes the **third series visual sibling — "Architect's Elevation / Spec Sheet"** (Fit = daylit engineering instrument; Sleep = clinical nocturne; Appearance = drafting table) and sets the Attractive-pillar palette: bone paper `#F4F1EA`, graphite ink `#1E2024`, warm-substrate terracotta `#C2703D`, cool-signal slate-blue `#5E7585`, ghosted-foundation grey `#9A958C`, alarm-only vermilion `#D9483B`. Parts 2.0–7.0 can inherit it.

## Outputs

- **SVG (source, editable):** `poster-2026-06-04-appearance-what-matters.svg`
- **PNG (2×):** `poster-2026-06-04-appearance-what-matters.png` — 2400×3000, ~362 KB
- **Published copy:** `visualization/Poster — Attractive - Appearance Part 1.0 - What Actually Matters.png` (canonical name for the blog, per the poster tracker contract)
- **Generator:** `build_poster.py` (kept in session `outputs/` scratch)

## Renderer & verification

- **Renderer:** CairoSVG 2.9.0 (pip-installed this run; not preinstalled in the sandbox — cairo system libs already present, no sudo needed). rsvg-convert / Playwright not used (CairoSVG was sufficient).
- **Verified:** PNG is non-empty (~362 KB > 50 KB threshold), dimensions exactly 2400×3000 (2× the 1200×1500 viewBox), rendered image reviewed — all four claims read at a glance (order, layers, epistemic line, borrowed foundation), failure overlay legible, single-red discipline respected.

## Deviations / notes

- **Fonts:** the brief specifies Inter (display) + JetBrains Mono (labels); the render host only had DejaVu Sans / DejaVu Sans Mono, used as faithful substitutes (same as all prior Fit posters). The SVG carries Inter / JetBrains Mono first in its font-family fallback chains, so a host with those fonts renders a 1:1 match — re-render there for final fidelity.
- **Headline choice:** used `THE WATCH DOESN'T FIX THE FACE.` (the brief's strongest scroll-stopper); per the brief's instruction, the failure overlay therefore uses `built top-down → it topples.` rather than repeating the headline.
- **Canvas:** portrait 1200×1500 (default 4:5), primary orientation per §3. Foundation slab anchored at the base, eye forced to enter low and climb.
