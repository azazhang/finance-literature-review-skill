# Finance Literature Review Skill

Finance-first literature review instructions for coding agents.

Repo: https://github.com/azazhang/finance-literature-review-skill

This project adapts the strongest public literature-research skill patterns to a PhD-in-Finance workflow:

- top-journal prioritization,
- published-versus-working-paper separation,
- identification-strategy tracking,
- finance-first synthesis with adjacent economics and accounting support.

## What This Skill Does

The skill turns a vague literature request into a structured review workflow:

1. scope the question,
2. set the venue ladder,
3. collect and verify sources,
4. extract finance-relevant paper attributes,
5. synthesize by mechanism and research design,
6. output a reading list, literature matrix, and gap statement.

It is designed for requests such as:

- "map the literature on bank competition and stability"
- "build a related literature section for disclosure and cost of capital"
- "give me the top papers and frontier working papers on climate finance"
- "separate the identification strategies in the payout literature"

## Finance Defaults

- Start with top finance journals.
- Then widen to adjacent top economics journals if the mechanism or identification strategy overlaps.
- Then widen to top accounting journals when the topic overlaps disclosure, reporting, auditing, governance, or information environment.
- Treat NBER, CEPR, SSRN, and RePEc / IDEAS as frontier inputs, but label them clearly as working papers.
- For each core empirical paper, capture:
  - sample,
  - sample period,
  - unit of observation,
  - identification strategy,
  - main finding,
  - mechanism,
  - main limitation,
  - venue tier.

## Supported Providers

| Provider | Repo Asset | Local Install Target | Status |
| --- | --- | --- | --- |
| Codex | `providers/codex/finance-literature-review/` | `~/.codex/skills/finance-literature-review` | supported |
| Cursor | `.cursor/skills/finance-literature-review/` | `~/.cursor/skills/finance-literature-review` | supported |
| Claude Code | `CLAUDE.md`, `.claude/commands/finance-lit-review.md` | `~/.claude/CLAUDE.md`, `~/.claude/commands/finance-lit-review.md` | supported |
| Gemini CLI | `GEMINI.md` | `~/.gemini/GEMINI.md` | supported |
| GitHub Copilot | `.github/copilot-instructions.md` | `~/.copilot/instructions.md` and repo-local instructions | supported |
| Antigravity | `.agent/workflows/finance_lit_review.md` plus `GEMINI.md` | workspace-local workflow, Gemini memory path | experimental |

## Antigravity Second Pass

Second-pass result:

- On this machine, Antigravity exposes a VS Code–style user settings file at `~/Library/Application Support/Antigravity/User/settings.json`.
- I did not find a separate first-class local skill/rules directory analogous to Codex or Cursor.
- The Gemini installation does expose `~/.gemini/GEMINI.md`, and Antigravity-related data also appears under `~/.gemini/antigravity/`.

So the practical support model is:

- **supported**: Gemini memory via `GEMINI.md`
- **experimental**: workspace workflow file at `.agent/workflows/finance_lit_review.md`

See [docs/provider-support.md](docs/provider-support.md).

## How To Use The Skill

The fastest explanation is:

- ask for a topic,
- specify whether you want published-only or frontier coverage,
- optionally specify geography, period, or subfield,
- ask for the desired output shape.

Examples:

- "Do a finance literature review on shareholder payouts after tax shocks. Published papers first, then frontier working papers. Give me a matrix and gap statement."
- "Map the disclosure literature relevant to cost of capital, with top accounting and top finance journals only."
- "Scan the climate finance literature, split theory, empirics, and frontier working papers, and prioritize papers useful for a dissertation second chapter."

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
- `.cursor/skills/finance-literature-review/`: Cursor project skill.
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

## Benchmark Review

See [docs/skill-landscape.md](docs/skill-landscape.md).
