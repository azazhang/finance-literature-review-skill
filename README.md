# Finance Literature Review Skill

A source-first research skill for financial economics. It helps agents discover the closest published and working papers, **retrieve and read primary research**, verify consequential claims against actual passages and exhibits, evaluate identification and economic contributions, and deliver a useful literature synthesis.

The governing rule: **no substantive claim about a paper without an actual inspected source supporting that claim**. An abstract-only paper can support provisional author-reported facts; it cannot ground independent judgments about identification, mechanisms, or novelty. When pivotal full text is unavailable, the agent tries legitimate open/working-paper versions and then asks the researcher for the PDF. It keeps working with accessible sources rather than inventing inaccessible research.

## Package

- [Main skill](skill/finance-literature-review/SKILL.md) — research objective, anti-fabrication evidence requirements, four substantive questions, and stopping rule.
- [Source verification](skill/finance-literature-review/references/source-verification.md) — full-text recovery, version identity, abstract quarantine, actual design/results/contribution reading, claim-level locators, and source-to-synthesis reconciliation.
- [Discovery](skill/finance-literature-review/references/discovery.md) — finance and related literature, current working-paper channels, citation chaining, and assessment of screening signals.
- [Critical synthesis](skill/finance-literature-review/references/critical-synthesis.md) — identification, competing mechanisms, intellectual lineage, genuine research gaps, and incremental contribution.
- [Outputs](skill/finance-literature-review/references/outputs.md) — scoped reading lists, deep dives, related-literature prose, gap maps, and claim provenance.
- [Optional matrix](skill/finance-literature-review/templates/literature-matrix.md) — source-located extraction and one documented real-paper illustration.

All local agents point to **one canonical package**, `skill/finance-literature-review/`. Previous Codex/Cursor duplicates and verbose provider-specific prompts have been superseded.

## Installation

```bash
python3 scripts/install_local.py --providers codex,cursor,claude,gemini,antigravity,agents,opencode
```

The installer uses symlinks to the canonical skill and can update known legacy links safely; other existing installations require explicit consent to overwrite. `--dry-run` previews changes. It also refreshes short managed pointers for Claude/Gemini/Copilot without overwriting unrelated text. The standalone Gemini web/desktop App has separate account-level skill management and is not installed by a Mac symlink.

**No programmatic literature-quality validator exists in this skill.** The source evidence, accurate identification of what the agent examined, and the actual quality of synthesis are the relevant tests. The installer is the repository's sole executable. Historical implementations remain recoverable in Git.

Repository: https://github.com/azazhang/finance-literature-review-skill
