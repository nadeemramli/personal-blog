---
title: QC & Gap Analysis
draft: true
tags:
  - operating-system
  - qc
  - gaps
date: 2026-05-31
---
> [!abstract] Two questions answered here.
> **(1)** What did the Operating System miss from the Google Sheets? **(2)** Across the whole series, what is costing us that we are not yet tracking *anywhere*?

## Part 1 — Sheets → Operating System QC

### What migrated cleanly ✅

Both **Item** tabs are fully in. All 41 rows of the Performance Enhancement *Item* sheet and all 22 of the Cognitive *Item* sheet are present as the 57 product notes (the four shared items — Magnesium, Apigenin, NAC, Alpha-GPC — were correctly merged, not dropped). Doses, 4 cost tiers, cycle weeks, importance, vendor, and the dosing schedule all carried over, and the EOD/ITD/Occasionally forecast logic was fixed.

### What we missed — these live in *other tabs*, never in the Item sheets

The gaps aren't migration errors; they're whole categories that only ever existed in the **Expenses**, **Budgeting**, and **Wishlist** tabs and so were never part of the model.

1. **Peptides — entire category missing.** CJC-1295/Ipamorelin, Retatrutide, SS31, MOTS-c, BPC-157, GHK-cu. Real and recurring: the Budgeting *Peptide* category runs **~RM350–440/month**, and Expenses shows live buys (CJC+Ipamorelin RM1,158; Retatrutide RM858 from Prime Pharma). The schema has a `Peptide` category with zero items in it.
2. **PCT (post-cycle therapy) missing.** HCG (Wishlist notes: *"super important, use around intra-cycle 2–4 weeks"*), HMG, Clomiphene (RM106), Tamoxifen (RM109). The `PCT` tag exists; no items carry it. For someone running anabolics this is a safety gap, not just a cost gap.
3. **Protein + Amino/Pre missing.** WPI, MPC, SPI, Critical Whey, plus L-Citrulline, Beta-Alanine, L-Carnitine, Glycerol, Glutamine. Budgeting: Protein **~RM190/mo**, Amino/Pre **~RM125/mo**. (Only Creatine made it across, via the cognitive sheet.)
4. **Food premium missing.** Milk, nuts, eggs, lentils, Greek yogurt, berries, mushrooms — the eating-clean delta. Budgeting Food **~RM190/mo**.
5. **Skin & Hair topicals missing.** From the 19 May 2026 Expenses batch: Tretinoin (RM178 + RM32), RU58841 raw (RM184), Ell-Cranel Alpha (RM172), topical Minoxidil 5% (RM261), LCTC+Minoxidil (RM102), Nizoral (RM29), plus DIY carriers (ethanol, propylene glycol). Only **oral** Minoxidil made it in — the whole Attractive/Skin & Hair stack is absent.
6. **Injection & dosing consumables missing.** Insulin syringes (NIPRO RM60×3), prep syringes, syringe filters (RM29), pill organizers, vial storage. These deplete and recur with the injectable protocol.
7. **App subscriptions missing.** MacroFactor (RM320/yr), Hevy (RM99). Recurring SaaS.
8. **Shipping / import overhead missing.** iHerb shipping was RM220 across Nov–Apr (~RM37/mo). A real tax on every overseas order.

### Schema fields worth adding (so the misses have a home)

- **`status`** (active / planned / retired) — right now `active` is a yes/no with no place for the **Wishlist** pipeline (future commitments like HCG, Armodafinil, Telmisartan, HGH). Planned items are future cost we should see coming.
- **`for_whom`** (self / family / "Along") — the Budgeting *Family* and *Along* plans show you fund supplements for others. That's a real cost dimension with no field today.
- **Restock fields** — the dashboards tracked `quantity_to_buy`, `restock_cost`, and a `Critical / High / Medium` priority bucket. We have days-until-empty + importance weight (enough to *derive* these), but no restock view surfaces them yet.
- **`shipping`/`import_overhead`** — so landed cost ≠ sticker cost.

## Part 2 — What every series costs that we don't track *anywhere*

The Operating System only knows about pills. But each pillar of the series carries recurring cost that lives in no sheet at all. Ranked by how big and how overlooked:

