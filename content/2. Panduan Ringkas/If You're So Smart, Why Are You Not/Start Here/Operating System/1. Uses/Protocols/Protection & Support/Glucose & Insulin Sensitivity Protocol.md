---
draft: true
type: protocol
name: "Glucose & Insulin Sensitivity Protocol"
phase: "Cut / Off-Season / Always-on"
goal: "Keep glucose control, appetite, insulin sensitivity, and renal-metabolic risk inside usable ranges."
status: "draft-v1"
pipeline: "P2/P3/P4"
owns: "Metformin, SGLT2, acarbose, berberine, retatrutide, glucose monitoring"
date: 2026-06-07
tags:
  - operating-system
  - protocol
  - glucose
  - insulin-sensitivity
  - cut
  - off-season
---
# Glucose & Insulin Sensitivity Protocol

> [!abstract] Owns the glucose-disposal and insulin-sensitivity layer across off-season mini-cuts, long cuts, GH/MK-677 bulks, and appetite-control phases.
> Product owners include [[Acarbose (50mg×100tab) — shopee-china]], [[Dihydroberberine (200mg×60tab) — iHerb]], [[Metformin-Empagliflozin FDC (500-5mg×300tab) — shopee-china]], standalone metformin offers, standalone empagliflozin offers, [[Retatrutide (60mg×10vial) — BFF-AMO]], [[Nicotinamide Riboside (250mg×60tab) — iHerb]], and the mitochondrial support notes routed through [[Methylene Blue Protocol]].

> [!danger] Boundary
> Metformin, SGLT2 inhibitors, GLP-1/GIP/GCGR agonists, and insulin-related decisions are medical decisions. This note documents harm-reduction gates and inventory ownership, not a self-prescribing instruction.

## Deployment Contexts

The same compound means different things depending on timing:

- **Off-season mini-cut:** short reset when bulk quality is drifting, appetite is high, waist is rising, or glucose tolerance is visibly worse.
- **Long cutting cycle:** glucose layer supports adherence, appetite control, and carb handling while the deficit does the main work.
- **Bulk recovery and partitioning:** used only when food load, GH/MK-677, sleep disruption, or fasting glucose trends justify a glucose layer.
- **Final shred:** only if the user has earned it through markers. SGLT2/diuretic/dehydration overlap is a major risk, not a cosmetic shortcut.

## Owned Products

- Meal-level carb handling: [[Acarbose (50mg×100tab) — shopee-china]]
- Nutrient partitioning support: [[Dihydroberberine (200mg×60tab) — iHerb]]
- Biguanide lane: standalone metformin notes and [[Metformin-Empagliflozin FDC (500-5mg×300tab) — shopee-china]]
- SGLT2 lane: standalone empagliflozin notes and [[Metformin-Empagliflozin FDC (500-5mg×300tab) — shopee-china]]
- Appetite/metabolic pharmacology: [[Retatrutide (60mg×10vial) — BFF-AMO]]
- Supportive metabolism: [[Nicotinamide Riboside (250mg×60tab) — iHerb]]
- Separate specialist note: [[Methylene Blue Protocol]]

## Entry Criteria

Use this protocol when at least one is true:

- Fasting glucose, post-meal glucose, HbA1c, waist trend, appetite, or pump/crash pattern suggests worsening insulin sensitivity.
- A GH/MK-677/high-food phase is beginning and glucose tolerance is a known constraint.
- A cut has stalled because appetite and carb handling are the limiting factors, not because the deficit is undefined.
- The planned phase uses retatrutide, SGLT2, metformin, or acarbose and needs safety gates.

## Required Baseline

Before the prescription-drug lanes are treated as operational, capture:

- Fasting glucose, HbA1c, fasting insulin if available, CMP, creatinine/eGFR, cystatin C if available, urine albumin/creatinine if kidney risk exists.
- Bodyweight, waist, BP/HR, hydration pattern, carb intake, alcohol intake, fasting window, and training time.
- Whether the phase is low-carb, ketogenic, fasting-heavy, dehydrating, stimulant-heavy, or using diuretics.

