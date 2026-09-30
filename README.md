# Finance Literature Review Skill

Finance-first literature review instructions for coding agents.

Repo: https://github.com/azazhang/finance-literature-review-skill

This project adapts the strongest public literature-research skill patterns to a rigorous PhD-in-Finance workflow:

- **Dynamic venue & working paper hierarchy**: Values Tier 1 working papers (NBER, CEPR, Central Banks, Top 3 R&Rs, AFA/WFA presentations) alongside core journals (JF, JFE, RFS) on frontier topics.
- **Systematic working paper discovery**: Explicit search channels across SSRN FEN eJournals, NBER programs, CEPR, central banks, annual conference proceedings, and finance JEL codes.
- **Abstract Quarantine & Anti-Hallucination**: Prohibits inferring contributions, identification strategies, or magnitudes from abstracts alone; mandates retrieving Introductions and table notes.
- **3-Anchor Introduction Protocol**: Verifies empirical designs, quantitative magnitudes, and self-stated contributions relative to landmark benchmark papers.
- **Intellectual lineage & boundary tracking**: Traces theoretical originators, causal identification benchmarks, and records what prior studies established vs. what they left open.
- **Granular econometric & identification tracking**: Captures specific exogenous shocks, primary datasets (Compustat, CRSP, Dealscan, Call Reports, TRACE), fixed effects structures, standard error clustering, and staggered DiD robustness in a 16-column matrix.
- **Finance-first synthesis**: Synthesizes by theoretical mechanism and causal design with adjacent economics and accounting support.
- **Zero citation fabrication**: Strict anti-hallucination guardrails and publication status verification.

## What This Skill Does

The skill turns a literature request into an academic review workflow:

1. **Scope & Topic Maturity**: Classify topic as frontier/emergent (where Tier 1 working papers lead) or mature paradigm (where peer-reviewed articles anchor).
2. **Build Search Grid**: Construct query grids across top journals, SSRN FEN, NBER programs, conference schedules, and JEL codes.
3. **Collect & Introduction Retrieval**: Retrieve full-text or Introduction sections (Paras 3–11); quarantine abstract-only papers to prevent hallucinated contributions.
4. **Extract Finance Matrix (16 Columns)**: Populate empirical matrix capturing datasets, shocks, fixed effects, verified findings, mechanisms, boundary conditions, and lineage roles.
5. **Synthesize by Mechanism & Lineage**: Contrast causal designs and theoretical channels; separate empirical correlations from mechanisms and preserve intellectual ownership.
6. **Deliver**: Output a prioritized reading list, complete literature matrix, draft-ready related literature section, or research gap map.

## Supported Providers

| Provider | Repo Asset | Local Install Target | Status |
| --- | --- | --- | --- |
| OpenAI Codex | `providers/codex/finance-literature-review/` | `~/.codex/skills/finance-literature-review` | supported |
| Cursor IDE | `.cursor/skills/finance-literature-review/` | `~/.cursor/skills/finance-literature-review` | supported |
| Google Antigravity | `providers/codex/...` + `.agent/workflows/...` | `~/.gemini/antigravity/skills/`, `.agent/workflows/` | supported |
| Claude Code | `CLAUDE.md`, `.claude/commands/finance-lit-review.md` | `~/.claude/CLAUDE.md`, `~/.claude/commands/` | supported |
| Gemini CLI | `GEMINI.md` | `~/.gemini/GEMINI.md` | supported |
| GitHub Copilot | `.github/copilot-instructions.md` | `~/.copilot/instructions.md` & repo `.github/` | supported |
| Universal Agents | `providers/codex/...` | `~/.agents/skills/finance-literature-review` | supported |
| OpenHands | `providers/codex/...` | `~/.openhands/skills/finance-literature-review` | supported |
| OpenClaw | `providers/codex/...` | `~/.openclaw/skills/finance-literature-review` | supported |
| OpenCode | `providers/codex/...` | `~/.opencode/skills/finance-literature-review` | supported |

## How To Use The Skill

The basic formula is:

> topic + empirical setting + source preference + output format

Examples:

- "Do a finance literature review on private credit growth and corporate borrowing. Treat as a frontier topic: prioritize Tier 1 working papers (NBER, CEPR, Top 3 R&Rs, AFA/WFA) alongside top finance journals. Deliver a matrix and research gap map."
- "Map the disclosure literature relevant to cost of capital, with top accounting (JAR, JAE, TAR) and top finance journals. Capture the exogenous shock, mechanism, and endogeneity threats for each paper."
- "Review the empirical literature on shareholder payouts following corporate tax shocks. Focus on quasi-natural experiments and staggered DiD designs, and produce a related literature section outline."

Detailed usage examples are in [docs/how-to-use.md](docs/how-to-use.md).

## Install

```bash
python3 scripts/install_local.py
```

Useful options:

```bash
python3 scripts/install_local.py --dry-run
python3 scripts/install_local.py --providers codex,cursor,claude,gemini,copilot
python3 scripts/install_local.py --mode copy
python3 scripts/install_local.py --force
```

## Verify

Repo structure:

```bash
python3 scripts/verify_repo.py
```

Local install state:

```bash
python3 scripts/verify_local_install.py
```

## Repo Structure

- `providers/codex/finance-literature-review/`: Codex-native skill package.
  - `references/contribution-extraction.md`: Abstract quarantine, 3-anchor introduction protocol, and ownership lineage.
  - `references/working-papers.md`: Working paper discovery channels, tiering, and evaluation.
  - `references/journal-priority.md`: Venue hierarchy and dynamic topic weighting.
  - `references/output-modes.md`: Detailed guides for reading lists, matrices, related-lit sections, and gap maps.
  - `references/synthesis-checklist.md`: Quality checklist before final delivery.
  - `templates/literature-matrix.md`: 16-column empirical finance matrix schema.
- `.cursor/skills/finance-literature-review/`: Cursor project skill (mirrors codex package).
- `CLAUDE.md` and `.claude/commands/finance-lit-review.md`: Claude Code memory and command.
- `GEMINI.md`: Gemini memory file.
- `.github/copilot-instructions.md`: GitHub Copilot repo instructions.
- `.agent/workflows/finance_lit_review.md`: experimental Antigravity workspace workflow.
- `docs/skill-landscape.md`: benchmark review of major public literature-research skills.
- `docs/how-to-use.md`: prompt patterns and usage examples.
- `docs/provider-support.md`: provider-by-provider support notes.
- `scripts/install_local.py`: local installer.
- `scripts/verify_repo.py`: repo validator.
- `scripts/verify_local_install.py`: local install validator.
