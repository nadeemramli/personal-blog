---
title: Annual Cycle Design
draft: true
tags:
  - operating-system
  - cycle-design
  - peds
  - cost
date: 2026-05-31
---
> [!abstract] How the PED protocol is actually run — and why the cost is annualized, not stacked.
> Nadeem does **not** run all compounds year-round (that's the naive model — "continuous Anavar is death"). The design is **continuous Testosterone + ONE rotating primary compound at a time**, following the [[Part 3.2 - Cycle Design|Cycle Design]] and [[Part 5.0 - Putting It All Together|worked-example]] logic from the Performance Enhancement series. This note is the source of truth for the [[Monthly Nut]] PED line.

## The design (continuous-but-rotating)

- **Testosterone — the always-on base.** Runs all 52 weeks (blast-and-cruise). Blast ~450 mg/wk (e.g. the 20-week EQ block), cruise lower (~250 mg/wk). *Modeled at a blended ~325 mg/wk — confirm your real cruise dose.*
- **EQ (Boldenone) — the long-ester offseason block.** ~20 weeks @ 300 mg/wk. The biggest rotating block; its long ester is *why* the block is long ([[Part 3.1 - The Anabolic Steroid Family Tree|family tree]]). Run at a sane dose because hematocrit is the limiter.
- **Anavar — DHT-family oral, on/off.** ~8 weeks on → ~6 weeks rest → ~8 weeks on (≈16 wk/yr), **never continuous**. Run with **MK-677** and **T4**.
- **MK-677** — runs **with Anavar** (~16 wk/yr), GH/IGF-1 pathway.
- **T4 (Levothyroxine)** — runs **with the Anavar/MK-677 block** (~16 wk/yr).
- **Trenbolone — the sharp tool, last.** ≤ 8 weeks max, 70–150 mg/wk. Only when a specific peak demands it ([[Part 5.0 - Putting It All Together|Year 3]] logic); prolactin watched.
- **Proviron — conditional.** SHBG/estrogen management **only when there's no other aromatase competitor**. With EQ in the stack, **Proviron is OFF**. ~8 wk/yr.

> [!note] The rule that prevents double-counting
> At any moment it's **Test + one or two rotating compounds**, not the whole cabinet. So the annual cost = each compound's `weekly dose × weeks/year × cost-per-mg`, summed, then ÷ 12 — not every compound priced as if it ran all year.

## The annual PED cost model

| Compound | Weekly dose | Weeks/yr | Cost/unit | RM/yr | RM/mo |
|---|---|---|---|---|---|
| Testosterone (blended) | ~311 mg | 52 | RM0.060/mg | 963 | 80.32 |
| EQ (Boldenone) | 350 mg | 20 | RM0.072/mg | 504 | 42.00 |
| Oxandrolone (Anavar) | 240 mg (40×6d) | 16 | RM0.20/mg | 768 | 64.00 |
| MK-677 | 140 mg | 16 | RM0.318/mg | 712 | 59.36 |
| Trenbolone Acetate | 110 mg | 8 | RM0.20/mg | 176 | 14.67 |
| Proviron | 175 mg | 8 | RM0.134/mg | 188 | 15.68 |
| Cardarine (GW-501516) | 105 mg | 8 | RM0.212/mg | 178 | 14.84 |
| Levothyroxine (T4) | 350 mcg | 16 | RM0.011/mcg | 60 | 4.97 |
| | | | | **3,549** | **295.83** |

**PED protocol ≈ RM296/mo annualized** — half the RM595 the naive year-round model produced. Each note carries a `weeks_per_year` field so this can be rebuilt as a Base view.

## Per-compound dosing context

> [!important] Testosterone runs in three tiers — E2-driven, not fixed
> Test is dialled to estrogen, **not** held at one number:
> - **Cruise — 200 mg/wk** (off-block baseline / TRT-ish).
> - **Mid-cruise — 350 mg/wk** (the *current* setting, run alongside EQ — EQ theoretically depletes/shifts E2, so Test is raised to keep the androgen:estrogen ratio in range).
> - **Blast — 550 mg/wk** (peak growth block).
>
> The RM80/mo line uses a blended ~311 mg/wk (≈24wk cruise + 20wk mid + 8wk blast). **All of this is provisional and re-set by bloodwork** — when a panel comes in, update the tier weeks and this line re-derives.

EQ at 350 mg/wk matches the live [[2026 Q2 Cycle]] schedule (Test 350 + EQ 350, 100mg/shot). Anavar + MK-677 run daily through their blocks; Cardarine is the cutting add.

> [!note] Cycle support is now situational too
> TUDCA (16wk, 17-alkylated orals only — Irbesartan covers kidney), P5P (8wk, Tren), CaDG (28wk) carry `weeks_per_year` in [[Monthly Nut]]. See [[Schedule Audit]].

## Links
- Method: [[Part 3.2 - Cycle Design]] · [[Part 5.0 - Putting It All Together]] · [[Part 5.1 - Cost]]
- Cost rollup: [[Monthly Nut]] · Current run: [[2026 Q2 Cycle]] · Protocols: [[Bulk Protocol]] / [[Cut Protocol]] / [[Lean Bulk Protocol]]
