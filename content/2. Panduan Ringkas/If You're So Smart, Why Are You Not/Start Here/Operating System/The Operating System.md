---
title: The Operating System
draft: true
tags:
  - operating-system
  - orderliness
  - index
date: 2026-05-31
---
> [!abstract] The operating layer of the whole series.
> Every section of [[The Real Problem Manifesto|If You're So Smart, Why Are You Not]] tells you *what* order to install. This folder is *how you run it* — the single place that holds every product, protocol, cost and dose across all the pillars, so the loop in [[The Upward Spiral — How the Order Compounds|The Upward Spiral]] can actually be priced and maintained.

## Why this exists

The series argues that orderliness is a **bill you pay daily**. A bill you can't see is a bill you can't manage. The sections (Fit, Healthy, Productive…) each carry a real recurring cost — money and time — and those costs are scattered across spreadsheets that are quantitatively fine but qualitatively dumb: a sheet can't tell you that an item dosed *every other day* lasts twice as long as one dosed *every day*, or that a product is "on-cycle only" versus "year-round".

So the operating system is built on **qualitative drivers**, not just numbers. How an item is dosed (ED, EOD, training-days, occasionally, cycling) decides how it is forecast. What an item is *for* (its tags) decides when it belongs in the stack. This folder models that in Obsidian first, using [Bases](https://help.obsidian.md/bases), before it graduates to a real database.

## The schemas (as Obsidian Bases)

Five kinds of note, surfaced through six [[Schema — Data Model|database views]]:

1. **[[Product List|Products]]** — `Products.base`. The catalog: brand, vendor, alternative price, usual promo price, dose per serving, dose per half serving, cost per bottle/vial, cost per dose. One note per product in [[[Products]]](Products).
2. **Product Usage** — `Product Usage.base`. The same product notes, viewed by *how we use them*: which pillar and protocol, importance, active/retired.
3. **Cycles & Dosing** — `Cycles & Dosing.base`. Cycle definitions and where each item sits in the current cycle — start date, phase, run-out.
4. **Dosing Information** — `Dosing Information.base`. The dosing-schedule dictionary (ED / EOD / Training Days / Intense Training Days / Occasionally / Cycling) with the `days_per_week` factor that drives every forecast.
5. **Sources** — `Sources.base`. How each product is bought, because landed cost ≠ sticker price: iHerb's RM22-per-RM450 shipping, the crypto + fees on overseas GMP (HCG/HMG), and so on.
6. **Overheads** — `Overheads.base`. The rest of the maintenance bill that isn't a pill: diagnostics ([[Bloodwork & Calculated Biomarkers|bloodwork]] + DEXA), gym, software/subscriptions, grooming, and **living/baseline** (rent RM0/family home, transport, utilities, phone/wifi ~RM585/mo). ~RM845/mo discretionary + ~RM585/mo living.
7. **Protocols** — `Protocols.base`. Phase stacks — [[Bulk Protocol|Bulk]], [[Cut Protocol|Cut]], [[Lean Bulk Protocol|Lean Bulk]] — documenting which products run in each phase (GHK-Cu + KPV always-on).

> [!note] Out of scope on purpose: **peptides** (CJC/Ipamorelin, Retatrutide, SS31, MOTS-c, BPC-157, GHK-cu) are funded by the **INDEXA** side-business and excluded from the personal maintenance bill. **Hevy** is a one-time lifetime app purchase, not a recurring cost.

The field model is documented in [[Schema — Data Model]], and it maps one-to-one onto the planned Retool/Postgres schema, so nothing has to be re-modelled when it moves.

## How the pieces connect

- A **product** is dosed on a **dosing schedule** and may belong to a **cycle**.
- The dosing schedule's `days_per_week` turns a per-dose amount into an *effective daily burn*; with stock on hand, that gives **days until empty** → the restock list.
- Cost per dose × effective daily burn → **cost per day** → rolled up per pillar → the **maintenance bill** the [[The Upward Spiral — How the Order Compounds|capstone]] is built on.

## A note on the duplication fix

In the old sheets, items used in two protocols (Magnesium, Apigenin, NAC, Alpha-GPC) were entered twice and double-counted. Here each physical product is **one note**, tagged for every protocol it serves. Count it once; use it everywhere.

> [!note] Status
> **Obsidian is the system of record.** Retool/Postgres has been parked — for a solo, LLM-maintained system, plain-text + Bases is more intuitive, version-able, and far more LLM-friendly. The `retool_order_schema.sql` is kept only as an export option if a live multi-user app is ever wanted. Forecasting that Bases can't do natively (run-out dates, cross-pillar roll-ups) is computed on demand and written back into the notes' frontmatter. See [[Schema — Data Model]] for the field model.
