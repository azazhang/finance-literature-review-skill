# Provider Support

This document details the support model, configuration paths, and packaging formats for all supported AI coding agents.

---

## 1. Commercial & IDE-Native Agents

### OpenAI Codex
* **Packaging Format**: Standard skill package with YAML frontmatter `SKILL.md`, references, and templates.
* **Install Target**: `~/.codex/skills/finance-literature-review`
* **Status**: Full first-class support.

### Cursor IDE
* **Packaging Format**: Cursor skill package with `SKILL.md`, `references/`, and `templates/`.
* **Install Target**: `~/.cursor/skills/finance-literature-review`
* **Status**: Full first-class support.

### Google Antigravity
* **Packaging Format**: 
  1. **Global Skills**: Antigravity discovers and registers skills directly from `~/.gemini/antigravity/skills/` (and its configuration link `~/.gemini/config/skills/`).
  2. **Workspace Workflow**: Workspace-local workflow file at `.agent/workflows/finance_lit_review.md`.
  3. **Global Memory**: Project and global agent instructions in `GEMINI.md`.
* **Install Target**: `~/.gemini/antigravity/skills/finance-literature-review`, `~/.gemini/GEMINI.md`, and repo `.agent/workflows/`
* **Status**: Full first-class support.

### Claude Code
* **Packaging Format**: Managed instruction block in `CLAUDE.md` plus dedicated custom slash command.
* **Install Target**: 
  * Memory: `~/.claude/CLAUDE.md` (via managed block)
  * Slash Command: `~/.claude/commands/finance-lit-review.md` (invoked via `/finance-lit-review`)
* **Status**: Full first-class support.

### Gemini CLI
* **Packaging Format**: Managed instruction block in `GEMINI.md`.
* **Install Target**: `~/.gemini/GEMINI.md`
* **Status**: Full first-class support.

### GitHub Copilot
* **Packaging Format**: Repository custom instructions (`.github/copilot-instructions.md`) and user-level custom instructions.
* **Install Target**: `~/.copilot/instructions.md` and repository `.github/copilot-instructions.md`
* **Status**: Full first-class support.

---

## 2. Open-Source Autonomous Agent Ecosystems

The skill package format (`SKILL.md` with progressive disclosure references and templates) conforms to the universal agent skills standard and is directly supported across open-source agent frameworks:

### Universal Agent Skills Directory
* **Install Target**: `~/.agents/skills/finance-literature-review`
* **Status**: Supported.

### OpenHands
* **Install Target**: `~/.openhands/skills/finance-literature-review`
* **Status**: Supported.

### OpenClaw
* **Install Target**: `~/.openclaw/skills/finance-literature-review`
* **Status**: Supported.

### OpenCode
* **Install Target**: `~/.opencode/skills/finance-literature-review`
* **Status**: Supported.

---

## 3. Automated Local Installation

To install or sync all providers automatically on your machine:

```bash
python3 scripts/install_local.py --force
```

To verify the installation status across all local tools:

```bash
python3 scripts/verify_local_install.py
```
