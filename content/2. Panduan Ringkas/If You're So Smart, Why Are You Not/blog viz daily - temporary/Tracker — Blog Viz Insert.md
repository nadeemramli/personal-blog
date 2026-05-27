---
title: Tracker — Blog Viz Insert
draft: true
tags:
date: 2026-05-27
---
# Tracker — Blog Viz Insert

**What this file is:** the insert task's memory — the final stage of the pipeline, companion to [[Tracker — Blog Viz Poster]]. Each run reads the poster tracker's _Posters produced_ list, checks what's already in _Inserted below_, and for each uninserted poster: reads the viz concept + article, finds the best placement, inserts the poster embed + a brief description, then logs it here. Bookkeeping only, not a blog post (hence `draft: true`).

**The contract (what this task is allowed to do):**
- ✅ Add a short italic description paragraph that **leads** (sits *above*) the poster, derived from the viz concept brief and tied back to the article
- ✅ Add the poster embed (`![[Poster — ....png]]`) directly beneath that description
- ❌ Edit, rewrite, or delete any existing article content
- ❌ Touch anything outside the target article

**Placement logic (how to choose the insertion spot):**
- Read the article fully before deciding. The poster is a *reference card* — it should land after the reader has absorbed the conceptual scaffolding it illustrates, so it clicks immediately.
- "Too early" = the reader hasn't been given enough context yet; the poster will confuse rather than clarify.
- "Too late" = the reader has already moved past the idea; the poster adds nothing.
- The sweet spot is typically: right after the section that *explains* the concept the poster visualizes, but *before* the article moves to a new idea or calls the reader to action.
- Prefer placing inside a section, not at the very end of the article (Takeaways / Task List / Sources sections are off-limits for poster insertion).

**Description format (updated 2026-05-27 — lead with the description, then the poster):**
- **Order:** the italic description comes *first*, the `![[Poster …]]` embed *second*. Lead the reader in so they're oriented before they ever see the poster, rather than explaining it after the fact.
- **Open by framing the poster's purpose** ("Here's a clean way to picture how X works…"), then hand the reader into it.
- **Anchor it to the article with Obsidian links.** Reference the specific points the poster visualizes using heading wikilinks — `[[Note Title#Heading|friendly text]]` — so a reader who jumps to the poster can click straight back to the explanation. Verify each heading target matches the article heading *exactly* (em dashes, colons, quotes, parentheses all count); a one-character mismatch breaks the link. Use the full `[[Note#Heading]]` form, not bare `[[#Heading]]`.
- **Source the wording** from the viz concept brief (§1 Big Idea + §4 Copy) and stay consistent with its language — don't invent new terminology.
- **Length:** ~2–4 sentences. Tell the reader *what the poster is* and *how to use it*; end with a one-line utility statement (e.g., "Pin it up and re-check it every week.").

Scope: this tracker covers the **"If You're So Smart, Why Are You Not"** Big Series only. Each Big Series keeps its own insert tracker beside its poster tracker.

---

## Inserted

| Concept | Poster file | Article | Insertion point | Date |
|---|---|---|---|---|
| [[Visualization Concept — Fit - Part 1.1 - What Actually Matters]] | `Poster — Fit - Part 1.1 - What Actually Matters.png` | `Fit/Aesthetic and Strength/Part 1.1 - What Actually Matters.md` | After the "Ultimately, this is how benchmarking…" summary paragraph that closes the Diagnostic Decision Tree section, before the "The only variable left is execution…" tool-stack paragraph. **Lead-in description (above poster) links back to `#How Benchmarking is Used (The Diagnostic Decision Tree)` and `#Strength and size are linked (for naturals especially)`.** | 2026-05-27 |
| [[Visualization Concept — Fit - Part 1.2 - Recomp, Cut or Bulk]] | `Poster — Fit - Part 1.2 - Recomp, Cut or Bulk.png` | `Fit/Aesthetic and Strength/Part 1.2 - Recomp, Cut or Bulk - How to Actually Decide.md` | After the "…that's the framework" wrap-up sentence ending the "Finding maintenance calories — the 2-week lock-in" section (the deltas Recomp ±0 / Cut −500 / Lean bulk +200–300 just stated), before the `---` divider into The Fitness Forecast. **Lead-in description (above poster) links back to `#Finding maintenance calories — the 2-week lock-in`, `#Rule 1: Understand "true weight"`, and `#The decision tree`.** | 2026-05-27 |

## Pending — poster exists in /visualization/, not yet inserted

- _None._ Both posters in `/visualization/` are now inserted. New entries appear here automatically when [[Tracker — Blog Viz Poster]] adds the next poster (Next up: Fit / Aesthetic & Strength / Part 2.0 — Structure of a Day).

## Notes

- **2026-05-27 fit check — both placements pass.** 1.1 sits between the Diagnostic Decision Tree summary and the tool-stack paragraph; 1.2 sits between the maintenance-framework wrap-up and the Fitness Forecast. Both arrive after the concept is fully explained and before the article moves on.
- **2026-05-27 revision (per author):** flipped both insertions to **lead with the description, poster beneath**, and wired the descriptions back to the articles with heading wikilinks so the reader has context before seeing the poster. Convention updated in the _Description format_ section above. All four heading-link targets verified against the live article headings (exact match incl. em dashes / colons / quotes).
- **2026-05-27 — pre-existing issue, NOT caused by this task (do not auto-fix):** in `Part 1.2`, the transition paragraphs "Now that you have your baseline from Part 1.1…" are duplicated (appear once just before `## The Fitness Forecast` and again as the first lines under it; one wikilink also reads `Part 1.1 - Recomp, Cut, or Bulk - What Actually Matters`, a malformed title). This sits *below* the poster insertion point and was left untouched per the contract. Flagging for manual review.
- **Never re-insert** a poster already listed in _Inserted_ above.
- This file wikilinks [[Tracker — Blog Viz Poster]] and [[Tracker — Blog Viz Daily]]; Obsidian's backlinks make the full three-stage pipeline visible from any node.
- Poster embeds use Obsidian wikilink syntax: `![[Poster — Fit - Part 1.1 - What Actually Matters.png]]`
