---
title: Product List
draft: true
tags:
  - operating-system
  - products
  - index
date: 2026-05-31
---
> [!abstract] The catalog — every product across every pillar, in one place.
> The live, sortable view is the embedded base below. Each row links to a product note with its full spec (prices, doses, cost per dose, dosing schedule, tags). Fields are defined in [[Schema — Data Model]].

## Live catalog

![[Products.base]]

## How it's organised

Products live as individual notes in `Operating System/Products/` and are tagged by pillar so the same item can serve more than one protocol without being duplicated. Roughly:

- **Fit → Performance Enhancement:** anabolics, SARMs, cutting agents, pre/intra-workout, and on-cycle support (Calcium D-Glucarate, DIM, Astragalus, TUDCA, Zinc, Boron).
- **Healthy → Blueprint:** year-round longevity stack (Vitamin C, Garlic, TMG, B-complex, CoQ10, D3/K2, NR, NAC) plus health-protective ancillaries (Tadalafil, Aspirin, Irbesartan, Rosuvastatin, Acarbose).
- **Healthy → Sleep:** Magnesium, Apigenin, Melatonin, Ashwagandha, Trazodone, Glycine.
- **Productive → Cognitive Enhancement:** Alpha-GPC, Creatine, Fish Oil, Uridine, CDP-Choline, Bacopa, Saffron, Rhodiola, L-Tyrosine, ALCAR, Caffeine, L-Theanine, Huperzine, Ginkgo, Nicorette.
- **Attractive → Hair:** Oral Minoxidil.

## Related views

- [[The Operating System]] — how the products, schedules and cycles connect.
- [[Schema — Data Model]] — the field model behind every note.
- `Product Usage.base`, `Cycles & Dosing.base`, `Dosing Information.base` — the other three views.

> [!note] `list_price` and `promo_price` are blank in most notes — those (alternative price / usual promo price) weren't in the source sheets. Everything else (cost per bottle, dose per serving, cost per dose, schedule) is populated.
