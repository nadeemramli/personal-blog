---
title: BulkSupplements Replacement Comparison
draft: true
tags: [operating-system, ledger, wishlist, cost, bulksupplements]
date: 2026-06-22
---
# BulkSupplements Replacement Comparison

Purpose: keep **Stock** as the functional layer we actually use, and use **Wishlist** as the comparison layer for possible lower-cost replacements.

BulkSupplements should only replace current iHerb/Shopee stock when the raw savings are large enough to beat three hidden costs:

- international shipping to Malaysia
- cash-upfront friction versus credit/installment purchases
- formulation/quality loss when replacing a finished capsule/softgel with commodity powder

## Source Capture

> [!info] Captured 2026-06-22
> - BulkSupplements sitemap: <https://www.bulksupplements.com/sitemap.xml>
> - Product sitemap: <https://www.bulksupplements.com/sitemap_products_1.xml?from=3928945066095&to=8490562683074>
> - Malaysia storefront check: `/my` connection closed, but `/en-my/products/{slug}` loaded. Variant availability was checked through `/en-my/products/{slug}.js`.
> - Live Malaysia product prices were pulled from BulkSupplements `/en-my` product JSON endpoints, where available.
> - FX assumption retained only for U.S.-only fallback math: **USD1 = RM4.05**. Malaysia-available rows now use localized RM prices.
> - Shipping/import/tax is **not included**.

## Decision Rule

| Raw annual savings before shipping | Decision |
|---:|---|
| < RM100/year | Usually ignore. Shipping and hassle will erase it. |
| RM100-250/year | Consider only if product is a clean commodity powder and quality is equivalent. |
| > RM250/year | Worth a serious cart test, especially if several products are bundled together. |

Quality override: keep iHerb/current if the BulkSupplements version is a worse format, unclear standardization, microdose-risk powder, oil-based absorption downgrade, or unavailable.

## Savings Breakdown

No, not every item saves RM250/year by itself. The RM250/year rule is a **cart-level decision threshold** after shipping/import/tax. Most single items are below that; BulkSupplements only starts to look interesting when several clean commodity powders are bundled together.

| Current stock | MY storefront candidate | Current annual cost | BulkSupplements annualized cost | Raw savings/year | Verdict |
|---|---|---:|---:|---:|---|
| Boswellia Extract | Available, 1kg RM210 | ~RM285.13 | ~RM91.98 | **RM193.15** | Strong candidate only if extract standardization is comparable. |
| Taurine | Available, 1kg RM129 | RM172.08 | ~RM47.09 | **RM124.99** | Clean commodity replacement. |
| L-Theanine powder option | Available, 1kg RM236 | RM105.00 | ~RM17.23 | **RM87.77** | Strong if using powder; capsule dose still needs label confirmation. |
| TMG / Betaine | Available, 1kg RM142 | RM121.80 | ~RM38.87 | **RM82.93** | Clean commodity replacement. |
| DIM 200mg EOD | Available, 365 caps RM65 | RM115.32 | ~RM32.50 | **RM82.82** | Saves well if 200mg EOD is acceptable. |
| TUDCA powder option | Available, 50g RM197 | RM189.24 | ~RM110.32 | **RM78.92** | Useful only from the 50g powder SKU; capsules were not clearly better. |
| Vitamin C | Available, 1kg RM120 | RM109.56 | ~RM43.80 | **RM65.76** | Clean commodity replacement. |
| Ginkgo Biloba | Available, 1kg RM185 | RM68.04 | ~RM6.94 | **RM61.10** | Cheap on paper; standardization and tiny dosing matter. |
| Beet Root Powder | Available, 1kg RM150 | ~RM323.70 | ~RM273.75 | **RM49.95** | Modest; check whether target is nitrate, polyphenols, or general beet powder. |
| Zinc Picolinate | Available, 240 softgels RM65 | RM127.80 | ~RM98.85 | **~RM28.95** | Too small alone; verify per-softgel zinc first. |
| Beta-Alanine | Available, 1kg RM137 | RM141.96 | ~RM114.26 | **RM27.70** | Small; shipping likely erases it. |
| C8 MCT Powder | Available, 1kg RM262 | ~RM985.60 | ~RM956.30 | **RM29.30** | Not a clean switch unless BulkSupplements MCT profile matches the current C8 target. |
| CoQ10 softgel option | Available, 120 softgels x 200mg RM99 | RM305.40 | ~RM301.13 | **RM4.27** | Not worth switching; powder has bioavailability caveat. |
| L-Tyrosine | Available, 1kg RM155 | RM63.84 | ~RM48.49 | **RM15.35** | Small. |
| L-Citrulline | Available, 1kg RM163 | RM177.48 | ~RM169.86 | **RM7.62** | Current source is already good. |
| Creatine Monohydrate | Available, 1kg RM137 | RM182.64 | ~RM250.03 | **-RM67.39** | BulkSupplements is worse than current Shopee source. |
| Alpha-GPC | **Not available on MY JSON** | RM259.20 | - | - | Remove from active savings count. |
| NAC | **Not available on MY JSON** | RM142.08 | - | - | Remove from active savings count. |
| ALCAR | **Not available on MY JSON** | RM113.40 | - | - | Remove from active savings count. |
| Glutamine | **Not available on MY JSON** | RM177.48 | - | - | Remove from active savings count. |

