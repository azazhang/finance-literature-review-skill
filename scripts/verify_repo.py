#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".github/copilot-instructions.md",
    "providers/codex/finance-literature-review/SKILL.md",
    "providers/codex/finance-literature-review/references/journal-priority.md",
    "providers/codex/finance-literature-review/templates/literature-matrix.md",
    ".cursor/skills/finance-literature-review/SKILL.md",
    ".cursor/skills/finance-literature-review/references/journal-priority.md",
    ".cursor/skills/finance-literature-review/templates/literature-matrix.md",
    ".claude/commands/finance-lit-review.md",
    "docs/skill-landscape.md",
    "scripts/install_local.py",
]


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED if not (repo_root / path).exists()]
    if missing:
        print("missing files:")
        for item in missing:
            print(f"- {item}")
        return 1

    codex_skill = (repo_root / "providers/codex/finance-literature-review/SKILL.md").read_text()
    cursor_skill = (repo_root / ".cursor/skills/finance-literature-review/SKILL.md").read_text()
    if "Never fabricate citations" not in codex_skill or "Never fabricate citations" not in cursor_skill:
        print("verification failed: missing citation guardrail in one or more skill files")
        return 1

    print("repo structure looks valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
