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
| [[Visualization Concept — Fit - Part 2.0 - Structure of a Day]] | `visualization/Poster — Fit - Part 2.0 - Structure of a Day.png` | Fit · Engineering Diagnostic Instrument | 2026-05-29 (backfill) | code-render → SVG (scratch) + PNG, 1200×1500 @2x (CairoSVG) |
| [[Visualization Concept — Fit - Part 3.1 - The Program - Concepts]] | `visualization/Poster — Fit - Part 3.1 - The Program - Concepts.png` | Fit · Engineering Diagnostic Instrument | 2026-05-29 | code-render → SVG (scratch) + PNG, 1200×1500 @2x (CairoSVG) |
| [[Visualization Concept — Fit - Part 3.2 - The Program - Rules and Building the Program]] | `visualization/Poster — Fit - Part 3.2 - The Program - Rules and Building the Program.png` | Fit · Engineering Diagnostic Instrument | 2026-05-30 | code-render → SVG (scratch) + PNG, 1200×1500 @2x (CairoSVG) |
| [[Visualization Concept — Fit - Part 3.3 - The Program - Example Programs]] | `visualization/Poster — Fit - Part 3.3 - The Program - Example Programs.png` | Fit · Engineering Diagnostic Instrument | 2026-05-31 | code-render → SVG (scratch) + PNG, 1200×2548 @2x → 2400×5096, ~803 KB (CairoSVG 2.9.0) |

## Pending — concept exists in /concepts/, poster not yet produced

- _None._ All concepts in `/concepts/` are now postered. New entries appear here automatically when [[Tracker — Blog Viz Daily]] adds the next concept (Next up: Fit / Aesthetic & Strength / Part 4.0 — Pharmacology).

## Naming convention

Poster filename mirrors its concept, swapping the leading `Visualization Concept` for `Poster`, saved under `/visualization/`:

`Visualization Concept — Fit - Part 1.1 - What Actually Matters.md`  →  `Poster — Fit - Part 1.1 - What Actually Matters.png`

**Only the PNG lives in `/visualization/`.** The hand-coded SVG is a raw working file kept in the session `outputs/` scratch — not published to the blog folder. If a poster needs a tweak, re-render from the SVG and overwrite the PNG in place; do not commit the SVG to `/visualization/`.

## Render notes (how these were made)

- **Method:** code-rendered SVG → PNG (no generative tool), so the exact §4 copy in every cell is preserved verbatim.
- **Output:** portrait PNG on a 1080-wide canvas, rendered at 2× for crispness; reads inline in the blog and saves cleanly to a phone.
- **Fonts:** design.md specifies Inter (display) + JetBrains Mono (labels). The render host only had DejaVu Sans / DejaVu Sans Mono, used as faithful substitutes. Re-render with Inter + JetBrains Mono on a host that has them for a 1:1 match.
- **Semantic colors:** design.md defines no success/warning/danger roles, so a restrained instrument-status triad was added inside the dark-console palette — success `#34D399`, warning `#FBBF24`, danger `#F87171`. Tune here if desired; keep them rationed (verdict dots / tags / accent bars only, never a fill wash).

## Notes

