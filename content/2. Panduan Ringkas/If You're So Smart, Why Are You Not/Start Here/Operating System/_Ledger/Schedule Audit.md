---
title: Schedule Audit
draft: true
tags:
  - operating-system
  - schedule
  - audit
  - daily-protocol
date: 2026-05-31
---
> [!abstract] The Daily Protocol — the seven dosing windows, and the QC that reconciles them against the OS.
> This is the day-to-day reference (transcribed from *The Daily Protocol v2.1* card) **and** the audit that makes sure every item you actually take is counted in [[Monthly Nut]]. Drop the PNG into this folder to embed it: `![[daily-protocol.png]]`.

## The seven windows
![[daily-protocol-v3-1.png]]
**07:45 — Morning (fasted)**
- *Performance:* Tadalafil ¼ tab · Methyl B Complex ½ · TMG (Betaine) 750mg · Aged Garlic Extract · T4/Levothyroxine *(cycle)*
- *Antioxidant:* Vitamin C 1000mg · TUDCA 250mg · NAC · Astragalus Root · **Copper 2mg** *(Zinc pairing)*
- *Ancillaries:* Aspirin 160mg · **Rosuvastatin 10mg** · **Irbesartan 75mg** · Oral Minoxidil 5mg

**08:30 — Brain + Mito (fat snack)**
- *Carrier:* mayonnaise · fish roe · virgin olive oil *(fat, for fat-soluble absorption)*
- *Brain:* Uridine 300 · CDP-Choline 750 · Fish Oil 3 caps · Saffron 300 · Bacopa 300
- *Mito:* CoQ10 400 · Nicotinamide Riboside 300 · Vitamin D3+K2
- *Ready (optional):* AL-CAR 1000 · Alpha-GPC 300 · Ginkgo 120 · Caffeine 200 · L-Theanine 400 · Huperzine-A 200mcg

**09:00–17:00 — Working Hydration**
- Pre-Workout (light) ¼ · Creatine 5g · L-Tyrosine 2g · Nicotine Gum (PRN)

**14:30 — Lunch Protein (first feeding)**
- **Whey Protein ~80g** · *Minerals:* Zinc · Boron · DIM · **Selenium 200mcg**

**16:30 — Pre-Workout**
- *Cycle:* Oxandrolone 10 · Proviron 10 · **Cardarine 10–20mg** · *Drivers:* Pre-Workout (full) · Alpha-GPC 300

**20:15 — Post-Workout**
- Magnesium Glycinate (partial) 100 · Ashwagandha 300–600 *(on cycle/days)* · Whey Protein ~80g

**22:30 — Sleep**
- Magnesium Glycinate 200–300 · Melatonin · Apigenin · Calcium D-Glucarate *(on cycle)* · Trazodone/Glycine *(optional)*

**Rules:** Copper:Zinc mandatory pairing (Cu 2mg AM / Zn PM) · prescriptions with water 30–60min before food · cycle glucose check q6–8wk on orals · EQ cocktail (Aspirin+ARB+tadalafil) + weekly BP/HR log.

---

## QC findings — schedule vs OS (fixed 31 May 2026)

| Issue | Item | Action |
|---|---|---|
| **Daily in schedule, but `paused` in OS → wrongly excluded** | Irbesartan (75mg), Rosuvastatin (10mg) | ✅ flipped active — these are your daily protective core (+~RM32/mo) |
| same | Ashwagandha (on cycle/days) | ✅ flipped active (OCC ~400mg) |
| **Missing from OS entirely** | **Copper** (mandatory Zinc pairing), **Selenium** (200mcg) | ✅ added (prices ESTIMATED — verify) |
| **Cutting compound not in cost model** | Cardarine (GW-501516) | ✅ added to PED model (~15mg ×8wk — confirm) |
| **Overcounted (year-round, but situational)** | TUDCA, P5P, Calcium D-Glucarate | ✅ now `weeks_per_year`: TUDCA 16 (orals only), P5P 8 (Tren), CaDG 28 (−~RM79/mo) |
| **Reconcile** | "Whey Protein" (schedule 80g ×2 = 160g/day) vs OS OTG 40g + SPI 60g (100g) | ⚠ **which is current?** Your earlier instruction said OTG 40 + SPI 60 |
| **Food (not yet priced)** | mayonnaise, fish roe, olive oil (fat carriers) | → part of the whole-food premium TODO |
| **Dose mismatches (minor cost)** | Astragalus (OS 1100 vs schedule 250), Alpha-GPC (300 vs 600 on training), Magnesium (EOD vs daily AM+PM) | flagged — confirm if you want exact |

> [!important] The TUDCA rule you specified
> Irbesartan (ARB) runs year-round for kidney/BP protection, so **TUDCA (liver) is only needed when a 17-alkylated oral is in the stack** (Anavar). Modeled at 16 weeks/year, not 52. P5P only with Tren (8wk). This is the situational cycle-support logic now baked into [[Monthly Nut]] via `weeks_per_year`.

## Net effect
The fixes nearly cancel: +RM60/mo (restored core + minerals) − RM79/mo (situational cycle support) + RM15 (Cardarine). **Monthly Nut stayed ~RM2,918**, but now every line maps to a real schedule entry. Open: confirm Whey 100 vs 160g, Copper/Selenium prices, Cardarine weeks.

## Links
- Cost rollup: [[Monthly Nut]] · Cycle logic: [[Annual Cycle Design]] · Freedom: [[Freedom Numbers]]