Calculation note: BulkSupplements annualized cost uses the captured Malaysia storefront pack price, then multiplies by expected yearly usage from [[Stack Cost Audit]] or the current product note.

## Stronger Candidates

These are the products where BulkSupplements is worth keeping in Wishlist for future cart comparison.

| Current stock | Current baseline | BulkSupplements candidate | Captured price | Rough verdict |
|---|---:|---|---:|---|
| Boswellia Extract | ~RM285/year at 1200mg/day | [[Boswellia Serrata Extract Powder (1kg) - BulkSupplements]] | MY: 1kg RM210 | Strong candidate if extract standardization matches Nutricost target. |
| Taurine | ~RM172/year | [[Taurine Powder (1kg) - BulkSupplements]] | MY: 1kg RM129 | Good commodity replacement; 1kg lasts ~2.7 years at 1g/day. |
| TMG / Betaine | ~RM122/year | [[TMG Betaine Powder (1kg) - BulkSupplements]] | MY: 1kg RM142 | Good clean powder replacement. |
| Vitamin C | ~RM110/year | [[Ascorbic Acid Vitamin C Powder (1kg) - BulkSupplements]] | MY: 1kg RM120 | Good commodity replacement if GI tolerance is fine. |
| DIM | ~RM115/year | [[DIM Capsules (200mg×365cap) - BulkSupplements]] | MY: 365 caps RM65 | Good if 200mg cap dosing fits the protocol; easier than powder. |
| L-Theanine | ~RM105/year | BulkSupplements L-Theanine powder/caps | MY: 1kg RM236 or 365 caps RM65 | Candidate, but verify capsule dose before replacing Nutricost 200mg caps. |
| Ginkgo Biloba | ~RM68/year | BulkSupplements Ginkgo Biloba Extract Powder | MY: 1kg RM185 | Raw powder is very cheap, but verify standardization and micro-scoop practicality. |
| TUDCA | ~RM189/year cycle-adjusted | BulkSupplements TUDCA Powder | MY: 50g RM197 | Powder may save money; capsules were not cheaper than current stock. Bitter/taste and dosing precision matter. |

## Weak Or No-Switch Candidates

