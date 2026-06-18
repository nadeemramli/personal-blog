---
title: Stock Runway — Overall
draft: true
type: chart-doc
tags: [operating-system, ledger, runway, forecast]
date: 2026-06-14
horizon: 2027-12-31
chart: "[[overall_runway.svg]]"
generator: "_Ledger/scripts/os_runway.py"
---
> [!abstract] Runway for every dose-tracked active product (67 items); stock read from each note's `stock_on_hand` frontmatter, run-out computed, grouped into **functional stacks** (each a colour) nested under three usage **modes**, ordered **daily → every-other-day → training**. Seasonal items use a **cut-aligned** burn. Regenerate: `python3 "4. Management/_Ledger/scripts/os_runway.py" "2. Catalog/Products" "4. Management/_Ledger/charts/overall_runway.svg"`.

## Structure
**Mode** → **functional stack** → item (with its **frequency** tag: daily / EOD / training / intra-WO / e4d / occ). Group titles carry the frequency word in Title Case (e.g. "Every-Other-Day Mitochondria Support"); the small per-item tag uses the short form (EOD, e4d).

### Continuous — linear annual burn
`daily_burn = daily_dose × (dpw/7) × (weeks_per_year/52)`. Stacks, in order:
Daily Cognitive · Daily Antioxidant / CV · Daily Protection / Ancillary · Nutrient Partitioning · Every-Other-Day Cognitive · Every-Other-Day Androgen Support · Every-Other-Day Mitochondria Support · Sleep / Recovery · Training-Day Performance · TRT Base.

EOD-named stacks are all dosed every-other-day (ALCAR, Ginkgo, Huperzine, L-Tyrosine, Nicorette, Copper, Selenium were corrected to EOD). The two "unique" stacks (Nutrient Partitioning, Protection / Ancillary) keep mixed cadences.

### Seasonal — cut-aligned (full cut)
Burns **only inside cut windows** (2026: 14 Jul–6 Oct · 2027: 1 Jun–24 Aug). Each item is drawn across the **full 12-week cut** at its in-cut rate (`weekly/7` or `daily×dpw/7`) so you can read whether stock covers a complete cycle. A solid bar that fills the cut = covered; a bar that stops short + **dashed red marker** = runs out mid-cycle (short for the rest of that cut). Runout = when cumulative cut-consumption empties stock.

### Situational — as-needed (grey, loose)
Ashwagandha, Modafinil, Trazodone, Acarbose, BPC-157, TB-500, TUDCA, Astragalus, Calcium D-Glucarate.

## dpw map
ED 7 · EOD 3.5 · training(TD) 6 · intra-WO(ITD) 4 · 5×/wk 5 · E4D 1.75 · OCC 4 · 1–2×/wk 1.5.

## Buy-now (🔴)
- **GHK-Cu + KPV** — at zero (daily EOD repair peptides, now in Protection / Ancillary). Trigger the TCI/INDEXA order.
- **Cytolin (T3)** — 0, due at cut start (14 Jul).
- **BPC-157 / TB-500** — ~30 days (now situational).

## Changes in this revision (2026-06-14)
- Groups ordered by frequency (daily → EOD → training); EOD stacks normalised to EOD dosing.
- **GHK-Cu, KPV** activated (were `restock`), set EOD, moved into **Daily Protection / Ancillary**.
- **Acarbose** → Situational (occasional). **BPC-157, TB-500** → Situational (as-needed recovery).
- **Retatrutide** → **E4D** (every 4 days) → empties ~13 Aug 2026.

## Links
- Chart: [[overall_runway.svg]] · PED-only: [[ped_runway.svg]] · Engine: [[Stock Forecast — Intake Protocol]]
- Restock policy: [[Restock SOP]] · Stock: [[Stock & Restock Plan]] · [[The Operating System]]
