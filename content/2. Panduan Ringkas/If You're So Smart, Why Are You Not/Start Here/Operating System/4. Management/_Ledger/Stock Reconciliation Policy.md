---
title: Stock Reconciliation Policy — POs drive stock
draft: true
tags:
  - operating-system
  - ledger
  - purchase-order
  - stock
  - policy
date: 2026-06-11
---
> [!abstract] Standing rule: **a purchase is not done until stock reflects it.** Stock forecasts are only trustworthy if `stock_on_hand` is reconciled against the Purchase Orders. The assistant runs this BEFORE any forecast.

## The rule
1. **Every PO updates stock.** When a PO is logged in `4. Management/Purchase Orders/`, immediately add its `→ Stock` quantity to the matching product note's `stock_on_hand`, and set `stock_as_of` to that date. (The Beligas POs already show the `→ Stock` column — follow that pattern for all vendors.)
2. **Before forecasting, reconcile first.** Sweep POs since each product's `stock_as_of` and apply any unposted purchases. Stale stock = wrong run-out dates (e.g. Cardarine read as 0 on 2026-06-11 while a 2026-06-08 PO had already added 2,000mg).
3. **Net against in-flight buys too** — cart / "almost paid" / on-the-way items count once paid; check the Google Sheet Expenses tab vs the PO folder for unlogged spend.
4. **Flag bought-but-not-catalogued** items into `0. Reconciliation — Gaps.md` instead of silently dropping them.
5. **Append the product Purchase Log.** Every posted PO adds a `Purchase` row to the matching Stock product note. Every physical count, usage/dose change, or confirmed empty pack adds a dated `Stock check`, `Usage change`, or `Depletion` row.
6. **Keep current state and history in sync.** A stock-check row must also update `stock_on_hand` + `stock_as_of`; a usage-change row must also update `daily_dose` / `dosing` and refresh `runout_forecast`.
7. **Do not invent lot provenance.** Current balances created before the Purchase Log are aggregate balances. List the supported acquisition POs, but mark exact surviving lots as unknown until a physical count or depletion event establishes them.

## How to reconcile (assistant)
- For each PO note, read its item table's `→ Stock` deltas (or the item × qty × package math) and add to the product note's `stock_on_hand`.
- Append the same event under the product's `## Purchase Log`, newest-first, with a wikilink to the PO.
- If a product note has no `→ Stock`-mapped PO since `stock_as_of`, leave it but note the gap.
- Re-run `_Ledger/scripts/os_nut.py` after posting.
- Run `_Ledger/scripts/os_purchase_logs.py "<Operating System path>" --apply` after importing or correcting historical POs; audit mode (without `--apply`) reports unmatched rows and product provenance gaps.

## Links
- POs: [[0. Purchase Orders]] · Gaps: [[0. Reconciliation — Gaps]] · Forecast SOP: [[Stock Forecast — Intake Protocol]] · Stock plan: [[Stock & Restock Plan]]
