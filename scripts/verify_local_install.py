#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

CORE_PATHS = {
    "codex": Path.home() / ".codex" / "skills" / "finance-literature-review",
    "cursor": Path.home() / ".cursor" / "skills" / "finance-literature-review",
    "claude_command": Path.home() / ".claude" / "commands" / "finance-lit-review.md",
    "antigravity_skill": Path.home() / ".gemini" / "antigravity" / "skills" / "finance-literature-review",
}

MANAGED_BLOCK_FILES = {
    "claude_memory": Path.home() / ".claude" / "CLAUDE.md",
    "gemini_memory": Path.home() / ".gemini" / "GEMINI.md",
    "copilot_instructions": Path.home() / ".copilot" / "instructions.md",
}

OPTIONAL_AGENT_TOOLS = {
    "agents_universal": Path.home() / ".agents" / "skills" / "finance-literature-review",
    "openhands": Path.home() / ".openhands" / "skills" / "finance-literature-review",
    "openclaw": Path.home() / ".openclaw" / "skills" / "finance-literature-review",
    "opencode": Path.home() / ".opencode" / "skills" / "finance-literature-review",
}

BLOCK = "finance-literature-review-skill:start"


def check_text_block(path: Path) -> str:
    if not path.exists():
        return f"missing: {path}"
    text = path.read_text()
    if BLOCK not in text:
        return f"present but unmanaged block missing: {path}"
    return f"ok: {path}"


def main() -> int:
    results = []
    failed = False

    for key, path in CORE_PATHS.items():
        exists = path.exists() or path.is_symlink()
        if not exists:
            failed = True
        results.append(f"{'ok' if exists else 'missing'}: {path}")

    for key, path in MANAGED_BLOCK_FILES.items():
        line = check_text_block(path)
        if not line.startswith("ok:"):
            failed = True
        results.append(line)

    for key, path in OPTIONAL_AGENT_TOOLS.items():
        if path.parent.exists():
            exists = path.exists() or path.is_symlink()
            if not exists:
                failed = True
            results.append(f"{'ok' if exists else 'missing'}: {path}")

    for line in results:
        print(line)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
