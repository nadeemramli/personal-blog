---
title: Obsidian Vault Article Registry
draft: true
tags:
date: 2026-05-24
Purpose: The single source of truth for canonical article filenames and their headings. Check this before writing ANY cross-article wikilink.
---

pair-with: obsidian-markdown-standardization-writing-article, nadeems-writing-personality

last-verified: 2026-05-24 (from vault screenshot + current outputs drafts)



# Obsidian Vault Article Registry

  

This file exists to kill two recurring bugs:

  

1. **Wrong title used as a reference** — a wikilink points at a filename that doesn't exist (e.g. `[[Fit Series Part 4.0 - Pharmacology]]` when the real file is `Part 4.0 - Pharmacology`). The link silently breaks.

2. **Unsuitable / duplicated titles** — a name so generic (`Part 4.0 - Pharmacology`) that it collides with a future article, or two notes that resolve ambiguously.

  

The fix for both is the same: **one list of the real filenames and their real headings, checked before every link.** This is that list.

  

> [!important] Check this file before writing any cross-article wikilink

> If a target isn't in this registry, do not invent it. Either confirm the exact filename against the live Obsidian vault, or ask Nadeem. A broken wikilink is worse than no link.

  

---

  

## Table of Contents

  

- [[#How Claude uses this file|How Claude uses this file]]

- [[#Naming convention|Naming convention]]

- [[#The vault tree|The vault tree]]

- [[#Hair series|Hair series]]

- [[#Fit series|Fit series]]

- [[#Skin and Healthy series|Skin and Healthy series]]

- [[#Pending decisions and flags|Pending decisions and flags]]

- [[#Maintaining this file|Maintaining this file]]

  

---

  

## How Claude uses this file

  

A four-step protocol, run every time a link is about to be written:

  

1. **Before any `[[...]]` cross-article link** — look up the target in the series tables below. Copy the **Canonical filename** verbatim (without `.md`). Never type a filename from memory.

2. **Before any `#Heading` link** — confirm the heading exists in that article's heading list below. Headings are linked **verbatim**, not slugified (Obsidian uses the literal heading text after `#`).

3. **If the target isn't listed** — stop. The article may not exist yet, or the registry is stale. Ask Nadeem for the exact filename, or confirm against the live vault, then add it here.

4. **When creating a brand-new article** — do not pick the title silently. Prompt Nadeem with 2–4 title options (see the Title Selection Protocol in the standardization spec), then register the chosen name here before drafting.

  

> [!tip] Why the registry beats guessing

> Obsidian resolves wikilinks by filename. If the link text matches a real file, a future rename in Obsidian auto-updates every link to it. If the link text is invented, the rename never reaches it — it stays broken forever. The registry guarantees links point at real files, so Obsidian's auto-sync can do its job.

  

---

  

## Naming convention

  

**Series-prefix, no "Series" word.** Every file is named:

  

```

<Series> Part X.Y - <Descriptive Title>

```

  

Examples: `Hair Part 1.1 - What Actually Matters`, `Fit Part 4.0 - Pharmacology`, `Hair Part 3.0 - What Actually Matters For The Beard`.

  

Why prefix at all:

  

- **Collision-proofing.** `Part 4.0 - Pharmacology` is too generic — Hair, Fit, and a future Healthy article could all want a "Pharmacology Part 4.0", and Obsidian would resolve `[[Part 4.0 - Pharmacology]]` ambiguously. `Fit Part 4.0 - Pharmacology` is globally unique.

- **Same descriptive title across series is fine.** `Hair Part 1.1 - What Actually Matters` and `Fit Part 1.1 - What Actually Matters` coexist cleanly because the prefix disambiguates.

- **Disambiguation within a series.** Where two parts share a descriptive stem, keep the distinguishing suffix: `Hair Part 1.1 - What Actually Matters` vs. `Hair Part 3.0 - What Actually Matters For The Beard`.

  

The folder still provides human-readable grouping (`Attractive / Hair / ...`), but the **filename does not depend on the folder** — wikilinks resolve on filename alone, so the prefix must live in the name.

  

> [!note] Slug hygiene still applies

> No apostrophes, no commas, no `& ? # % +` in filenames. `.` is allowed for part numbering. See the Slug and filename rules in the standardization spec.

  

---

  

## The vault tree

  

Top-level structure (from the vault screenshot, 2026-05-24):

  

```

If You're So Smart, Why Are You Not

├── Attractive

│   ├── Hair

│   │   ├── Part 1.1 - What Actually Matters For Your Hair

│   │   ├── Part 1.2 - How to Actually Track and Decide

│   │   ├── Part 2.0 - The Stack and the Routine

│   │   └── Part 3.0 - What Actually Matters For The Beard

│   ├── Skin   (no parts visible yet)

│   └── Fit

│       ├── Part 1.1 - What Actually Matters

│       ├── Part 1.2 - Recomp, Cut or Bulk - How to Actually Decide

│       ├── Part 2.0 - Structure of a Day

│       ├── Part 3.1 - The Program - Concepts

│       ├── Part 3.2 - The Program - Rules and Building the Program

│       ├── Part 3.3 - The Program - Example Programs

│       ├── Part 4.0 - Pharmacology

│       └── Part 5.0 - Tech Integration

└── Healthy   (no parts visible yet)

```

  

> [!warning] The vault currently uses the OLD names (no series prefix)

> The **Canonical filename** column below is the target state under the chosen convention. The vault files still carry the old names until renamed in Obsidian. Because Nadeem chose "spec + registry now, rename later", links written today should still target the **current vault name** until the rename happens — then switch to canonical. Each row lists both.

  

---

  

## Hair series

  

Series prefix: **Hair**. Folder: `Attractive / Hair`.

  

| Part | Canonical filename (target) | Current vault name | Draft in outputs | Status |

|---|---|---|---|---|

| 1.1 | `Hair Part 1.1 - What Actually Matters` | `Part 1.1 - What Actually Matters For Your Hair` | `Hair - Part 1.1 - What Actually Matters.md` | Drafted ✓ |

| 1.2 | `Hair Part 1.2 - How to Actually Track and Decide` | `Part 1.2 - How to Actually Track and Decide` | `Hair - Part 1.2 - How to Actually Track and Decide.md` | Drafted ✓ |

| 2.0 | `Hair Part 2.0 - The Stack and the Routine` | `Part 2.0 - The Stack and the Routine` | `Hair - Part 2.0 - The Stack and the Routine.md` | Drafted ✓ |

| 2.1 | `Hair Part 2.1 - DIY RU58841 Preparation` | *(not in screenshot — confirm)* | `Hair - Part 2.1 - DIY RU58841 Preparation.md` | Drafted ✓ / vault TBD |

| 3.0 | `Hair Part 3.0 - What Actually Matters For The Beard` | `Part 3.0 - What Actually Matters For The Beard` | `Beard - Part 1 - What Actually Matters.md` | Drafted ✓ (was standalone "Beard Part 1") |

  

### Headings (link targets)

  

**Hair Part 1.1 — What Actually Matters**

  

- Why this Hair Series exists

- Scalp health vs. visible hair

- Hair follicles are finite — the only number that matters

- The growth cycle in 60 seconds

- The sliding scale: miniaturization → fibrosis

- How chemical stacks actually interact with the follicle

- The three diagnostic KPIs

- Tiers of measurement

- Peach fuzz or slick skin: the at-home tell

- The decision the rest of the series rests on

- Part 1.1 Takeaways

- Your Day 1 Task List

- Sources & references

  

**Hair Part 1.2 — How to Actually Track and Decide**

  

- Bridge from Part 1.1

- Why 6 months, not 3

- The baseline lock-in

- The clinic strategy: Tier 2 vs. Tier 3

- What the trichoscopy actually shows

- The attribution map: which compound drives which KPI

- The 12-month timeline

- The 6-month re-scan: diagnostic decision tree

- Part 1.2 Takeaways

- Your Baseline-to-12-Month Task List

- Sources & references

  

**Hair Part 2.0 — The Stack and the Routine**

  

- Bridge from Part 1.2

- The 90/10 frame

- The deliberate exclusion: why no finasteride or dutasteride

- Tier 1 — The Pharmacy Stack

- Tier 2 — The Research Stack

- Beyond pharmacology — mechanical and environmental protocols

- Sourcing tiers

- Bloodwork

- The optimized daily and weekly schedule

- Layering rules

- Cycle management

- How to think about all of this

- Part 2.0 Takeaways

- Your Tier-1 Stack Task List

- Sources & references

  

**Hair Part 2.1 — DIY RU58841 Preparation**

  

- Bridge from Part 2.0

- The MPMD framework in brief

- The vehicle chemistry: ethanol vs. propylene glycol

- Equipment and ingredients checklist

- The batch math: how much to make at once

- Step-by-step preparation

- Storing the bulk powder (the 250 g question)

- Storing and applying the active solution

- Part 2.1 Takeaways

- Your DIY Prep Task List

- Sources & references

  

**Hair Part 3.0 — What Actually Matters For The Beard**

  

- The one thing that makes the beard different

- Beard follicle biology: androgens are the friend, not the enemy

- The diagnostic question: dormant vs. truly absent

- KPIs for the beard

- The stack

- The deliberate exclusions: never block androgens on the beard

- The routine

- Timeline and the permanence bonus

- Beard Part 1 Takeaways *(heading still says "Beard Part 1" — rename to "Part 3.0" when the file is renamed)*

- Your Beard Task List

- Sources & references

  

---

  

## Fit series

  

Series prefix: **Fit**. Folder: `Attractive / Fit`. These already exist in the vault; the canonical column is the target rename.

  

| Part | Canonical filename (target) | Current vault name | Status |

|---|---|---|---|

| 1.1 | `Fit Part 1.1 - What Actually Matters` | `Part 1.1 - What Actually Matters` | Live in vault |

| 1.2 | `Fit Part 1.2 - Recomp, Cut or Bulk - How to Actually Decide` | `Part 1.2 - Recomp, Cut or Bulk - How to Actually Decide` | Live in vault |

| 2.0 | `Fit Part 2.0 - Structure of a Day` | `Part 2.0 - Structure of a Day` | Live in vault |

| 3.1 | `Fit Part 3.1 - The Program - Concepts` | `Part 3.1 - The Program - Concepts` | Live in vault |

| 3.2 | `Fit Part 3.2 - The Program - Rules and Building the Program` | `Part 3.2 - The Program - Rules and Building the Program` *(title truncated in screenshot — confirm)* | Live in vault |

| 3.3 | `Fit Part 3.3 - The Program - Example Programs` | `Part 3.3 - The Program - Example Programs` | Live in vault |

| 4.0 | `Fit Part 4.0 - Pharmacology` | `Part 4.0 - Pharmacology` | Live in vault |

| 5.0 | `Fit Part 5.0 - Tech Integration` | `Part 5.0 - Tech Integration` | Live in vault |

  

> [!note] Headings for Fit parts are not yet captured here

> The Fit articles live in the vault, not in this outputs folder, so their headings can't be auto-read. When a Hair/Beard article needs to deep-link into a Fit section, confirm the exact heading against the live vault (or ask Nadeem) and record it here. The one already used in the drafts: the LCLT / L-Carnitine reference points into **Fit Part 4.0 - Pharmacology** — confirm the precise heading text there before finalizing that link.

  

---

  

## Skin and Healthy series

  

No parts written yet. When the first one is drafted:

  

- **Skin** — prefix `Skin`, folder `Attractive / Skin`.

- **Healthy** — prefix `Healthy`, folder `Healthy`.

  

Run the Title Selection Protocol, then register the chosen filename and headings here.

  

---

  

## Pending decisions and flags

  

Three things need Nadeem's confirmation; none block the spec or registry from being usable today:

  

1. **Hair Part 1.1 title — drop the "For Your Hair" suffix?** The vault title is `What Actually Matters For Your Hair`. With the new `Hair` prefix, `Hair Part 1.1 - What Actually Matters` already reads unambiguously, and the suffix becomes redundant. Recommendation: drop it. (The beard at 3.0 *keeps* "For The Beard" because it shares the "What Actually Matters" stem with 1.1 inside the same series.)

2. **Hair Part 2.1 (DIY RU58841) — does it exist in the vault?** It's drafted in outputs but not visible in the screenshot. Confirm whether it's a real sub-part of 2.0, embedded in 2.0, or not yet imported.

3. **Fit Part 3.2 full title.** The screenshot truncates it to "...Rules and Building the Progr…". Assumed: `The Program - Rules and Building the Program`. Confirm the exact wording — it's a future link target.

  

Also queued (from earlier, unrelated to naming): the **KPV 500 mcg** dose default and the **GHK-Cu SubQ** route in Hair Part 2.0 are still flagged for confirmation.

  

---

  

## Maintaining this file

  

- This registry is **maintained by hand** — the live Obsidian vault isn't connected to this session, so it can't be auto-synced. Treat it as the canonical record and update it whenever an article is created, renamed, or restructured.

- When an article is renamed in Obsidian, update its **Current vault name** here so links written before the rename still resolve.

- Keep the heading lists in step with the articles — a `#Heading` link is only as good as the heading it targets.

- One row per article. One heading list per article. If it's not here, it doesn't get linked.