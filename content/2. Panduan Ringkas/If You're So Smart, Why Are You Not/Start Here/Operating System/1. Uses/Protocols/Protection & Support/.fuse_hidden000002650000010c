---
draft: true
type: protocol
name: "Blood Pressure & Fluid Escalation Protocol"
phase: "Always-on"
goal: "Control blood pressure, resting heart rate, edema, and fluid shifts during enhanced phases."
status: "draft-v1"
pipeline: "P4"
owns: "ARB/PDE5/beta-blocker/diuretic decision tree"
date: 2026-06-07
tags:
  - operating-system
  - protocol
  - p4
  - blood-pressure
  - fluid
---
# Blood Pressure & Fluid Escalation Protocol

> [!abstract] Owns the cardiovascular escalation layer: ARB choice, PDE5 support, resting-HR control, and diuretic/fluid decisions.
> This is the decision owner for [[Irbesartan (150mg×120tab) — shopee-china]], [[Telmisartan (40mg×30tab) — indiamart]], [[Tadalafil (10mg×100tab) — shopee-china]], [[Tadalafil (20mg×100tab) — Jigar Healthcare]], [[Nebivolol (2.5mg×100tab) — Jigar Healthcare]], [[Nebivolol Nebiheal (5mg×10tab) — Equicare Ventures]], [[Nebivolol Nebiheal (10mg×10tab) — Equicare Ventures]], [[Indapamide (2.5mg×60tab) — shopee-china]], [[Aged Garlic Extract (300mg×300tab) — iHerb]], [[Magnesium Glycinate (210mg×240tab) — iHerb]], and [[Taurine (1000mg×100cap) — iHerb]].

> [!danger] Boundary
> Harm-reduction documentation, not a prescription. Any prescription BP drug, beta-blocker, PDE5 inhibitor, or diuretic requires clinician review, baseline labs, and a written stop rule before use.

## What This Protocol Owns

- Daily BP and resting-HR interpretation during blast, cruise, bulk, cut, and stimulant phases.
- Choosing one ARB lane rather than stacking ARBs.
- Deciding whether a BP problem is pressure-driven, heart-rate-driven, or fluid-driven.
- Deciding when [[Indapamide (2.5mg×60tab) — shopee-china]] is inappropriate because dehydration/electrolyte risk is higher than the edema problem.
- Handing off lipid and renal abnormalities to [[Lipid Management Protocol]] and [[Renal & Hepatic Support Protocol]].

## Entry Criteria

Use this protocol when any of these appear:

- Repeated home BP readings are above the target range after confirming cuff size, posture, rest period, and measurement timing.
- Resting HR is persistently elevated relative to baseline, especially during stimulant-heavy cuts.
- Morning scale weight jumps quickly with ankle/hand/face edema, poor sleep, or shortness of breath.
- A compound known to raise blood pressure, water retention, hematocrit, sympathetic tone, or appetite is being added.
- A long bulk, high-carb phase, GH/MK-677 phase, or final-shred stimulant phase is starting.

## Pre-Check Before Escalation

Before changing the drug layer, log the non-drug inputs for 3-7 days:

- Sodium consistency, potassium-rich foods, hydration, alcohol, sleep duration, stimulant load, nicotine, and training stress.
- Morning BP/HR, evening BP/HR, bodyweight, edema notes, and headache/palpitations.
- Current cycle phase and whether the BP rise started with an androgen, GH/MK-677, thyroid, clen/yohimbine, or diet change.
- Latest CMP/electrolytes, creatinine/eGFR, cystatin C if available, hematocrit, and urine albumin/creatinine if kidney risk is present.

## Decision Ladder