| Current stock | BulkSupplements match | Reason |
|---|---|---|
| Creatine Monohydrate | Creatine Monohydrate Powder | Malaysia storefront 1kg RM137; current Shopee 1kg source is cheaper. |
| L-Citrulline | L-Citrulline Powder | Malaysia storefront 1kg RM163; current HK/Shopee price is already competitive before shipping. |
| Beta-Alanine | Beta Alanine Powder | Malaysia storefront 1kg RM137; only small raw savings, so shipping likely erases it. |
| Glutamine | L-Glutamine Powder | Malaysia product JSON returned 404; not a real MY replacement right now. |
| L-Tyrosine | L-Tyrosine Powder | Small savings only; not enough alone. |
| C8 MCT Powder | MCT Powder | Malaysia storefront 1kg RM262 gives slight raw savings, but not a clean switch unless BulkSupplements MCT profile matches the current C8 target. |
| Beet Root Powder | Organic Beet Root Powder / Extract | Small raw savings only; extract is not a direct 1:1 replacement unless nitrate/polyphenol target is defined. |
| Fish Oil | Fish Oil Softgels | Main 1000mg softgel SKU was out of stock; fish oil quality/density/oxidation matters more than raw price. Keep current unless EPA/DHA math is superior. |
| CoQ10 | CoQ10 Powder / Softgels | Powder is cheaper but may be a bioavailability downgrade unless taken with fat/oil; softgels were not clearly cheaper than current. |
| Magnesium Glycinate | Magnesium Glycinate Powder/Caps | Compare by **elemental magnesium**, not compound weight. Current replacement decision needs label math first. |
| Zinc | Zinc Picolinate Softgels | Small savings at best; current California Gold is already acceptable. |
| Selenium | Selenium Glycinate Capsules/Powder | Capsule savings likely small; powder is microdose-risky and not worth it. |
| Copper | Copper Gluconate Powder | Not same format as NOW copper bisglycinate; microdose-risky. Keep current. |
| Boron | Boron Citrate | 10mg capsules and powder were available on MY storefront, but current protocol uses 5mg EOD; dose format is awkward and savings are likely small. |
| Bacopa | Bacopa Extract Powder | All variants were out of stock at capture. |
| Phosphatidylserine | Phosphatidylserine Capsules/Powder | All variants were out of stock at capture. |
| BHB Salts | Calcium/Potassium/Sodium BHB | Not a clean replacement for current blended BHB salts; electrolyte profile changes. |
| EAA | Essential Amino Acids Powder | Good wishlist candidate as a new protocol product, not a current stock replacement. |

## No Clean BulkSupplements Match Found

Keep current product/source unless a future sitemap search finds a cleaner replacement:

- Alpha-GPC: U.S. page exists, but Malaysia `/en-my/products/alpha-gpc-l-alpha-glycerylphosphorylcholine.js` returned 404.
- NAC: U.S. page exists, but Malaysia `/en-my/products/n-acetyl-l-cysteine-nac.js` and `/en-my/products/nac-pills.js` returned 404.
- ALCAR: U.S. page exists, but Malaysia `/en-my/products/acetyl-l-carnitine-alcar.js` and `/en-my/products/acetyl-l-carnitine-capsules.js` returned 404.
- CDP-Choline
- Uridine Monophosphate
- Nicotinamide Riboside
- Vitamin D3/K2
- Vitamin E Tocotrienol Complex
- Aged Garlic Extract
- Apigenin
- P5P
- Calcium D-Glucarate
- Yohimbine
- formulated pre-workout
- formulated intra-workout
- protein powders from current local/HK sources
- pharma/PEDs, peptides, hair, skin, food, and consumables

## Bulk Cart Strategy

Do not buy one BulkSupplements item alone unless it is urgent. The better test is a cart containing several clean commodity replacements:

1. Taurine Powder 1kg
2. TMG Betaine Powder 1kg
3. NAC Powder 1kg
4. Ascorbic Acid Powder 1kg
5. ALCAR Powder 1kg
6. Alpha-GPC Powder 1kg, only if powder storage/dosing is acceptable
7. Boswellia Extract Powder 1kg, only if standardization checks out
8. DIM 200mg capsules, if the 200mg dosing tier fits

Decision threshold for a real switch: after adding shipping/import/tax, the cart should still save **at least RM250/year** versus current purchases, or reduce product cost by **at least 25-30%** with no quality downgrade.

## Links

- Wishlist: [[Taurine Powder (1kg) - BulkSupplements]] · [[TMG Betaine Powder (1kg) - BulkSupplements]] · [[NAC Powder (1kg) - BulkSupplements]] · [[Ascorbic Acid Vitamin C Powder (1kg) - BulkSupplements]] · [[Acetyl L-Carnitine HCl Powder (1kg) - BulkSupplements]] · [[Alpha GPC Powder (1kg) - BulkSupplements]] · [[Boswellia Serrata Extract Powder (1kg) - BulkSupplements]] · [[DIM Capsules (200mg×365cap) - BulkSupplements]]
- Baseline: [[Stack Cost Audit]]
