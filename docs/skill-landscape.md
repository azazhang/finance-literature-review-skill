# Skill Landscape Review

This review was compiled on 2026-04-04 from GitHub repository metadata, public skill files, and official provider documentation.

## Scope And Inclusion Rule

I treated a repo as "major" if at least one of the following held:

- It had clear traction by stars in the current skill / agent ecosystem.
- It was recent and directly focused on literature review or academic research workflows.
- It contained real skill files or command files rather than a marketing-only README.

I excluded obvious mirrors, forks without material changes, and ultra-thin one-file copies unless they added a distinct workflow idea.

## Benchmark Repos

| Repo | Stars | Updated | Why It Matters |
| --- | ---: | --- | --- |
| [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) | 17,352 | 2026-04-05 | The heavyweight reference repo. Broad scientific skill catalog with a dedicated literature-review skill and separate paper-lookup skill. |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | 1,906 | 2026-04-05 | The strongest literature-review-specific academic pipeline I found. Strong orchestration, checkpoints, review modes, and systematic-review references. |
| [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) | 1,389 | 2026-04-05 | Strong writing companion repo that complements research-stage skills. Useful for downstream survey drafting patterns. |
| [ymx10086/ResearchClaw](https://github.com/ymx10086/ResearchClaw) | 244 | 2026-04-05 | A broader personal research assistant ecosystem with extensible skills and literature-review positioning. |
| [wentorai/research-plugins](https://github.com/wentorai/research-plugins) | 180 | 2026-04-04 | Broad plugin collection. Good for seeing packaging breadth, weaker as a canonical workflow reference. |
| [lingzhi227/agent-research-skills](https://github.com/lingzhi227/agent-research-skills) | 24 | 2026-04-03 | Interesting because it carries an explicit survey-generation skill, citation-management skill, and AutoSurvey-inspired writing workflow. |
| [stephenlzc/AI-Powered-Literature-Review-Skills](https://github.com/stephenlzc/AI-Powered-Literature-Review-Skills) | 8 | 2026-04-01 | Low-star but current and directly about literature survey. Useful contrast case for browser-first and bilingual search workflows. |

Star counts and timestamps above were read from the GitHub REST API on 2026-04-04 / 2026-04-05.

## What The Strongest Repos Get Right

### 1. Multi-Stage Workflow Beats One-Shot Prompting

The strongest repos break the task into stages:

- scope the question,
- build a search strategy,
- search multiple sources,
- screen and deduplicate,
- verify metadata,
- synthesize findings,
- review the synthesis.

This is a real best practice. Finance literature reviews also benefit from staged execution because venue quality, identification strategy, and publication status matter.

### 2. Citation Verification Is Mandatory

The best repos treat citations as a separate problem, not an afterthought:

- K-Dense splits literature review from paper lookup and citation management.
- Imbad0202 separates bibliography, source verification, synthesis, and report compilation.
- lingzhi227 has explicit citation validation and BibTeX management steps.

This is essential. Any finance-oriented skill that does not explicitly prevent invented citations is not production-grade.

### 3. Progressive Disclosure Matters

The strongest skills keep the main trigger file concise and push details into references, templates, or scripts. K-Dense does this particularly well.

That pattern is worth keeping because it preserves context window budget and makes the skill maintainable.

### 4. Quality Gates Improve Reliability

Imbad0202's repo is especially strong here:

- checkpoint agents,
- bias review,
- editorial review,
- ethics review,
- capped revision loops.

Even if a finance skill does not need 13 agents, the underlying idea is right: insert explicit quality gates before final synthesis.

### 5. Output Templates Are Not Optional

The better repos ship output scaffolds:

- literature matrices,
- review templates,
- APA / BibTeX workflows,
- structured report sections.

For finance, the template should also capture empirical design, sample period, venue tier, and whether a claim comes from a working paper or published paper.

## Weaknesses In The Current Landscape

### 1. Almost No Finance-First Calibration

This is the biggest gap.

I did not find a strong open-source skill that defaults to:

- top finance journals first,
- adjacent top economics journals second,
- top accounting journals when relevant,
- working paper series treated as frontier but clearly provisional.

That gap is why this repo exists.

### 2. Flat Monolithic Treatment of Working Papers

Many research skills either ignore working papers or dump them into a flat bottom tier.

That is fundamentally wrong in finance and economics. In frontier or fast-moving topics (e.g., GenAI in market pricing, regional banking runs, private debt, climate risk), elite working papers (NBER, CEPR, Central Banks, Top 3 R&Rs, AFA/WFA/NBER SI presentations) often lead the profession years before print publication. A literature review must distinguish:
- Tier 1: institutional series (NBER, CEPR, Fed FEDS, BIS, ECB) and advanced screening (R&Rs at Top 3/Top 5, AFA/WFA acceptance).
- Tier 2: top university series and high-download SSRN FEN papers.
- Tier 3: early unvetted preprints.

Furthermore, on frontier topics, Tier 1 working papers sit co-equal with Top 3 journal publications for mechanism discovery and active empirical debate, while for mature paradigms peer-reviewed articles provide the foundational anchor.

### 3. Too Little Tracking Of Identification Strategy & Data Infrastructure

Generic scientific review skills often emphasize thematic synthesis only.

In empirical finance, a useful literature review must record:
- research design & source of exogenous variation (specific policy, tax change, regulatory threshold, RDD cutoff),
- data infrastructure (Compustat/CRSP, Dealscan, TRACE, Call Reports, HMDA, TAQ, SEC EDGAR text),
- sample filters & exclusions (financials/utilities exclusion, price floors),
- unit of observation,
- econometric nuances (fixed effects structure, Petersen clustering, modern staggered DiD diagnostics),
- economic mechanism / transmission channel,
- main limitation and identification threats.

Without that, the review is not especially useful for a referee, dissertation chapter, or top-journal positioning memo.

### 4. The "Abstract Trap" and Hallucinated Contributions

A major vulnerability across virtually all existing literature skills is that agents read only the title and abstract, and then interpolate the rest. Because abstracts are promotional summaries, they lack the specific exogenous shock, baseline coefficients, fixed effects, and identification limitations. Agents end up:
- inventing methodologies and effect sizes,
- assigning false intellectual ownership (e.g., crediting a 2022 empirical paper with originating a theoretical mechanism derived in 1983),
- blurring the line between what a paper established and what it left open.

This repo directly solves this via a **Three-Tier Verification Quarantine** (`[Full-Text]`, `[Intro/Table]`, `[Abstract-Only]`), the **3-Anchor Introduction Retrieval Protocol**, and explicit **Intellectual Lineage Tracking**.

### 5. Too Much Provider-Specific Lock-In

Several repos are strong conceptually but tightly coupled to one tool or one command surface. This repo avoids that by shipping provider-native wrappers around the same finance workflow.

## The Best Ideas Borrowed Into This Repo

From K-Dense:

- multi-database search mentality,
- separation of literature review from paper lookup,
- reference-file progressive disclosure,
- explicit output templates.

From Imbad0202:

- quality gates,
- mode-driven workflow,
- systematic-review discipline,
- journal-fit thinking.

From lingzhi227:

- survey-generation workflow,
- citation-validation emphasis,
- coherence after drafting, not just before.

From stephenlzc:

- bilingual query generation,
- practical browser-first fallback logic when APIs are unavailable.

From ResearchClaw / research-plugins:

- packaging awareness,
- broader "research assistant" framing,
- extensibility mindset.

## Design Decisions For This Repo

### Kept

- staged workflow,
- citation verification,
- output templates,
- provider-native packaging,
- concise top-level skill files with deeper references.

### Added

- dynamic finance / econ / accounting venue ladder with subfield differentiation,
- working paper quality tiering (Tier 1 vs 2 vs 3, R&R status, top conference screening),
- operational discovery channels for working papers (SSRN FEN, NBER programs, CEPR, Central Banks, top conferences, JEL codes),
- topic maturity-based dynamic weighting (frontier co-equality vs mature bedrock anchors),
- abstract quarantine & 3-anchor introduction retrieval protocol,
- 16-column empirical finance literature matrix,
- intellectual lineage and boundary condition tracking (what papers established vs what they left open),
- deep econometric nuance tracking (exogenous shocks, fixed effects, clustering, staggered DiD diagnostics),
- publication status verification (checking if older working papers were subsequently published).

### Deliberately Not Added

- giant agent swarms,
- unnecessary framework complexity,
- finance-domain hallucination guards that rely on undocumented heuristics,
- provider-specific abstractions when a native file format is already enough.

## Provider Standards Used

- Codex: local installed skill format based on the bundled OpenAI `skill-creator` guidance in `/Users/friend/.codex/skills/.system/skill-creator/SKILL.md`.
- Cursor: skill directory format based on the bundled Cursor `create-skill` guidance in `/Users/friend/.cursor/skills-cursor/create-skill/SKILL.md`.
- Copilot: repository custom instructions per [GitHub Docs](https://docs.github.com/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=visualstudio).
- Claude Code: project and user memory via [Anthropic memory docs](https://docs.anthropic.com/en/docs/claude-code/memory), plus custom commands/subagents from the Claude Code docs ecosystem.
- Gemini CLI: `GEMINI.md` context files per [Gemini CLI configuration docs](https://geminicli.com/docs/reference/configuration/).

## Source Links

Repositories:

- https://github.com/K-Dense-AI/claude-scientific-skills
- https://github.com/K-Dense-AI/claude-scientific-writer
- https://github.com/Imbad0202/academic-research-skills
- https://github.com/ymx10086/ResearchClaw
- https://github.com/wentorai/research-plugins
- https://github.com/lingzhi227/agent-research-skills
- https://github.com/stephenlzc/AI-Powered-Literature-Review-Skills

Official provider docs:

- https://docs.github.com/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot?tool=visualstudio
- https://docs.anthropic.com/en/docs/claude-code/memory
- https://docs.anthropic.com/en/docs/claude-code/sub-agents
- https://geminicli.com/docs/reference/configuration/

Antigravity second-pass note:

- On this machine I found Antigravity user settings and Antigravity-related Gemini state, but no distinct Antigravity user skill directory analogous to Codex or Cursor.
- Because of that, this repo now treats Gemini memory as the stable integration path and ships a best-effort workspace workflow file for Antigravity rather than claiming first-class official skill support.
