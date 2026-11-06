#!/usr/bin/env python3
"""Install one canonical finance-literature-review Agent Skill for local agents.

Only handles links/copies and short user-level pointers. It does not grade
literature reviews, validate papers, or provide a false research-quality gate.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

MARKER = "finance-literature-review-skill"
START = f"<!-- {MARKER}:start -->"
END = f"<!-- {MARKER}:end -->"

PROVIDERS = (
    "codex", "cursor", "claude", "gemini", "antigravity", "agents",
    "opencode", "openhands", "openclaw", "copilot",
)


def args_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the canonical finance literature review skill.")
    parser.add_argument("--providers", default=",".join(PROVIDERS),
                        help="Comma-separated local agents to update (default: all supported).")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changes.")
    parser.add_argument("--force", action="store_true",
                        help="Replace an existing noncanonical skill installation explicitly.")
    parser.add_argument("--mode", choices=("symlink", "copy"), default="symlink",
                        help="Default: one shared canonical version via symlink.")
    args = parser.parse_args()
    args.providers = {v.strip().lower() for v in args.providers.split(",") if v.strip()}
    invalid = args.providers - set(PROVIDERS)
    if invalid:
        parser.error("Unknown provider(s): " + ", ".join(sorted(invalid)))
    return args


def install(src: Path, dst: Path, root: Path, args: argparse.Namespace) -> str:
    src = src.resolve()
    if dst.is_symlink():
        if dst.resolve() == src:
            return f"current: {dst}"
        # The v1 repository shipped two duplicate copies; their links become
        # broken when those duplicates are removed. Migrate our own old links.
        old_target = dst.resolve()
        is_our_legacy = old_target == root or root in old_target.parents
        if not is_our_legacy and not args.force:
            return f"SKIPPED external symlink (use --force): {dst}"
        if args.dry_run:
            return f"would replace legacy symlink: {dst} -> {src}"
        dst.unlink()
    elif dst.exists():
        if dst.is_dir() and (dst / "SKILL.md").is_file() and args.mode == "copy":
            if (dst / "SKILL.md").read_bytes() == (src / "SKILL.md").read_bytes():
                return f"current copy: {dst}"
        if not args.force:
            return f"SKIPPED existing installation (use --force): {dst}"
        if args.dry_run:
            return f"would replace existing installation: {dst}"
        if dst.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()

    if args.dry_run:
        return f"would install: {dst} -> {src} [{args.mode}]"
    dst.parent.mkdir(parents=True, exist_ok=True)
    if args.mode == "symlink":
        dst.symlink_to(src, target_is_directory=True)
    else:
        shutil.copytree(src, dst)
    return f"installed: {dst} -> {src} [{args.mode}]"


def update_managed_block(destination: Path, content: str, args: argparse.Namespace) -> str:
    managed = f"{START}\n{content.strip()}\n{END}"
    old = destination.read_text(encoding="utf-8") if destination.exists() else ""
    if START in old or END in old:
        if START not in old or END not in old:
            return f"SKIPPED malformed managed block: {destination}"
        first = old.index(START)
        last = old.index(END, first) + len(END)
        new = old[:first] + managed + old[last:]
    else:
        new = old.rstrip() + ("\n\n" if old.strip() else "") + managed + "\n"
    if old == new:
        return f"current pointer: {destination}"
    if args.dry_run:
        return f"would refresh managed pointer: {destination}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(new, encoding="utf-8")
    return f"refreshed managed pointer: {destination}"


def main() -> int:
    args = args_parser()
    root = Path(__file__).resolve().parents[1]
    src = root / "skill" / "finance-literature-review"
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"canonical skill missing: {src}")

    home = Path.home()
    roots = {
        "codex": [home / ".codex" / "skills"],
        "cursor": [home / ".cursor" / "skills"],
        "claude": [home / ".claude" / "skills"],
        "gemini": [home / ".gemini" / "config" / "skills"],
        "antigravity": [home / ".gemini" / "antigravity" / "skills"],
        "agents": [home / ".agents" / "skills"],
        "opencode": [home / ".opencode" / "skills"],
        "openhands": [home / ".openhands" / "skills"],
        "openclaw": [home / ".openclaw" / "skills"],
    }
    for provider in PROVIDERS:
        if provider not in args.providers:
            continue
        for folder in roots.get(provider, []):
            print(install(src, folder / "finance-literature-review", root, args))

        if provider == "claude":
            print(update_command(root / ".claude" / "commands" / "finance-lit-review.md",
                                 home / ".claude" / "commands" / "finance-lit-review.md",
                                 root, args))
            print(update_managed_block(home / ".claude" / "CLAUDE.md",
                                       (root / "CLAUDE.md").read_text(encoding="utf-8"), args))
        elif provider == "gemini":
            print(update_managed_block(home / ".gemini" / "GEMINI.md",
                                       (root / "GEMINI.md").read_text(encoding="utf-8"), args))
        elif provider == "copilot":
            print(update_managed_block(home / ".copilot" / "instructions.md",
                                       (root / ".github" / "copilot-instructions.md").read_text(encoding="utf-8"), args))

    return 0


def update_command(src: Path, dst: Path, root: Path, args: argparse.Namespace) -> str:
    """Install a small optional Claude command without changing other commands."""
    if dst.is_symlink():
        if dst.resolve() == src.resolve():
            return f"current command: {dst}"
        old_target = dst.resolve()
        if not (old_target == root or root in old_target.parents) and not args.force:
            return f"SKIPPED unrelated command link: {dst}"
        if args.dry_run:
            return f"would migrate command link: {dst}"
        dst.unlink()
    elif dst.exists():
        if not args.force:
            return f"SKIPPED existing command: {dst}"
        if args.dry_run:
            return f"would replace command: {dst}"
        if dst.is_dir():
            return f"SKIPPED command directory: {dst}"
        dst.unlink()
    if args.dry_run:
        return f"would install command: {dst}"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.symlink_to(src.resolve())
    return f"installed command: {dst}"


if __name__ == "__main__":
    raise SystemExit(main())
