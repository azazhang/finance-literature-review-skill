---
name: finance-literature-review
description: Conduct finance-first literature reviews and related-work synthesis. Use when the user asks for a literature review, related literature section, annotated bibliography, gap map, journal-targeted reading list, finance or macro-finance paper scan, corporate finance or asset-pricing synthesis, banking or disclosure literature summary, or adjacent economics / accounting review. Prioritize top finance journals first, then adjacent top economics and accounting journals, then clearly labeled working papers from NBER, CEPR, SSRN, and RePEc.
metadata:
  version: 0.1.0
  domain: finance
---

# Finance Literature Review

## What This Skill Does

This skill turns a broad literature request into a disciplined finance research workflow:

1. scope the question,
2. define the venue ladder,
3. collect and verify sources,
4. extract finance-relevant study attributes,
5. synthesize by mechanism and design,
6. produce a reading list, matrix, and gap statement.

## When To Use

Use this skill when the user wants:

- a literature review or related literature section,
- an annotated bibliography,
- a finance reading list,
- a working-paper scan,
- a referee-style map of the literature,
- a thesis / dissertation literature chapter start,
- a topic scan across finance, economics, and accounting.

## Hard Rules

- Never fabricate citations or metadata.
- Always separate published papers from working papers.
- Prefer top finance journals first.
- Only widen to adjacent economics or accounting journals when they are genuinely relevant to the question.
- For empirical papers, capture sample, period, unit of observation, identification strategy, key result, mechanism, and main limitation.
- If only titles or abstracts are available, say so directly.

## Default Source Order

1. Published top finance journals.
2. Adjacent top economics journals.
3. Top accounting journals when the topic overlaps disclosure, reporting, auditing, governance, or information environment.
4. Working-paper outlets: NBER, CEPR, SSRN, RePEc / IDEAS.
5. Broad metadata indices and cross-disciplinary sources.

See [references/journal-priority.md](references/journal-priority.md).

## Workflow

### Step 1: Scope The Review

Clarify:

- topic,
- subfield,
- mechanism,
- geography,
- sample period,
- whether the user wants published-only or frontier coverage,
- final output type.

If the request is vague, ask the smallest number of scoping questions needed to fix the venue ladder and the search terms.

### Step 2: Build A Search Grid

Define:

- core concepts,
- finance-specific synonyms,
- adjacent economics / accounting terms,
- method terms,
- regulation / event names,
- dataset names,
- frontier working-paper outlets.

### Step 3: Collect Sources

Prioritize seminal published papers first, then recent papers, then frontier working papers.

Do not let frontier working papers crowd out the canonical published literature in a mature area.

### Step 4: Extract A Finance Matrix

Use the matrix template in [templates/literature-matrix.md](templates/literature-matrix.md).

For each important paper, capture:

- citation,
- venue tier,
- published vs working paper,
- research question,
- sample and period,
- unit of observation,
- identification strategy,
- key finding,
- mechanism,
- main limitation,
- why it matters for the user's question.

### Step 5: Synthesize

Prefer synthesis by:

- mechanism,
- identification strategy,
- sample or institutional setting,
- consistency vs disagreement in results,
- published evidence vs frontier evidence.

Avoid paper-by-paper summaries unless the user explicitly asks for them.

### Step 6: Deliver

Default deliverables:

- scoped review question,
- prioritized reading list,
- literature matrix,
- synthesis,
- research gaps,
- citation block.

## Finance-Specific Heuristics

- If the topic is asset pricing, keep theory, empirics, and measurement separate.
- If the topic is corporate finance, separate mechanism papers from reduced-form identification papers.
- If the topic is banking or macro-finance, be explicit about policy regime and sample window.
- If the topic overlaps accounting, flag whether the evidence is about disclosure, reporting quality, auditing, or governance.
- If a result is still mostly a working-paper literature, say that the evidence base is provisional.

## Optional Tooling

- Use Zotero if a structured citation library is available.
- Use metadata APIs or official journal pages before relying on scraped summaries.
- Use PDF extraction only when the text is actually needed for design or mechanism verification.
