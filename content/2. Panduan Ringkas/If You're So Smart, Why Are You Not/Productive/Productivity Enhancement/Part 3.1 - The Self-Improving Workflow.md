---
title: Part 3.1 — The Self-Improving Workflow
draft: false
tags:
  - productive
  - productivity
  - ai
  - workflow
  - systems
date: 2026-05-30
---
> [!abstract] This is **Part 3 of 7** in the Productivity Enhancement Series
>
> - **Part 1 — Foundation:** [[Part 1.0 - The Productivity Stack|The Productivity Stack]] · [[Part 1.1 - The Enemy of Productivity|The Enemy of Productivity]]
> - **Part 2 — The Physical Layer:** [[Part 2.0 - The Machine and the Room|The Machine and the Room]]
> - **Part 3 — The Workflow Engine (2 sub-articles):**
> 	- **Part 3.0:** [[Part 3.0 - The Workflow Engine|The Workflow Engine]] (the five-step loop)
> 	- **Part 3.1 (this article):** [[Part 3.1 - The Self-Improving Workflow|The Self-Improving Workflow]] (feedback once, the task gets permanently sharper)
> - **Part 4 — The Knowledge System:** [[Part 4.0 - PARA|PARA]] · [[Part 4.1 - Progressive Summarization|Progressive Summarisation]] · [[Part 4.2 - The Operating System|The Operating System]]
> - **Part 5 — The Tactical Toolkit:** [[Part 5.0 - The Tactical Toolkit|The Tactical Toolkit]]
> - **Part 6 — JIT Project Management:** [[Part 6.0 - Just-in-Time Project Management|Just-in-Time Project Management]]
> - **Part 7 — AI as a Worker:** [[Part 7.0 - The Agentic AI Framework|The Agentic AI Framework]] · [[Part 7.1 - From Chat to Continuous Worker|From Chat to Continuous Worker]] · [[Part 7.2 - Persistent Memory|Persistent Memory]]
> ----
## Table of Contents

