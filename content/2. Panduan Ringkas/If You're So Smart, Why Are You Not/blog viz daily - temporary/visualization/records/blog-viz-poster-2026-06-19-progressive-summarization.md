# Blog Viz Poster — 2026-06-19 (Progressive Summarisation)

- **Date:** 2026-06-19 (third poster run logged this date)
- **Source brief:** `concepts/Visualization Concept — Productive - Productivity Enhancement Part 4.1 - Progressive Summarization.md` (most-recently-modified concept; the Daily tracker's named next-up after Part 4.0 PARA, "closes the Knowledge sub-arc 4.0 → 4.1 → 4.2")
- **Article:** Productive · Productivity Enhancement · **Part 4.1 — Progressive Summarisation** (7th poster of the track)
- **Locked style:** "Neural Signal Schematic" (one pillar = one style), landscape `viewBox 1500×1200`
- **Renderer:** CairoSVG 2.9.0 (rsvg-convert + Playwright unavailable in sandbox; DejaVu font fallback for Inter / JetBrains Mono)

## Visual concept used

New sub-archetype = the **"Resolution-Lock Distiller"** — a per-map signal-conditioning bench whose hero is a **fixed-footprint frame whose width never grows while its resolution climbs**. The whole poster exists to make one inversion obvious at a glance: *more in, same size, sharper* — you don't pile knowledge up, you sharpen it.

Left→right reading:
- **RAW CAPTURE (left):** a dim jagged "wall of highlights" waveform (high amplitude, ~0 information density) + a small amber fork `NO MAP YET? → START ONE`.
- **THE LOOP — an open single pass (not a ring):** **ENCOUNTER** (a coupler/gate that passes only if a map already exists) → **INTEGRATE** (the heart: a lit-cyan FUNDAMENTAL rail = *restate in your own words, decide what's true & matters — the retrieval rep*, with the locked **×AI MULTIPLIER** bolt-on tapped above = *the diff, drafted; dark until the own-words rail is live; it proposes, you decide*) → **LINK** (a tap pinning the source to its node, parked in a dim **RESOURCES →** side-rail — a 4.0/PARA callback) → **PRUNE** (a subtractor/eraser cutting a node now wrong/redundant; flagged as *the only Productive loop with a DELETE*).
- **HERO — the FIXED-FOOTPRINT MAP FRAME (centre-right):** a crisp rectangle holding a live cyan constellation, with three faint ghost-refinement states behind it (a node-blur resolving to a sharp point, a fuzzy edge snapping to a clean line, a cluster crystallising into a one-line summary). A horizontal **dimension line with end-arrows** tags the unchanging width (`W = CONSTANT · 1 MAP · FOOTPRINT NEVER GROWS`); a vertical **RESOLUTION/CONTRAST meter** on the frame edge reads high and climbing. Caption: `more in · same size · sharper`.
- **Inset (top-right) — "the original technique, collapsed":** a 4-rung emphasis ladder (capture → bold → highlight → summary) behind an amber **USE-GATE** (`USE DECIDES — notes you never reopen never get summarised`), a bracket folding the ladder into one node (`the map IS Layer 4 by construction`), plus the small ×AI key (`own words → the diff` vs `raw dump → slop`).
- **Bottom band — the keystone TWIN-TRACE METER "SHARPER, NOT LONGER.":** shared axis = inputs accumulated over time; a ghosted-grey **HOARD** curve climbing-and-dimming (taller = harder to re-read = the failure) vs a cyan **MAP** band whose footprint stays flat while its internal tick density/contrast rises (same size, grows sharper).
- **The ONE RED OBJECT — the orphan / re-read trap:** a captured note that *skipped* INTEGRATE, saved as a growing stack of dim disconnected highlight-walls leaking red, stamped `RE-READ = 0 · SAVED YOU NOTHING` (`Mindlessness in a study costume [→ 1.1]`). Red appears nowhere else.
- **Footer:** `METABOLISE, DON'T ACCUMULATE.` + callbacks (`same shape as 3.1 — write the improvement back into the durable artifact`; `INTEGRATE is a learning rep disguised as note-keeping`; `→ Part 4.2 · make it ACT, not just inform`).

Colour rationed exactly per §5: cyan = live map / clean conditioned signal / lit INTEGRATE fundamental / sharpening resolution trace; amber = every ordinary caution (use-gate, raw-dump→slop, no-map fork, PRUNE); **exactly one red** (the orphan/re-read trap); dim grey = ghosted rising hoard, parked source-notes, faint earlier refinement ticks. §7 respected: the highlighter wall appears only as the ghosted wrong-state / red orphan (never the solution); the map is an instrument display, not a glowing-brain bubble cloud; the hero meter shows **flat footprint, rising resolution** (the "knowledge grows!" up-and-right pile is drawn grey as the failure); not a sibling redraw (open chain into a fixed frame, not 3.0's ring / 3.1's RAM↔DISK latch / 4.0's heat bus); AI is only the ×bolt-on diff comparator.

## Outputs (in `visualization/`)

- SVG: `Poster — Productive - Productivity Enhancement Part 4.1 - Progressive Summarization.svg` (~48 KB)
- PNG: `Poster — Productive - Productivity Enhancement Part 4.1 - Progressive Summarization.png` (3000×2400, ~507 KB)
- Note: the poster *name* keeps the concept filename's spelling **"Summarization"** (with a z) verbatim per the naming convention, even though the article/series text uses "Summarisation".

## Verification

PNG verified non-empty, 3000×2400, ~507 KB (PIL). Full poster read back and inspected, plus two high-res crops (the ENCOUNTER→INTEGRATE→LINK→PRUNE chain + ×AI bolt-on; the hero dimension line). Single red confined to the orphan trap. Two collisions found and fixed on the second render: (1) the `WRITE → FRAME` annotation overlapped the `INTEGRATE · THE HEART` header → moved up beside the ×AI box and the INTEGRATE caption shortened; (2) LINK's two under-node labels crowded the INTEGRATE caption → collapsed to a single `pin source → its node` line on the tap path, and the redundant `conditioned signal →` tag removed; (3) the dimension tag background box was too narrow so the dimension line showed through the text → widened to 324 px. No clipping after fixes.

## Deviations / notes

- No prior poster existed for this concept → clean build, no deletes (exactly one PNG + one SVG).
- Record named with the concept slug suffix because a `blog-viz-poster-2026-06-19-*.md` record already existed (the Self-Improving Workflow run earlier today).
- Path-reconciliation policy unchanged: the scheduled-task's hard-coded `local_dbaa9cdd …\outputs` path is not mounted in this run session; the connected `blog viz daily - temporary/` folder (concepts/ + trackers + visualization/) is the source of truth.
- Continuity: Part 4.0 PARA already has a poster on disk (built earlier today). Part 3.0 — The Workflow Engine still has a concept but **no poster** (left pending from the 3.1 run). Next up after this = **Part 4.2 — The Operating System** (closes the Knowledge sub-arc; keep distinct from this distiller — an instrument where the sharpened map becomes an *actuator*, not just a display).
