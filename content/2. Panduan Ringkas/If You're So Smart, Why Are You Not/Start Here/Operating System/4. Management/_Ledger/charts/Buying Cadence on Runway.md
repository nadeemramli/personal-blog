---
title: Buying Cadence on Runway
draft: true
tags:
  - operating-system
  - ledger
  - stock
  - restock
  - buying-cadence
date: 2026-06-21
---
> [!abstract] When to restock — the runway, overlaid with iHerb's biggest sale windows.
> Same run-out engine as the [[overall_runway.svg|main runway]], but instead of cut / lean-bulk phase bands it shades **iHerb sale windows** in gold. Read each bar's end date against the nearest gold band: if a product runs dry **just before or inside** a sale, hold the buy for the discount; if it runs out well before the next sale, buy now (or bridge with one bottle).

![[buying_runway.png]]

## The iHerb sale calendar (gold bands)

| Window | When | What |
|---|---|---|
| **Mid-year clearance** | ~June | Seasonal clear-out; decent sitewide cuts |
| **Anniversary Sale** ⭐ | **September** (month-long) | iHerb's **biggest** event — ~**28%** off popular brands/categories. **Time the big bucket-A supplement stock-up here.** |
| **Black Friday / Cyber Monday** | November | Weekly deal drops, steep sitewide discounts, gift sets |
| **Year-end clearance** | mid–late December | Holiday gifting + clearance |

## How to read it
- **Bar ends inside / just before a gold band →** wait for the sale to restock (especially the iHerb supplement stack).
- **Bar ends a long way before the next band →** buy now, or buy one bridging unit to reach the sale.
- **Timeline markers:** bold vertical line = **year** boundary (Jan), dashed = **quarter** (Apr/Jul/Oct), faint = month.
- Sales repeat every year; bands are drawn for 2026 + 2027 within the horizon (→ 31 Jan 2028).

> [!tip] Practical play
> Most of **Bucket A** in [[Stock & Restock Plan]] is iHerb supplements. The cheapest path to "fully stocked to horizon" is to **front-load the bulk iHerb buy in the September Anniversary Sale** (~28% off), and only buy-now the items that run dry before then (check the red/amber dates on this chart).

## Regenerate
- Main runway: `python3 "4. Management/_Ledger/scripts/os_runway.py" "2. Catalog/Products"`
- This buying-cadence view: `python3 "4. Management/_Ledger/scripts/os_runway.py" "2. Catalog/Products" "4. Management/_Ledger/charts/buying_runway.svg" buying`
- Sale dates live in the `SALES=[...]` list in `os_runway.py`; adjust if iHerb shifts its calendar.

## Links
- Main runway: `charts/overall_runway.svg` · Restock plan: [[Stock & Restock Plan]] · Deals: [[Price & Sourcing Optimization]] · Operating system: [[The Operating System]]
