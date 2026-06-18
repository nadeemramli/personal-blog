# Blog Viz Poster — Run Record

- **Date:** 2026-06-18 (second poster of the day)
- **Source brief:** `concepts/Visualization Concept — Productive - Productivity Enhancement Part 2.0 - The Machine and the Room.md` (today's brief — the most-recently-modified concept on disk, mtime Jun 18 05:42, with its dated pointer `concepts/blog-viz-2026-06-18-part-2-0-the-machine-and-the-room.md`; cross-checked against the poster tracker, whose prior entry ends "Next up = Part 2.0 — The Machine and the Room").
- **Article:** Productive · Productivity Enhancement · **Part 2.0 — The Machine and the Room** (3rd poster of the track; the Physical Layer).
- **Locked pillar style:** Neural Signal Schematic (Productive). New sub-archetype this poster: **Operating-Environment Enclosure Section** — a landscape cutaway of one rated workstation bay.

## Visual concept used

A landscape cutaway SECTION of a single workstation "equipment bay": the whole poster is framed by the ROOM as a rated **enclosure envelope**, and one bright cyan **ATTENTION CURRENT** enters at the left wall, threads left→right through the bay's components, and arrives at a lit **WORK / OUTPUT** node on the right. The four article sections become parts of one machine: **SCREENS** = the I/O wall (three ports permanently assigned `MAKE · REFERENCE · COMMS`, a ghosted single-port throwing an amber `ALT-TAB` switching-tax spark, a tier rail `1 leaky · 2 floor · 3 standard · 4–6 power` with a viewing-cone and an `ULTRAWIDE = TWO` chip); **MACHINE / RAM** = the board with a context-hold capacitor visibly bleeding into a `WAIT-STATE` (`WAITING = CONTEXT DECAYING`; ticks `16GB FLOOR · 32GB COMFORTABLE · SSD NON-NEGOTIABLE`; tagged `HIGHEST RETURN-ON-RINGGIT`); **DESK** = a `WITHIN ARM'S REACH` reachable-zone ring around a keyboard glyph with clutter swept off as amber parasitic competitors (`CLEAN SURFACE = LOWER NOISE FLOOR`, `STAND UP = A CONTEXT SWITCH IN DISGUISE`); **ROOM** = the enclosure envelope plus three edge controls — LIGHT (glare bounce corrected, top-left), SOUND (a left-wall noise-shield passing a steady masking band but pierced by one amber spike, `STEADY PASSES · SUDDEN PIERCES`), and the primary hero.

**Hero #1 — the THERMAL DERATING CEILING:** a top-right temperature gauge with a green operating band `21–25°C` and the needle pushed into the amber hot zone (`~31°C, 2pm`); a horizontal **derating ceiling** line rides above the WORK node and visibly *caps* the cyan output bar regardless of upstream push. **Hero #2 — the COST-INVERSION LEVERAGE LEDGER** (lower-right "receipt"): bars sized by friction-sealed, cheapest tallest (`2nd MON RM400–700` biggest leak → `RAM` → `SSD` → `ARM` → `FAN/AC` → `CHAIR RM400–1,200` shortest), with a dim "what you expected to need" ghost behind the expensive end and the caption "order of leverage, not price" under the lockup **THE CHEAPEST FIXES SEAL THE BIGGEST LEAKS.** Along the current rail, three sealed junctions (`SEAL`) show each cheap fix plugging a leak-to-ground so the current arrives whole.

**The single RED object** = the upstream `WILLPOWER · MAX` override knob, wired in and failing against the heat-derating ceiling — output stays clamped, red fault lamp `CAN'T OUT-DISCIPLINE THE ROOM` ("grinding through the 2 pm heat and blaming your willpower"). Resolution band: an `ALL FOUR RATED` ribbon (`SCREENS ✓ · MACHINE ✓ · DESK ✓ · ROOM ✓ → FULL OUTPUT`) under the plate **THE SETUP DISAPPEARS. ONLY THE WORK IS LEFT.**, a tie-line chip (`PHYSICAL LAYER = the buy-once defence vs DISTRACTION → Part 1.1`), and the three-pillar footer (`COGNITIVE = hardware · LEARNING = software · PRODUCTIVITY = the OS`). Three "why it works" micro-annotations are pinned to their components (heat → PLOS Med 2018; clutter → McMains & Kastner 2011; screens → Part 1.1).

Colour rationed exactly per the brief §5: cyan = live attention current / sealed junctions / lit screen channels / charged-then-clamped output / the RATED state; amber = every out-of-spec caution (hot needle, alt-tab spark, capacitor bleed, clutter, stand-up trip, sound spike, budget chips, diminishing-returns); EXACTLY ONE red (the willpower-vs-heat fault); dim grey = ghosted single-screen / "wanted higher" / expensive-end ghost.

## Outputs

- SVG: `visualization/Poster — Productive - Productivity Enhancement Part 2.0 - The Machine and the Room.svg` (27,757 B)
- PNG: `visualization/Poster — Productive - Productivity Enhancement Part 2.0 - The Machine and the Room.png` (609,719 B, 3000×2400 = 2× the 1500×1200 viewBox)

## Renderer & verification

- **Renderer:** CairoSVG at 2× (3000×2400). rsvg-convert + Playwright unavailable in this sandbox (consistent with prior runs); fonts fall back to DejaVu Sans / DejaVu Sans Mono — legible and on-style.
- **Verified:** SVG well-formed (minidom) on the mount; PNG non-empty, 3000×2400 (PIL); rendered PNG read back and inspected at full size plus four region crops (gauge, desk, lower-right WORK/fault/ledger cluster, lower-left RATED ribbon). Single red confined to the willpower-vs-heat fault; no clipping; no text collisions after fixes.
- **No prior poster** for this concept → no deletes (exactly one PNG + one SVG, per output conventions).

## Build fixes / deviations

- First render had three overlaps in the lower-right: the red fault caption crossed the WORK output bar, a stray free-floating red dot added extra red, and the RATED-ribbon intro phrase ran into the SCREENS stamp. Fixed: extended the current rail and moved the WORK node to the far right with its label above the rail (clear of the fault block); removed the stray red dot (preserving the one-red rule); replaced the intro phrase with a compact `ALL FOUR RATED / the bay disappears` kicker and finished the ribbon arrow with a `FULL OUTPUT` tag.
- **Mount-sync truncation recurred** (known issue): file-tool (Write/Edit) writes of the ~28 KB SVG to the Windows folder were truncated to `<svg ` / NUL-padded on the Linux render mount, breaking the XML. Fixed per established workaround — wrote the complete final SVG directly into the render mount via a bash heredoc (entity-escaped the non-DejaVu `⊹` glyph as `&#8759;`), validated, rendered there, then `cp`-ed the validated SVG + PNG into `visualization/`.
- **Brief found via the connected blog folder** (no transcript fallback needed). Path-reconciliation policy unchanged: the scheduled-task file's hard-coded `local_dbaa9cdd … \outputs` path is not mounted; the live source of truth is this `blog viz daily - temporary/` folder.
