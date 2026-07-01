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

One note per physical product, stored in `Operating System/Products/` — split into two trees (since 2026-06-07):

> [!note] Identity & idempotency (one note = one compound × spec × vendor)
> - **Every** product note — Stock and Wishlist — is named **`Compound (spec) — vendor`** (e.g. `MK-677 (10mg×50tab) — kohohpharma`). RAG-friendly: the filename alone tells you what, how much, and from whom.
> - **`product_id`** = deterministic slug of the filename (e.g. `mk-677-10mgx50tab-kohohpharma`). This is the **idempotency key**: before creating any product note, check the id — if it exists, UPDATE that note, never create a second one. Same compound from a different vendor or in a different spec = different id = its own note.
> - **`compound`** = bare compound name — the grouping key across vendors/specs. Old short names live in `aliases` so old links/searches still resolve.
> - **`Products/Stock/<stack>/`** = bought/own it · **`Products/Wishlist/<stack>/`** = comparing, never bought. Buying a Wishlist offer → move the note to `Stock/<stack>/` (id stays the same).
> - Fast-changing state (active / restock / paused / retired) is the `status` **field**, never a folder.
> - **Guard:** `_Ledger/scripts/os_qc_ids.py "2. Catalog"` — fails on duplicate ids, missing fields, id/filename drift, or planned-vs-folder mismatch. Run after any product add/rename.

