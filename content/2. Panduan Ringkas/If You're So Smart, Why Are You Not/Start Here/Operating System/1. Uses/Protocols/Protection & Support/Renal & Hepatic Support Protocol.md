---
draft: true
type: protocol
name: "Renal & Hepatic Support Protocol"
phase: "Always-on / Oral windows"
goal: "Protect kidney and liver markers during blasts, oral windows, high-BP phases, and aggressive cuts."
status: "draft-v1"
pipeline: "P4"
owns: "Kidney/liver support, oral support, hydration, cystatin C/eGFR"
date: 2026-06-07
tags:
  - operating-system
  - protocol
  - p4
  - renal
  - hepatic
---
# Renal & Hepatic Support Protocol

> [!abstract] Owns the kidney/liver monitoring and support layer.
> Product owners include [[Astragalus Root (550mg×240tab) — iHerb]], [[TUDCA (250mg×60tab) — iHerb]], [[NAC (600mg×180tab) — iHerb]], [[Selenium (100mcg×240tab) — iHerb]], [[Copper (Bisglycinate) (2mg×100tab) — iHerb]], [[Methyl B Complex (250mg×60tab) — iHerb]], [[Vitamin C (1000mg×60tab) — iHerb]], [[TMG (Betaine) (750mg×120tab) — iHerb]], [[Calcium D-Glucarate (500mg×120tab) — iHerb]], [[DIM (300mg×120tab) — iHerb]], [[Zinc (50mg×120tab) — iHerb]], and [[Boron (5mg×240tab) — iHerb]].

> [!danger] Boundary
> Support supplements do not make nephrotoxic, hepatotoxic, dehydrating, hypertensive, or oral-AAS phases safe. This note is a monitoring and stop-rule layer.

## What This Protocol Owns

- Kidney marker interpretation: creatinine/eGFR, cystatin C, urine albumin/creatinine, BP, hydration, and hematocrit context.
- Liver marker interpretation: ALT, AST, GGT, bilirubin, ALP, symptoms, alcohol, oral AAS, and supplement/drug burden.
- Oral-window support handoff from [[Oral and Extreme Deployment Protocol]].
- Renal overlap with [[Blood Pressure & Fluid Escalation Protocol]] and SGLT2/diuretic overlap from [[Glucose & Insulin Sensitivity Protocol]].

## Entry Criteria

Use this protocol when:

- Any oral AAS, tren, aggressive stimulant/thyroid cut, dehydration phase, or diuretic lane is planned.
- BP is elevated, hematocrit is high, urine markers are abnormal, or creatinine/eGFR/cystatin C is drifting.
- ALT/AST/GGT/bilirubin rise or symptoms suggest hepatic stress.
- A support product is being added to the stack and needs ownership rather than being scattered through product notes.

## Baseline Requirements

- CMP: creatinine/eGFR, electrolytes, ALT, AST, ALP, bilirubin.
- Cystatin C if muscularity, creatine use, or high meat intake makes creatinine hard to interpret.
- Urinalysis and urine albumin/creatinine when BP, kidney risk, SGLT2 use, or high hematocrit is present.
- CBC/hematocrit, BP log, hydration pattern, alcohol, oral AAS dates, and supplement list.

## Decision Framework

1. **Pressure and hydration first.** Kidney support starts with BP control, hydration consistency, sodium consistency, and avoiding dehydration games.
2. **Separate creatinine noise from kidney signal.** Creatine, high muscle mass, high meat intake, dehydration, and hard training can move creatinine. Use cystatin C and urine markers when the signal is unclear.
3. **Oral-AAS liver gate.** [[TUDCA (250mg×60tab) — iHerb]] and [[NAC (600mg×180tab) — iHerb]] belong to oral-window support, but abnormal labs or symptoms stop the oral; support products do not overrule the stop condition.
4. **Renal support lane.** [[Astragalus Root (550mg×240tab) — iHerb]] and BP control sit in the renal-protection lane.
5. **Methylation/antioxidant floor.** [[TMG (Betaine) (750mg×120tab) — iHerb]], [[Methyl B Complex (250mg×60tab) — iHerb]], [[Vitamin C (1000mg×60tab) — iHerb]], [[Selenium (100mcg×240tab) — iHerb]], [[Copper (Bisglycinate) (2mg×100tab) — iHerb]], and [[Zinc (50mg×120tab) — iHerb]] are support tools that need dose sanity and duplication checks.
6. **Hormonal-support overlap.** [[DIM (300mg×120tab) — iHerb]], [[Calcium D-Glucarate (500mg×120tab) — iHerb]], [[Boron (5mg×240tab) — iHerb]], and [[Zinc (50mg×120tab) — iHerb]] cross into estrogen/PCT support. Avoid double-counting with [[PCT Support Layer Protocol]] and [[Oral and Extreme Deployment Protocol]].

## Stop / Review Rules

Stop the stressor and review if:

- ALT/AST/GGT/bilirubin rise substantially or jaundice, dark urine, pale stool, severe itching, right-upper-quadrant pain, or severe fatigue appears.
- eGFR/cystatin C worsens, urine albumin rises, edema appears with high BP, or electrolyte abnormalities occur.
- Dehydration, heat illness, vomiting, diarrhea, or SGLT2/diuretic overlap is present.
- Multiple hepatotoxic or nephrotoxic agents are stacked without a written reason.

## Monitoring

- **Routine enhanced phases:** CMP, CBC, BP, lipids, and urine markers on the system's bloodwork cadence.
- **Oral windows:** baseline CMP, mid-window check if risk is high, and post-window check.
- **Diuretic/SGLT2 overlap:** electrolytes, renal markers, hydration, ketone-symptom watch, and BP.
- **Kidney uncertainty:** cystatin C and urine albumin/creatinine rather than arguing from creatinine alone.

## Red Flags

Urgent review: jaundice, severe abdominal pain, confusion, fainting, severe dehydration, very low urine output, blood in urine, severe edema/shortness of breath, dark urine with muscle pain, or rapidly worsening BP.

## Stock Math

- **TUDCA/NAC oral window:** `daily_units x oral_window_days`, plus reserve only if another oral window is scheduled.
- **Astragalus renal lane:** `daily_units x active_phase_days`.
- **Micronutrients:** consolidate across PCT, sleep, shield, and renal protocols so zinc/magnesium/B-complex are not duplicated.
- **Labs as inventory:** if a protocol requires same-window labs, the lab budget is part of the stock math.

## Links

- Build map: [[Protocol Build Map]]
- Related: [[Year-Round Shield]], [[Blood Pressure & Fluid Escalation Protocol]], [[Glucose & Insulin Sensitivity Protocol]], [[Oral and Extreme Deployment Protocol]], [[PCT Support Layer Protocol]]
