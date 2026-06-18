---
draft: true
type: protocol
name: "Recomposition & Lean Bulk Deployment Protocol"
phase: "Recompose / Lean Bulk"
goal: "Govern the off-season growth/hold block — when to run recomp (maintenance) vs lean bulk (small surplus), how to escalate, and when to bridge into a cut."
status: "draft-v1"
pipeline: "P1/P2/P3"
owns: "Recomp vs lean-bulk mode switch, surplus sizing, partitioning/glucose gates, bridge-to-cut timing"
date: 2026-06-18
tags:
  - operating-system
  - protocol
  - lean-bulk
  - recompose
  - off-season
  - deployment
---
# Recomposition & Lean Bulk Deployment Protocol

> [!abstract] Owns the off-season growth/hold calendar.
> [[Recomposition & Lean Bulk Protocol]] says *what the stack contains* and *which calorie mode* you're in. This note decides *when* to run recomp vs lean bulk, *how much* surplus to allow, *when* to escalate or pull guardrails, and *when* the block becomes the **bridge into a cut**. The two modes share one chemistry — this governor moves the calorie dial and the gates.

> [!info] Theory: [[Muscle Building Pathways (Theory)]] explains *why* partitioning + the GH/insulin Akt arm matter — the mTORC1 chain and the three compartments this block is trying to fill.

> [!danger] Boundary
> Deployment governor, not a prescription. Test/EQ/Tren/Anadrol/Masteron, HGH/secretagogues, Metformin/SGLT2, GLP-1/GIP/GCGR agonists (Retatrutide), ARBs/β-blockers each require owner-protocol safety gates and clinician-reviewed bloodwork. Every start is gated on [[Bloodwork & Calculated Biomarkers]].

## Deployment Clock

| Field | Rule |
|---|---|
| **Trigger** | Post-cut consolidation, or a planned off-season growth block, or a "hold and harden" window before a cut. |
| **Mode select** | **Recompose = maintenance kcal** (hold weight, improve composition, restore insulin sensitivity, sharpen dryness — the cut bridge). **Lean bulk = +200–500 kcal** (slow muscle gain, fat capped ≤ ~15%). Same stack; only calories + gates differ. |
| **Duration logic** | Runs with the off-season block (typically medium, 12 wk; up to long/eq if EQ is the lateral — see [[Endocrine Design Rules]] Rule 3). Recomp bridge can be a short 3–6 wk taper into the cut. |
| **Deployment logic** | Food + training base first. Layer GH/partitioning tools, then glucose guardrails, then (only as a deliberate blast) the harsh oral/Tren overlay. Escalate by composition trend, bloods, BP/HR, glucose, sleep. |
| **Stock math** | Block demand; separate INDEXA-funded GH stock from personal stock; count harsh-overlay tools only for the weeks they actually run. |

## Owned Products

