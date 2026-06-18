---
draft: true
type: protocol
name: "Fertility Push Protocol"
phase: "Fertility"
goal: "Separate active fertility restoration from generic PCT and track semen-analysis, HCG/HMG, labs, and timeline."
status: "draft-v1"
pipeline: "PCT"
owns: "HCG/HMG fertility-specific path"
date: 2026-06-07
tags:
  - operating-system
  - protocol
  - fertility
  - pct
  - hcg
  - hmg
---
# Fertility Push Protocol

> [!abstract] Owns the active fertility path.
> Product owners include [[HCG renjian (10×2000IU) — Overseas GMP]], [[HCG livzon (10×4000IU) — Overseas GMP]], and [[HMG (10×75IU) — Overseas GMP]]. This is distinct from ordinary PCT because the outcome is semen parameters and conception readiness, not simply feeling recovered.

> [!danger] Boundary
> Fertility restoration after suppressive PED use should be managed with a reproductive urologist/endocrinologist. This note tracks decisions, labs, semen analysis, safety, and stock; it does not replace medical care.

## What This Protocol Owns

- Active conception timeline and fertility-specific recovery.
- Semen-analysis cadence and interpretation handoff.
- HCG/HMG inventory and injection logistics.
- Whether general PCT is insufficient and fertility-specific care is needed.

## Owned Products

- [[HCG renjian (10×2000IU) — Overseas GMP]]
- [[HCG livzon (10×4000IU) — Overseas GMP]]
- [[HMG (10×75IU) — Overseas GMP]]

## Entry Criteria

Use this protocol when:

- There is an active fertility goal or planned conception timeline.
- The user is suppressed, recently came off, or has poor semen parameters.
- Baseline semen analysis is available or scheduled.
- Reproductive clinician involvement is available.
- Injection hygiene and product legitimacy are resolved.

## Baseline Requirements

- Semen analysis: volume, concentration, total count, motility, morphology if available.
- Hormones: total/free testosterone, LH, FSH, estradiol, prolactin, SHBG if available.
- Health context: varicocele history, heat exposure, illness, medications, sleep, alcohol, nicotine, and cycle history.
- Partner timeline and fertility-workup context if relevant.

## Decision Framework

1. **Define the endpoint.** Natural conception, sperm banking, assisted reproduction, or simply restoring semen parameters are different goals.
2. **Stop suppressive inputs.** Ongoing suppressive androgen exposure fights the fertility objective.
3. **Use semen-analysis timelines.** Spermatogenesis is slow; judge changes over repeat analysis windows rather than daily symptoms.
4. **HCG/HMG are specialist tools.** HMG adds FSH-like stimulation logic and should not be treated as a generic PCT add-on.
5. **Lifestyle matters.** Sleep, heat avoidance, alcohol/nicotine control, nutrition, micronutrients, and stress can materially affect semen quality.

## Monitoring

- Semen analysis on the clinician-defined cadence, often measured in multi-month windows.
- Hormone labs: TT/FT, LH/FSH, estradiol, prolactin as directed.
- Symptoms: testicular volume/ache, libido, mood, nipple symptoms, acne, edema.
- Logistics: HCG/HMG vial dates, reconstitution/storage, injection-site reactions, consumables.

## Red Flags

Seek review for severe testicular pain, breast tissue growth, severe mood disturbance, allergic reaction, injection-site infection, major edema, severe acne, or abnormal labs that suggest the plan is overshooting or failing.

## Exit Criteria

Exit or change strategy when:

- Semen parameters reach the target for the fertility plan.
- Sperm banking is completed.
- The clinician changes the pathway to assisted reproduction or another endocrine approach.
- Side effects, cost, product integrity, or timeline make the current route unsuitable.

## Stock Math

- HCG and HMG stock are counted by total IU, vial strength, and expected fertility-window length only after a clinician-reviewed plan exists.
- HMG is tracked separately because it is fertility-specific, expensive, and not a generic recovery item.
- Consumables from [[Injection Hygiene & Consumables Protocol]] are part of the fertility budget.
- Semen-analysis and lab costs are part of the protocol budget.

## Links

- Build map: [[Protocol Build Map]]
- Related: [[Coming-Off PCT Sequence]], [[Intra-Cycle HCG Maintenance Protocol]], [[PCT Support Layer Protocol]], [[Injection Hygiene & Consumables Protocol]]
