---
draft: true
type: protocol
name: "Methylene Blue Protocol"
status: "to-build → review"
pipeline: "P3/P4 (mitochondrial)"
owns: "MB dosing, timing, and the hard contraindication list against Nadeem's daily cardio + brain stacks"
date: 2026-06-08
tags:
  - operating-system
  - protocol
  - methylene-blue
  - safety
---
# Methylene Blue Protocol

> [!danger] Boundary — read first
> Methylene Blue (MB) is a **potent MAO inhibitor at any meaningful dose**. You run a **prescription-grade cardiovascular + lipid regimen** (ARB, statin, beta-blocker, PDE5, antiplatelet) and a **serotonergic/catecholaminergic brain stack**. Layering an unprescribed MAOI onto that is genuinely high-risk — serotonin syndrome and hypertensive/hypotensive crises are the failure modes, and they are medical emergencies. **Clear this with your prescribing physician/cardiologist before running it.** This note is harm-reduction documentation, not a prescription.

> [!warning] Units — mg, NEVER grams
> MB is dosed in **milligrams**. The 10g / 25g on the jar is **package size**, not a dose. **15 g = ~3,000× a dose = poisoning** (methemoglobinemia, serotonin syndrome). At 5 mg/day a 25 g jar lasts **~13 years**.

## 1. Dose (low-dose nootropic/mitochondrial window)

| | |
|---|---|
| **Target** | **5–10 mg/day** total (≈0.05–0.11 mg/kg @ 91kg — deliberately *sub*-pharmacological) |
| **Start** | **5 mg**, hold 1–2 wks to assess response before considering 10 mg |
| **Frequency** | **2–3×/week**, or 5-on / 2-off — **NOT daily** |
| **Ceiling** | stay well under 2 mg/kg (~180mg) — above that MB *reverses* to pro-oxidant + strong MAOI + nitric-oxide suppressor |

> [!note] Why not daily: MB half-life is **14–27 h**. Daily dosing accumulates and silently converts a "safe low dose" into a standing high-dose MAOI environment. The breaks are the safety mechanism.