- **Anabolic base lane:** [[Testosterone Enanthate Etho 450 (450mg-ml ×10ml) — beligaspharmacy Intl|Test E]], [[Boldenone Undecanoate (250mg-ml ×10ml) — kohohpharma|EQ (Boldenone)]], **Masteron (Drostanolone)** *(not in catalog — source; [[Proviron (25mg×50tab) — kohohpharma|Proviron]] is the in-stock analog)*, **Anadrol (Oxymetholone)** *(not in catalog — source; [[Oxandrolone (Anavar) (10mg×100tab) — kohohpharma|Anavar]] is the in-stock oral)*, [[Trenbolone Acetate Acro (100mg-ml ×10ml) — beligaspharmacy Intl|Trenbolone Acetate]] — harsh-oral/Tren on-off windows via [[Oral and Extreme Deployment Protocol]] + Tren neuro-cover [[Neuroprotection Protocol (Tren)]]
- **GH / IGF-1 lane:** [[MK-677 (10mg×50tab) — kohohpharma|MK-677]], [[HGH (100iu-kit) — TCI|HGH]], [[CJC-1295 (No DAC) + Ipamorelin (10mg×10vial) — TCI|CJC-1295 + Ipamorelin]]
- **Partitioning lane:** [[Retatrutide (60mg×10vial) — BFF-AMO|Retatrutide]] (micro-dose)
- **Metabolic-guardrail lane:** [[Metformin-Empagliflozin FDC (500-5mg×300tab) — shopee-china|Metformin + Empagliflozin (FDC)]], [[Methylene Blue (25g powder) — heiltropfen|Methylene Blue]]
- **Hormonal-shield lane:** [[P5P (Pyridoxal-5-Phosphate) (50mg×240cap) — iHerb|P5P]] (prolactin antagonist — mandatory with MK-677 + Tren)
- **Cardio lane:** [[Irbesartan (150mg×120tab) — shopee-china|Irbesartan]], [[Nebivolol (2.5mg×100tab) — Jigar Healthcare|Nebivolol]], [[Telmisartan (40mg×30tab) — indiamart|Telmisartan]]
- **Training fuel lane:** [[Alpha-GPC (300mg×120tab) — iHerb|Alpha-GPC]], [[Pre-Workout (1014g) — iHerb|Pre-Workout]], [[Intra-Workout (651g) — iHerb|Intra-Workout]]
- **Muscle-sparing β2 / thyroid lane:** [[Clenbuterol (40mcg×100tab) — kohohpharma|Clenbuterol]] (80 mcg = 2 tabs) + [[Ketotifen (1mg×120tab) — Lazada|Ketotifen]] (1–2 mg pre-bed, restores β2 density); [[Levothyroxine (T4) (50mcg×100tab) — shopee-china|Levothyroxine (T4)]] + [[Cytolin (25mcg×100tab) — kohohpharma|Cytomel (T3)]] at **4:1 (100:25 mcg)** — see the muscle-sparing layer below
- **Always-on:** [[GHK-Cu (1000mg-box) — TCI|GHK-Cu]], [[KPV (100mg-box) — TCI|KPV]]
- **Required substrate:** [[Training Nutrition & Pre-Intra Protocol]]

## Entry Criteria

Run this block only when:

- A blood panel has cleared the start ([[Bloodwork & Calculated Biomarkers]]); E₂, hematocrit, lipids, glucose, BP are known baselines.
- The **mode is chosen up front** — recomp (hold) vs lean bulk (gain) — with the calorie target written before the drug plan.
- Training progression, protein (~200 g), carbs, steps, and sleep are logged.
- The endocrine base complies with [[Endocrine Design Rules]] (continuous Test + the chosen lateral; flag if Test > 450 or more than one lateral is planned).

## Mode Structure

1. **Base (both modes):** establish the calorie target (maintenance or +200–500), protein anchor, training progression, hydration/electrolytes, always-on shield.
2. **GH / partitioning layer:** MK-677 (+ P5P shield), micro-dose Retatrutide, Methylene Blue. These make the calories productive.
3. **Glucose guardrail:** Metformin + Empagliflozin at ~2 PM with the first meal (see stack note timing). Enter/escalate only via [[Glucose & Insulin Sensitivity Protocol]] gates.
4. **Cardio guardrail:** ARB or Nebivolol when EQ/MK-677 push BP or hematocrit — via [[Blood Pressure & Fluid Escalation Protocol]].
5. **Harsh-oral / Tren windows:** Masteron, Anadrol, and Tren are part of this base but **time-boxed** — Tren ≤8 wk, Anadrol ≤6–8 wk, the Tren+Anadrol pair ~4–6 wk — while Test/EQ/Masteron run the full 16–20 wk. On/off windows governed by [[Oral and Extreme Deployment Protocol]] + [[Neuroprotection Protocol (Tren)]].
6. **Bridge taper:** in the last 3–6 wk before a cut, drop to **recomp/maintenance**, hold the base + guardrails, let composition and insulin sensitivity sharpen, then hand off.

