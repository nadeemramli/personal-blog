# Blog Viz Poster — Run Record

- **Date:** 2026-06-15
- **Source brief:** `concepts/Visualization Concept — Productive - Cognitive Enhancement Part 4.2 - The Enhanced Stack.md` (in the connected blog folder `blog viz daily - temporary/`)
- **Article:** Productive · Cognitive Enhancement · **Part 4.2 — The Enhanced Stack**
- **Series style:** "Neural Signal Schematic" (locked Productive-pillar style, inherited verbatim from Part 4.0). New sub-archetype: **the six-channel Overdrive Console**.

## Visual concept used

A portrait six-channel "Overdrive Console" rendering the enhanced bio-circuit as a signal-gain rack. Six vertical channel strips — IGNITION, ACETYLCHOLINE, NEUROGENESIS, SHIELD, NEUROSTEROIDS, STATE — sit side by side. A single bright cyan **NATURAL CEILING** datum runs unbroken across all six at the lower third: below it is the established, lit, safe base (steady cyan glow); above it is the darkening, warming **overdrive band** where risk climbs and return flattens (the vertical axis = risk up / return down, with a flattening marginal-return curve on the right margin). Each channel docks a tier-coded module: Tier 1 Rx compounds (Modafinil, Memantine) drawn **gated/padlocked**, Tier 3 peptides drawn **hatched/translucent** (unproven, not gentler), amber cautions for the amphetamine cardiovascular tax and racetam-headache. The SHIELD channel is wired with a faint tie-bar coupling it to channels 1–3 (it rises with the performance dials; performance meter reads down, protection up — "the shield you add because you're enhancing"). The poster's only two reds are the two kill-switches — **Dihexa** (barbed module that won't seat, c-Met oncogene / no human data) on Neurogenesis and **Phenibut** (red lockout bar, dependence/withdrawal trap) on State. An amber checkpoint glyph carries the 4.0 callback (`PASS THE 4.0 GATE FIRST`) with most traces dead-ending dim at the ceiling. A lower-left Golden Rule inset contrasts a smooth combined low-dose waveform against a clipped max-dosed one. A subordinate landscape foot ribbon shows "A Maximal Day — a map, not a menu" as a gas-and-brakes wave that rises into the excitatory tunnel then falls back into recovery and deep-sleep reset. Thesis lockup: `SAME CIRCUIT — TURNED UP. THE DESTINATION IS BACK AT THE BASE.`

## Palette (locked tokens, §5)

Cyan `#2DD4BF` = live signal/base; amber `#E8A23D` (warming to `#B8431F`/`#D77A4A` at the top of the band) = caution/tiers/overdrive/gate; coral red `#FF5C5C` used **only twice** (Dihexa + Phenibut); off-white `#E6E8EE` text; dim grey `#39424E` for inactive/dead-ended/unproven. Near-black ground `#0B0F14` with a cyan glow at the ceiling and a cooler/warmer darkening toward the top.

## Outputs

- SVG: `visualization/Poster — Productive - Cognitive Enhancement Part 4.2 - The Enhanced Stack.svg`
- PNG: `visualization/Poster — Productive - Cognitive Enhancement Part 4.2 - The Enhanced Stack.png`

## Renderer & verification

- **Renderer:** CairoSVG (rsvg-convert and Playwright unavailable in the sandbox, per established precedent).
- **Render size:** portrait `viewBox 1200×1500` @2× → **2400×3000**, ~373 KB. PNG non-empty, dimensions confirmed via PIL.
- **XML:** validated well-formed (ElementTree) before the final render.
- **Visual inspection:** full poster + a zoomed footer crop read back. Confirmed: six channel strips with the cyan natural-ceiling datum, gated/hatched tier coding, coupled SHIELD tie-bar, exactly two reds (Dihexa barbed + Phenibut lockout), the gate callback, Golden Rule clipping inset, and the rise-then-fall Maximal-Day ribbon all render.
- **Build fixes:** the outputs-side SVG tail repeatedly lost its closing `</text></g></svg>` on a file-tool → mount sync (known issue); the footer thesis was split into two lines and the closing tags were re-appended via bash, then XML re-validated before the final render.

## Deviations from the brief

- Headline chosen from the brief's three options: **`THE EDGE OF THE MAP`** (the thesis lockup borrows the third option, "same circuit — turned up").
- No prior poster existed for this concept, so no deletes were needed (exactly one PNG + one SVG written).
- Tier 2 (racetams) shown as an "OTC-ish" mid card to sit between the gated Tier 1 and hatched Tier 3 — kept neutral, amber only on its one cost (headache without choline).

**Next up on this track:** Cognitive Enhancement **Part 4.3 — The Hybrid Stack** (make it a patch-bay / what-to-unplug-when-you-plug-in device, not another gain console) and **Part 4.1 — The Natural Stack** (the clean daily engine that *is* this poster's natural-ceiling datum).
