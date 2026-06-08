---
title: Peptide Sourcing Tiers
draft: true
type: reference
tags:
  - operating-system
  - sourcing
  - peptides
date: 2026-06-06
---
> [!abstract] The peptide-supplier **waterfall** — which vendor to use for what, in order.
> Peptides are INDEXA-funded (excluded from the personal bill) but still need a sourcing decision. This is the routing logic; the per-vendor cost structure lives in each [[#Vendors|Source note]].

## The waterfall (current)

```
1. BFF / AMO   → Retatrutide ONLY (the one product we source here)
2. TCI         → anything that IS on the TCI price list
3. Uther       → anything NOT on the TCI price list (the catch-all)
4. [Tier-2 candidate]  → ADDING NOW — price lists pending
```

| Order | Vendor | Use for | Status |
|---|---|---|---|
| 1 | **[[BFF-AMO\|BFF / AMO]]** | Retatrutide only | active · **priced** (R60 $0.48/mg) |
| 2 | **[[TCI]]** | Any peptide on the TCI list (primary) | active · **priced** — broadest + cheapest HGH ($70/100iu) |
| 2b | **[[JEC]]** | MOTS-C / Ipamorelin / KPV (TCI weak here) | **secondary — recommended add** |
| 3 | **[[Uther]]** | Catch-all not on TCI's list | active · cheapest BPC-157 ($50) |
| — | **[[Alice-TFC]]** | GHK-Cu ($39), TB-500 ($109) | opportunistic |
| — | **[[ZLZ]]** | GLP family at 100-box volume | opportunistic |

> [!important] Tier-2 decision (resolved): **TCI primary + JEC secondary.** See [[Peptide Price Comparison]] for line-by-line routing. Also flagged: **move HGH off rupharma → TCI** ($70 vs $220 per 100iu).

> [!note] How to pick the tier-2 add
> When you paste the candidate price lists, score each on: (a) coverage of the lines TCI/Uther are weakest on, (b) price per mg on your highest-volume peptides (Reta, MOTS-C, BPC-157, CJC/Ipa), (c) shipping-to-MY + payment friction, (d) reship/seizure guarantee. I'll build the comparison table here once they're in.

## Adjacent international vendors (non-peptide, just added)
These carry *some* peptides/HGH too — relevant if consolidating orders:
- [[rupharma]] — Somatropin/HGH, HCG, HMG, PT-141, Khavinson peptides (flat $30 ship)
- [[pctmart]] — GH, PCT, ancillaries (DHL $25 / EE free)
- [[5arsociety]] — neurosteroids (niche)

## Price lists (all recorded ✅)
Full comparison → **[[Peptide Price Comparison]]**.
- **[[BFF-AMO]]** — GLP-1 list, Reta R60 $0.48/mg (Tier-1, Reta).
- **[[TCI]]** — broadest; HGH $70/100iu, SS-31, Tα1 (Tier-2 primary).
- **[[JEC]]** — MOTS-C/Ipamorelin/KPV cheapest (Tier-2 secondary).
- **[[Uther]]** — BPC-157 $50 (Tier-3 catch-all).
- **[[Alice-TFC]]** — GHK-Cu $39, TB-500 $109.
- **[[ZLZ]]** — GLP family at volume.

## Links
- Funded by: INDEXA (see [[The Operating System]] scope note) · Peptide products: `Products/Peptides/`
- Vendors: [[rupharma]] · [[pctmart]] · Price view: [[International Vendor Price Sheet]]
- Operating system: [[The Operating System]] · [[Schema — Data Model]]
