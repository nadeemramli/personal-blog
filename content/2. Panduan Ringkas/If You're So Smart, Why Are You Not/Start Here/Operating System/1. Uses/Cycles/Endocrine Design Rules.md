---
title: Endocrine Design Rules
draft: true
type: reference
tags:
  - operating-system
  - cycle-design
  - peds
  - p1
date: 2026-06-06
---
> [!abstract] The timeless **Pipeline 1 (Endocrine)** rules — *how* any cycle is designed, separate from *which* cycle you're running.
> Pairs with [[Cycle Roadmap (to FFMI 28-29)]] (the sequence) and the per-cycle notes (the specifics). Absorbed from the retired "Annual Cycle Design" note. Method follows [[Part 3.2 - Cycle Design]] + [[Part 5.1 - Putting It All Together]].

## Rule 1 — Continuous-but-rotating
**Continuous Testosterone + ONE (occasionally two) rotating primary compound at a time** — never the whole cabinet. "Continuous Anavar is death." Every block = Test base + the one tool that phase needs (Tren for a cut, EQ/Primo for a bulk, etc.).

## Rule 2 — Testosterone dose zones (E2-driven, reset by bloodwork)
| Zone | Dose | Use |
|---|---|---|
| Cruise | ~200 mg/wk | off-block / recovery |
| **Sweet spot** | **350 mg/wk** | current default — best tolerance:growth |
| Mid | 400 mg/wk | lean-bulk base |
| Danger-mid | 500 mg/wk | blast ramp |
| **Danger (max)** | **600 mg/wk** | hard ceiling — peak blast only |

All provisional — a panel re-sets the dose. Every cycle's start is gated on bloods.

## Rule 2b — Lateral compound logic (EQ vs Primobolan)
The rotating anabolic alongside Test, chosen by phase + E2 behaviour:
- **Primobolan** — **mild on E2**, non-aromatizing, no water. **Lean-bulk default = Test 450 + Primo 200 mg/wk.** Also a clean cut-lateral, or added to a Test-only cycle when test alone isn't enough anabolic. (Now sourced — preferred over EQ for cleanliness.)
- **EQ (Boldenone)** — **tanks E2**, so the blast design is **Test 450 → ramp 500–600 once EQ saturates** (raise test to restore E2/androgen:estrogen ratio). The classic long-block blast lateral; hematocrit is the limiter.
- **Rule:** Primobolan and EQ are *alternatives* in the same slot — run one. Primo if you want mild/clean; EQ if you want the bigger blast (accepting the E2-management + Hct load).

## Rule 3 — On/off windows per compound
| Compound | Window | Rule |
|---|---|---|
| Testosterone | 52 wks | always-on base (blast/cruise) |
| EQ (Boldenone) | ~20 wk @ 300 | long-ester offseason block; hematocrit is the limiter |
| **Primobolan** | bulk/cut lateral | **cleaner non-aromatizing alt to EQ** (now sourced) — preferred |
| Anavar | 8 on / ~6 off (~16 wk/yr) | **never continuous**; run with MK-677 + T4 |
| MK-677 | with Anavar block (~16 wk/yr) | GH/IGF-1 |
| T4 | with Anavar/MK block (~16 wk/yr) | metabolic |
| Trenbolone | ≤ 8 wk, 70–150 mg | sharp tool, peak only; prolactin watched (P5P) |
| Proviron | ~8 wk, conditional | **OFF when EQ is in the stack** (no double aromatase competitor) |

## Rule 4 — No double-counting (the cost method)
At any moment it's **Test + one or two rotating compounds**, not the whole cabinet — so annual PED cost is:
`Σ (weekly dose × weeks_per_year × cost-per-mg) ÷ 12`
…**not** every compound priced as if it ran all year. Each product note carries a `weeks_per_year` field so this rebuilds as a Base view. Live cost now comes from the **per-cycle stock plans** ([[Cut Campaign Stock & Cost]]) rolled into [[Monthly Nut]].

> [!note] Legacy annualized model (illustrative, pre-Primo, old FX) — kept for the *method*, not the numbers:
> Test ~311mg×52 · EQ 350×20 · Anavar 240×16 · MK 140×16 · Tren 110×8 · Proviron 175×8 · Cardarine 105×8 · T4 350mcg×16 → **≈ RM296/mo annualized** (vs ~RM595 naive year-round). Rebuild live in [[Monthly Nut]] at current FX 4.1.

## Rule 5 — Cycle support is situational too
- **TUDCA** — ~16 wk, only with 17-alkylated orals (Irbesartan