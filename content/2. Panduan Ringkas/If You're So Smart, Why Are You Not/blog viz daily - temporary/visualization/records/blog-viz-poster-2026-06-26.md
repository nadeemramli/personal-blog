---
title: Blog Viz Poster Run — 2026-06-26
draft: true
date: 2026-06-26
---
# Blog Viz Poster Run — 2026-06-26

- **Date:** 2026-06-26
- **Source brief:** `Visualization Concept — Healthy - Blueprint Part 3.0 - The Five Habits.md`
  (in `…/blog viz daily - temporary/concepts/`; dated alias `blog-viz-2026-06-26-part-3-0-the-five-habits.md`, both modified 05:41 today — confirmed as today's run against `Tracker — Blog Viz Daily.md`)
- **Article:** Healthy pillar · Blueprint track · Part 3.0 — *The Five Habits* (Part 3 of 6, THE PROTOCOL)
- **Pillar style:** Healthy **"Clinical Nocturne"** (near-black `#0B0F14` ground · cyan `#2DD4BF` = build/in-range · amber `#E8A23D` = remove/wired-but-wrong · single scarce red `#FF5C5C`)

## Visual concept used
Rendered the brief's non-negotiable hero: a **clinical sustenance / perfusion manifold** read left→right. Four lit **cyan supply trunks you BUILD** enter from the left, **stepped in gauge by leverage** with SLEEP the fattest/lowest (carrying a violet `← KEYSTONE · Part 2.0` marker), then NUTRITION, EXERCISE, and CONNECTION thinnest-but-still-lit — each with a terse one-spec clip. They feed a calm central **in-range core vessel** (`THE NUMBERS · HELD IN RANGE`, a held cyan level with a faint grey "miss one → it droops" slack line). On the right, the asymmetry: **one amber EXTRACTION/DRAIN line you REMOVE** (habit 5, "Things to avoid") flowing OUT to a sealed waste trap, carrying contaminant chips (UPF · smoking/vaping · alcohol · scrolling · addictive) and a hard **bright-line valve**. A ghosted, struck-through **rejected add-on caddy** (supplements, cold plunge, fasting timer, extra wearable, exotic powder — all unplugged) sits upper-right; from it the **single saturated red** connector reaches past the basics to jam exotica straight into the core (`ADD EXOTICA BEFORE BASICS = avoiding the boring habit that moves the number`). Docked secondaries: an honest-promise **time-ribbon** (amber RESISTANCE head → 1mo / 6mo / 2–5yr cyan rise-and-hold), the AUDIT + "install one habit this month" method chips, the `→ Part 3.1` handoff, and the thesis lockup **FEWER, NOT MORE · FOUR IN, ONE OUT · SLEEP FIRST**. Board kept deliberately bare — the negative space and the refused caddy *are* the "fewer, not more" argument. Four-in / one-out silhouette is the dominant read.

## Outputs (in `visualization/`)
- SVG: `visualization/Poster — Healthy - Blueprint Part 3.0 - The Five Habits.svg`
- PNG: `visualization/Poster — Healthy - Blueprint Part 3.0 - The Five Habits.png`
- Canvas: 1600×1000 viewBox (landscape 16:10, per brief §3 — a manifold reads horizontally), rendered @2× → **3200×2000**, ~598 KB.

## Renderer & verification
- **Renderer:** CairoSVG 2.9.0 (Playwright + rsvg-convert + Inkscape all unavailable this sandbox; CairoSVG installed via pip).
- **Verification:** XML well-formedness checked via ElementTree (passed); PNG confirmed non-empty (~598 KB) at exact 3200×2000; visually inspected full image + zoomed center/right crops — four-in/one-out manifold legible, red kept singular and in shadow, caddy struck/unplugged, drain asymmetry clear.
- **One fix during QA:** the `⑤` circled-five glyph rendered as a tofu box (DejaVu lacks U+2465) → replaced with a hand-drawn amber circle + "5" badge matching the supply-trunk numbers.
- **Fonts:** DejaVu Sans / DejaVu Sans Mono fallbacks (JetBrains Mono / Inter not installed in sandbox); all special glyphs used (≈ ≥ ↑ ↓ → − · ▸ ←) confirmed rendering under DejaVu.

## Deviations / notes
- **Build pipeline note:** the file-tool ⇄ bash FUSE mount diverged mid-run (an incremental edit left the mount with a stale truncated copy that wouldn't refresh, breaking the render). Recovered by writing the authoritative SVG directly inside the bash sandbox via heredoc, rendering there, then `cp`-ing both final files into `visualization/`. No effect on output fidelity.
- First (and only) poster for this concept — no prior PNG/SVG to delete.
- Per the brief's path-reconciliation note, the scheduled task's hard-coded `local_…/outputs` path is unreachable; the connected-folder `visualization/` is the authoritative home and trackers here are the source of truth.
