---
title: Pipelines
draft: true
type: index
tags:
  - operating-system
  - pipelines
  - uses
  - index
date: 2026-06-06
---
> [!abstract] The **Uses** layer — how the Operating System is actually run.
> [[The Operating System]] says *why* the OS exists; [[Schema — Data Model]] says *how the data is shaped*; the [[Product List|Catalog]] says *what exists*; the `_Ledger` says *what it costs*. This note says **how it's operated**: four pipelines, each owning a lever, each with a metric and a trigger. Start here when planning or running a cycle.

## The four pipelines

| # | Pipeline | What it owns (the lever) | Primary metric | Action trigger | Lives in |
|---|---|---|---|---|---|
| **P1** | **Endocrine** (Base) | Test / EQ / HCG — the MPS engine | Hematocrit `<52%` + Sensitive E₂ | Week-8 blood work | [[Endocrine Design Rules]] + the live cycle |
| **P2** | **Bio-Feedback** (Fuel) | Calories — bulk / cut / maintain | Gym logbook + Body Fat % | Stalled strength OR loss of abs | [[Cut Protocol]] / [[Bulk Protocol]] / [[Recomposition & Lean Bulk Protocol|Lean Bulk]] |
| **P3** | **Deployment** (Accelerators) | Tiered orals / adjusters | Variable dosing (μg thyroid/clen) | Mini-cut tier trigger | [[Off-Season Mini-Cut & Accelerator Tiers]] |
| **P4** | **Year-Round** (Shield) | Cardio / renal / metabolic protection | BP `<120/80` + lipids | Daily morning anchor | [[Year-Round Shield]] |

## How they interact

```
            ┌─────────────────────────────┐
            │  P4 SHIELD (constant floor)  │   ← never cycles
            └─────────────────────────────┘
   P2 (BF% + strength) ──► picks SEASON ──► sets P3 TIER
            │                                    │
            ▼                                    ▼
   "food or drug?" ◄── bloods gate ──► P1 dose pull (if tolerated)
```

1. **P2 decides the season** (BF% + strength → bulk / cut / maintain).
2. **The season sets P3's tier** (high-BF cut opens at Tier 1; escalate as you lean out; Tier 3 only post-lean-bulk).
3. **P1 reacts to P2 + bloods** (stall → "food or drug?"; P1 only moves a dose if tolerability allows, else P2 moves food).
4. **P4 never moves** — it tightens, never loosens, as the others add cardiovascular/renal load.

## Pipeline → notes

- **P1 Endocrine** → [[Endocrine Design Rules]] (3-tier Test: cruise 200 / mid 350 / blast 550, + EQ block, HCG) · current run: [[2026 Q3 Cut to 15%]] · history: [[2026 Q2 Cycle]]
- **P2 Bio-Feedback** → [[Cut Protocol]] · [[Bulk Protocol]] · [[Recomposition & Lean Bulk Protocol|Lean Bulk]] (refeed/diet-break periodization documented in the active campaign)
- **P3 Deployment** → [[Off-Season Mini-Cut & Accelerator Tiers]] (Tier 1 → 2 → 3 ladder)
- **P4 Year-Round** → [[Year-Round Shield]] (Rosuvastatin · ARB · Tadalafil · Retatrutide · L-Carnitine · Aspirin)
- **Feedback loop** → [[Bloodwork & Calculated Biomarkers]] (the data that gates P1)

## Active campaign
- **[[2026 Q3 Cut to 15%]]** — 26% → 15% @ 90 kg, two medium cuts. Cut Week 0 = 11 Jun 2026 (test-cycle week 8).

## The rest of the OS
- **Why:** [[The Operating System]] · **What next:** [[Skeleton — Build Map]]
- **Catalog (what exists):** [[Product List]] · **Schema (data model):** [[Schema — Data Model]]
- **Management (numbers):** [[Monthly Nut]] · [[Stock & Restock Plan]] · [[Price & Sourcing Optimization]] · [[Freedom Numbers]]