## Muscle-sparing layer — β2 (Clen + Ketotifen) & Thyroid (T4:T3)

The engine for **building muscle while losing fat at the same time** — it raises the burn and partitions nutrients while *protecting* lean tissue, so it suits both recomp (maintenance) and lean bulk (small surplus). The same tools appear in the [[Cut Protocol|cut]], but the **context differs**: in a cut the job is muscle *preservation* in a deficit; here the job is *simultaneous gain + fat loss*.

**β2 — [[Clenbuterol (40mcg×100tab) — kohohpharma|Clenbuterol]] 80 mcg + [[Ketotifen (1mg×120tab) — Lazada|Ketotifen]] 1–2 mg (pre-bed):**
- **Anti-catabolic MPS, not just a fat-burner.** Vastus lateralis (quadriceps) biopsies at **80 mcg** show activated **Protein Kinase A (PKA)** and phosphorylated **ribosomal protein S6 (RpS6)** — the explicit intracellular pathways that *upregulate muscle protein synthesis and reduce protein degradation*. At this dose clen is doing partitioning/anti-catabolic work, not only lipolysis.
- **Ketotifen** (antihistamine) up-regulates/restores β2-receptor density, reversing the downregulation that normally forces 2-on/2-off clen cycling — so 80 mcg keeps working over a longer continuous run; its sedation also offsets clen's stimulation. Dose pre-bed.

**Thyroid — [[Levothyroxine (T4) (50mcg×100tab) — shopee-china|T4]] : [[Cytolin (25mcg×100tab) — kohohpharma|T3]] at 4:1 (100 mcg : 25 mcg):**
- Standard physiological-style ratio for **nutrient partitioning + raised BMR** without the muscle-wasting/suppression risk of T3-heavy dosing. More T4, low T3 = a gentle metabolic lift that fits a recomp/lean-bulk — vs the [[Cut Protocol|cut]], where T3 may be pushed higher (2–3 tabs) for a finite window.

**Net effect:** raised BMR + adrenergic lipolysis strip fat while PKA/RpS6 + the anabolic base hold MPS high → simultaneous gain + loss. Runs under the same cardiac/glucose guardrails as the rest of the stack (next).

## Decision Framework

1. **Food + mode first.** No defined calorie target, no block. Recomp holds weight; lean bulk adds ≈0.25–0.5%/wk. If lean-bulk gain runs faster, it's fat — tighten toward recomp or [[Off-Season Mini-Cut & Accelerator Tiers|mini-cut]].
2. **Dose-rule check.** This base (Test 500 + EQ + Masteron + Anadrol + Tren) is multi-lateral and conflicts with [[Endocrine Design Rules]] (Rules 1–2) **by design** — run it as a *protected blast* at recomp/lean-bulk calories, gated on bloods, not as the default off-season base. If you want the rule-clean version, fall back to Test ≤450 + one lateral.
3. **Prolactin gate.** While MK-677 runs, P5P 50–100 mg/day is mandatory (EQ-estrogen × MK-677-prolactin gyno trap).
4. **Glucose gate.** If MK-677/GH/food pushes fasting or post-meal glucose, edema, or lethargy → enforce [[Glucose & Insulin Sensitivity Protocol]]; SGLT2 hydration/electrolyte rules apply.
5. **Retatrutide constraint.** Micro-dose only (0.5–1.0 mg/wk) — partitioning, not appetite kill. If it suppresses intake enough to miss the calorie/protein target, cut it.
6. **Harsh-oral hard caps.** Tren ≤8 wk, Anadrol ≤6–8 wk, the harsh pair ~4–6 wk; liver (TUDCA/NAC) + BP + Tren neuro cover active throughout.
7. **β2 / thyroid gate.** Clen + T3 both raise HR/cardiac demand — don't run on uncontrolled BP/HR or poor sleep. Titrate clen in (40→80 mcg) and keep ketotifen pre-bed; add taurine + potassium/electrolytes for clen cramps. Hold the gentle T4:T3 4:1 unless an aggressive window justifies more T3. BP/HR via [[Blood Pressure & Fluid Escalation Protocol]].

