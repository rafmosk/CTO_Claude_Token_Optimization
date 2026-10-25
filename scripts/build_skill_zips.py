#!/usr/bin/env python3
"""Build or check the ZIP files of the skills in examples/.

A skill is any folder containing a SKILL.md file. Its ZIP is written next to
the folder, with the folder at the root of the archive, as claude.ai expects:

    examples/token-budget/token-budget/SKILL.md
    -> examples/token-budget/token-budget.zip  (contains token-budget/SKILL.md, ...)

Usage:
    python scripts/build_skill_zips.py          build or rebuild every ZIP
    python scripts/build_skill_zips.py --check  fail if a ZIP is missing or out of date
"""

from __future__ import annotations

import io
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)  # fixed timestamps keep the ZIP reproducible


def skill_dirs() -> list[Path]:
    return sorted(p.parent for p in EXAMPLES.rglob("SKILL.md"))


def build_bytes(skill: Path) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill.rglob("*")):
            if path.is_dir() or path.name.startswith("."):
                continue
            arcname = f"{skill.name}/{path.relative_to(skill).as_posix()}"
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, path.read_bytes())
    return buffer.getvalue()


def main(argv: list[str]) -> int:
    check = "--check" in argv
    problems = 0
    for skill in skill_dirs():
        target = skill.parent / f"{skill.name}.zip"
        data = build_bytes(skill)
        rel = target.relative_to(ROOT)
        if check:
            if not target.exists() or target.read_bytes() != data:
                print(f"{rel}: missing or out of date. Run: python scripts/build_skill_zips.py")
                problems += 1
            else:
                print(f"{rel}: up to date")
        else:
            target.write_bytes(data)
            print(f"{rel}: built")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
