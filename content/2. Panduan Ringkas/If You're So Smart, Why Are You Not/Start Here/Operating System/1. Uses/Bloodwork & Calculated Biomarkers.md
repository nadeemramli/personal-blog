---
title: Bloodwork & Calculated Biomarkers
draft: true
tags:
  - operating-system
  - bloodwork
  - biomarkers
  - reference
date: 2026-05-31
---
> [!abstract] The diagnostics cost layer + the "compute, don't pay" cheat sheet.
> Companion to the [[Part 1.1 - Measuring Yourself|Blueprint measuring article]]. Labs pad a "82 tests" promo by counting calculated results as separate tests. Same math is public — run it yourself, pay only for true assays.

## The diagnostics budget

| Item | Cost | Cadence | Eff. RM/mo | Note |
|---|---|---|---|---|
| Symphony Health Screening (82 + 6 tumor) | RM319 (N/P RM399) | yearly | ~26.58 | Base panel; promo 20% off |
| DEXA full-body (Sunway) | RM499 | yearly | ~41.58 | Single-site RM150–300; twice/yr optional |
| InBody | RM0 | — | 0 | Bundled in gym membership |

Tracked as `Diagnostics` in the [[The Operating System|Overheads ledger]].

## The headline trade: don't buy Free Testosterone

A direct **free testosterone** assay sells as an add-on around **RM 300–420**. But free T is *calculated* anyway (Vermeulen equation) from **Total T + SHBG + Albumin**. Total T and Albumin sit in the base panel, so you only buy the **SHBG add-on (~RM 180)** and compute **Free T + Bioavailable T** yourself. One add-on, two markers, ~RM 240 saved.

## What to PAY for (true assays, not derivable)

SHBG (~RM180) · Fasting insulin · ApoB · Lp(a) *(once in life)* · hs-CRP (~RM40) · DHEA-S (~RM75) · DHT *(no cheap proxy)* · Homocysteine (~RM60) · Iron profile (~RM70 → gives Ferritin + Serum Iron + TIBC).

## What to COMPUTE (free off cheap inputs)

### Hormones
- **Free & Bioavailable Testosterone** — Vermeulen eqn (Total T, SHBG, Albumin).
- **Free Androgen Index (FAI)** = (Total T ÷ SHBG) × 100.
- **A/G ratio** — Globulin = Total Protein − Albumin; A/G = Albumin ÷ Globulin. *(Liver panel.)*

### Lipids / cardiovascular *(off the lipid panel)*
- **LDL (Friedewald)** = Total Chol − HDL − (TG ÷ 2.2)  *(mmol/L; invalid if TG > ~4.5)*.
- **VLDL** = TG ÷ 2.2 (mmol/L).
- **Non-HDL cholesterol** = Total Chol − HDL.
- **Remnant cholesterol** = Total Chol − HDL − LDL.
- **TG : HDL ratio** — insulin-resistance + LDL-particle-size proxy.
- **Total Chol : HDL** and **LDL : HDL** ratios.
- **Atherogenic Index of Plasma (AIP)** = log₁₀(TG ÷ HDL), molar.

### Metabolic
- **TyG index** = ln(TG[mg/dL] × Fasting Glucose[mg/dL] ÷ 2) — insulin-resistance surrogate that needs **no insulin assay** (just TG + glucose you already have). The cheapest IR read.
- **HOMA-IR** = (Glucose × Insulin) ÷ 22.5 — needs the fasting-insulin add-on.
- **eAG** (estimated average glucose) = 28.7 × HbA1c − 46.7 (mg/dL).

### Liver *(LFT + CBC)*
- **De Ritis ratio** = AST ÷ ALT.
- **FIB-4** = (Age × AST) ÷ (Platelets × √ALT) — fibrosis screen.
- **APRI** = (AST ÷ AST-upper-limit) ÷ Platelets × 100.

### Kidney *(renal panel)*
- **eGFR** — CKD-EPI (Creatinine, age, sex).
- **BUN : Creatinine ratio** — hydration / kidney stress.

### Iron *(iron profile)*
- **Transferrin saturation** = (Serum Iron ÷ TIBC) × 100.

### Inflammation *(off the CBC differential — free)*
- **NLR** = Neutrophils ÷ Lymphocytes.
- **PLR** = Platelets ÷ Lymphocytes.
- **SII** = Platelets × Neutrophils ÷ Lymphocytes.

### Electrolytes / minerals *(renal + bone)*
- **Anion gap** = Na − (Cl + HCO₃).
- **Corrected calcium** = Ca + 0.02 × (40 − Albumin[g/L]).
- **Calculated osmolality** = 2 × Na + Glucose + Urea (mmol/L).

### Vitals *(your own devices, free)*
- **MAP** = DBP + (SBP − DBP) ÷ 3 *(home BP cuff)*.
- **FFMI** = Lean mass ÷ height² *(DEXA / InBody — see [[Part 1.1 - Measuring Yourself|the article]])*.

> [!warning] Where the shortcuts break
> Calculated markers are for **tracking and budgeting**, not edge-case diagnosis. Friedewald LDL fails at very high TG; TyG/HOMA-IR are trends not diagnoses; FIB-4 mis-reads at age extremes. When a *computed* number looks alarming, that is when you pay for the direct assay.

## Source / sourcing
Screening + DEXA are local clinic visits (RM, card). See [[The Operating System]] and [[Schema — Data Model]].
