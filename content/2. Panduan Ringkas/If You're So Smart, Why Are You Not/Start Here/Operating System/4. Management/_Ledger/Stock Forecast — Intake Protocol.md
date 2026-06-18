---
title: Stock Forecast — Intake Protocol
draft: true
tags:
  - operating-system
  - ledger
  - stock
  - runbook
  - sop
date: 2026-06-11
---
> [!abstract] What this is
> A standing **SOP for the assistant**. Whenever Nadeem asks the stock-forecast question, run this intake **before** computing — the answer is only as good as the cycle context, and the catalog has known data gaps that silently break the math. Ask first, then forecast.

## Trigger phrases (any of these → run intake)
- "Are we good stock-wise till end of next year / [date]?"
- "Calculate and forecast our stock."
- "What do we need to figure out, buy, and prepare?"
- "What info do you need to confirm this?" / "Want me to recheck stock?"

## Step 0 — Reconcile POs → stock FIRST (mandatory)
Per [[Stock Reconciliation Policy]]: sweep `4. Management/Purchase Orders/` for any buy newer than each product's `stock_as_of` and post it to `stock_on_hand` before computing. **Stale stock = wrong forecast** (e.g. Cardarine showed 0 while a PO had already added 2,000mg). Also account for the [[Training Rhythm]] (3-on-1-off, ~5.25 training days/wk) for training-day-dosed items.

## Step 1 — Ask these intake questions FIRST (do not skip)

1. **Horizon** — to what date? *(Default if unstated: 31 Dec of next calendar year.)*
2. **Current cycle & phase** — what PED cycle is running right now, and what's the next campaign? (e.g. cut starting 14 Jul). Which compounds are **on vs off** for it?
3. **Test ester status** — which Test is active, how many weeks of stock remain, and what's the **handoff** (incoming ester / PO not yet logged)?
4. **PED calendar** — still matches `Endocrine Design Rules` / `Annual Cycle Design`? Any dose changes from bloodwork? *(Burn is driven by weekly-mg × weeks/year — confirm before costing PEDs.)*
5. **Recent buys not yet in the sheet** — anything bought / in-cart / on-the-way to **net against stock** before forecasting? (Check `Purchase Orders/` vs Expenses sheet.)
6. **Peptide protocol** — current dose + frequency + cycle-weeks for each active peptide (INDEXA-funded, so excluded from the nut but still stock-forecast). Restock flags? (GHK-Cu / HGH / KPV historically zero.)
7. **Situational / rarely-used items** — present the bucket-B + paused checklist; Nadeem marks **restock Y/N** per item (these aren't daily-dosed, so the engine can't infer them).

## Step 2 — Compute (the engine a spreadsheet can't replace)
- Script: `_Ledger/scripts/os_nut.py "<OS folder>"`. Stock view = `days_until_empty = stock_on_hand ÷ effective_daily`.
- `effective_daily = daily_dose × (days_per_week/7) × (weeks_per_year/52)`; DPW: ED 7, EOD 3.5, ITD 4, OCC 4, TD 6.
- PEDs use the calendar: `weekly_mg × weeks_per_year` → mg/yr; run-out = `stock_on_hand ÷ (mg_yr/365)`.
- Shelf-life items (skin/hair/consumables) deplete by `shelf_life_months`, not dose — treat as **ongoing rebuy (bucket B)**, not a one-time stock-up.
- `stock_on_hand` convention: **total mass in the dose unit** (mg / mcg / g). Powders in g; tabs/vials in mg. Spot-check units before trusting.

## Step 3 — Output
Three buckets: **(A) one-time bulk to reach horizon** (dose items, minus what's on hand), **(B) ongoing rebuy** (perishables + occasional), **(C) already covered**. Plus a **vendor-grouped buy list ordered by lead time** (kohohpharma/crypto + INDEXA/TCI are slowest — flag first) and run-out dates. Feed totals to `Freedom Numbers`.

## Known data-quality watchpoints (verify before asserting)
- `stock_on_hand` ~70% populated; `daily_dose` ~58%; `weeks_per_year` ~12%; no `stock_unit` field.
- Paused items don't burn — exclude unless Nadeem reactivates them.
- Watch duplicate physical-vial vs calendar-line notes (e.g. *Etho Test 450* = Beligas Test E = the calendar Test line). Don't double-count; retire empties.

## Links
- [[Stock & Restock Plan]] · [[Monthly Nut]] · [[Freedom Numbers]] · [[Price & Sourcing Optimization]] · Cycle: [[Annual Cycle Design]] · Reconcile: [[0. Reconciliation — Gaps]]
