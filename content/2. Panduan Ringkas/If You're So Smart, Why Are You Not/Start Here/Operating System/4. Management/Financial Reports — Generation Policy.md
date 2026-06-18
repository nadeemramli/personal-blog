---
title: Financial Reports — Generation Policy
draft: true
tags: [operating-system, management, policy, report, financial-os]
date: 2026-06-12
---
> [!abstract] How Obsidian produces the financial visual reports. One script regenerates everything from live vault data into `_Ledger/charts/` and rewrites `_Ledger/Financial Snapshot.md`. Pairs with [[Agent Operating Checklist]] and [[FOS 1 — Income Layer]].

## Trigger phrases
- "draw the sankey / cash-flow pipeline", "monthly forecast payment diagram"
- "show our PED stock / runway", "what runs out when", "impact of paying the CC on PED buys"
- "refresh the financial snapshot / report"

## The one command
```
python3 "4. Management/_Ledger/scripts/os_reports.py" .
```
Run from the Operating System folder. It (1) reads overheads + products live, (2) writes `_Ledger/charts/cashflow_sankey.svg` and `ped_runway.svg`, (3) rewrites `_Ledger/Financial Snapshot.md` embedding both with a numbers table. **Always run [[Stock Reconciliation Policy|PO→stock reconcile]] first** so stock is current.

## Report 1 — Monthly cash-flow Sankey
Income sources (left) → take-home hub → allocations (right): Living+Ayra · Overheads · Foundation (protocol) · CC payoff · Buffer. Flow widths are proportional to RM. Surplus = income − maintenance nut; CC payoff = the saving rate redirected from GX; buffer = remainder (funds PED buys or speeds the card).

## Report 2 — PED stock runway
One bar per PED from today to its run-out date (`stock_on_hand ÷ effective_daily`; PEDs use `weekly_mg × weeks/yr ÷ 364`). Red = at zero / buy now; amber < 6mo; blue within horizon; green = covered. A dashed line marks **CC-cleared** (`CC_balance ÷ saving_rate`) so the buy-vs-payoff collision is visible (e.g. Test E refill ~Dec vs CC clear ~Nov).

## Obsidian rendering notes
- SVGs are **self-contained**: hardcoded palette + a light card background, so they read on any Obsidian theme (no CSS variables — those only work in the Cowork chat renderer).
- Embedded via `![[charts/<file>.svg]]`. Obsidian renders inline.

## Source of truth — [[FOS 0 — Financial Inputs]]
All financial numbers (salary, ACCA, INDEXA, saving rate, CC balance, Ayra, optionality ceiling, liquid savings) live in **one note: [[FOS 0 — Financial Inputs]]** frontmatter. Both `os_nut.py` and `os_reports.py` read it at runtime (fallback to built-in defaults if absent). **Edit the number in FOS 0 once → re-run → every report updates.** Only `PED_CAL` still lives in the scripts (must match across `os_nut.py`/`os_reports.py`).

## Links
- Output: [[Financial Snapshot]] · Engine: `os_nut.py` · [[Agent Operating Checklist]] · [[Stock Reconciliation Policy]] · [[FOS 1 — Income Layer]] · [[FOS 3 — Debt & Credit Recovery]]
