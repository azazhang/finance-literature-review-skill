# Provider Support

This file records the current provider-support judgment for this repo.

## Supported

### Codex

- Format: skill directory with `SKILL.md`
- Install target: `~/.codex/skills/finance-literature-review`

### Cursor

- Format: skill directory with `SKILL.md`
- Install target: `~/.cursor/skills/finance-literature-review`

### Claude Code

- Format: `CLAUDE.md` plus `.claude/commands/*.md`
- Install target: `~/.claude/CLAUDE.md`, `~/.claude/commands/finance-lit-review.md`

### Gemini CLI

- Format: `GEMINI.md`
- Install target: `~/.gemini/GEMINI.md`

### GitHub Copilot

- Format: repo-local instructions plus merged user instructions
- Install target: repo `.github/copilot-instructions.md`, optional `~/.copilot/instructions.md`

## Experimental

### Antigravity

Second-pass findings on this machine:

- Antigravity appears to be a VS Code–style app with user settings at `~/Library/Application Support/Antigravity/User/settings.json`.
- I did not find a distinct built-in user skill/rules directory comparable to Codex or Cursor.
- Antigravity-related state appears under `~/.gemini/antigravity/`, which strengthens the case that Gemini memory is the stable integration point.

Conclusion:

- The **supported** install path is still Gemini memory via `GEMINI.md`.
- The repo also ships an **experimental** workspace workflow file at `.agent/workflows/finance_lit_review.md` as a best-effort adapter for agent-first IDE workflows.

This experimental adapter should be treated as a convenience layer, not a guaranteed official standard.

Why that file shape:

- A community-documented Antigravity workflow convention describes workspace workflows as Markdown files in `.agent/workflows/` with YAML frontmatter.
- I still did not find an official first-party local skill directory analogous to Codex or Cursor, so I am treating this as a best-effort workflow adapter rather than claiming official parity.

Reference:

- https://antigravity.codes/blog/workflows
- https://antigravity.codes/rules/antigravity-workflows/antigravity-workflow-fundamentals