## Decision Ladder

1. **Food architecture first.** Carb timing, fiber, protein target, step count, and training placement come before drug escalation.
2. **Meal-specific control.** [[Acarbose (50mg×100tab) — shopee-china]] owns meal-level carb spikes; it is not a fix for uncontrolled daily calories.
3. **Supplemental partitioning.** [[Dihydroberberine (200mg×60tab) — iHerb]] belongs in the lower-risk support lane when the signal is mild.
4. **Metformin lane.** Metformin is for persistent insulin-resistance patterns, GH/MK-677 food-load issues, or a planned cut where glucose markers justify it. It requires renal gating and illness/contrast/surgery stop rules.
5. **SGLT2 lane.** Empagliflozin is higher-risk in this context because fasting, low-carb dieting, dehydration, heat, diuretics, and heavy training can stack with ketoacidosis risk. Do not combine casually with final-shred dehydration or [[Indapamide (2.5mg×60tab) — shopee-china]].
6. **Retatrutide lane.** [[Retatrutide (60mg×10vial) — BFF-AMO]] owns appetite/metabolic leverage, but also changes nutrition tolerance. Pair with hydration, protein, electrolytes, and training-quality checks.
7. **FDC constraint.** [[Metformin-Empagliflozin FDC (500-5mg×300tab) — shopee-china]] is ratio-locked. Do not pretend it is two independently adjustable drugs; every empagliflozin change also changes metformin exposure.

## Stop / Hold Rules

Hold and review the glucose layer during acute illness, vomiting, diarrhea, dehydration, prolonged fasting, very low-carb dieting, surgery, contrast imaging, suspected infection, or unexplained abdominal pain/nausea/fatigue.

For SGLT2 specifically, ketone symptoms matter even if glucose is not high. Euglycemic ketoacidosis can present with normal-ish glucose.

## Monitoring

- **Daily during deployment:** bodyweight, appetite, hydration, training quality, GI tolerance, dizziness, unusual fatigue.
- **Glucose checks:** fasting glucose and targeted post-meal checks when changing food or glucose agents.
- **Labs:** HbA1c, CMP, creatinine/eGFR, cystatin C if available, urine albumin/creatinine if kidney risk exists.
- **Overlap checks:** BP/fluid via [[Blood Pressure & Fluid Escalation Protocol]], renal status via [[Renal & Hepatic Support Protocol]], cut timing via [[Off-Season Mini-Cut Protocol]] and [[Cutting Cycle Deployment Protocol]].

## Red Flags

Urgent review: nausea/vomiting, abdominal pain, deep or rapid breathing, confusion, fruity breath, severe weakness, dehydration, genital/urinary infection symptoms, fainting, severe hypoglycemia symptoms, or ketones with illness/fasting.

## Stock Math

- **Acarbose:** `meals_covered_per_day x cut_days`, not calendar days.
- **Dihydroberberine:** `daily_units x active_phase_days`.
- **Metformin:** calculate by metformin mg exposure, especially when comparing XR/SR/FDC offers.
- **Empagliflozin:** calculate by empagliflozin mg exposure; never hide the paired metformin exposure in the FDC.
- **Retatrutide:** track vial concentration, total mg, titration waste, and reserve separately from tablet stock.

## Reference Anchors

- Metformin renal and lactic-acidosis safety anchor: [FDA metformin renal warning update](https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-revises-warnings-regarding-use-diabetes-medicine-certain?id=1712) and [DailyMed metformin label](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=f6581ce6-0f9f-4887-ae83-4c6ecde619f3).
- Empagliflozin/metformin SGLT2 ketoacidosis and dehydration anchor: [FDA label](https://www.accessdata.fda.gov/drugsatfda_docs/label/2015/205649s003lbl.pdf).

## Links

- Build map: [[Protocol Build Map]]
- Related phase protocols: [[Off-Season Mini-Cut Protocol]], [[Cutting Cycle Deployment Protocol]], [[Bulk Recovery & Partitioning Protocol]], [[Final Shred Deployment Protocol]]
