---
title: Stock & Restock Plan
draft: true
tags:
  - operating-system
  - ledger
  - stock
  - restock
date: 2026-05-31
---
> [!abstract] Goal #2: minus what you already hold, what does it cost to fully stock 12 months — and what's the ongoing monthly after?
> Built from `stock_on_hand` × the forecast engine (`days_until_empty = stock ÷ effective_daily`). Complements the live `0. Stock & Restock.base` view with costed top-up. Feeds [[Freedom Numbers]]. **Rev 2 — simplified per Nadeem (perishables + protein/aminos treated as ongoing, not stock-tracked).**

## The answer in two buckets

| | RM | Nature |
|---|---|---|
| **A — One-time bulk stock-up** (dose items to 12-mo supply) | **~RM 5,647** | Buy once, covers the year; then RM0 until next year |
| **B — Ongoing** (skin, hair, syringes + protein/aminos/eggs/minerals) | **~RM 7,677/yr** (~RM640/mo) | Deplete continuously / used as-needed; re-buy through the year |
| Already on hand (value) | ~RM 5,297 | The bulk-buying paying off |
| **Total to cover next 12 months** | **~RM 13,324** | |

> [!important] The read for your save-for-next-year goal
> Front-load **~RM5,647 once** on the bulk dose items and they cost **RM0 until next year**; after that your recurring spend is just bucket B (~RM640/mo of things that genuinely deplete or you buy as-needed). That predictability is the precondition for routing surplus into [[Freedom Numbers|Emergency → Optionality → Freedom]] instead of lumpy re-orders. **10 items are already covered past 12 months.**

---

## A — Buy now to reach a 12-month supply (bulk dose items)

| Item | Stack | ~RM to top up |
|---|---|---|
| Testosterone | PEDs | 800 |
| Oxandrolone (Anavar) | PEDs | 528 |
| MK-677 | PEDs | 522 |
| Nicorette Gum | Cognitive | 333 |
| Uridine | Cognitive | 317 |
| CDP-Choline | Cognitive | 256 |
| Aged Garlic Extract | Ancillaries | 244 |
| NAC ⚠ corrected (was overcounted) | Ancillaries | 140 |
| Rhodiola, Cardarine, Tren, CoQ10, Astragalus, TUDCA | various | 130–200 each |
| Bacopa, CaDG, L-Theanine, Creatine, Irbesartan, Magnesium, DIM, Vit C… | various | < 120 each |

**Already covered >12 months (RM0):** EQ, Proviron, T4, Aspirin, Melatonin, Rosuvastatin, Tadalafil, Vitamin D3/K2, Caffeine, L-Tyrosine.

> [!note] NAC corrected 2026-06-18: physical count = **1 bottle (108,000 mg)**, down from a 270,000 mg overcount. It is **no longer covered >12 months** — runway now ~**5 Dec 2026**, so it moves into the near-term top-up list above (≈RM140 for ~2 boxes to reach a 12-month supply). See [[Supplement Restock — by Depletion Group]] (Group B).

> [!note] PEDs use the [[Endocrine Design Rules]] calendar (Test 16,200mg/yr, Anavar 3,840mg…) minus current vials.

---

## B — Ongoing (~RM7,677/yr, ~RM640/mo)

Per your note, kept simple — these aren't stock-tracked, you re-buy as they run down:
- **Perishable/continuous:** skin (Medicube, Eucerin, Originote, Tretinoin), hair topicals (Ell-Cranel, Oral Minox, Nizoral, Topical Minox, RU+carriers), injection consumables.
- **Protein / aminos / food / minerals:** OTG, SPI, L-Citrulline, Beta-Alanine, Glutamine, L-Carnitine, eggs, Copper, Selenium — used variably (often slower than daily), so treated as buy-as-needed rather than a one-time stock-up.

This is where the [[Price & Sourcing Optimization|deals]] bite hardest (protein mix, Oral Minox re-source).

## Open items
- Confirm "fully stock **12 months**" is the target (vs to calendar year-end).
- Stock assumes `stock_on_hand` is in the dose unit (mg/g) — spot-check a few.

## Links
- Cost basis: [[Monthly Nut]] · Deals: [[Price & Sourcing Optimization]] · Cycle: [[Endocrine Design Rules]] · Live view: `0. Stock & Restock.base`
