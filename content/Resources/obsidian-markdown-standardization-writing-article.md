---
title: Obsidian Markdown Standardization for Articles
draft: true
tags:
date: 2026-05-24
Purpose: Strict spec for formatting long-form essays in the Nadeem house style
---

derived-from: Fit Series Parts 1.1, 1.2, 2.0, 3.1, 4.0

pair-with: nadeems-writing-personality, obsidian-vault-article-registry


# Obsidian Markdown Standardization — Writing an Article

  

This is the structural spec. Every article follows the same skeleton, uses the same callouts, the same emphasis stack, and the same end-of-article blocks. Voice rules live in [[nadeems-writing-personality]]; this file is purely about form. Canonical filenames and headings — the targets every wikilink points at — live in [[obsidian-vault-article-registry]].

  

> [!important] Read this whole file before drafting a new series part

> The skeleton is rigid on purpose. Predictable structure lets the voice carry the load.

  

---

  

## Table of Contents

  

- [[#The article skeleton|The article skeleton]]

- [[#Series banner|Series banner]]

- [[#Table of contents|Table of contents]]

- [[#Headers and hierarchy|Headers and hierarchy]]

- [[#Callout taxonomy|Callout taxonomy]]

- [[#Emphasis stack|Emphasis stack]]

- [[#Tables|Tables]]

- [[#Math notation|Math notation]]

- [[#Diagnostic decision-tree pattern|Diagnostic decision-tree pattern]]

- [[#Tiers and branches|Tiers and branches]]

- [[#Wikilinks|Wikilinks]]

- [[#Image embeds|Image embeds]]

- [[#Footnotes and citations|Footnotes and citations]]

- [[#End-of-article blocks|End-of-article blocks]]

- [[#Slug and filename rules|Slug and filename rules]]

- [[#Naming convention|Naming convention]]

- [[#Title Selection Protocol|Title Selection Protocol]]

- [[#Reference Integrity Protocol|Reference Integrity Protocol]]

- [[#The full template|The full template]]

  

---

  

## The article skeleton

  

Every part follows this order. No skipping, no reordering.

  

1. **Series banner** — `> [!abstract]` callout with the full series map.

2. `----` horizontal rule.

3. `## Table of Contents` — anchor/wikilink list of all H2s and load-bearing H3s.

4. `---` horizontal rule.

5. **(Optional) Top-of-article disclaimer** — only if scope warrants it (e.g., the Part 2 work-from-home caveat, the Part 4 pharmacology framing).

6. **Bridge paragraph** — what the prior part established, what this part adds. Ends with a thesis sentence.

7. **Main concepts** under H2s and H3s. Mechanism → example → table or callout.

8. **Practical protocol or framework** — the executable middle section.

9. `---` horizontal rule before the wrap-up.

10. `## Part X.Y Takeaways` — always a `> [!check]` callout with 5–7 bolded items.

11. `## Your [Scope] Task List` — numbered, action-verb-first.

12. `> [!note] Up next` — wikilinks to subsequent parts.

13. `---` horizontal rule.

14. `> [!warning] Disclaimer` — same boilerplate, scope-adjusted.

15. `---` horizontal rule.

16. `## Sources & references` — footnotes with named studies and linked sources.

  

---

  

## Series banner

  

Every part opens with this exact pattern. Update the "this article" marker per part.

  

```markdown

> [!abstract] This is **Part X of N** in the Fit Series. The full path:

>

> - **Part 1 - The Goal (2 sub-articles):**

>   - **Part 1.1:** [[Fit Part 1.1 - What Actually Matters|What Actually Matters]]

>   - **Part 1.2 (this article):** [[Fit Part 1.2 - Recomp, Cut or Bulk - How to Actually Decide|Recomp, Cut or Bulk]]

> - **Part 2:** [[Fit Part 2.0 - Structure of a Day|Structure of a Day]] - one-line summary

> - **Part 3 - The Program (3 sub-articles):**

>     - **Part 3.1:** [[Fit Part 3.1 - The Program - Concepts|Concepts]] - one-line summary

>     - **Part 3.2:** [[Fit Part 3.2 - The Program - Rules and Building the Program|Rules]] - one-line summary

>     - **Part 3.3:** [[Fit Part 3.3 - The Program - Example Programs|Examples]] - one-line summary

> - **Part 4:** [[Fit Part 4.0 - Pharmacology|Pharmacology]] - one-line summary

> ----

```

  

Rules:

  

- Use `> [!abstract]`, not any other callout type, for the banner.

- The current article is marked with `(this article)` after its part number.

- Use full Obsidian wikilink form `[[Full Filename|Display Text]]`. Every filename carries the **series prefix** (`Fit Part 3.1 - …`) and is looked up in [[obsidian-vault-article-registry]] — never type a filename from memory. The example above uses the Fit series; swap in the series you're writing.

- One-line summaries after each top-level part are optional but recommended once the part exists.

- Terminate with `> ----` inside the callout (four hyphens) for visual closure.

  

---

  

## Table of contents

  

Immediately after the banner. Use H2 `## Table of Contents`, then a flat bullet list of **heading-wikilinks** — never markdown anchor links.

  

> [!warning] Do not use `[Text](#slug)` anchor links in the TOC

> A markdown anchor link resolves against the *current page URL*, so the moment the article is viewed or exported outside Obsidian it becomes a broken link like `https://.../local_sessions/…#section-name`. Obsidian heading-wikilinks resolve against the note graph instead — they survive export, and they survive renames. Always use the wikilink form below.

  

```markdown

## Table of Contents

- [[#Section name|Section name]]                          <!-- same-article: omit the filename before # -->

- [[#Subsection name|Subsection name]]

- [[Fit Part 4.0 - Pharmacology#Section name|Display]]    <!-- cross-article: full canonical filename before # -->

```

  

Rules:

  

- **Same-article entries use the `[[#Heading|Display]]` shortcut** — no filename before the `#`. This is rename-proof: it follows the note no matter what the file is called.

- **Cross-article entries use the full `[[Filename#Heading|Display]]` form** — with the exact canonical filename, looked up in [[obsidian-vault-article-registry]], before the `#`.

- **Text after `#` is the heading verbatim**, not a slug. `[[#The sliding scale: miniaturization → fibrosis|The sliding scale]]` — colons, em-dashes, and arrows are all fine. (Avoid `#`, `|`, `^`, `[`, `]` *inside* a heading you intend to link to.)

- The display text after the `|` is normally identical to the heading; shorten it only when the heading is long.

- Include all H2s. Include H3s only when they're load-bearing (decision branches, KPI tables, key definitions). Indent H3 entries one level under their parent H2.

- Terminate the TOC with `---` horizontal rule before the bridge paragraph.

  

---

  

## Headers and hierarchy

  

- `# H1` — only for the article title, and only if not using YAML frontmatter title. In practice, the title comes from the filename via Obsidian, so H1 is usually skipped inside the body.

- `## H2` — primary sections (~5–10 per article).

- `### H3` — subsections within an H2 (~2–4 per H2 when needed).

- `#### H4` — used rarely, only for sub-sub-classifications (e.g., currency-of-effect groupings inside a Tier).

- No `#####` or deeper. If you're reaching for H5, restructure.

  

Headers are sentence case, not title case. Em-dashes inside headers are allowed and encouraged for two-clause headers: `## Fatigue vs. stimulus — the core economy`.

  

---

  

## Callout taxonomy

  

Callouts do load-bearing structural work. Each type has a specific job. Don't substitute.

  

| Callout | When to use | Example |

|---|---|---|

| `> [!abstract]` | Series banner at top of every article | *"This is Part 1 of 4..."* |

| `> [!NOTE]` | Soft segues, cross-references to other parts, "up next" handoffs | *"Up next: Part 1.2 — How to Actually Decide"* |

| `> [!tip]` | The practical play — the cheapest/easiest way to apply the concept | *"Use a daily home scale for trend tracking, and get a DEXA scan every 3–6 months."* |

| `> [!important]` | Non-negotiables, hard rules, conceptual reframes | *"MRV is individual."* / *"Don't lean bulk until lean enough to see your abs."* |

| `> [!warning]` | Traps, risks, the closing article disclaimer | *"The trap"* / *"Disclaimer: Not medical advice"* |

| `> [!info]` | Mechanism explainers and definitions that need standalone framing | *"The GLUT4 mechanism"* |

| `> [!check]` | The Takeaways block — always 5–7 bolded items | *"Key concepts to internalize"* |

| `> [!GOAL]` | Framing the target of a phase or section (used in the diagnostic tree) | *"Losing 0.5–1.0% body fat per week while maintaining strength."* |

| `> [!quote]` | Pedant-soothers and side commentary that's slightly cheeky | *"PS to the pedants..."* |

| `> [!danger]` | Reserved for the largest traps where the consequence is severe | *"Fake progressive overload"* |

  

Rules:

  

- Callout type names are case-sensitive in Obsidian. Use the casing in the table.

- A callout always has a **header line** after the type marker: `> [!tip] The practical play` — the body of the callout then starts on the next line with `> ` continuation.

- Callouts must not nest more than one level. If you find yourself nesting, the inner callout probably wants to be plain prose.

- Don't put `==highlight==` inside callouts. The callout already carries the emphasis.

- Don't end an article in a callout. Always close with the Sources & References H2 below all callouts.

  

---

  

## Emphasis stack

  

Three levels, used distinctly:

  

| Mark | Job | Frequency |

|---|---|---|

| `==highlight==` | The single sentence the reader must survive forgetting | **1–3 per article maximum** |

| `**bold**` | Term-of-art labels, proper nouns, the first appearance of named concepts, list-item leads | Liberal |

| `*italic*` | Asides, soft framing, *"the *what*"* contrast pairings, foreign words | Moderate |

  

Rules:

  

- `==highlight==` is for *concepts*, not *examples*. Highlight the rule, not the demonstration.

- **Bold** is also used for the leading term of every bullet in a Takeaways or Task List block: `**True weight:** Daily weight is noise.`

- *Italic* is preferred over **bold** for emphasis inside running prose — bold is reserved for first-mentions and labels.

- Never combine `**==bold-and-highlight==**`. Pick one.

- Never use `_underscore italic_` — always asterisks. Consistency matters for downstream tooling.

  

---

  

## Tables

  

Standard markdown tables for any numerical reference. Two patterns recur:

  

**Pattern 1 — Multi-tier KPI table** (used for strength standards, body fat bands, etc.):

  

```markdown

|Lift|Beginner|Intermediate|Advanced|Elite|

|---|---|---|---|---|

|**Bench Press**|0.5× BW|1.0× BW|1.5× BW|2.0× BW|

```

  

**Pattern 2 — Two-column lookup table** (used for KPIs paired with targets):

  

```markdown

| Metric         | Target                                              |

| -------------- | --------------------------------------------------- |

| Body Fat %     | Men: 10–14% (lean, visible abs) → sub-10% (stage). |

```

  

Rules:

  

- First column is always **bold** when it's a label/proper noun.

- Use `×` (multiplication sign), not `x`, for ratios.

- Use en-dashes `–` for ranges (`10–14%`), not hyphens `-`.

- Right-pad cells with spaces for source readability — Obsidian renders fine either way, but the raw markdown is friendlier to read.

- Don't use tables for fewer than three rows of data. A short list of two items is prose.

  

---

  

## Math notation

  

Use LaTeX-style math with double-dollar delimiters for block equations:

  

```markdown

$$\text{FFMI} = \frac{\text{Lean Mass (kg)}}{\text{Height (m)}^2}$$

```

  

Rules:

  

- Block math (`$$...$$`) is preferred for formulas the reader will reference back to.

- Inline math (`$x$`) is acceptable for single variables in flowing prose.

- Always immediately follow a formula with a plain-English restatement: *"Or equivalently: take your total weight, subtract the fat mass, divide by height in meters squared."*

- Worked example follows the restatement, with a concrete number: *"An 80 kg man at 15% body fat has 68 kg of lean mass — at 1.78 m, that's an FFMI of 21.5. Solidly intermediate."*

  

---

  

## Diagnostic decision-tree pattern

  

This is one of the most distinctive structural patterns. Used wherever the reader needs to troubleshoot a stalled phase or pick a direction.

  

```markdown

### Branch N: [Phase name]

  

> [!GOAL]

> **[The target of this phase, one sentence.]**

  

- **Symptom:** [Observable thing the reader will see.]

    - *Diagnosis:* [What that symptom actually means.]

    - *Action:* [Specific change to make, with numbers where possible.]

  

- **Symptom:** [Next scenario.]

    - *Diagnosis:* [...]

    - *Action:* [...]

```

  

Rules:

  

- Always three branches minimum when this pattern appears — one branch in isolation looks weak.

- Each branch opens with a `> [!GOAL]` callout stating the target.

- Each scenario is exactly: **Symptom → Diagnosis → Action**.

- Action items contain specific numbers (kcal, kg, %, weeks) whenever possible.

- Don't use this for taxonomies. Use it only for *troubleshooting* — when the reader has a known state and needs the next move.

  

---

  

## Tiers and branches

  

Two recurring numbering patterns:

  

**Tiers** — when classifying tools or methods by quality, cost, or risk:

  

```markdown

1. **Tier 1 — [Label]** [Description]

    2. **Margin of error / cost / property:** [details]

3. **Tier 2 — [Label]** [Description]

4. **Tier 3 — [Label]** [Description]

```

  

Example: scanner tiers in Part 1.1 (consumer → commercial → DEXA), supplement tiers in Part 4.0 (Natty → Half-Natty).

  

**Branches** — when classifying decision states or phases:

  

```markdown

### Branch 1: [Phase name]

### Branch 2: [Phase name]

### Branch 3: [Phase name]

```

  

Example: the diagnostic decision tree in Part 1.1 (Cut / Bulk / Performance).

  

Tiers are nested-numbered (parent → sub-properties). Branches are top-level H3s with their own structure inside. Don't mix them.

  

---

  

## Wikilinks

  

Always use Obsidian double-bracket wikilinks for internal references:

  

```markdown

[[Fit Part 1.1 - What Actually Matters|Display Text Here]]

[[Fit Part 1.2 - Recomp, Cut or Bulk - How to Actually Decide#Rule 1 Understand "true weight"|Rule 1]]

```

  

Rules:

  

- The pre-pipe portion is the **exact canonical filename** (without `.md`), series prefix included — looked up in [[obsidian-vault-article-registry]], never typed from memory. See [[#Reference Integrity Protocol|Reference Integrity Protocol]].

- The post-pipe portion is the **display text** as it should appear in prose.

- For cross-article jumps to a specific section, use `[[Filename#Section Heading|Display]]`, with the heading text verbatim.

- For a jump *within the same article*, drop the filename: `[[#Section Heading|Display]]`.

- Filename slugs use spaces, hyphens, and `.` — but **never apostrophes or commas**. See [[#Slug and filename rules|Slug and filename rules]].

- External URLs use standard markdown `[text](url)` — never wikilinks.

  

---

  

## Image embeds

  

Obsidian embed syntax:

  

```markdown

![[Pasted image 20260430184219.png]]

```

  

Rules:

  

- Images live in the same vault and are referenced by filename only — no path.

- Default name (`Pasted image YYYYMMDDHHMMSS.png`) is acceptable but ideally rename to a descriptive slug: `![[ffmi-curve-natural-lifters.png]]`.

- Captions are not part of the embed syntax — write the caption as a plain `*italic*` line directly below the embed.

- Don't wrap images in callouts.

  

---

  

## Footnotes and citations

  

Two equivalent footnote conventions appear in the corpus. Pick one per article and stay consistent.

  

**Style A — Obsidian native footnotes** (preferred for new articles):

  

```markdown

... improving training output.[^4]

  

[^4]: L-Carnitine and fatty acid transport into mitochondria: well-established biochemistry; clinical fat loss outcomes are mixed.

```

  

**Style B — Manual numbered references** (used when migrating from another platform):

  

```markdown

... improving training output.[[4]](#fn-4)

  

## Sources & references

4. L-Carnitine and fatty acid transport... [↩︎](#fnref-4)

```

  

Rules for the footnote *content*:

  

- Open with the **claim or topic in plain words**, not a bare URL.

- Name the author and year for studies: *"Looney et al. (2025), comparison of InBody to DEXA..."*

- Link to the most authoritative source: peer-reviewed paper > clinical org page > reputable secondary explainer.

- Format external links as `[domain.com — short title](URL)` so the source is visible in the link itself.

- Multiple sources in one footnote is fine; separate with " and " or semicolons.

  

---

  

## End-of-article blocks

  

The wrap-up is rigid. In order:

  

### 1. The Takeaways block

  

```markdown

## Part X.Y Takeaways

> [!check] Key concepts to internalize

>

> - **[Label term]:** [one-sentence concept].

> - **[Label term]:** [one-sentence concept].

> - ... (5–7 items total)

```

  

Rules:

  

- Always 5–7 items. Fewer feels thin; more dilutes the signal.

- Each item leads with a **bold label** then a colon then the concept.

- Items are full sentences, not fragments.

- The label term is reusable vocabulary — use the same label that was bolded on first appearance in the body.

  

### 2. The Task List

  

```markdown

## Your [Scope] Task List

[One-sentence framing of why this list exists.]

  

1. **[Action verb + object]** — [detail, including specific tool or threshold].

2. **[Action verb + object]** — [detail].

... (typically 5–9 items)

```

  

Rules:

  

- Scope label matches the article's timeframe: "Day 1", "Week 1–2", "Daily", "Concept-to-Action", "Tier-1 Stack".

- Every item starts with a **bolded action verb in imperative form**: "Get Scanned", "Estimate starting TDEE", "Weigh in every morning".

- Tool names inside items are also bolded: `**Hevy**`, `**MacroFactor**`, `**InBody**`.

- Item descriptions are specific — include thresholds, frequencies, or methods.

  

### 3. Up next callout

  

```markdown

> [!note] Up next

> For [X], go to [[<Series> Part Y - ...|Display]].

>

> To skip ahead to [Z], go to [[<Series> Part W - ...|Display]].

```

  

Rules:

  

- Always link to *all* subsequent parts the reader might jump to, not just the immediate next.

- The immediate next part is the first link.

- Keep this short — 1–3 lines.

  

### 4. Disclaimer

  

```markdown

> [!warning] Disclaimer

> Not medical advice. Everything here reflects personal experience and reading of the research. Consult a medical professional before making significant changes to diet, training, or supplement protocol — especially with underlying health conditions.

```

  

Rules:

  

- The base wording above is the default. Adjust scope words ("diet, training, or supplement protocol") to fit the article topic.

- For Tier 2 pharmacology articles, the disclaimer is heavier and names the specific risk class (see Part 4.0 closing disclaimer).

  

### 5. Sources & References

  

```markdown

## Sources & references

[^1]: [Source one]

[^2]: [Source two]

```

  

Or for Style B:

  

```markdown

## Sources & references

1. [Source one] [↩︎](#fnref-1)

2. [Source two] [↩︎](#fnref-2)

```

  

Always the final block. Nothing after it.

  

---

  

## Slug and filename rules

  

This is where most cross-link breakage comes from. Strict rules:

  

- **No apostrophes** in filenames. *"If You're So Smart"* → `If-Youre-So-Smart` or `If-You-re-So-Smart` (prefer the former).

- **No commas** in filenames. *"Smart, Why Are You Not"* → `Smart-Why-Are-You-Not`.

- **Hyphens for spaces** at slug level; spaces in display titles only.

- **No `&`, `?`, `#`, `%`, `+`** in filenames — these get URL-encoded and break sharing.

- **`.` is allowed** for part numbering (`Part 1.1`, `Part 2.0`).

- **Keep total slug length under ~80 characters.** Longer slugs get truncated by some link previewers.

  

> [!warning] Apostrophes and commas in URLs

> Technically allowed by RFC 3986, but in practice they break link auto-detection across nearly every chat/forum/markdown renderer. Treat them as forbidden in slugs.

  

For internal anchors (TOC links):

  

- All-lowercase, hyphen-separated, punctuation stripped.

- *"Recomp, Cut or Bulk — How to Decide"* → `#recomp-cut-or-bulk--how-to-decide` (em-dash becomes `--`).

- Test by clicking after publishing — Obsidian's anchor generation has edge cases.

  

---

  

## Naming convention

  

Every article filename follows one pattern:

  

```

<Series> Part X.Y - <Descriptive Title>

```

  

`Hair Part 1.1 - What Actually Matters`, `Fit Part 4.0 - Pharmacology`, `Hair Part 3.0 - What Actually Matters For The Beard`. The series prefix is mandatory; the word "Series" is **not** used (`Hair Part 1.1`, never `Hair Series Part 1.1`).

  

Why the prefix:

  

- **Collision-proofing.** A bare `Part 4.0 - Pharmacology` collides the moment a second series wants a pharmacology part — `[[Part 4.0 - Pharmacology]]` then resolves ambiguously. `Fit Part 4.0 - Pharmacology` is globally unique.

- **Reuse of descriptive titles.** `Hair Part 1.1 - What Actually Matters` and `Fit Part 1.1 - What Actually Matters` coexist cleanly.

- **Auto-sync survives.** Once a link targets the real filename, renaming the file in Obsidian rewrites every link to it automatically. A link to an invented name never gets that benefit — it just stays broken.

  

Within a series, keep a disambiguating suffix where two parts share a stem: `Hair Part 1.1 - What Actually Matters` vs. `Hair Part 3.0 - What Actually Matters For The Beard`.

  

The canonical name for every existing article lives in [[obsidian-vault-article-registry]]. That file is the source of truth; this section is the rule that generates it.

  

---

  

## Title Selection Protocol

  

Titles are decisions, not defaults. For **every new article**, before drafting a single line:

  

1. Propose **2–4 candidate titles** to the author, each with a one-sentence rationale, and mark a recommendation.

2. Each candidate already carries the **series prefix and part number**: `Hair Part 4.0 - <candidate>`.

3. Favor titles **specific enough not to collide** with a plausible future article. "Pharmacology" alone is too broad; the series prefix is what carries it.

4. Once chosen, **register the filename and its headings in [[obsidian-vault-article-registry]]** before writing the body.

  

Never name a new article silently. The cost of a careless title is every future link that has to be hunted down and rewritten.

  

---

  

## Reference Integrity Protocol

  

The rule that keeps links from breaking. Before writing **any** `[[...]]` that points at another article:

  

1. **Look it up in [[obsidian-vault-article-registry]].** Copy the canonical filename verbatim.

2. **If it isn't in the registry** — stop. Don't invent the name. Confirm the exact filename against the live Obsidian vault, or ask the author, then add it to the registry.

3. **For a `#Heading` deep-link** — confirm the heading exists in that article's heading list in the registry, and link it **verbatim** (Obsidian doesn't slugify wikilink headings).

4. **Same-article links** use the `[[#Heading|Display]]` shortcut and skip the registry — but the heading must still exist in this file.

  

> [!important] A wrong reference is invisible until it's clicked

> `[[Fit Series Part 4.0 - Pharmacology]]` looks fine in the raw text and silently fails because the real file is `Fit Part 4.0 - Pharmacology`. The registry exists so this never ships. When in doubt, ask — don't guess a filename.

  

---

  

## The full template

  

Copy this for any new article. Fill in the brackets.

  

```markdown

> [!abstract] This is **Part X of N** in the <Series> Series. The full path:

>

> - **Part 1 - [Section name]:**

>   - **Part 1.1:** [[<Series> Part 1.1 - Filename|Display]]

>   - **Part 1.2:** [[<Series> Part 1.2 - Filename|Display]]

> - **Part 2 (this article):** [[<Series> Part 2.0 - Filename|Display]]

> - **Part 3:** [[<Series> Part 3.0 - Filename|Display]]

> - **Part 4:** [[<Series> Part 4.0 - Filename|Display]]

> ----

  

## Table of Contents

- [[#First H2 section|First H2 section]]

- [[#Second H2 section|Second H2 section]]

- [[#Part X.Y Takeaways|Part X.Y Takeaways]]

- [[#Your Day 1 Task List|Your Day 1 Task List]]   <!-- replace "Day 1" with this article's scope -->

- [[#Sources & references|Sources & references]]

  

---

  

[Bridge paragraph: what the prior part established, what this part adds, thesis sentence.]

  

## First H2 section

  

[Framing sentence — why this section exists.]

  

[Main prose with mechanism. Em-dashes do work. Land on a punchline.]

  

> [!important] [Header for the non-negotiable]

> [Body — the rule, in plain words.]

  

### First H3 subsection

  

[Continued prose. Tables and callouts where they earn their keep.]

  

| Column | Column | Column |

|---|---|---|

| **Label** | data | data |

  

## Second H2 section

  

[Bridge sentence from prior section.]

  

> [!tip] The practical play

> [The cheapest/easiest version of the principle.]

  

---

  

## Part X.Y Takeaways

> [!check] Key concepts to internalize

>

> - **[Term]:** [one-sentence concept].

> - **[Term]:** [one-sentence concept].

> - **[Term]:** [one-sentence concept].

> - **[Term]:** [one-sentence concept].

> - **[Term]:** [one-sentence concept].

  

## Your [Scope] Task List

[One-sentence framing.]

  

1. **[Action verb + object]** — [detail with specific tool or threshold].

2. **[Action verb + object]** — [detail].

3. **[Action verb + object]** — [detail].

4. **[Action verb + object]** — [detail].

5. **[Action verb + object]** — [detail].

  

> [!note] Up next

> For [X], go to [[<Series> Part Y - Filename|Display]].

>

> To skip ahead to [Z], go to [[<Series> Part W - Filename|Display]].

  

---

  

> [!warning] Disclaimer

> Not medical advice. Everything here reflects personal experience and reading of the research. Consult a medical professional before making significant changes to diet, training, or supplement protocol — especially with underlying health conditions.

  

---

  

## Sources & references

[^1]: [Source one — author, year, journal/site. [domain.com — short title](URL)]

[^2]: [Source two]

```

  

---

  

> [!tip] Pair with the voice guide and the registry

> Three files work together. **Voice** — stance, POV, rhythm, what to avoid — lives in [[nadeems-writing-personality]]. **Form** — this file — handles skeleton, callouts, and links. **Targets** — the canonical filenames and headings every link points at — live in [[obsidian-vault-article-registry]]. All three must hold for the writing to read as ours and for the links to resolve.