---
draft: true
type: protocol
name: "Intra-Cycle HCG Maintenance Protocol"
phase: "On-Cycle / PCT Prep"
goal: "Define when on-cycle HCG maintenance is considered, blocked, monitored, and handed off to PCT or fertility protocols."
status: "draft-v1"
pipeline: "P1/PCT"
owns: "On-cycle testicular maintenance"
date: 2026-06-07
tags:
  - operating-system
  - protocol
  - pct
  - hcg
  - endocrine
---
# Intra-Cycle HCG Maintenance Protocol

> [!abstract] Owns the on-cycle HCG maintenance decision.
> Product owners include [[HCG renjian (10×2000IU) — Overseas GMP]] and [[HCG livzon (10×4000IU) — Overseas GMP]]. This protocol is about deciding whether maintenance is appropriate during a suppressive cycle, not about replacing a clinician-managed fertility plan.

> [!danger] Boundary
> HCG is prescription endocrine medication. Use requires clinician review, product legitimacy, injection hygiene, estrogen-side-effect monitoring, and a written handoff plan.

## What This Protocol Owns

- Whether HCG is being used during a cycle for testicular-maintenance intent.
- Separation between on-cycle maintenance, coming-off PCT, and fertility push.
- Stock math for vial strength, IU inventory, reconstitution, and consumables.
- Handoff to [[Coming-Off PCT Sequence]] or [[Fertility Push Protocol]].

## Owned Products

- [[HCG renjian (10×2000IU) — Overseas GMP]]
- [[HCG livzon (10×4000IU) — Overseas GMP]]

## Entry Criteria

Use this protocol only when:

- The user is currently on a suppressive endocrine cycle or planning one.
- The goal is maintenance of testicular function/size or easier transition into later recovery.
- Baseline endocrine labs and cycle plan are known.
- Injection consumables and storage/reconstitution rules are ready through [[Injection Hygiene & Consumables Protocol]].
- Estrogen-side-effect monitoring is active.

## Hard Blocks

Do not deploy casually if:

- Product authenticity, concentration, or storage is uncertain.
- There is no injection-hygiene setup.
- Gynecomastia/E2 symptoms are uncontrolled.
- There is testicular pain, mass, or unexplained swelling.
- The user is actually trying to conceive now; that belongs in [[Fertility Push Protocol]].

## Monitoring

- Symptoms: testicular size/ache, libido, mood, acne, water retention, nipple sensitivity, mood swings.
- Labs when appropriate: total/free testosterone, estradiol-sensitive assay if available, LH/FSH context, prolactin if symptoms indicate.
- Logistics: vial puncture date, reconstitution date, remaining IU, syringe/sawb count, storage.
- Cycle context: androgen dose changes, aromatase inhibitor decisions, and planned off-ramp.

## Red Flags

Stop and review for severe testicular pain, breast tissue growth or marked nipple symptoms, allergic reaction, injection-site infection, major mood destabilization, severe edema, or unexpected endocrine lab changes.

## Exit Criteria

Exit or hand off when:

- The cycle ends and PCT timing becomes the main question.
- A fertility goal becomes active.
- Side effects outweigh the maintenance rationale.
- Product/storage integrity becomes questionable.

## Stock Math

- Count total IU per package and total IU per vial separately.
- Track opened/reconstituted vial date and discard date.
- Convert the planned calendar into total IU demand only after clinician-reviewed dosing is known.
- Add consumables from [[Injection Hygiene & Consumables Protocol]]: syringes, swabs, labels, and sharps capacity.

## Links

- Build map: [[Protocol Build Map]]
- Related: [[Coming-Off PCT Sequence]], [[Fertility Push Protocol]], [[Injection Hygiene & Consumables Protocol]]
