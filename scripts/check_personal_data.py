#!/usr/bin/env python3
"""Scan the repository for common patterns of personal data and secrets.

Usage:
    python scripts/check_personal_data.py [path ...]

Without arguments it scans the whole repository.

Optional local blocklist: create a file named `.privacy-blocklist` in the
repository root (it is git-ignored) with one term per line, for example your
own name, employer or email. Matches are reported like any other finding.
Lines starting with # are ignored.

Exit code 0 = nothing found, 1 = possible personal data found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
SKIP_FILES = {"LICENSE", ".privacy-blocklist"}
TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".json", ".py", ".js", ".ts",
    ".html", ".css", ".csv", ".toml", ".ini", ".cfg", ".sh", "",
}

PATTERNS: dict[str, re.Pattern[str]] = {
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "phone number": re.compile(r"(?<![\w/])\+\d{1,3}[\s.-]?\d{2,4}[\s.-]?\d{3,4}[\s.-]?\d{2,4}\b"),
    "IBAN": re.compile(r"\b[A-Z]{2}\d{2}(?:\s?[A-Z0-9]{4}){3,7}(?:\s?[A-Z0-9]{1,4})?\b"),
    "Anthropic API key": re.compile(r"\bsk-ant-[A-Za-z0-9_-]{10,}"),
    "OpenAI-style API key": re.compile(r"\bsk-[A-Za-z0-9]{20,}"),
    "GitHub token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "claude.ai private link": re.compile(r"claude\.ai/(?:chat|project|share)/[0-9a-f-]{8,}"),
}

# Values that look like matches but are allowed (placeholders, documentation).
ALLOWED = {
    "noreply@github.com",
    "noreply@anthropic.com",
}


def load_blocklist() -> list[str]:
    path = ROOT / ".privacy-blocklist"
    if not path.exists():
        return []
    terms = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms


def iter_files(targets: list[Path]):
    for target in targets:
        if target.is_file():
            yield target
            continue
        for path in target.rglob("*"):
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
                continue
            if path.name in SKIP_FILES:
                continue
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            yield path


def scan(path: Path, blocklist: list[str]) -> list[tuple[int, str, str]]:
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return findings
    for lineno, line in enumerate(text.splitlines(), start=1):
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                value = match.group(0)
                if value in ALLOWED:
                    continue
                findings.append((lineno, label, value))
        lowered = line.lower()
        for term in blocklist:
            if term.lower() in lowered:
                findings.append((lineno, "blocklist term", term))
    return findings


def main(argv: list[str]) -> int:
    targets = [Path(a).resolve() for a in argv] or [ROOT]
    blocklist = load_blocklist()
    total = 0
    for path in iter_files(targets):
        for lineno, label, value in scan(path, blocklist):
            rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
            print(f"{rel}:{lineno}: possible {label}: {value}")
            total += 1
    if total:
        print(f"\n{total} possible finding(s). Remove them or replace with placeholders such as <EMAIL>.")
        return 1
    print("No personal data patterns found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
