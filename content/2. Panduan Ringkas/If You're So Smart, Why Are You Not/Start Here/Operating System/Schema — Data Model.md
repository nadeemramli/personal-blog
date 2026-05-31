---
title: Schema — Data Model
draft: true
tags:
  - operating-system
  - schema
  - reference
date: 2026-05-31
---
> [!abstract] The field-by-field data model behind [[The Operating System]].
> Three note types (Product, Dosing Schedule, Cycle) surfaced through four Bases. Every field below is a frontmatter property on the note; each maps to a column in the planned Retool/Postgres schema so the markdown layer and the database stay in sync.

## 1. Product  (`type: product`)

One note per physical product, stored in `Operating System/Products/`.

| Property | Type | Notes |
|---|---|---|
| `name` | text | Product name |
| `brand` | text | Manufacturer (Nutricost, California Gold, kohohpharma…) |
| `vendor` | text | Where bought (iHerb, Shopee, Lazada, shopee-china) |
| `source` | text | Links to a [[#5. Source|Source]] note — the sourcing/shipping cost model |
| `pillar` | text | Attractive / Fit / Healthy / Productive / Rich / Successful |
| `sub_series` | text | e.g. Performance Enhancement, Blueprint, Cognitive Enhancement |
| `category` | text | Steroid, Pharmacology, SARM, Supplement, Cycle support, Ancillary, Nootropic, Topical/Pharma |
| `importance` | text | Very / Moderate / Slight / Non-essential (restock priority) |
| `status` | text | active / paused (owned, not running) / planned (wishlist) / retired |
| `dosing` | text | Schedule code → links to a [[Dosing Information]] note (ED/EOD/TD/ITD/OCC/CYC) |
| `use` | text | Daily / Cycling / Cutting / Occasionally |
| `active` | checkbox | The "use it / don't use it" switch |
| `count_in_total` | checkbox | Set false to avoid double-counting a shared item |
| `cycle_weeks` | number | Cycle length in weeks |
| `package_size` | number | Units (tabs) or volume (ml) per bottle |
| `size_unit` | text | tabs / ml / g |
| `base_dose` | number | Dose per serving |
| `dose_unit` | text | mg / mcg / g |
| `cost_per_bottle` | number (RM) | Cost per bottle/vial |
| `list_price` | number (RM) | Alternative / full price *(to fill)* |
| `promo_price` | number (RM) | Usual promotion price *(to fill)* |
| `current_phase` | text | early / medium / high / highest / not_started |
| `stock_on_hand` | number | Units currently held |
| `daily_dose` | number | Amount per administration (drives forecast with the schedule factor) |
| `product_tags` | list | On-cycle only, Cutting, Liver support, Cognitive stack… |

**Derived (Base formulas, not stored):** `dose_per_half_serving = base_dose / 2`; `cost_per_dose = cost_per_bottle / package_size`; `effective_daily = daily_dose × days_per_week / 7`; `days_until_empty = stock_on_hand / effective_daily`.

## 2. Dosing Schedule  (`type: dosing_schedule`)

The qualitative→quantitative bridge. Stored in `Operating System/Dosing Schedules/`.

| Property | Type | Notes |
|---|---|---|
| `code` | text | ED, EOD, TD, ITD, OCC, CYC |
| `label` | text | Human label |
| `interval_days` | number | "Every N days" (ED=1, EOD=2); blank if not interval-based |
| `days_per_week` | number | Planning frequency. Interval-based = 7 ÷ interval_days (EOD = 7/2) |
| `days_per_week_min` / `_max` | number | Range (Occasionally = 3–5) |
| `forecast_method` | text | frequency / manual / cycle |

> [!important] The forecast rule
> Effective daily burn = `daily_dose × days_per_week / 7`. **EOD = every 2 days = 7/2 per week** (per-dose = weekly dose × 2/7), so EOD items last twice as long as ED. Intense Training Days = 4/7. Occasionally = 3–5/week (default 4). This is what a spreadsheet can't express and why the model lives here.

## 3. Cycle  (`type: cycle`)

A defined run window. Stored in `Operating System/Cycles/`.

| Property | Type | Notes |
|---|---|---|
| `cycle_name` | text | e.g. "2026 Q2 Cycle" |
| `start_date` | date | Cycle start |
| `weeks` | number | Length |
| `current_phase` | text | early / medium / high / highest |
| `items` | list | Links to the product notes in this cycle |

## 4. Source  (`type: source`)

How a product is bought — because landed cost ≠ sticker price, and the cost *structure* differs by source. Stored in `Operating System/Sources/`. Each product's `source` field points here.

| Property | Type | Notes |
|---|---|---|
| `source_name` | text | iHerb, Shopee, Lazada, kohohpharma, shopee-china, Overseas GMP (crypto), Prime Pharma, Apple Store, Grocer |
| `method` | text | Direct (international) / Marketplace / Direct (overseas GMP) / App Store |
| `currency` | text | RM, or USD → RM |
| `shipping_model` | text | e.g. iHerb = **RM22 fixed per RM450 order** (order cap → forecast one shipment per RM450 of basket) |
| `payment` | text | Card / e-wallet / **Crypto** (HCG, HMG) / bank |
| `fees` | text | Extra cost layers — e.g. crypto conversion + network + handling for overseas GMP |

> [!note] Shipping lives here, not on the product. iHerb shipping is **RM22 per RM450 of basket**, so it's forecast per-order, not per-item. Overseas GMP (HCG/HMG) carries crypto + handling fees that vary — tracked on the source, added to landed cost.

## 5. The Bases (views)

| Base | Over | Shows |
|---|---|---|
| `Products.base` | Product notes | Catalog: brand, vendor, prices, doses, cost/dose |
| `Product Usage.base` | Product notes | How used: pillar, sub_series, dosing, importance, active |
| `Cycles & Dosing.base` | Cycle + Product | Current cycle, phase, run-out |
| `Dosing Information.base` | Dosing Schedule notes | The dosing dictionary + forecast factors |
| `Sources.base` | Source notes | Sourcing cost models: method, currency, shipping, payment, fees |
| `Overheads.base` | Overhead notes | Non-supplement recurring costs: diagnostics, gym, software, grooming, **living** — cost, billing, eff. monthly |
| `Protocols.base` | Protocol notes | Phase stacks: Bulk / Cut / Lean Bulk — goal + the products in each |

## 6. Overhead  (`type: overhead`)

The maintenance bill beyond pills — recurring costs the supplement schema can't model (no dose). Stored in `Operating System/Overheads/`.

| Property | Type | Notes |
|---|---|---|
| `name` | text | e.g. Gym Membership, Claude (Max), DEXA Full-Body Scan |
| `pillar` / `sub_series` | text | Which series the cost belongs to |
| `category` | text | Diagnostics / Gym / Software / Learning / Grooming / Insurance / Investment / **Living** (rent, transport, utilities, phone, wifi) |
| `cost` | number (RM) | Headline price |
| `billing` | text | monthly / yearly / one-time / shelf (consumable) / bundled / free |
| `shelf_life_months` | number | For consumables (grooming) — drives eff. monthly |
| `eff_monthly` | number (RM) | Normalised monthly cost (monthly = cost; yearly = ÷12; shelf = ÷ shelf_life; one-time/free/bundled = 0) |
| `status` | text | active / planned / retired |
| `source` | text | Where billed |

Current ledger ≈ **RM 845/mo effective** (diagnostics ~68, gym 129, software ~537, grooming ~134, learning ~17). Diagnostics: Symphony screening RM319/yr + DEXA RM499/yr; InBody bundled in gym. Software: Claude RM400/mo dominates. Grooming: shelf-life-adjusted from the old Moving Planner.

> [!note] Funding & scope (overheads)
> - **Insurance / Takaful** = employer-covered for now (RM0 personal); status `planned`, deep-dive soon. It's the Baseline floor from [[The First Path of Controlling Your life|First Path]].
> - **Investment frictions** = negligible (Wahed / Moomoo / ASB / AHB / EPF; no high-level trading), tracked as a note, not a cost.
> - **Learning** = scholarship covers formal credentials; only boots.dev (RM200/yr) recurs.
> - **MacroFactor + Hevy** moved here from Products (they're software, not dosed).

## Retool / Postgres mapping

**Retool is parked** — Obsidian Bases is now the system of record. This mapping is kept only as an export blueprint, in case a live multi-user app is ever wanted (`retool_order_schema.sql`). The mapping is direct:

- Product → `items` (+ `inventory` for stock/phase, + `dose_tiers` for the 4-tier costs).
- Dosing Schedule → `dosing_schedules`.
- Cycle → `cycles`.
- `product_tags` → `tags` via `item_tags` (many-to-many).
- Source → `sources`; `product.source` → `items.source_id`.
- New product fields `status` and `source` → add `status` and `source_id` columns to `items`.
- Base views → SQL views (`v_item_costs`, `v_pillar_summary`).

Keep field names aligned on both sides and migration is a copy, not a re-model. *(These new fields/tables aren't in the current `.sql` yet — they'll be added in the next Retool pass.)*

## Funding & scope notes

- **Peptides are now catalogued but excluded from personal cost.** The 8-peptide stack (BPC-157, HGH, Thymosin Alpha-1, GHK-Cu, MOTS-C, SS-31, KPV, Retatrutide) lives in Products with full 2-year economics, tagged `INDEXA-funded` + `count_in_total: false` — funded by the **INDEXA** side-business, so visible but never added to the maintenance bill.
- **Living/Baseline costs added** to Overheads (category `Living`): rent RM0 (family home), car/bikes RM0 (paid off), fuel/TNG/electricity/water/phone/wifi ~RM585/mo — unifies cost-of-living with protocol cost for an honest freedom number.
- **Phase protocols (type `protocol`)**: Bulk / Cut / Lean Bulk notes document each stack; phase tags `Bulk` / `Cut only` / `Always-on`. GHK-Cu + KPV are always-on.
- **P5P** added as cycle support (prolactin, 8-wk).
- **Hevy is a one-time lifetime purchase** (RM347), not recurring — its note carries `count_in_total: false`.
- **PCT items are `planned`** (owned-price known, not currently run): two HCG candidates + HMG, priced in USD via the crypto source.
- **New categories added:** PCT, Protein, Amino/Pre, Food, Consumable, Software (alongside the original Steroid/Pharmacology/SARM/Supplement/Cycle support/Ancillary/Nootropic/Topical).
- **Skin & hair topicals** carry cost only — expected dosage, size and run-time are TBD (Nadeem to add), so they don't forecast run-out yet.