| Property | Type | Notes |
|---|---|---|
| `name` | text | Product name (kept stable — scripts key on it) |
| `product_id` | text | **Idempotency key** — slug of `Compound (spec) — vendor` filename; unique across Stock+Wishlist |
| `compound` | text | Bare compound name — groups all offers/specs of the same substance |
| `aliases` | list | Old short filename(s), keeps legacy links & search working |
| `brand` | text | Manufacturer (Nutricost, California Gold, kohohpharma…) |
| `vendor` | text | Where bought (iHerb, Shopee, Lazada, shopee-china) |
| `warehouse` | text | Vendor's shipping warehouse — drives shipping cost/minimums and feasibility (e.g. anabolicpharmacist: Turkish/Indian/PharmaQo; beligaspharmacy: International/**Thailand (MY feasibility untested)**) |
| `availability` | text | Stock state **at capture date**, e.g. `in_stock (2026-06-08)` — for fast-sellout vendors like Beligas; re-check before ordering |
| `source` | text | Links to a [[#5. Source|Source]] note — the sourcing/shipping cost model |
| `pillar` | text | Attractive / Fit / Healthy / Productive / Rich / Successful / **Recovery** / **Antioxidant** — Recovery + Antioxidant are *functional* pillars registered 2026-06-19 (Recovery = joint/tissue recovery, e.g. Boswellia; Antioxidant = oxidative defence, e.g. Vitamin E), alongside the original life-domain pillars |
| `sub_series` | text | e.g. Performance Enhancement, Blueprint, Cognitive Enhancement |
| `category` | text | Steroid, Pharmacology, SARM, Supplement, Cycle support, Ancillary, Nootropic, Topical/Pharma |
| `importance` | text | Very / Moderate / Slight / Non-essential (restock priority) |
| `status` | text | active / **restock** (in use, needs reorder) / paused (owned, not running) / planned (= Wishlist folder) / retired |
| `stack` | text | **Operational group** (the grouping key): Hair / Skin / PEDs / PCT / Cycle Support / Ancillaries & Supplement / Cognitive Stack / Peptides / Protein & Pre-Intra / Consumables |
| `restock` | text | Buy now / Buy this month / Buy monthly / Buy weekly / Check / OK / Not needed now / — (INDEXA) |
| `dosing` | text | Schedule code → links to a [[0. Dosing Information.base|Dosing Information]] note (ED/EOD/TD/ITD/OCC/CYC) |
| `use` | text | Daily / Cycling / Cutting / Occasionally |
| `protocols` | list | Links to the protocol notes that own use decisions, entry/exit criteria, monitoring, and stock math |
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
| `stock_on_hand` | number | Units (mg) currently held |
| `stock_as_of` | date | **When `stock_on_hand` was last verified** — provenance of the count (physical count or derived). Tells you how trustworthy the stock figure is. |
| `runout_forecast` | date | **Projected empty date** at the current dose — a stored snapshot of the engine's `days_until_empty` (which is live-computed). Quick "when do I reorder" without running the script. |
| `daily_dose` | number | Amount per administration (drives forecast with the schedule factor) |
| `product_tags` | list | On-cycle only, Cutting, Liver support, Cognitive stack… |

**Derived (Base formulas, not stored):** `dose_per_half_serving = base_dose / 2`; `cost_per_dose = cost_per_bottle / package_size`; `effective_daily = daily_dose × days_per_week / 7`; `days_until_empty = stock_on_hand / effective_daily`.

### Product body: `## Purchase Log`

Every Stock product note carries a chronological audit table with:

| Column | Meaning |
|---|---|
| `Date` | PO date or the date stock/usage was checked |
| `Event` | `Purchase`, `Stock update`, `Stock check`, `Usage change`, `Depletion`, or `Provenance gap` |
| `PO / source` | Wikilink to the immutable PO, or the source of a manual count |
| `Change or balance` | Quantity added/removed, or the aggregate balance observed |
| `Usage at update` | Dose + schedule in force at that time |
| `Note` | Run-out snapshot, physical-count context, lot/batch detail, or unresolved provenance |

`stock_on_hand`, `stock_as_of`, `daily_dose`, `dosing`, and `runout_forecast` remain the machine-readable current state. The Purchase Log is the append-only history explaining how that state changed. Existing balances are aggregate rather than lot-level FIFO; exact surviving-lot attribution begins only when a physical count or depletion event identifies the lot.

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
| `current_phase` | text | **In-cycle progression**: early / medium / high / highest (NOT cycle length) |
| `length_class` | text | **Cycle-length class**: `short` (8wk) / `medium` (12wk) / `long` (16wk max) / `eq` (20wk — Equipoise exception: Boldenone needs ≥12wk, run at 20) / `short-extended` (irregular, e.g. extended to burn an ester down) |
| `items` | list | Links to the product notes in this cycle |

## 4. Source  (`type: source`)

How a product is bought — because landed cost ≠ sticker price, and the cost *structure* differs by source. Stored in `Operating System/Sources/`. Each product's `source` field points here.

| Property | Type | Notes |
|---|---|---|
| `source_name` | text | iHerb, Shopee, Lazada, kohohpharma, shopee-china, Overseas GMP (crypto), TCI, Apple Store, Grocer |
| `method` | text | Direct (international) / Marketplace / Direct (overseas GMP) / App Store |
| `currency` | text | RM, or USD → RM |
| `shipping_model` | text | e.g. iHerb = **RM22 fixed per RM450 order** (order cap → forecast one shipment per RM450 of basket) |
| `payment` | text | Card / e-wallet / **Crypto** (HCG, HMG) / bank |
| `fees` | text | Extra cost layers — e.g. crypto conversion + network + handling for overseas GMP |

> [!note] Shipping lives here, not on the product. iHerb shipping is **RM22 per RM450 of basket**, so it's forecast per-order, not per-item. Overseas GMP (HCG/HMG) carries crypto + handling fees that vary — tracked on the source, added to landed cost.

## 5. The Bases (views)

| Base | Over | Shows |
|---|---|---|
| `0. Products.base` | All product notes | Master catalog: brand, vendor, prices, doses, cost/dose |
| `0. Stock & Restock.base` | All product notes | Stock check + `restock` flag — a "To buy" view and an "All stock" view |
| `0. <Stack>.base` ×10 | Products of one `stack` | One per group (Hair, PEDs, Cognitive…), inside that stack's folder |
| `0. Product Usage.base` | Product notes | How used: pillar, sub_series, use, protocols, dosing, importance, active |
| `Cycles & Dosing.base` | Cycle + Product | Current cycle, phase, run-out |
| `Dosing Information.base` | Dosing Schedule notes | The dosing dictionary + forecast factors |
| `Sources.base` | Source notes | Sourcing cost models: method, currency, shipping, payment, fees |
| `Overheads.base` | Overhead notes | Non-supplement recurring costs: diagnostics, gym, software, grooming, **living** — cost, billing, eff. monthly |
| `Protocols.base` | Protocol notes | Phase stacks: Bulk / Cut / Lean Bulk — goal + the products in each |

> [!tip] Semantics: why a `stack` field (and is it the best way?)
> Your groups (Hair, PEDs, Ancillaries/Supplement, Cognitive, Peptide…) cut *across* `category` and `pillar` — a steroid and a SARM are different categories but the same "PEDs" stack. So the cleanest model is **one dedicated `stack` field** as the operational grouping key, rather than overloading category or pillar. Each group then = a base filtered `stack == "X"`, and the products physically live in a folder per stack with that base (`0. <Stack>.base`) pinned on top. This is more robust than folder-only grouping (the filter still works if a note moves) and keeps the single source of truth in the note's frontmatter. Bases live **inside their folders**, not on the OS root, so the "first page" stays clean.

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
- `product_tags` → `tags` via `item_tags` (
