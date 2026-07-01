---
title: Product Label Facts Backfill
draft: true
type: operating_system_workflow
tags:
  - operating-system
  - product-labels
  - catalog
date: 2026-06-19
---
# Product Label Facts Backfill

Goal: add official label/nutrition facts and product images to stock product notes where a public primary retailer or manufacturer page exists.

Source priority for iHerb stock: use the iHerb product page first for product image and label facts, because it reflects the purchased SKU more reliably than manufacturer catalog pages. Use manufacturer pages only as fallback when the iHerb page is unavailable, incomplete, or clearly stale.

## Standard note section

Each product gets a `## Label Facts` section containing:

- Official source URL
- Saved product image path
- Package size and serving size
- Brand dosage instruction
- Supplement Facts / Nutrition Facts / active ingredients table
- Other ingredients
- Brand warnings or cautions
- Capture date

Frontmatter fields to add where available:

```yaml
source_url:
label_image:
label_facts_image:
label_verified_as_of:
```

## 2026-06-19 iHerb stock pass

Scope: iHerb-related products currently in stock, limited to products with an identifiable official manufacturer/brand source. No-brand China/India products and products without a reliable public label source are intentionally excluded until a product URL or label screenshot is available.

| Metric | Count |
|---|---:|
| iHerb stock products checked | 43 |
| Product notes updated with `## Label Facts` | 43 |
| Product notes intentionally skipped / blocked | 0 |
| Product image files saved | 101 |

## Completed sources

| Source | Products completed | Notes |
|---|---:|---|
| Nutricost official site | 29 | Saved front product images and Supplement Facts panels where exposed by the official product media. |
| Life Extension official site | 1 | [[Methyl B Complex (250mg×60tab) — iHerb]] |
| Swanson official site | 1 | [[Coleus Forskohlii (400mg×60tab) — iHerb]] |
| iHerb product pages | 12 | [[Melatonin (20mg×240tab) — iHerb]], [[Selenium (100mcg×240tab) — iHerb]], [[Zinc (50mg×120tab) — iHerb]], [[Copper (Bisglycinate) (2mg×100tab) — iHerb]], [[Fish Oil (Omega-3) (1100mg×240softgel) — iHerb]], [[Nicotinamide Riboside (250mg×60tab) — iHerb]], [[Vitamin C (1000mg×60tab) — iHerb]], [[Vitamin D3-K2 (125mcg×180tab) — iHerb]], [[CoQ10 (400mg×180tab) — iHerb]], [[Glycine (1000mg×100tab) — iHerb]], [[Aged Garlic Extract (300mg×300tab) — iHerb]], [[Taurine (1000mg×100cap) — iHerb]] |

## Intentionally skipped / blocked

| Product | Reason |
|---|---|
| None remaining from this iHerb stock pass | User supplied direct iHerb URLs on 2026-06-19; all 9 previously blocked notes were updated from iHerb pages. |

## Next manual inputs that would unblock the skipped items

- A direct official product URL that opens publicly.
- A clear label screenshot from iHerb or the bottle.
- Permission to use logged-in/browser-visible pages for iHerb-only house brands.

## Batch order

1. iHerb / manufacturer supplement labels
2. Shopee nutrition products with credible brand pages
3. Food products with nutrition panels
4. Skincare products with ingredient lists, not nutrition facts
5. Pharma/PED/peptides: active ingredient and package insert/source only, not nutrition facts