1. **Measurement cleanup first.** Fix poor readings, inconsistent sodium, dehydration, missed sleep, and stimulant stacking before calling it a pharmacology problem.
2. **Base pressure control.** If BP is persistently high, the ARB lane is the base decision. Pick one lane only: [[Irbesartan (150mg×120tab) — shopee-china]] or [[Telmisartan (40mg×30tab) — indiamart]], not both.
3. **Endothelial/pump support.** [[Tadalafil (10mg×100tab) — shopee-china]] or [[Tadalafil (20mg×100tab) — Jigar Healthcare]] belongs here when the goal is endothelial support, BP support, or pump quality. Avoid with nitrates or unsafe hypotension risk.
4. **Heart-rate control.** [[Nebivolol (2.5mg×100tab) — Jigar Healthcare]] and alternatives are only for HR/BP patterns where heart rate is part of the problem. Flag stimulant conflicts because beta-blockade can mask stress and blunt clen/yohimbine response.
5. **Fluid-driven escalation.** [[Indapamide (2.5mg×60tab) — shopee-china]] is not a cosmetic dryness tool. It only belongs in a fluid/BP problem with electrolyte monitoring and a stop rule.
6. **Supportive floor.** [[Aged Garlic Extract (300mg×300tab) — iHerb]], [[Magnesium Glycinate (210mg×240tab) — iHerb]], and [[Taurine (1000mg×100cap) — iHerb]] are low-friction support tools, not substitutes for medical BP control.

## Diuretic Guardrails

Do not use the diuretic lane casually when any of these are present:

- Active dehydration, vomiting, diarrhea, heat illness, sauna abuse, heavy sweating, or very low-carb/ketogenic dieting.
- Concurrent SGLT2 use from [[Glucose & Insulin Sensitivity Protocol]] without a hydration and ketone plan.
- Low sodium, low potassium, gout flare, kidney-function deterioration, or unexplained dizziness.
- Peak-week manipulation without clinician oversight and same-week electrolytes.

## Monitoring

- **Daily:** morning BP/HR, evening BP/HR, bodyweight, edema, headache, dizziness, palpitations.
- **Weekly during escalation:** 7-day BP average, resting-HR trend, stimulant exposure, sodium consistency.
- **Labs when drug layer changes:** CMP/electrolytes, creatinine/eGFR, cystatin C if available, hematocrit, urine albumin/creatinine if renal risk is present.
- **Cross-checks:** lipids via [[Lipid Management Protocol]], kidney/liver via [[Renal & Hepatic Support Protocol]], glucose/SGLT2 risk via [[Glucose & Insulin Sensitivity Protocol]].

## Red Flags

Escalate to urgent medical care rather than adjusting the stack if there is chest pain, fainting, severe shortness of breath, neurological symptoms, severe headache with very high BP, confusion, one-sided weakness, new vision changes, or signs of severe dehydration/electrolyte disturbance.

Stop and review the protocol if BP drops with dizziness, resting HR becomes abnormally low for the user, edema worsens despite intervention, kidney markers deteriorate, potassium/sodium are abnormal, or a new drug interaction appears.

## Stock Math

- **ARB lane:** `daily_units x 365 x years_covered`, plus reserve if it is the always-on BP anchor.
- **PDE5 lane:** separate daily-anchor use from occasional use; do not mix tablet strengths in projections without converting to active mg.
- **Nebivolol lane:** project only if HR-control lane is active; keep a small reserve rather than treating it as universal.
- **Indapamide lane:** pulse/rescue inventory only unless clinician-directed daily use exists. Track electrolyte-lab availability with the stock note.
- **Supportive floor:** project with [[Year-Round Shield]] and sleep/PCT overlap so magnesium/taurine are not double counted.

## Reference Anchors

- Indapamide label safety anchor: electrolyte monitoring, renal caution, and withholding if renal impairment progresses. See [DailyMed Indapamide](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=deb83f97-6c61-4a09-bed6-18dcf1183405).

## Links

- Build map: [[Protocol Build Map]]
- Constant floor: [[Year-Round Shield]]
- Related: [[Renal & Hepatic Support Protocol]], [[Glucose & Insulin Sensitivity Protocol]], [[Lipid Management Protocol]]
