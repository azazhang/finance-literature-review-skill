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

### 2. Too Little Attention To Published Versus Working Paper Status

Many research skills treat papers as interchangeable units.

That is often wrong in finance. A current NBER or SSRN draft can be extremely important, but a literature review still needs to tell the reader whether the result is:

- published in a top journal,
- published in a field journal,
- still a working paper,
- only weakly cited or weakly verified.

### 3. Too Little Tracking Of Identification Strategy

Generic scientific review skills often emphasize thematic synthesis only.

In empirical finance, a useful literature review usually needs to record:

- research design,
- identification strategy,
- sample period,
- unit of observation,
- key outcome variable,
- mechanism story,
- main limitation.

Without that, the review is not especially useful for a referee, dissertation chapter, or top-journal positioning memo.

### 4. Too Much Provider-Specific Lock-In

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

- finance / econ / accounting venue ladder,
- explicit published-versus-working-paper separation,
- identification-strategy extraction,
- finance-oriented synthesis axes,
- support for NBER / CEPR / SSRN / RePEc as frontier inputs.

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
