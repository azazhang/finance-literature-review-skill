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
    parser.add_argument(
        "--mode",
        choices=["symlink", "copy"],
        default="symlink",
        help="Install by symlink or copy. Default: symlink.",
    )
    parser.add_argument(
        "--providers",
        default="codex,cursor,claude,gemini,copilot,antigravity",
        help="Comma-separated providers to install. Default installs all supported targets.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing changes.")
    return parser.parse_args()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def parse_provider_list(raw: str) -> set[str]:
    providers = {item.strip().lower() for item in raw.split(",") if item.strip()}
    valid = {"codex", "cursor", "claude", "gemini", "copilot", "antigravity"}
    unknown = providers - valid
    if unknown:
        raise SystemExit(f"unknown providers: {', '.join(sorted(unknown))}")
    return providers


def link_or_copy(src: Path, dest: Path, force: bool, mode: str, dry_run: bool) -> str:
    if not dry_run:
        ensure_parent(dest)
    if dest.exists() or dest.is_symlink():
        if dest.is_symlink() and dest.resolve() == src.resolve():
            return f"kept existing link: {dest}"
        if not force:
            return f"skipped existing path: {dest}"
        if not dry_run:
            remove_path(dest)
    if dry_run:
        return f"would install {dest} from {src} via {mode}"
    if mode == "symlink":
        dest.symlink_to(src, target_is_directory=src.is_dir())
        return f"linked {dest} -> {src}"
    if src.is_dir():
        shutil.copytree(src, dest)
    else:
        shutil.copy2(src, dest)
    return f"copied {src} -> {dest}"


def merge_block(dest: Path, source_text: str, dry_run: bool) -> str:
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
    if dry_run:
        return f"would merge managed block into {dest}"
    ensure_parent(dest)
    dest.write_text(new_text)
    return f"merged managed block into {dest}"


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    home = Path.home()
    providers = parse_provider_list(args.providers)

    actions = []

    codex_src = repo_root / "providers" / "codex" / "finance-literature-review"
    cursor_src = repo_root / ".cursor" / "skills" / "finance-literature-review"
    claude_cmd_src = repo_root / ".claude" / "commands" / "finance-lit-review.md"

    if "codex" in providers:
        actions.append(
            link_or_copy(
                codex_src,
                home / ".codex" / "skills" / "finance-literature-review",
                args.force,
                args.mode,
                args.dry_run,
            )
        )
    if "cursor" in providers:
        actions.append(
            link_or_copy(
                cursor_src,
                home / ".cursor" / "skills" / "finance-literature-review",
                args.force,
                args.mode,
                args.dry_run,
            )
        )
    if "claude" in providers:
        actions.append(
            link_or_copy(
                claude_cmd_src,
                home / ".claude" / "commands" / "finance-lit-review.md",
                args.force,
                args.mode,
                args.dry_run,
            )
        )
        actions.append(
            merge_block(home / ".claude" / "CLAUDE.md", (repo_root / "CLAUDE.md").read_text(), args.dry_run)
        )
    if "gemini" in providers:
        actions.append(
            merge_block(home / ".gemini" / "GEMINI.md", (repo_root / "GEMINI.md").read_text(), args.dry_run)
        )
    if "copilot" in providers:
        actions.append(
            merge_block(
                home / ".copilot" / "instructions.md",
                (repo_root / ".github" / "copilot-instructions.md").read_text(),
                args.dry_run,
            )
        )
    if "antigravity" in providers:
        actions.append(
            "note: antigravity has no confirmed separate local skill directory on this machine; workspace file .agent/workflows/finance_lit_review.md is repo-local and GEMINI.md remains the supported memory path."
        )

    print("\n".join(actions))
    return 0


if __name__ == "__main__":
    sys.exit(main())
