# Finance Literature Review Skill

An open-source, finance-first literature review skill pack for coding agents.

The goal is straightforward: take the best parts of the strongest public literature-research skills, then adapt the defaults for a PhD-in-Finance workflow. That means top-journal prioritization, published-versus-working-paper separation, explicit identification-strategy tracking, and strong support for adjacent economics and accounting literatures.

## Why This Exists

The public skill landscape is now broad, but most of it falls into one of three buckets:

- Very strong generic science skills that are not finance-first.
- Broad academic pipelines that emphasize orchestration more than field-specific source prioritization.
- Thin literature-review wrappers with good ideas but weak source verification or venue calibration.

I did not find a strong open-source skill that is explicitly optimized for finance literature reviews with finance, economics, and accounting venue ladders as first-class defaults.

## What This Repo Ships

- `providers/codex/finance-literature-review/`: Codex-native skill package.
- `.cursor/skills/finance-literature-review/`: Cursor project skill.
- `CLAUDE.md` and `.claude/commands/finance-lit-review.md`: Claude Code project memory plus a reusable command.
- `GEMINI.md`: Gemini project context.
- `.github/copilot-instructions.md`: GitHub Copilot repository instructions.
- `AGENTS.md`: generic cross-agent project context.
- `scripts/install_local.py`: installs or merges the provider-specific assets into local user directories.
- `scripts/verify_repo.py`: verifies that the repo has the expected shape.
- `docs/skill-landscape.md`: benchmark review of the major public literature-research skill repos and provider standards.

## Finance-Specific Defaults

- Start with top finance journals, then adjacent top economics and accounting journals, then frontier working papers.
- Explicitly separate published evidence from working papers.
- Capture identification strategy, sample, period, unit of observation, mechanism, and main limitation for each key paper.
- Prefer synthesis by question, mechanism, and empirical design rather than paper-by-paper summaries.
- Treat NBER, CEPR, SSRN, and RePEc as important frontier sources, but do not let them displace mature published evidence when the literature is already established.
- Flag whether evidence is top-tier, adjacent-tier, or provisional.

## Local Provider Targets

- Codex: `~/.codex/skills/finance-literature-review`
- Cursor: `~/.cursor/skills/finance-literature-review`
- Claude: `~/.claude/CLAUDE.md` and `~/.claude/commands/finance-lit-review.md`
- Gemini: `~/.gemini/GEMINI.md`
- Copilot: `~/.copilot/instructions.md`

Antigravity note:
No separate documented instruction-file convention was found on this machine for Antigravity. The detected Google Gemini installation already uses `~/.gemini/GEMINI.md`, so this repo treats Gemini as the supported target for the Gemini/Antigravity stack.

## Install

```bash
python3 scripts/install_local.py
```

Optional:

```bash
python3 scripts/install_local.py --force
```

`--force` only replaces existing managed links. It does not wipe unrelated user files.

## Verify

```bash
python3 scripts/verify_repo.py
```

## Benchmark Review

See [docs/skill-landscape.md](docs/skill-landscape.md).

## Publishing Status

The repo is ready to initialize and push, but GitHub publication depends on either:

- an existing empty remote repository URL, or
- GitHub CLI / another authenticated repo-creation path on this machine.

The local environment available in this session does not include `gh`, and the connected GitHub tools here do not expose repository creation.