- **Never regenerate** a poster already listed in _Posters produced_.
- Style is locked per pillar — see [[Series Style Policy — If You're So Smart, Why Are You Not]] (Fit = Engineering Diagnostic Instrument). Do not change style mid-pillar.
- This file wikilinks [[Tracker — Blog Viz Daily]]; Obsidian's backlinks make the relationship visible from both trackers.
- **2026-05-30 run — Part 3.2 postered.** Sub-archetype within the locked Fit style: **build-up assembly schematic with standing-orders rail and failure-modes strip** — engineering reference card. Right side: four-tier vertical build-up (Tier 1 = 24 joint-movement chips in 6 region groups · Tier 2 = 6 compound-pattern chips + isolation-fillers sidebar + bold connector curves on SQUAT and VERTICAL PULL as worked examples, the other four faint/dashed · Tier 3 = 7-axes rail + lat-pulldown main/accessory inset + isolation→compound / variation→variation carryover panel + direct×1.0/indirect×0.5 weighting chip + 5-node horizontal-push rotation chain with one axis tagged per arrow · Tier 4 hero = Variation Cycle closed loop with iteration spiral exiting to "12+ months → 18–30 high-lifecycle variations" callout and three guardrail chips). Left rail: 4 GROWTH RULES (G·01–G·04) + 7 EXECUTION RULES (E·01–E·07) as instrument-bay rows. Bottom: 5 ECU-style failure-mode chips (static stretch, <3 min rest, soreness chasing, program-hopping, fake PO → links to 3.1 fault annex). Semantic color rationed per §5 of the brief: success role on the cycle loop perimeter, iteration callout, and the "both sides or the machine stalls" tagline only; warning role exclusively on the five failure-mode chips; danger role deliberately NOT used (preserves its meaning on 3.1's post-MRV collapse). Renderer: CairoSVG 2.9.0 (rsvg-convert unavailable — sandbox lacks sudo; Playwright skipped as CairoSVG was sufficient). Output verified at 2400×3000, 647 KB.
- **2026-05-31 run — Part 3.3 postered.** Sub-archetype within the locked Fit style: **dual-configuration datasheet + shared output meter + mesocycle timeline + configuration selector** — the spec sheet that documents two variants of one product. Layout: two **co-equal columns** (CONFIG A · Anterior/Posterior — 4 day-cards A–D, 2× freq, ~19 sets/session; CONFIG B · Full-Body EOD — 3 day-cards FB1–FB3, 3× freq, ~15 sets/session), each with a **weekly cadence strip** as a timing diagram (A = on-on-off-on-on-off-off clustering; B = on-off-on-off-on-off-off spacing — frequency as rhythm), identical structure so they read as two settings of one control. Hero move: two rails **converge** from both column bases into ONE **shared output meter** — per-muscle weekly-volume bars (Quads/Hams/Chest/Back/Shoulders/Arms) with the **MAV→MRV band 12–18 shaded** (callback to 3.1), both A+B bars inside the band on every row = "same goal, different route." Below: **mesocycle timeline** (long clock) — vertical-push slot rotation Machine Press → Seated DB → Standing OHP → Machine Press (higher ceiling) across Meso 1–4, with a **rising-ceiling baseline** stepping up at each handoff. Then **selector gate** (schedule + recovery → A/B, incl. "avoid B if recovery compromised") and **5-lever adaptation strip** + closing maxim chip. Semantic color rationed to TWO states only per §5: success (MAV→MRV band + rising ceiling) and warning (the two cautions); **danger deliberately NOT used** (green-light "go-execute" poster; cautionary weight lives upstream on 3.1/3.2). Density lighter than 3.2 on purpose. All §4 copy verbatim. Canvas 1200×2548 (taller than the 1500 default — the brief's full layout needs the room; brief specifies portrait/tall). Timeline zone height bumped + baseline amplitude reduced after a coordinate check flagged a potential baseline/segment-box overlap. Renderer: CairoSVG 2.9.0 (pip-installed this run — not preinstalled in the sandbox; cairo system libs already present, no sudo needed; rsvg-convert/resvg absent, Playwright not needed). Output verified at 2400×5096, ~803 KB. The sandbox shell returned delayed/empty results intermittently this run (boot + mid-render), so the render appeared to fail before retries surfaced the real success; the PNG render + copy to `/visualization/` ultimately completed and are verified. **This completes the 3-part programming sub-arc (3.1 → 3.2 → 3.3).** Working SVG + `build_poster.py` + `render.py` live in session `outputs/` scratch (not published to `/visualization/`).
- **2026-05-30 cleanup note.** The sandbox couldn't delete files in `/visualization/`, so the run also left behind a lowercased duplicate `poster-2026-05-30-rules-and-building-the-program.png` (and matching `.svg`) plus an extra `.svg` copy named to the convention. The canonical PNG `Poster — Fit - Part 3.2 - The Program - Rules and Building the Program.png` is the one to use; the rest can be removed manually. The hand-coded SVG and Python generator live in the session `outputs/` scratch (`build_poster.py`, `poster-2026-05-30-rules-and-building-the-program.svg`).
