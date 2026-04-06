#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


EXPECTED = {
    "codex": Path.home() / ".codex" / "skills" / "finance-literature-review",
    "cursor": Path.home() / ".cursor" / "skills" / "finance-literature-review",
    "claude_command": Path.home() / ".claude" / "commands" / "finance-lit-review.md",
    "claude_memory": Path.home() / ".claude" / "CLAUDE.md",
    "gemini_memory": Path.home() / ".gemini" / "GEMINI.md",
    "copilot_instructions": Path.home() / ".copilot" / "instructions.md",
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
    for key in ("codex", "cursor", "claude_command"):
        path = EXPECTED[key]
        exists = path.exists()
        failed = failed or not exists
        results.append(f"{'ok' if exists else 'missing'}: {path}")

    for key in ("claude_memory", "gemini_memory", "copilot_instructions"):
        line = check_text_block(EXPECTED[key])
        if not line.startswith("ok:"):
            failed = True
        results.append(line)

    for line in results:
        print(line)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
