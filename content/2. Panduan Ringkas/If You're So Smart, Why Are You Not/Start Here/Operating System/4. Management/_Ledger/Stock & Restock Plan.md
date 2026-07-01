---
title: Stock & Restock Plan
draft: true
tags:
  - operating-system
  - ledger
  - stock
  - restock
date: 2026-06-19
---
> [!abstract] Goal #2: minus what you already hold, what does it cost to fully stock to the horizon — and what's the ongoing monthly after?
> Built from `stock_on_hand` × the forecast engine (same burn model as [[overall_runway.svg|the runway chart]]: continuous = `daily × days_per_week/7 × weeks/52`; seasonal = in-cut rate × cut-days). **Rev 3 — 2026-06-19**, regenerated after the stock-vs-PO reconciliation (corrected quantities for Aspirin, Rosuvastatin, Indapamide, Trazodone, T4, Acarbose, Vit D3/K2, Zinc, Proviron, Nicorette). Horizon **31 Dec 2027**; cuts 14 Jul 2026 + Jun 2027.

## The answer in three buckets

| Bucket | RM | Nature |
|---|---|---|
| **A — One-time bulk to reach 31 Dec 2027** (dose items, minus stock on hand) | **≈ RM 11,988** | Buy once; covers through end-2027 |
| **B — Ongoing rebuy** (skin, hair, protein/aminos, consumables, as-needed, INDEXA peptides) | **≈ RM 640/mo** (carried from Rev 2; not re-costed) | Deplete continuously / bought as-needed |
| **C — Already covered past horizon** | RM 0 | 6 items last beyond 31 Dec 2027 |

> [!important] What the reconciliation changed
> The corrected counts moved **Vitamin D3/K2 out of "covered" and into bucket A** (it was a 3-bottle phantom; the real 1 bottle runs out ~14 Jun 2027). Aspirin, Rosuvastatin and T4 landed close to before. Bucket A is larger than Rev 2's RM5,647 mainly because the horizon is now **18.5 months** (to end-2027) and it includes the TRT base + two cuts, not a flat 12-month supply.

---

## A — One-time bulk buy-list, ordered by vendor lead time

Order the slow vendors first — they gate the 14 Jul cut.

### 🔴 Tier 1 — slow / international / crypto (order FIRST) — ≈ RM 4,557
| Item | Vendor | Buy | RM |
|---|---|---|---|
| Oxandrolone (Anavar) | kohohpharma | 5 btl | 1,030 |
| MK-677 | kohohpharma | 6 btl | 954 |
| Proviron | kohohpharma | 2 btl | 336 |
| Cardarine (GW-501516) | kohohpharma | 2 btl | 215 |
| Clenbuterol | kohohpharma | 2 btl | 212 |
| Cytolin (T3) | kohohpharma | 2 btl | 212 |
| Etho Testosterone 450 (TRT base) | beligaspharmacy Intl | 5 btl | 1,332 |
| Acro Trenbolone 100 | beligaspharmacy Intl | 1 btl | 266 |

### 🟠 Tier 2 — overseas pharma (India/intl, ~2–3 wk) — ≈ RM 84
| Item | Vendor | Buy | RM |
|---|---|---|---|
| Nebivolol (Nebiheal 5mg) | Equicare Ventures | 8 btl | 56 |
| Tadalafil (Vidalista 10mg) | Equicare Ventures | 6 btl | 28 |

### 🟡 Tier 3 — iHerb + shopee-china (~1–2 wk) — ≈ RM 6,748
**iHerb (≈ RM 5,197):** CoQ10 2btl·602 · Alpha-GPC 6btl·596 · Magnesium Glycinate 7btl·574 · Uridine 6btl·375 · Aged Garlic 3btl·378 · CDP-Choline 3btl·373 · Apigenin 3btl·240 · NAC 2btl·140 · L-Theanine 2btl·138 · Fish Oil 2btl·206 · Bacopa 3btl·170 · Nicotinamide Riboside 3btl·155 · DIM 2btl·152 · Saffron 2btl·135 · Zinc 3btl·116 · Vitamin C 6btl·108 · TMG 2btl·80 · Taurine 1btl·71 · Copper 2btl·70 · Huperzine-A 1btl·68 · Methyl B 2btl·66 · **Vitamin D3/K2 1btl·66** · Acetyl L-Carnitine 1btl·65 · Boron 1btl·58 · Caffeine 1btl·57 · Ginkgo 1btl·52 · Melatonin 1btl·51 · Selenium 1btl·35

