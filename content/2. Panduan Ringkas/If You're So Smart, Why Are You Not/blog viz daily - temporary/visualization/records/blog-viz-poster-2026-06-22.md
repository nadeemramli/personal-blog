# Blog Viz Poster — 2026-06-22

- **Date:** 2026-06-22
- **Source brief:** `concepts/blog-viz-2026-06-22-part-7-2-persistent-memory.md`
- **Article:** Productive · Productivity Enhancement · **Part 7.2 — Persistent Memory** (series finale: 13th of 13 Productivity Enhancement articles; closes the Productive pillar's two tracks)
- **Locked pillar style:** Neural Signal Schematic
- **Concept (instrument):** The Dual-Port Non-Volatile Shared Memory Core — concentric hub-and-rim

## Visual concept used

The poster renders the article's thesis literally as a **dual-port non-volatile memory core**: one shared store of plain-text cells that two ports both read from and write to. Dead-centre sits the hero — a brightly-lit cyan **SHARED MEMORY · PLAIN TEXT** core, etched with a faint Markdown substrate (`#`, `-`, `[[ ]]`), built as a lattice of small colour-typed cells (P preference · S project-state · D decision+why · R reference) joined by two-way link traces, with an amber **INDEX RAIL** along the top edge and a **NON-VOLATILE · DISK** badge. A bright traversal pulse fans out from the PROJECT cell to its people / decisions / history / refs ("assemble context on demand"). The **YOU** port (off-white, the human's second mind) reaches in from the left and the **AGENT** port (cyan ×AI bolt-on) from the right on a RUN CYCLE — `RELOAD ↑` pulls cells up into a small dim volatile context-window buffer (with a `SESSION WIPE` glyph) at run-start, `RECORD ↓` latches one learned cell back down at run-end. The convergence reveal — a struck-through, greyed **AGENT'S OWN SEPARATE MEMORY** re-routed and merged onto the one core, under a bright **ONE STORE · TWO PORTS** bracket — does the finale's emotional payload. All writes pass a single amber **REFINE — SHARPEN, DON'T DUPLICATE** gate. The one scarce red object is a duplicate/contradiction rot cluster lower-left (`STALE · CONTRADICTION` / "the base that only grows, dies") that the agent reads and stalls on. The whole seven-layer stack is bent into a closed **ring welded back into the hub** at the bottom (Knowledge System node → CLOSURE WELD → core), with AI-as-Worker at the top writing back down — the literal picture of "the stack is a loop, not a ladder." Composition is hub-and-rim/concentric, deliberately the only radial layout in the 22-poster Productive set (all 12 prior Productive instruments were linear). Closing line carried: **FUNDAMENTALS UNCHANGED. AI RAISED EVERY CEILING.**

## Outputs

- SVG: `visualization/Poster — Productive - Productivity Enhancement Part 7.2 - Persistent Memory.svg`
- PNG: `visualization/Poster — Productive - Productivity Enhancement Part 7.2 - Persistent Memory.png` (3280×2640, ~524 KB)

## Renderer & verification

- **Renderer:** CairoSVG (rsvg-convert unavailable in sandbox; apt install blocked). Rendered at 2× the 1640×1320 viewBox.
- **Verification:** PNG non-empty (~524 KB, well over the 50 KB floor) and at expected 3280×2640 dimensions. Read back full render + region crops (core interior, right-side agent/buffer cluster, bottom refine/rot band, legend). Two fixes applied after first render: (1) widened the REFINE gate box so its label no longer overflowed; (2) relocated the FOUR MEMORY TYPES legend from the cramped core↔agent gap into the clean upper-left negative space to clear the agent's READ/WRITE link label. A dropped `</svg>` closing tag (lost between edits) was re-appended and XML validity re-confirmed before the final render.

## Deviations / notes

- **Brief-naming discrepancy (autonomous choice):** today's brief is named `blog-viz-2026-06-22-part-7-2-persistent-memory.md` in `concepts/`, not the SKILL's `Visualization Concept — …` scheme, so the `Visualization Concept — *` Glob found nothing. Selected today's brief as the most-recently-modified `blog-viz-2026-06-22-*` concept file. Poster stem still follows the convention (and matches the stem the brief itself specifies).
- No prior 7.2 poster existed, so no delete was required; exactly one PNG + one SVG written.
- Palette held to the locked Neural Signal Schematic logic: cyan = live/own-system, amber = gate/index/reference/addressing, single scarce red = duplication-rot only, off-white = human/preference, dim grey = corrected instinct / wiped buffer.