- [The problem: you keep giving the same feedback](#the-problem-you-keep-giving-the-same-feedback)
- [The fix: write the correction down where the AI reads it](#the-fix-write-the-correction-down-where-the-ai-reads-it)
- [The two files: context and procedure](#the-two-files-context-and-procedure)
- [The loop: do, correct, save, improve](#the-loop-do-correct-save-improve)
- [A worked example: this blog](#a-worked-example-this-blog)
- [What to put where](#what-to-put-where)
- [Part 3 Takeaways](#part-3-takeaways)
- [Your Self-Improving Workflow Task List](#your-self-improving-workflow-task-list)
- [Sources & references](#sources--references)

---

> [!important] The problem: you keep giving the same feedback
> Here's the failure that makes AI feel like more work, not less. You ask it to draft something, it gets the format wrong, you correct it, you get a usable result. Tomorrow you ask for the same kind of thing, and it makes ==the exact same mistake again==, because the chat from yesterday is gone. You are re-teaching the same lesson every single session. The fix is not a better prompt. It's giving the AI a *memory of your corrections* that survives between sessions, so feedback you give once is feedback the system keeps. That is the self-improving workflow, and it's the single highest-leverage habit in this entire series.

---
## The fix: write the correction down where the AI reads it

The whole trick is one sentence: ==when the AI gets something wrong, don't just fix the output, fix the *instructions*, by writing the correction into a file the AI reads at the start of every task.==

A normal correction lives in the chat and dies with it. A *durable* correction lives in a file that gets loaded into the AI's context every time, so the next run starts from the corrected version. The chat is RAM (wiped each session); these files are disk (they persist). You're moving your hard-won feedback from RAM to disk.

This connects directly to the [[Part 3.0 - The Workflow Engine|workflow loop]]: the *Reflect* step isn't only for your task lists, it's for your instructions too. Every time a repeatable task goes wrong, the reflection is "what should I write down so this never happens again?"

---
## The two files: context and procedure

You need two kinds of file, because there are two kinds of thing the AI keeps not knowing.

> [!check] The two artifacts
> - **Project instructions — the standing context.** The always-on facts about *you* and *your situation* that should colour everything: who you are, your role, your audience, your hard preferences, your constraints, your tone. This is loaded into every task in that project. In Claude this is a Project's custom instructions; the same idea exists as a workspace's system prompt or a "rules" file.
> - **A skill (or `skills.md`) — the reusable procedure.** The step-by-step how-to for one *specific repeatable task*: "how I write a LinkedIn post," "how I prepare the weekly supplement reorder," "how I format an invoice email." Loaded when that task comes up.[^skills]

The division is simple and worth getting right: ==**project instructions answer "who am I and what do I always care about"; a skill answers "how do I do this specific thing."**== Context is about *you*; procedure is about *the task*. Mixing them makes both bloated and vague. Your tone preference is context (it applies to everything you write). The exact section order of your weekly report is procedure (it applies to that one task).

---
## The loop: do, correct, save, improve

The mechanism is a four-step loop wrapped around any repeatable task:

1. **Do.** Run the task with whatever instructions you have so far. The first time, they'll be thin. Fine.
2. **Correct.** When the output is wrong, fix it the way you always would, in the chat.
3. **Save.** Here's the step everyone misses: ask the AI to *write that correction back* into the right file. "Add to my skill: section headers should be declarative statements, never questions." Now it's on disk.
4. **Improve.** Next run, the task starts from the upgraded instructions. The mistake doesn't recur. You give *new* feedback, which also gets saved.

> [!tip] The compounding is the whole point
> Each pass, the instructions get a little sharper and the corrections get fewer. ==A task you fought with in January runs almost untouched by March, not because the AI got smarter, but because your instructions did.== This is compounding applied to workflow: small saved corrections accumulate into a procedure so precise that the task essentially runs itself. An un-saved correction is linear (you pay it every time); a saved correction is a one-time cost with a permanent payoff.

> [!warning] You have to actually do step 3
> The reason most people don't get the compounding is that they stop at step 2. They fix the output, feel the small satisfaction of a good result, and never write it down. Make "save the correction" a reflex. If you find yourself typing a correction you've typed before, that's the alarm: it should have been saved the first time.

---
## A worked example: this blog

This is not hypothetical; it's how these very articles get written. The standing context lives in **project instructions**: that I write a personal blog, the section structure, who the reader is. The repeatable procedure for "write a blog article in my style" lives in a **skill**: the frontmatter format, the abstract-callout-then-TOC opener, the use of Obsidian callouts and `==highlights==`, the Takeaways-and-Task-List ending.

Then corrections got saved, and the procedure sharpened:

- Early drafts leaned on em-dashes in the prose. The correction ("in body prose use parentheses, colons, or sentence splits; keep em-dashes only in titles and labels") was written into the rules, not just fixed once. Every draft since starts with that constraint already applied.[^emdash]
- Early drafts sometimes wrote "you" to mean *me, the author* ("you asked for a better term"). The correction ("in published articles, 'you' is always the reader, never the author or the drafting chat") got saved as a standing voice rule.[^reader]

The result is exactly the compounding above: the things I used to correct on every article, I now never correct, because the instruction caught them before they were written. ==The blog didn't get a better writer; it got better instructions.== Your own version might be a sales-email skill, a meeting-notes skill, or a code-review skill. The mechanism is identical.

---
## What to put where

A quick reference for the boundary, because getting it right is most of the value.

| Goes in **project instructions** (context: about you) | Goes in a **skill** (procedure: about the task) |
|---|---|
| Your role, business, and audience | The exact steps to produce one deliverable |
| Tone and voice preferences (apply to everything) | The required format / template for that deliverable |
| Hard constraints and things to never do | Task-specific do's and don'ts |
| Standing facts about your situation | The checklist you run before calling it done |

And one thing goes in *neither*: long-lived, evolving knowledge about your world (people, projects, decisions, history) belongs in **persistent memory**, the agent's long-term store, which is [[Part 7.2 - Persistent Memory|Part 7.2]]. The rule of thumb: project instructions are *small and stable*, skills are *procedural and per-task*, and memory is *large and growing*. Keep them in their lanes and each stays useful.

> [!note] This is the Context node, previewed
> When you reach [[Part 7.0 - The Agentic AI Framework|Part 7.0]], you'll see "Context" as a formal stage in the agentic pipeline: the dynamic information injected into the model so it makes better decisions. The self-improving workflow *is* context engineering, done by hand, on the small scale of a single repeatable task. Master it here on one workflow and the whole agentic layer in Part 7 becomes obvious.

*Here's the whole self-improving loop as one memory bench: the chat drawn as a volatile RAM rail that wipes every session, the files as a persistent disk rail that only ever gains chips, and the hero between them is the [[Part 3.1 - The Self-Improving Workflow#The loop: do, correct, save, improve|SAVE]] latch that copies a correction down to disk (the step everyone skips). The disk splits into the two banks from [[Part 3.1 - The Self-Improving Workflow#The two files: context and procedure|context and procedure]] (project instructions about you, a skill about the task), the right-hand meter shows corrections decaying run over run (the model didn't improve, the instructions did), and the lower dock carries this blog's own saved rules from [[Part 3.1 - The Self-Improving Workflow#A worked example: this blog|the worked example]]. Its one red mark is the unsaved fix that re-emerges identical next session, so pin it up: an unsaved correction is a tax, a saved one is an asset.*

![[Poster — Productive - Productivity Enhancement Part 3.1 - The Self-Improving Workflow.png]]

---
> [!check] Part 3 Takeaways
> - The reason AI feels like more work is that **corrections die with the chat**. You re-teach the same lesson every session.
> - The fix: when the AI gets something wrong, **fix the instructions, not just the output**, by writing the correction into a file it reads every time.
> - Two artifacts: **project instructions** (standing context about you) and **skills** (reusable procedure for one task). Context is about you; procedure is about the task.
> - The loop is **Do → Correct → Save → Improve.** The missed step is *Save*; make it a reflex.
> - Saved corrections **compound**: a task you fought in January runs itself by March, because the instructions got sharper, not the model.
> - Evolving knowledge about your world goes in **persistent memory** ([[Part 7.2 - Persistent Memory|Part 7.2]]), not instructions. Keep the three lanes separate.

---
## Your Self-Improving Workflow Task List

> [!todo] This week
> - [ ] Pick the one AI task you repeat most and where you keep giving the same feedback.
> - [ ] Write a first **project instruction**: three lines on who you are, your audience, and your tone.
> - [ ] Start a **skill** for that task: the format and the steps, even if rough.
> - [ ] Next time you correct the output, do step 3 out loud: "save that to my skill so it sticks."
> - [ ] In two weeks, check whether the corrections are getting fewer. If they are, the loop is working; if not, you're skipping the Save step.

---
## Sources & references

[^skills]: The "skill" / `skills.md` pattern (a reusable, model-readable procedure file) and standing project instructions are features of modern AI assistants such as Claude (Projects custom instructions; Agent Skills / `CLAUDE.md`-style instruction files). The principle is tool-agnostic: any system that lets you persist instructions the model loads each session supports the same self-improving loop.
[^emdash]: A real example from this blog's own saved rules: em-dashes are kept out of body prose (parentheses, colons, and sentence splits are used instead) and reserved for titles, group labels, and citations.
[^reader]: A second saved rule: in published articles the second-person "you" always addresses the reader, never the author or the private drafting conversation. Both rules were corrections that were written back into the instructions once and have applied automatically since.