1. **Bloodwork & diagnostics (Healthy / Blueprint).** This is the sharpest one: the Blueprint series is *built* on measuring your biomarkers, and on a PED protocol regular panels (lipids, hormones, HbA1c, liver, hematocrit) are effectively mandatory. Lab panels, plus DEXA/InBody and the odd consult, are a recurring cost we preach and don't budget. *Biggest credibility gap.*
2. **Insurance / takaful (Peaceful — the Baseline).** Life, medical, and critical-illness cover is the literal "fully-funded floor" the First Path essay talks about (*"the low-risk position behind everything else"*). Premiums are likely one of the **largest** recurring line items and appear nowhere.
3. **Software / SaaS stack (Productive / Productivity Enhancement).** The Productivity series is *about* tooling, yet its own running cost is untracked: Claude, Obsidian (sync/publish), Retool, blog hosting + domain, MacroFactor, Hevy, plus any automation/design tools. Bundled, this is a meaningful monthly tax.
4. **Peptides + PCT + injection consumables (Fit / PE).** Already covered above — flagged again because it's both cost and safety.
5. **Protein + food premium (Healthy / Nutrition).** ~RM300–400/mo combined; the most "obvious" cost, hiding in a deprecated sheet.
6. **Learning & credentials (Rich / Successful).** ACCA exam fees (your Learning capstone was literally *ACCA-exam week*), course subscriptions, books. Lumpy but real during study cycles.
7. **Investment frictions (Rich / Multiplying Money).** Brokerage fees, fund expense ratios, platform and FX costs. Small percentages, but they compound *against* you — the mirror image of the wealth machine.
8. **Gym & training (Fit).** Membership or equipment depreciation, apparel/footwear replacement, recovery tools (massage gun, foam roller), chalk/straps wear.
9. **Grooming & sunscreen (Attractive / Appearance).** Daily sunscreen alone is non-trivial and central to the skin thesis; plus barber, devices.
10. **Time — the cost we never price.** The loop is time-expensive: training, cooking, the sleep protocol, deliberate learning. Rich and Successful are "time, not cash," but *every* pillar spends hours. A time budget would show which orders are actually the most expensive to hold.

### The unifying point

The maintenance bill in [[The Upward Spiral — How the Order Compounds|the capstone]] is currently **understated** — it only counts pills. A true bill adds peptides/PCT, protein/food, skin/hair, bloodwork, insurance, and the SaaS stack. Two of those (bloodwork, insurance) aren't optimisations — they're the safety floor the whole thesis rests on. They should be the *first* things added, not the last.

> [!note] Suggested next moves
> 1. Add the missing **product** categories to the OS (peptides, PCT, protein/amino, skin-hair topicals, consumables) — I have the costs from the sheets.
> 2. Add `status`, `for_whom`, and `shipping` fields to the [[Schema — Data Model|schema]] (and mirror in the Retool DB).
> 3. Open three non-supplement cost notes the series implies but never tracked: **Bloodwork**, **Insurance/Takaful**, **Software & Subscriptions**.

---

## Part 3 — Final gap pass (after the build)

**Now resolved:** peptides (excluded — INDEXA-funded), PCT (HCG ×2, HMG, Clomiphene, Tamoxifen), protein/amino/eggs, skin & hair topicals, injection consumables, diagnostics + the calculated-biomarker strategy, gym, the software/subscription stack, grooming, and boots.dev learning. The OS is now complete for **everything you consume or apply**.

What's left are costs that leave every month for reasons *other than a product*:

1. **Base living costs sit outside the OS.** Rent (~RM1,814), car (RM500), fuel + TNG (~RM250), electricity + water (~RM140), WiFi + phone (~RM195) live only in the Moving Planner budget. The OS tracks *protocol* maintenance; the capstone's "buy your freedom" math needs the **full** monthly nut = living + protocol. **Decision needed:** absorb a `Living/Baseline` category into Overheads, or formally split "Order-protocol bill" from "Total cost of living" and link the budget. (Recommend one unified ledger — otherwise the freedom number is fiction.)
2. **Savings / emergency-fund allocation is untracked.** ~RM200/mo toward a 3× salary buffer — the literal Baseline floor from [[The First Path of Controlling Your life|First Path]]. It's a *payment to order*, not leftover money.
3. **Time is still unpriced.** Training, cooking, the sleep protocol, learning, blog/content hours. The loop's largest non-cash cost, and there's no time budget. A `hours_per_week` field per pillar would show which orders are most expensive to *hold*, not just to *buy*.
4. **Device depreciation / replacement.** Wearable, BP cuff, gym equipment, syringe-prep kit — capex that recurs on a multi-year cycle, not amortised anywhere.
5. **Future / contingent costs.** Post-employer **insurance premiums** (when employer cover ends), and — if applicable — **zakat** on savings/income (a real recurring Malaysian obligation). Flag now so they don't ambush the freedom math later.
6. **Minor:** actual food / Grab (consciously dropped), barber/haircut, domain price to confirm.

**Headline:** the consumable side is done. The remaining gaps are all *living costs, savings, and time*. Unifying this OS with the budget sheet is the last structural step before the maintenance bill is honest.
