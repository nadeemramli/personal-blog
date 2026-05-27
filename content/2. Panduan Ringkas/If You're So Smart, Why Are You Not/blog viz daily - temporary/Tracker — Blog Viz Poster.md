---
title: Tracker — Blog Viz Poster
draft: true
tags:
date: 2026-05-27
---
# Tracker — Blog Viz Poster

**What this file is:** the poster task's memory — the companion to [[Tracker — Blog Viz Daily]]. Each run reads the daily tracker's _Covered_ list (the concepts that now exist in `/concepts/`), produces a poster for any concept **not yet in _Posters produced_ below**, then logs it here so the same visualization is never regenerated. Bookkeeping only, not a blog post (hence `draft: true`).

**How a poster is produced (the contract):** for each concept, follow three layers, in order —
1. `aether-call-to-action-DESIGN.md` — global color / type / spacing / surface tokens.
2. The concept's embedded **§6 locked style** (Fit pillar = _Engineering Diagnostic Instrument_; logged in [[Series Style Policy — If You're So Smart, Why Are You Not]]).
3. The concept's exact §3 layout and §4 copy (verbatim — the copy *is* the payload).

Then **name the file after its concept** and save it to `/visualization/`.

Scope: this tracker covers the **"If You're So Smart, Why Are You Not"** Big Series only — same scope as [[Tracker — Blog Viz Daily]]. Each Big Series keeps its own poster tracker beside its daily tracker.

---

## Posters produced

| Concept | Poster file | Pillar · style | Date | Render |
|---|---|---|---|---|
| [[Visualization Concept — Fit - Part 1.1 - What Actually Matters]] | `visualization/Poster — Fit - Part 1.1 - What Actually Matters.png` | Fit · Engineering Diagnostic Instrument | 2026-05-27 | code-render → PNG, 1080×1522 @2x |
| [[Visualization Concept — Fit - Part 1.2 - Recomp, Cut or Bulk]] | `visualization/Poster — Fit - Part 1.2 - Recomp, Cut or Bulk.png` | Fit · Engineering Diagnostic Instrument | 2026-05-27 | code-render → PNG, 1080×1536 @2x |

## Pending — concept exists in /concepts/, poster not yet produced

- _None._ Both concepts in `/concepts/` are now postered. New entries appear here automatically when [[Tracker — Blog Viz Daily]] adds the next concept (Next up: Fit / Aesthetic & Strength / Part 2.0 — Structure of a Day).

## Naming convention

Poster filename mirrors its concept, swapping the leading `Visualization Concept` for `Poster`, saved under `/visualization/`:

`Visualization Concept — Fit - Part 1.1 - What Actually Matters.md`  →  `Poster — Fit - Part 1.1 - What Actually Matters.png`

## Render notes (how these were made)

- **Method:** code-rendered SVG → PNG (no generative tool), so the exact §4 copy in every cell is preserved verbatim.
- **Output:** portrait PNG on a 1080-wide canvas, rendered at 2× for crispness; reads inline in the blog and saves cleanly to a phone.
- **Fonts:** design.md specifies Inter (display) + JetBrains Mono (labels). The render host only had DejaVu Sans / DejaVu Sans Mono, used as faithful substitutes. Re-render with Inter + JetBrains Mono on a host that has them for a 1:1 match.
- **Semantic colors:** design.md defines no success/warning/danger roles, so a restrained instrument-status triad was added inside the dark-console palette — success `#34D399`, warning `#FBBF24`, danger `#F87171`. Tune here if desired; keep them rationed (verdict dots / tags / accent bars only, never a fill wash).

## Notes

- **Never regenerate** a poster already listed in _Posters produced_.
- Style is locked per pillar — see [[Series Style Policy — If You're So Smart, Why Are You Not]] (Fit = Engineering Diagnostic Instrument). Do not change style mid-pillar.
- This file wikilinks [[Tracker — Blog Viz Daily]]; Obsidian's backlinks make the relationship visible from both trackers.
