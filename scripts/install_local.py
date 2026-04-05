#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

BLOCK_START = "<!-- finance-literature-review-skill:start -->"
BLOCK_END = "<!-- finance-literature-review-skill:end -->"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install local provider assets for the finance literature review repo.")
    parser.add_argument("--force", action="store_true", help="Replace existing managed links if needed.")
    return parser.parse_args()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def symlink_path(src: Path, dest: Path, force: bool) -> str:
    ensure_parent(dest)
    if dest.exists() or dest.is_symlink():
        if dest.is_symlink() and dest.resolve() == src.resolve():
            return f"kept existing link: {dest}"
        if not force:
            return f"skipped existing path: {dest}"
        remove_path(dest)
    dest.symlink_to(src, target_is_directory=src.is_dir())
    return f"linked {dest} -> {src}"


def merge_block(dest: Path, source_text: str) -> str:
    ensure_parent(dest)
    managed_block = f"{BLOCK_START}\n{source_text.strip()}\n{BLOCK_END}\n"
    existing = dest.read_text() if dest.exists() else ""
    if BLOCK_START in existing and BLOCK_END in existing:
        start = existing.index(BLOCK_START)
        end = existing.index(BLOCK_END) + len(BLOCK_END)
        new_text = existing[:start] + managed_block + existing[end:]
    else:
        prefix = existing.rstrip()
        if prefix:
            new_text = prefix + "\n\n" + managed_block
        else:
            new_text = managed_block
    dest.write_text(new_text)
    return f"merged managed block into {dest}"


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    home = Path.home()

    actions = []

    codex_src = repo_root / "providers" / "codex" / "finance-literature-review"
    cursor_src = repo_root / ".cursor" / "skills" / "finance-literature-review"
    claude_cmd_src = repo_root / ".claude" / "commands" / "finance-lit-review.md"

    actions.append(
        symlink_path(codex_src, home / ".codex" / "skills" / "finance-literature-review", args.force)
    )
    actions.append(
        symlink_path(cursor_src, home / ".cursor" / "skills" / "finance-literature-review", args.force)
    )
    actions.append(
        symlink_path(claude_cmd_src, home / ".claude" / "commands" / "finance-lit-review.md", args.force)
    )

    actions.append(
        merge_block(home / ".claude" / "CLAUDE.md", (repo_root / "CLAUDE.md").read_text())
    )
    actions.append(
        merge_block(home / ".gemini" / "GEMINI.md", (repo_root / "GEMINI.md").read_text())
    )
    actions.append(
        merge_block(home / ".copilot" / "instructions.md", (repo_root / ".github" / "copilot-instructions.md").read_text())
    )

    print("\n".join(actions))
    print("note: antigravity was detected locally, but no separate documented instruction-file convention was found; Gemini installation is the supported path.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
