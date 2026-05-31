---
title: Part 4.0 — The Learning System
draft: false
tags:
  - successful
  - learning
  - skill-acquisition
  - obsidian
  - system
date: 2026-05-30
---
> [!abstract] This is **Part 4 of 5** in the Learning & Skill Acquisition Series
>
> - **Part 1 — Foundation:**
> 	- **Part 1.0:** [[Part 1.0 - How Learning Actually Happens|How Learning Actually Happens]] (the two layers: physical brain + cognitive map)
> - **Part 2 — Mindset (2 sub-articles):**
> 	- **Part 2.0:** [[Part 2.0 - Mental Models for Learning|Mental Models for Learning]] (the four-step method)
> 	- **Part 2.1:** [[Part 2.1 - Deliberate Practice|Deliberate Practice]] (the mechanism behind step 4)
> - **Part 3 — Behavioural (2 sub-articles):**
> 	- **Part 3.0:** [[Part 3.0 - The Behavioral Protocol|The Behavioral Protocol]] (the day-shape that produces learnable hours)
> 	- **Part 3.1:** [[Part 3.1 - Recovery and NSDR|Recovery and NSDR]] (the consolidation half of the loop)
> - **Part 4 — System:**
> 	- **Part 4.0 (this article):** [[Part 4.0 - The Learning System|The Learning System]] (Obsidian + Excalidraw, structure vs context, the publish workflow)
> - **Part 5 — Chemistry:**
> 	- **Part 5.0:** [[Part 5.0 - Pharmacological Support|Pharmacological Support]] (the learning-specific read of the Cognitive escalation protocol)
> ----
## Table of Contents

