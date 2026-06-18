# Blog Viz Poster — 2026-06-17

**Date:** 2026-06-17
**Source brief:** `concepts/Visualization Concept — Productive - Cognitive Enhancement Part 3.0 - Cognitive Performance Compounds.md` (in the connected `blog viz daily - temporary/` folder)
**Article:** Productive / Cognitive Enhancement / **Part 3.0 — Cognitive Performance Compounds** (8th Cognitive poster; first of the two Pharmacology articles 3.0/3.1)

## Visual concept used

Locked **"Neural Signal Schematic"** Productive style, with a new sub-archetype: a **FAULT-ROUTED DIAGNOSTIC BOARD** read left→right as a signal that enters as a complaint and leaves as a correct, measured action. **STEP 1** is a three-way SYMPTOM PROBE (CAN'T START → Drive, CAN'T RETAIN → Memory [lit route], DRIVEN BUT STUCK → Flexibility) — only one route lights, making diagnosis the first act. **STEP 2** is the full-height BEHAVIOURAL-FIX GATE where most faults dead-end "free" (callback to 2.0). The body is **three lever-lanes**, each a bright cyan **Tier-2 trunk you live on**, with a **locked Tier-1 tap** (amber padlock, "high-stakes only") above and a **hatched Tier-3 tap** (dim, "you are the study") below — so tiers read as branches off the trunk, never a climb-to-stronger ladder. DRIVE carries the Modafinil "fix sleep first" honesty mark and the amphetamine **bleed** leaking into two external PEACEFUL↓ / HEALTHY↓ pillar-buses. MEMORY is the focal lane: it **forks** into FUEL (CDP-Choline preferred, Alpha-GPC stroke-signal caveat, ALCAR, Bacopa) and BRAKE-RELEASE (Huperzine-A cycle-it; locked Donepezil/Galantamine "sledgehammer"), recombining at a **summing junction = the one red object**: the CHOLINERGIC OVERLOAD lamp (MORE CHOLINE ≠ MORE MEMORY). FLEXIBILITY is the un-alarmed calm lane (L-Theanine, Ashwagandha, Saffron, 5-HTP; locked Buspirone with a bolted "benzodiazepines excluded on purpose" sub-gate; hatched Selank/Phenibut with an amber dependence lockout). A **NICOTINE jumper** bridges Drive↔Memory. **STEP 4** is the VERDICT comparator (clean cyan Tier-2 wave vs jagged clipped Tier-1-maxed) under the law plate `STRONGEST FOR THE WRONG LEVER < RIGHT AT THE LOWEST TIER`, with a `CHANGE ONE VARIABLE · THEN MEASURE` feedback loop back to the probe. Foot ribbon = a 3×3 lane×tier dot-map (Tier-2 row lit, Tier-1 padlocked, Tier-3 hatched) + closing stamp `DIAGNOSE THE LEVER · START LOW · CHANGE ONE THING`. Colour discipline per §5: cyan = live signal/Tier-2; amber = all caution (gates, locks, honesty marks, bleed, lockouts); **exactly one red** (the overload lamp); dim grey = fenced/unproven.

## Outputs (authoritative copies in `visualization/`)

- PNG: `visualization/Poster — Productive - Cognitive Enhancement Part 3.0 - Cognitive Performance Compounds.png` (3400×2300, ~514 KB)
- SVG: `visualization/Poster — Productive - Cognitive Enhancement Part 3.0 - Cognitive Performance Compounds.svg` (~45 KB, editable raw source)
- Generator: `gen_poster.py` (session scratch) — hand-coded SVG, landscape `viewBox 1200…` → actual `1700×1150` @2×.

## Renderer & verification

- **Renderer: CairoSVG 2.9.0** (rsvg-convert and Playwright/Chromium both unavailable in this sandbox; apt install of librsvg2-bin failed). Rendered at 2× (3400×2300). Because CairoSVG ignores SVG filters, the glow was hand-faked with layered translucent shapes so the schematic holds up without `feGaussianBlur`.
- Fonts fall back to DejaVu Sans / DejaVu Sans Mono at render time (Inter/JetBrains Mono unavailable), consistent with prior Cognitive posters. Emoji/risky glyphs avoided: padlocks drawn as vectors (not 🔒); `✓` and `≆` removed; only DejaVu-safe glyphs used (`·`, `≠`, `≤`, `↓`, `→`).
- Verified: PNG non-empty (514 KB > 50 KB), dimensions 3400×2300 as expected. Full view + region crops (DRIVE, MEMORY fork/red lamp, FLEXIBILITY, VERDICT, probe/gate/nicotine, foot ribbon) read back and inspected — single red confined to the overload lamp, no text collisions after fixes.
- **Build fixes:** (1) Modafinil reality tag + amphetamine caption originally overran the DRIVE trunk and collided with the Tier-3 label → relocated to a clean stack below the trunk. (2) The MEMORY red overload stamp overflowed into the VERDICT column → junction moved left (JUNC_X 1052→980) and fuel chips compressed so the stamp fits within the lane. (3) FLEXIBILITY "wired but stuck" plate overlapped Buspirone and the memory "sledgehammer" caption dropped into the flex lane → FLEX lane centre lowered (812→840), tagline moved top-left, sledgehammer kept inside the locked chip band. (4) NICOTINE label box overlapped the gate → jumper + label moved into the clear gap right of the gate.

## Deviations / fallbacks

- **Path reconciliation:** the scheduled-task's hard-coded outputs path is not mounted; the connected `blog viz daily - temporary/` folder is the reachable source of truth (consistent with prior runs). Brief found directly via the `concepts/` folder (most-recently-modified, Jun 17), no transcript fallback needed.
- Clean run — no prior poster existed for this concept, so no deletes (exactly one PNG + one SVG).
- Minor faithful compressions for legibility (shortened captions, single-word tap labels) but all named compounds, tiers, honesty marks, the fuel-vs-brake fork, the one red overload, and the verdict law are present per the brief.