**shopee-china (≈ RM 1,551):** Mirabegron 4btl·830 · Metformin+Empagliflozin FDC 1btl·323 · Irbesartan 2btl·280 · Levothyroxine (T4) 2btl·106 · Rosuvastatin 1btl·12

> [!note] Patched 2026-06-19 for [[PO 2026-06-19 — iHerb]]: Uridine 9→6 btl, NAC 3→2 btl, L-Theanine 3→2 btl (−RM326 total). The iHerb subtotal, Tier-3 total, and Bucket A above were reduced by the same RM326; all other compounds unchanged. Re-run `os_nut.py` for a full regenerate. (Astragalus +1 btl and new Boswellia are not in this dose buy-list — Astragalus is as-needed; Boswellia has no dose set yet.)
>
> **⚠️ Stale prices — regenerate.** The two 2026-06-19 invoices ([[PO 2026-06-19 — iHerb|739095421]], [[PO 2026-06-19 — iHerb 2|739095579]]) corrected several `cost_per_bottle`s vs the figures used above: Uridine 62.40→79.31, NAC 70→95.30, L-Theanine 69→85.18, DIM 75.75→84.64, Zinc 38.81→49.75, Boswellia 75.31→70.31. Stock also changed (Boswellia 2 btl, DIM/Zinc/CaDG +1 btl). The per-box RM here are now stale; **`os_nut.py` regen** will pick up the corrected prices and stock. The hand-curated [[Supplement Restock — by Depletion Group]] has already been updated to the new prices/dates.

### 🟢 Tier 4 — local MY marketplace (fast) — ≈ RM 599
| Item | Vendor | Buy | RM |
|---|---|---|---|
| Nicorette Gum | Shopee | 2 btl | 326 |
| Ketotifen | Lazada | 2 btl | 173 |
| Creatine Monohydrate | Shopee | 1 btl | 100 |

---

## B — Ongoing rebuy (~RM 640/mo, not stock-tracked)

Per your Rev 2 simplification — re-buy as they run down, not a one-time stock-up. This is where [[Price & Sourcing Optimization|deals]] bite hardest.

- **Perishable / continuous (31):** Skin (Medicube ×3, Eucerin, Originote ×3, Tretinoin ×2), hair (Ell-Cranel, Oral Minoxidil, Nizoral, Topical Minox, RU58841 + Ethanol/Propylene carriers), injection consumables (Insulin Syringes 30g/31g, Alcohol Swab), protein/aminos/intra (OTG, SPI, Pre/Intra-Workout, Beta-Alanine, Glutamine, L-Citrulline, L-Carnitine, Glycerol, BHB Salts, C8 MCT), Whole Eggs.
- **As-needed (7):** Acarbose, Ashwagandha, Astragalus, Calcium D-Glucarate, Modafinil (Modaheal), TUDCA, Trazodone — occasional dosing, buy when low.
- **INDEXA peptides (9, RM0 personal):** BPC-157, CJC-1295+Ipamorelin, GHK-Cu, HGH, KPV, MOTS-C, Retatrutide, SS-31, TB-500 — INDEXA-funded, excluded from the nut. **GHK-Cu, HGH, KPV currently at zero → restock via INDEXA/TCI** (slowest lead time — flag first). See [[Cycle PED Restock — Decision & Buy Plan]].

## C — Already covered past 31 Dec 2027 (RM 0)

Aspirin (→ Jan 2028), L-Tyrosine (→ 2028), Methylene Blue, Memantine (Momenta), P5P, Ezetimibe (Zetiheal). Plus the as-needed items in B with multi-year supply (e.g. Acarbose → 2031).

## Caveats / manual checks
- **PED/seasonal costing is approximate** — assumes both cuts (168 cut-days) and rounds up to whole vials. The authoritative PED buy plan is [[Cycle PED Restock — Decision & Buy Plan]] / [[Endocrine Design Rules]].
- **Anastrozole (Anastrolin)** has no `daily_dose`, so the engine can't forecast it — set its cut dosing manually before ordering.
- **Excluded (paused/retired):** Indapamide, Coleus Forskohlii, Dihydroberberine, Glycine, Yohimbine, HMB, Boldenone Undecanoate, the kohohpharma Test E-C and shopee-china Tadalafil — don't burn unless reactivated.
- Bucket B's RM640/mo is carried from Rev 2, not re-costed this pass.

## Links
- Runway chart: `charts/overall_runway.svg` · Cost basis: [[Monthly Nut]] · Deals: [[Price & Sourcing Optimization]] · PEDs: [[Cycle PED Restock — Decision & Buy Plan]] · Feeds: [[Freedom Numbers]] · Live view: `0. Stock & Restock.base`
