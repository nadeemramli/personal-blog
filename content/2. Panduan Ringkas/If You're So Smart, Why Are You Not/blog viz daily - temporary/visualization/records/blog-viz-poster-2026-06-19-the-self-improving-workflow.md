# Blog Viz Poster — 2026-06-19 (The Self-Improving Workflow)

- **Date:** 2026-06-19
- **Source brief:** `concepts/Visualization Concept — Productive - Productivity Enhancement Part 3.1 - The Self-Improving Workflow.md` (most-recently-modified concept, confirmed against `Tracker — Blog Viz Daily.md` line for the 2026-06-19 2nd-of-day run)
- **Article:** Productive · Productivity Enhancement · Part 3.1 — The Self-Improving Workflow (5th poster of the track; CLOSES Part 3 "The Workflow Engine" with 3.0)
- **Locked style:** "Neural Signal Schematic" (Productive pillar)
- **Sub-archetype:** Write-Back Memory Bench / Non-Volatile Latch

## Visual concept used

A landscape two-tier RAM↔DISK memory schematic read left→right across discrete RUNs of one repeatable task. The **VOLATILE RAM RAIL ("THE CHAT")** on top is a row of session cells — RUN 1·JANUARY (hot, amber corrections + a discharge-to-ground WIPE glyph), then RUN 2·FEB, RUN 3, RUN 4, BY MARCH — visibly cooling from amber-messy to clean cyan ("RUNS ITSELF"), the compounding rendered as a left-hot→right-calm gradient. The hero is the centre-seam **WRITE-ENABLE LATCH (SAVE)** — biggest/brightest, fed by an amber "copy down" correction from RUN 1, with a `← FROM 3.0 · REFLECT TAP` inlet and a `WRITE = 1 · one-way · latched` control line; its output passes a **ROUTE BY OWNER** node onto the **NON-VOLATILE DISK RAIL ("THE FILES")** — a cyan bus split into hardware banks: PROJECT INSTRUCTIONS (small·stable), SKILL/skills.md (procedural·per-task), and a ghosted/fenced PERSISTENT MEMORY bank (→ Part 7.2). A dashed RELOAD-AT-RUN-START arrow rises back into RUN 2. Right column stacks the **CORRECTIONS/RUN** compounding meter (cyan curve decaying to zero over a grey flat "UNSAVED — paid every run" line; caption "THE MODEL DIDN'T IMPROVE. THE INSTRUCTIONS DID.") above the **red ALARM annunciator** (fixed-in-chat → WRITE=0 never latched → session wipe → SAME BUG re-emerges → "TYPING THIS AGAIN? IT SHOULD'VE BEEN SAVED."). Lower-left WORKED EXAMPLE dock seats this blog's two real saved rules (em-dash → parentheses, "you" = the reader); lower-right a "same task, 3 months apart" Jan→Feb→Mar timeline. Foot through-line: "AN UN-SAVED CORRECTION IS A TAX. A SAVED ONE IS AN ASSET."

One-red discipline held: red appears only on the un-saved recurring correction (RAM cell + alarm panel). Calm-as-resolution held: the clean later runs carry no alarm. Floppy/hard-drive/glowing-AI clichés avoided; the "what goes where" table is rendered as disk banks, not a flat two-column image; the RUN/time axis is preserved.

## Outputs (in `visualization/`)

- SVG: `visualization/Poster — Productive - Productivity Enhancement Part 3.1 - The Self-Improving Workflow.svg`
- PNG: `visualization/Poster — Productive - Productivity Enhancement Part 3.1 - The Self-Improving Workflow.png`

## Render + verification

- **Renderer:** CairoSVG 2.9.0 (Playwright/Chromium and rsvg-convert were unavailable in the sandbox; CairoSVG is the established fallback). Rendered at 2× (3000×2400 from the 1500×1200 viewBox).
- **Verification:** PNG non-empty (~529 KB, well over the 50 KB floor), dimensions confirmed 3000×2400 via PIL. XML validated with ElementTree (well-formed). Visually inspected full poster + two high-res crops (centre-left latch/save path, right meter/alarm) — all text legible, no clipping, save→disk→reload loop and one-red object read correctly.
- **Fonts:** sandbox has only DejaVu; the locked Inter / JetBrains Mono families fall back to DejaVu Sans / DejaVu Sans Mono (same fallback as every prior poster in this set).

## Deviations / notes

- No prior poster existed for Part 3.0 or Part 3.1, so no delete-before-write was needed; exactly one PNG + one SVG now exist for this concept.
- Mid-build, an Edit-tool write of the SVG landed truncated on the bash-mounted copy (final `<text>` line + `</svg>` missing, stable at 30,404 bytes) while the file-tool view was complete. Repaired surgically in bash (kept intact lines 1–369, re-appended the final line + `</svg>`); XML then validated clean before rendering.
- Brief had multiple headline options; used the recommended `THE CHAT FORGETS. THE FILE REMEMBERS.`
