---
title: Restock SOP
draft: true
type: runbook
tags:
  - operating-system
  - ops
  - restock
  - sop
date: 2026-06-11
---
> [!abstract] **The repeatable procedure** for "what do I need to buy?" — rescan the catalog, bucket by run-out, **segment by vendor (= shipment)**, and cost each order **landed** (product + shipping + crypto/FX + customs). Run **quarterly**, and any time a 🔴 item hits zero.

## 1. When to run
- **Quarterly** (Mar / Jun / Sep / Dec), and
- **On trigger:** any active item's `runout_forecast` crosses into the next ~8 weeks, or a `stock_on_hand` hits 0.

## 2. Procedure
1. **Refresh stock truth.** Confirm `stock_on_hand` + `stock_as_of` are current (recent POs reflected — the #1 cause of false urgency). Recompute `runout_forecast` = `stock ÷ (daily_dose × days_per_week/7)`.
2. **Scan all `Stock/` products**, bucket each by run-out:
   - 🔴 **Must buy now** — out **< ~8 weeks** (or stock = 0). Cut-critical items always here.
   - 🟡 **Cheaper to grab now** — out **within the year** — pre-buy to ride a discount / amortise shipping.
   - ⏭️ **Skip** — stocked **> 12 months**.
   - 🚚 **In transit** — `availability` contains "transit" → already ordered, do NOT rebuy.
   - ⚙️ **Situational** — no daily clock (cycle-only, consumable, deprioritized) → buy *as the cycle needs*, not on the calendar.
3. **Segment by `vendor`** — one order per vendor (each = a separate shipment + shipping charge). Consolidate a vendor's 🔴 + 🟡 into ONE basket to pay shipping once.
4. **Cost each vendor order LANDED** (see §3). Set the reorder horizon (default: to the next planned scan / end-of-year).
5. **Output** a dated note `_Ledger/Restock Scan — <Mon YYYY>.md` with the per-vendor baskets + landed costs + which calendar reminders to set.

## 3. Landed-cost model
> **LANDED = (product × FX) + shipping + crypto/network fee + customs**

The sticker price is never the real cost. Always cost the four layers:

| Layer | Notes |
|---|---|
| **Product** | sum of `cost_per_bottle × qty`. In USD for intl vendors → × FX. |
| **Shipping** | per the vendor's `shipping_model` (basket-based, flat, or per-package). |
| **Crypto / FX fee** | crypto-paid orders carry a **network + conversion overhead — observed ~15–20%** (Beligas #269258: RM864 → +RM177 = ~20%). FX itself: **RM4.0/USD** (Nadeem's rate). |
| **Customs** | buyer-paid on most intl pharma; usually small/none but budget for it. |

### Vendor cost profiles
| Vendor | Cur | Shipping | Pay | Crypto/FX overhead |
|---|---|---|---|---|
| [[iHerb]] | RM | **RM22 per RM450 basket** → fill to RM450 | Card | none |
| [[shopee-china]] / Shopee / [[Lazada]] | RM | in listing (local) | e-wallet | none |
| [[kohohpharma]] | RM | **~RM10 max/order, no MOQ** (courier-of-choice) | Card/bank | none |
| [[Equicare Ventures]] | USD | **$25–30/package, max 50 strips/pkg** (bac water free) | crypto? | FX 4.0 |
| [[beligaspharmacy]] | USD | **$25 flat (Intl only)** · −10% code VIGOROUS | **ETH** | **~20%** |
| [[BFF-AMO]] | USD | $45 flat, free >$450 | crypto | FX + crypto |
| [[TCI]] (peptides, INDEXA) | USD | **$4 flat, FREE over $500/order** | crypto | FX + crypto · **INDEXA-funded** |

> [!tip] Shipping economics drive the strategy: **iHerb** = fill to RM450; **Equicare** = fill packages to 50 strips, never spill; **crypto vendors** (Beligas/BFF/TCI) = consolidate big + rare to dilute the ~20% crypto overhead.

---

## 4. WORKED EXAMPLE — Restock Scan, Jun 2026
Current 🔴 must-buy, segmented by vendor, costed landed (FX 4.0). _Quantities marked ⚠️ = confirm; shipping now locked for all vendors._

### 🛒 iHerb (coupon order — fill the RM450 basket)
| Item | Qty | Product RM |
|---|---|---|
| [[CDP-Choline (300mg×120tab) — iHerb\|CDP-Choline]] | 1 | 125.27 |
| [[Bacopa Monnieri (500mg×120tab) — iHerb\|Bacopa]] | 1 | 57.11 |
| [[Uridine Monophosphate (300mg×60tab) — iHerb\|Uridine]] | 1 | 62.40 |
| [[Pre-Workout (1014g) — iHerb\|Pre-Workout]] (buffer) | 1 | 155.30 |
| [[Intra-Workout (651g) — iHerb\|Intra-Workout]] (buffer) | 1 | 118.69 |
| _+ cheaper-to-grab cluster_ (L-Theanine, Taurine, Selenium, Mg, Zinc, CoQ10, Vit C) | | ~598 |
| **Product** | | **~519 core / ~1,117 w/ cluster** |
| Shipping (RM22 per RM450) | | 22 (×1 basket core; ×3 w/ cluster = 66) |
| Crypto | | 0 |
| **LANDED (core)** | | **~RM541** (before coupon −%) |

### 💊 kohohpharma (cut PEDs — needed by ~14 Jul cut start)
| Item | Qty | Product RM |
|---|---|---|
| [[MK-677 (10mg×50tab) — kohohpharma\|MK-677]] | ⚠️ ~3 boxes (cut = 20mg/day ×12wk) | ~477 |
| [[Oxandrolone (Anavar) (10mg×100tab) — kohohpharma\|Anavar]] | ⚠️ 1 box (bulk/oral-deploy) | 206 |
| **Product** | | **~683** |
| Shipping (~RM10 max/order) + crypto 0 | | ~10 |
| **LANDED** | | **~RM693** |

### 🧬 TCI / INDEXA peptides (GHK-Cu + KPV at ZERO 🔴)
| Item | Qty | Product RM |
|---|---|---|
| [[GHK-Cu (1000mg-box) — TCI\|GHK-Cu]] | 1 box | 237.90 |
| [[KPV (100mg-box) — TCI\|KPV]] | 1 box | 277.55 |
| _(BPC-157, TB-500, MOTS-C run out Jul–Aug — add to same order)_ | | + |
| **Product** | | **~515 (urgent only)** |
| Shipping ($4 flat; urgent basket $129 < $500 → pay it) | | ~16 |
| **Crypto ~20%** | | ~103 |
| **LANDED** | | **~RM634 · INDEXA-funded (excluded from personal cost)** |

> [!tip] TCI ships **free over $500/order** (~RM2,000). The urgent GHK+KPV basket alone is only ~$129, so add the Jul–Aug run-outs (BPC-157, TB-500, MOTS-C) to clear free shipping — the $4 saving is trivial, but consolidating one big crypto order also dilutes the ~20% overhead.

> [!warning] Time-critical: **GHK-Cu + KPV = 0** → trigger the INDEXA/TCI peptide order now. **MK-677 + Anavar** run dry as the cut begins (~14 Jul) → place the kohoh order this week for shipping lead time.

## Links
- Scan output: `_Ledger/Restock Scan — <date>` · Stock view: [[Stock & Restock Plan]] · Sources: [[The Operating System]]
- Cost roll-up: [[Monthly Nut]] · Schema: [[Schema — Data Model]]