- [Why a system at all](#why-a-system-at-all)
- [The split that makes the system work](#the-split-that-makes-the-system-work)
- [Why Obsidian specifically](#why-obsidian-specifically)
- [Excalidraw and Canvas: the structure layer](#excalidraw-and-canvas-the-structure-layer)
- [The publish workflow (the under-rated piece)](#the-publish-workflow-the-under-rated-piece)
- [The deconstruction module (setting up a new skill in the system)](#the-deconstruction-module-setting-up-a-new-skill-in-the-system)
- [The anti-pattern: notes as a substitute for thinking](#the-anti-pattern-notes-as-a-substitute-for-thinking)
- [Part 4 Takeaways](#part-4-takeaways)
- [Your System Task List](#your-system-task-list)
- [Sources & references](#sources--references)

---

> [!important] The system serves the method; the system is not the method
> [[Part 2.0 - Mental Models for Learning|Part 2.0]] gave you the four-step method (history → narrative → root → practice). The system this article describes is a *substrate* for that method: a place to draw the map, capture the context, run the practice loop, and (eventually) share the artefact. ==The system is not a substitute for the method.== An immaculate Obsidian vault built by someone who never sat in [[Part 3.0 - The Behavioral Protocol|a focused block]] is a museum of intentions. Read this article in that order: method first, system second.

---
## Why a system at all

You can learn things without a system. People did, for most of human history. The question is whether you can learn things *cumulatively*, across years, across multiple domains, in a way that compounds rather than evaporates.

The default for almost everyone is that learning evaporates. You read a book and a year later remember the title and the one most-shareable sentence. You complete a course and six months later realise you couldn't pass the final again. You build a working understanding of a domain at work, change jobs, and find it half-gone within a year. This isn't because your brain is broken; it's because ==without a system to externalise the map you built, the map decays at roughly the rate of the underlying cognitive layer.==

The job of a learning system, in one sentence:

> [!check] The system's job
> ==To externalise the map you built in your head so that (a) the map outlives the cognitive trace, (b) you can revise structure later instead of rebuilding it, and (c) future-you can read present-you's reasoning, not just present-you's conclusions.==

A system that does those three things turns scattered hours of learning into compounding capital. A system that doesn't do those three things — a folder of PDFs, a stack of highlighted books, a hundred half-read Kindle samples — is storage, not capital.

---
## The split that makes the system work

The single design decision that makes a learning system actually function (and the one most knowledge-management writing gets wrong) is this:

> [!check] The split
> ==**Structure** and **context** are different artefacts, and they live in different tools.==
> - **Structure** is the shape: how concepts relate, what's central and what's peripheral, what the map looks like. Lives in a **visual canvas** (Excalidraw, Obsidian Canvas).
> - **Context** is the substance: definitions, explanations, examples, edge cases, your own reasoning, links to sources. Lives in **notes** (Obsidian markdown files).

You need both. A canvas without notes is a picture; you can't reason from it. Notes without a canvas are a pile; you can't see what relates to what. The split solves the failure mode of every knowledge-management approach that picks one or the other: pure-text systems (Notion, Roam) become impenetrable as they grow; pure-visual systems (Miro, Whimsical) can't hold real depth.

A *single concept* gets both:
- One Excalidraw or Canvas file showing where this concept sits relative to its neighbours
- A small set of notes holding the actual content (definition, examples, your reasoning, the sources)
- Wiki-links between the two, in both directions

This mirrors how [[Part 1.0 - How Learning Actually Happens|Part 1.0]] described learning itself: the cognitive layer builds a *map* (the structure) and fills it with *semantics* (the context). The split in the system makes that split *visible and editable.*

---
## Why Obsidian specifically

Almost every recommendation in this article would work on any sufficiently flexible note-taking tool. The reason this series recommends Obsidian specifically comes down to three properties, in order of importance:

### 1. Local-first, plain markdown

Your notes are *files on your computer*, in plain markdown. Not in someone's cloud database, not in a proprietary format. This matters for two reasons that don't show up until five years in:

- **You can embed AI against your vault.** Local-first means your notes are *available* to any tool that can read files: AI editors (Cursor, Zed), local LLMs, custom scripts, anything. This is the difference between a vault that *informs* your AI use and a vault that AI use *can't even see*.
- **You can outlive the tool.** Obsidian could disappear tomorrow and your vault is still readable in any text editor, any time, forever. Notion users learn this lesson the hard way every few years; Roam users learned it the hardest way.

### 2. Wiki-links and graph-native structure

The `[[wiki-link]]` is the atomic operation of the system: it lets you connect anything to anything *by name*, without filing it in a hierarchy. The graph view shows the resulting structure. The hierarchy of folders is *optional*; the graph is the actual structure of your knowledge.

This matters for the [[Part 2.0 - Mental Models for Learning|four-step method]] because:
- The **root note** (step 3) is the highest-degree node in the graph for that domain. You can literally *see* it.
- **Context anchors** (the connections to that root) are the edges in the graph.
- New information has a place to go because you link it to existing notes; the graph self-organises around the roots over time.

### 3. The plugin ecosystem (Excalidraw, Canvas, others)

Obsidian's plugin model is what makes the structure-vs-context split *living in one place* possible. Excalidraw runs as a plugin; Canvas is built in; you can open an Excalidraw file and immediately link from a shape on the canvas to a note in your vault, and from a note back to a region of the canvas. The two halves talk to each other.

> [!warning] What Obsidian is not
> Obsidian is not a project-management tool, a calendar, a task manager, or a database in any sophisticated sense. ==Trying to make it those things produces the most frustrated former-Obsidian-users you'll meet.== Use it for the thing it's exceptional at (a personal, queryable, durable knowledge vault) and use other tools for the other jobs.

---
## Excalidraw and Canvas: the structure layer

Excalidraw (handwritten-style infinite canvas, runs as an Obsidian plugin) and Obsidian Canvas (built-in node-and-edge canvas) are the two structure tools. They do slightly different jobs:

- **Excalidraw** is best for *drawing* a map: free-form shapes, arrows, handwritten annotations, the way you'd sketch on a whiteboard. Best for an evolving understanding of a domain, especially in the early "still figuring out the shape" phase.
- **Canvas** is best for *holding* a map of existing notes: cards that *are* your notes, arranged spatially, edges showing relationships. Best once a domain has stabilised and you're maintaining the structure rather than drafting it.

A typical workflow:

> [!check] One concept, one canvas, one set of notes
> 1. **New domain:** open an Excalidraw file. Sketch the shape as you understand it after the [[Part 2.0 - Mental Models for Learning|step-1 history hour]]. Centre = your candidate root note. Branches = the load-bearing concepts.
> 2. **Each concept becomes a note.** Definitions, examples, your reasoning, sources. Link the note back to the Excalidraw file.
> 3. **Refine the structure as it stabilises.** The original Excalidraw sketch gets messy as you learn; redraw it when it does. The *redrawing itself* is unlearning ([[Part 1.0 - How Learning Actually Happens|Part 1.0]]) made physical.
> 4. **Migrate to Canvas when stable.** Once the structure stops changing, move it to an Obsidian Canvas where each node is the actual note. This is the maintained version of the map.

The visible artefact this produces is exactly what [[Part 1.0 - How Learning Actually Happens|Part 1.0]] described as "the cognitive map," but external, editable, and shareable.

---
## The publish workflow (the under-rated piece)

Here's the piece almost nobody talks about, and it changes everything: ==build your blog/site directly on top of the vault.==

The mechanics: Obsidian → static-site generator (Quartz, Astro, Eleventy, etc.) → GitHub repo → push → deployed site. Once the pipeline is set up, the publish flow becomes "open Obsidian, edit a note, set `draft: false`, `git push`, the site updates." (This blog is built exactly this way; the article you're reading right now is a markdown file in a vault that was pushed to a repo.)

Why this is so disproportionately useful:

> [!check] What the publish workflow does
> - **Learning artefact and public artefact are the same file.** You don't write notes for yourself and then *separately* write blog posts for the public. You write notes, and the ones that mature get a `draft: false`. ==The friction between learning and sharing collapses to one bit.==
> - **The social pressure of public notes is a forcing function for clarity.** Notes nobody else will read can be cryptic; notes that might be read by anyone have to make sense. The clarity you're forced to add is the same clarity that benefits *future-you*. The audience is the editor.
> - **You can read your own notes on the go.** Phone, laptop, anywhere. The vault is for editing; the site is for re-reading. The two together give you the full read-write loop wherever you are.
> - **Public notes attract the right corrections.** Someone with deeper expertise in a topic you wrote about will, sometimes, tell you you got it wrong. ==This is the [[Part 1.0 - How Learning Actually Happens|reality-check loop]] running on free, asynchronous, expert-sourced feedback.== It's worth more than most paid courses.

The objection most people raise is that they're "not ready to publish." This is almost always a misreading. You don't have to publish *everything*. You don't have to publish *finished* work. You just have to publish *something*: the notes you'd be willing for someone to see. The threshold "willing for someone to see" is a useful editorial filter; the absence of any such filter is what produces the unreadable vault.

> [!tip] What to publish, what to keep private
> A reasonable default: anything that's reached a stable narrative version (the [[Part 2.0 - Mental Models for Learning|step-2]] retelling, polished) is publishable. Anything still in the messy step-3 or step-4 phase stays in the vault. The site shows the *settled* parts of your map; the vault holds the *working* parts.

---
## The deconstruction module (setting up a new skill in the system)

[[Part 2.0 - Mental Models for Learning|Kaufman's]] Rapid Skill Acquisition principles slot cleanly into the system as a *new-skill setup checklist.* When you decide to acquire a new skill, the system gets a standard scaffold; this is what goes on it.

> [!check] New-skill setup (do this once, the day you commit to a new skill)
> 1. **Choose one lovable, useful project.** Not "learn Spanish." *"Be able to hold a 20-minute conversation with my partner's family in Spanish."* The project gives the practice a target. ==The lovability matters as much as the usefulness; the discomfort budget is finite, and a project you don't actually want to complete burns through it fast.==
> 2. **Deconstruct the skill into sub-skills.** Open Excalidraw. Centre node = the skill. Branches = the 5–10 sub-skills it actually breaks down into. (Spanish: pronunciation, core grammar, top-1000 vocabulary, conversational flow, listening comprehension, cultural context.) The sub-skills don't have to be perfect; they have to be *separately practisable.*
> 3. **Identify critical tools.** What do you need to practise effectively? Apps, books, conversation partners, environment. List them. Acquire them now, before the motivation passes.
> 4. **Remove barriers to practice.** The single biggest predictor of whether you'll practise tomorrow is *how many seconds it takes to start.* Pre-stage the materials. Bookmark the practice site. Charge the device. Put the textbook on the chair you'll sit in. ==Every second of setup is a second the discomfort budget pays for before you've done any practice.==
> 5. **Create feedback loops.** How will you know you're improving? An app's progress bar (weak signal but cheap), a recording you make and compare to a month later (strong signal, slightly expensive), an actual practitioner who can correct you (strongest signal, most expensive). Pick at least one; cheaper-but-real is better than expensive-and-aspirational.
> 6. **Practise by the clock, in short bursts, at the [[Part 3.0 - The Behavioral Protocol|edge of ability]].** The block lives in Part 3.0. The skill setup lives here.

This is six items, takes about an hour the day you decide to start, and reliably collapses the first-week activation energy that kills most skill-acquisition attempts.

---
## The anti-pattern: notes as a substitute for thinking

Every system in this article has the same failure mode, and it's worth naming explicitly because it kills most knowledge-management projects.

==The system can become a substitute for thinking instead of an aid to it.==

The pattern: you read something good. You highlight it. You clip it into the vault. You add tags. You link it to three other notes. You feel productive. You haven't *thought* about it once. The clipping and tagging *felt* like engagement, and your brain pattern-matches the feeling as "I learned this," but you didn't; you just *filed* it.

This shows up everywhere in the productivity-tools subculture: vaults of 10,000 notes built by people who can't summarise a single domain they've supposedly studied; "second brain" workflows where the first brain has gone quiet; weekly reviews of an ever-growing library that gets bigger but not denser. The system is doing the *appearance* of the work; the work itself isn't happening.

The diagnostic:

> [!check] Is the system serving the method, or replacing it?
> - **Serving:** the system holds artefacts of your thinking. The map in Excalidraw is one you can re-draw because *you drew it.* The notes are your own reasoning, not someone else's text. The graph is dense because the connections came from you working through the material.
> - **Replacing:** the system holds clippings, tags, and links to other people's writing. The "map" was inherited from a textbook or a course. The notes are quotes with your highlights. The graph is mostly auto-generated metadata, not earned connections.

The fix is not to delete the system. It's to remember which way the dependency runs: ==the method (Parts 1–3 of this series) is what produces the learning; the system (this article) holds the artefacts.== A vault that holds artefacts of real thinking is invaluable. A vault that holds clippings in lieu of thinking is a museum of intentions.

A simple practical rule: ==for every page of text you *capture* from outside sources, write at least one paragraph of your own response, reasoning, or example.== If you can't write that paragraph, you didn't actually engage with the source; you just filed it. The capture-to-engagement ratio is the most honest measure of whether your system is serving you or the other way around.

---
## Part 4 Takeaways

> [!check] What to carry forward
> - **The system's job is to externalise the map**, so it outlives the cognitive trace, can be revised structurally, and lets future-you read present-you's reasoning.
> - **Structure and context are different artefacts in different tools.** Visual canvas (Excalidraw / Obsidian Canvas) for structure; markdown notes (Obsidian) for context. Each concept gets both.
> - **Obsidian's value is local-first plain markdown, wiki-link graph, and the plugin ecosystem.** Local-first matters more every year; wiki-links are the atomic operation; plugins make the structure-context split live in one place.
> - **The publish workflow is the under-rated piece.** Vault → static site → push. Learning artefact and public artefact are the same file; the social pressure is the editor; corrections from strangers are free expert-sourced reality-checks.
> - **New-skill setup (the deconstruction module): one lovable project, sub-skill breakdown on a canvas, critical tools acquired, barriers removed, feedback loops set, practise by the clock.** Once per new skill, ~1 hour, kills first-week activation energy.
> - **The anti-pattern: notes as a substitute for thinking.** Clipping and tagging feel productive without being thinking. The fix: for every page captured, write at least one paragraph of your own. Capture-to-engagement ratio is the honest measure.
> - **The system serves the method; the system is not the method.** A vault built without the [[Part 2.0 - Mental Models for Learning|four-step method]] and [[Part 3.0 - The Behavioral Protocol|the focused-block day]] is a museum of intentions.

---
## Your System Task List

> [!tip] Stand up the minimum viable system this week
> - **Install Obsidian.** Free. Point it at a new folder. Install the Excalidraw plugin.
> - **Pick one current learning project** (a course, an exam, a new domain, a skill).
> - **Run the new-skill setup once** for that project. One lovable target, sub-skill breakdown in Excalidraw, tools listed, barriers removed.
> - **Write three notes the way the method wants them written.** Not clippings — your own reasoning. One per load-bearing concept. Link them to the Excalidraw canvas in both directions.
> - **Stand up the publish workflow when the vault has 10+ notes.** Quartz is the lowest-friction option for an Obsidian vault → site. Push it to a free Netlify or GitHub Pages account. ==The friction of the *first* publish is high; every subsequent one is `git push`.==
> - **Read [[Part 5.0 - Pharmacological Support|Part 5.0]] next.** It's the chemistry-margin layer, framed as the learning-specific read of the [[Part 4.0 - The Escalation Protocol|Cognitive escalation protocol]].

---
## Sources & references

[^1]: Knowledge graphs and personal knowledge management: the wiki-link / backlink model traces through Niklas Luhmann's *Zettelkasten* (now well-documented in Sönke Ahrens's *How to Take Smart Notes*, 2017). Obsidian, Roam, Logseq, and similar tools all implement variants of the same idea.

[^2]: Josh Kaufman, *The First 20 Hours* (2013), Chapter 1 ("Ten Principles of Rapid Skill Acquisition"). The deconstruction-into-sub-skills and remove-barriers-to-practice items in particular are well-supported by the broader skill-acquisition literature (Ericsson) and behaviour-design literature (BJ Fogg on friction as the primary determinant of habit installation).

[^3]: The "second brain" failure modes: Tiago Forte's *Building a Second Brain* (2022) popularised the term; the critiques (notes as substitute for thinking, capture without engagement) trace through Andy Matuschak's working notes and a substantial subsequent discussion. The capture-to-engagement-ratio diagnostic in this article is the practical distillation.

[^4]: Static-site generators for Obsidian vaults: Quartz (used for this blog; Jacky Zhao, MIT-licensed, currently the lowest-friction option for Obsidian → publishable site). Alternatives include Astro, Eleventy, Hugo, and others. The specific tool matters less than the *workflow* (vault → site → push).

> [!danger] Disclaimer
> The specific tools recommended here (Obsidian, Excalidraw, Quartz) are the ones this blog runs on. ==The split (structure vs context), the publish workflow, and the deconstruction module are tool-agnostic; the specific Obsidian recommendation is replaceable with anything that gives you local-first plain text, wiki-link graphs, and visual canvas support.== If you already have a working system that does those three things, don't switch.