**Measuring from the [[Methylene Blue (25g powder) — heiltropfen|heiltropfen USP powder]]:** make a **1% solution = 10 mg/ml** (1 g powder in 100 ml distilled water; heiltropfen spoon = 0.2 g → 5 scoops/100 ml). Then:
- **5 mg = 0.5 ml** · **10 mg = 1.0 ml** · (the cut's 3 mg = 0.3 ml) — drawn with an insulin syringe. Store dark/cool; it stains everything.

## 2. Timing — and the conflict with the fasted T4/T3 slot

> [!important] DO NOT take MB in the 07:30 fasted slot with T4/T3 + morning cardio meds.
> - **Thyroid absorption:** MB is a reactive dye that shifts gastric pH/mucosal binding → can blunt T4/T3 uptake (thyroid meds are absorption-sensitive).
> - **BP whiplash:** the 07:30 slot has **Tadalafil + Irbesartan** (vasodilators); MB opposes NO → unpredictable BP swings / orthostatic dizziness if co-timed.

**Resolved slot: ~08:30–09:00**, **≥60 min after the 07:30 thyroid dose**, with a small food buffer. Confirmed against Nadeem's morning timeline:

| ~06:00 | fasted Zone-2 cardio (pre-meds) |
|---|---|
| **07:30** | **T4/T3 + BP cluster** (Tadalafil, Irbesartan, Rosuvastatin, Aspirin) — MB must NOT ride here |
| **~08:30–09:00** | **MB**, ≥60 min after thyroid (lets T4/T3 absorb + the BP-med peak pass), with food |

MB is deliberately **not** put in the ~06:00 fasted-cardio slot — keeping it ≥60 min after the 07:30 thyroid is what protects thyroid absorption. Take with a little food (don't pair MB fasted with aspirin — GI).

## 3. Hard contraindications (serotonin syndrome / hypertensive crisis)

Never combine MB with:
- **Antidepressants** — SSRIs/SNRIs (escitalopram, sertraline, fluoxetine, duloxetine), TCAs, other MAOIs.
- 🔴 **Trazodone (in YOUR sleep stack)** — serotonergic antidepressant (SARI); + MB's MAO-A inhibition → **serotonin syndrome**. **Avoid on MB days entirely** — MB's 14–27 h half-life means same-day spacing isn't enough; don't run trazodone the night before, of, or after an MB dose. *(added 2026-06-19)*
- **Serotonergic psychedelics / supplements** — MDMA, LSD, psilocybin, ayahuasca, **5-HTP, tryptophan**.
- **Stimulants** — amphetamines (Adderall/Vyvanse), methylphenidate; MB amplifies them → cardiac strain, panic.
- **Certain analgesics** — tramadol, meperidine, **dextromethorphan** (OTC cough syrup).

## 4. Cross-check against YOUR stacks

### Daily cardiovascular / lipid meds
| Compound | Risk w/ MB | Action |
|---|---|---|
| [[Nebivolol (2.5mg×100tab) — Jigar Healthcare\|Nebivolol]] (**now in stock** — Nebiheal 5mg) | 🚨 High | MB amplifies β-blocker hypotension + bradycardia → HR too low, dizzy spells. Watch closely / separate. *(status updated 2026-06-19: was "future")* |
| [[Irbesartan (150mg×120tab) — shopee-china\|Irbesartan]] 75mg | 🚨 High | compounded BP-lowering → hypotension/lethargy. Monitor BP. |
| [[Tadalafil (10mg×100tab) — shopee-china\|Tadalafil]] 5mg | ⚠️ Mod | MB opposes the NO pathway tadalafil works on → blunted effect / BP volatility. Separate timing. |
| [[Rosuvastatin (10mg×28tab) — shopee-china\|Rosuvastatin]] | ⚠️ Mod | MB's CYP effects can slow statin clearance → more muscle-soreness risk. |
| [[Ezetimibe (10mg×10tab) — indiamart\|Ezetimibe]] 10mg | ⚠️ Low-mod | minor; monitor with the statin. |
| [[Aspirin (100mg×60tab) — shopee-china\|Aspirin]] 100mg | 🟢 OK | no systemic interaction — **GI only**: don't take MB fasted alongside aspirin. |

> [!check] Rosuvastatin dose — RESOLVED 2026-06-08
> Confirmed **10 mg** (Nadeem had been mis-saying "100mg"; OS data was always 10mg). No action — flagging kept as a reminder the standard max is 40mg/day.

### Brain stack — on MB days you must strip the red-flag tools
| Item | Risk | On MB days |
|---|---|---|
| [[Saffron (88.5mg×240tab) — iHerb\|Saffron]] | 🚨 High (serotonin syndrome) | **REMOVE** — saffron is a mild SSRI-like; + MAOI = serotonin spike. |
| [[L-Tyrosine (500g) — iHerb\|L-Tyrosine]] | 🚨 High (hypertensive crisis) | **REMOVE** — catecholamine precursor + MAOI → norepinephrine flood, BP spike (dangerous on your BP meds). |
| [[Caffeine (200mg×250tab) — iHerb\|Caffeine]] | ⚠️ Yellow | **cut 50–75%** — MB amplifies stimulants → jitters/panic, HR. |
| [[Huperzine-A (200mcg×240tab) — iHerb\|Huperzine-A]] | ⚠️ Yellow | **drop or reduce** — MB has weak AChE-inhibition; + Hup-A + your high choline ([[Alpha-GPC (300mg×120tab) — iHerb\|Alpha-GPC]] / [[CDP-Choline (300mg×120tab) — iHerb\|CDP-Choline]]) → cholinergic overload (fog, twitches, headache). |
| [[Acetyl L-Carnitine (500mg×180tab) — iHerb\|ALCAR]] | 🟢 Synergy | keep — elite mito energy pairing (electron carrier + fatty-acid shuttle). |
| [[Uridine Monophosphate (300mg×60tab) — iHerb\|Uridine]] · [[Fish Oil (Omega-3) (1100mg×240softgel) — iHerb\|Omega-3]] · [[Phosphatidylserine (100mg×120cap) — iHerb\|Phosphatidylserine]] · [[Creatine Monohydrate (1000g) — Shopee\|Creatine]] · [[L-Theanine (200mg×240tab) — iHerb\|L-Theanine]] · [[Bacopa Monnieri (500mg×120tab) — iHerb\|Bacopa]] | 🟢 Safe | keep — structural/ATP support; PS is compatible with MB days and is not a serotonergic/catecholamine amplifier. L-Theanine also buffers MB over-stim. |

### Adrenergic / sympathomimetic stack — separate or reduce on MB days *(added 2026-06-19)*
MB is an MAO-A inhibitor, so it stacks with anything that raises catecholamine tone → ↑BP/HR.

| Item | Risk | On MB days |
|---|---|---|
| **Clenbuterol** | 🟠 Mod | β₂-agonist + MAOI → additive ↑HR/BP, arrhythmia risk. Separate; don't peak together; monitor BP/HR. |
| **Mirabegron** | 🟠 Mod | β₃-agonist (raises BP on its own) + MAOI. Monitor BP; separate. |
| **Nicotine (Nicorette)** | 🟠 Mod | triggers adrenal catecholamine release; MAOI amplifies the pressor effect. Avoid heavy use on MB days. |
| **Modafinil (Modaheal)** | 🟠 Mod | dopaminergic/wakefulness stimulant; MAOI amplifies → BP/anxiety. Avoid concurrent. |
| **Pre-Workout / Intra-Workout** | 🟠 Mod | likely caffeine/stimulant vehicles (± nitrates) → treat as caffeine; check labels, reduce on MB days. |
| ⏸️ **Yohimbine** (currently paused) | 🔴 High | α₂-antagonist → norepinephrine surge + MAOI = **hypertensive crisis**. Paused now; **if reinstated, treat as a hard 🔴 — never run on MB days.** |

### Mild / theoretical — monitor *(added 2026-06-19)*
- **Ginkgo Biloba**, **Apigenin** — weak intrinsic MAO inhibition → additive with MB. Monitor.
- **Melatonin** — serotonin-pathway metabolite; theoretical only. Monitor.
- **Beet Root Powder** — nitrate → NO donor; MB opposes the NO/cGMP axis (same as tadalafil) → blunted effect. Monitor BP.
- **T4 / T3 (Levothyroxine / Cytolin)** — thyroid sensitises tissue to catecholamines → additive adrenergic with an MAOI (separate issue from the absorption-timing conflict in §2). Keep dosing separated; monitor HR/BP.

## 5. Verdict

Run honestly, MB is a **poor fit for your current design** without surgery on it: to dose it safely you'd strip **Saffron + L-Tyrosine + Huperzine-A**, halve **caffeine**, and accept added load on a tightly-tuned BP/lipid regimen. If you still want the mitochondrial benefit:
- **5 mg, 2–3×/week, ~08:30–09:00 (≥60 min after thyroid) with food**, on days you're **not** running the red-flag cognitive tools.
- Cut's MB is timed at **~08:30–09:00** (≥60 min after the 07:30 thyroid), **not** the fasted Zone-2 slot — synced in [[2026 Q3 Cut to 15%]].
- **Physician sign-off first**, given the prescription cardio stack.

## Links
- Product: [[Methylene Blue (25g powder) — heiltropfen|MB powder]] · Used in: [[2026 Q3 Cut to 15%]] · [[Glucose & Insulin Sensitivity Protocol]]
- Build map: [[Protocol Build Map]] · System: [[The Operating System]] · [[Schema — Data Model]]