## Escalation Rules

- Add one new stressor at a time so sides are traceable.
- Don't escalate off one flat week — check adherence, sleep, water, sodium, training stress first.
- SGLT2 tools stay out of dehydrating/ketogenic/illness/diuretic-heavy windows.
- Don't open the harsh-oral windows (Anadrol/Tren) on poor sleep, uncontrolled BP/HR, or high hematocrit.

## Exit Criteria

End, taper, or hand off when:

- **Lean bulk:** weight gain exceeds target and waist rises faster than performance → downshift to recomp or [[Off-Season Mini-Cut Protocol]].
- **Recomp:** composition has held/improved and the cut window has arrived → hand to [[Cut Protocol]] / [[Cutting Cycle Deployment Protocol]].
- Fasting/post-meal glucose worsens; edema, numbness/tingling, BP rise, apnea signs, or lethargy appear.
- Bloods (E₂, hematocrit, lipids, renal/hepatic) breach owner-protocol stop rules.

## Monitoring

- **Daily:** bodyweight, appetite, sleep, digestion, training readiness, edema; glucose checks while GH/glucose tools active; resting HR, tremor, and cramps while clen/thyroid run.
- **Weekly:** waist, photos, lifts, 7-day average calories/protein/carbs, steps, BP/HR trend.
- **Labs:** via [[Year-Round Shield]], [[Lipid Management Protocol]], [[Renal & Hepatic Support Protocol]], [[Glucose & Insulin Sensitivity Protocol]] — hematocrit watched closely on EQ.

## Red Flags

Stop and review for hypoglycemia symptoms, severe edema, shortness of breath, chest pain, uncontrolled BP, rapid glucose deterioration, gyno onset/prolactin signs, severe GI intolerance, sleep-apnea signs, worsening numbness/tingling, injection-site/systemic reaction, or — on clen/thyroid — sustained resting tachycardia, palpitations, severe tremor/anxiety, or heat intolerance.

## Stock Math

- Base + GH + guardrail lanes: `active_block_days × planned_units`; separate INDEXA-funded GH from personal stock.
- Retatrutide: count total mg + titration waste at the micro-dose.
- Glucose/SGLT2: count only days the glucose gate is active.
- Time-boxed harsh orals (Tren/Anadrol) + Masteron: Test/EQ/Masteron run the full block; count Tren/Anadrol only for their gated weeks; source the off-catalog items (Masteron, Anadrol) first.
- β2 / thyroid lane: clen 80 mcg/day = **2 × 40 mcg tabs/day**; ketotifen 1–2 mg pre-bed; T4 100 mcg = **2 × 50 mcg tabs/day** (or the 100 mcg tab); T3 25 mcg = **1 × 25 mcg tab/day**. Count by active days; ketotifen enables continuous clen, so model the full run, not 2-on/2-off.
- Food/fuel: protein, intra-workout, electrolytes, eggs, carbs count as part of the block.
- Re-run [[Stock Forecast — Intake Protocol]] after any mode/dose/compound change.

## Links

- Parent stack: [[Recomposition & Lean Bulk Protocol]]
- Theory: [[Muscle Building Pathways (Theory)]]
- Endocrine rules: [[Endocrine Design Rules]] · Bloods gate: [[Bloodwork & Calculated Biomarkers]]
- Related: [[Bulk Protocol]], [[Bulk Recovery & Partitioning Protocol]], [[Off-Season Mini-Cut Protocol]], [[Off-Season Mini-Cut & Accelerator Tiers]], [[Cut Protocol]], [[Cutting Cycle Deployment Protocol]], [[Oral and Extreme Deployment Protocol]]
- Live run: [[2026 Q4 — Lean Bulk 1]]
