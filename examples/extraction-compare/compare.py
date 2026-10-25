#!/usr/bin/env python3
"""Compare two extraction results field by field.

Typical use: the same collection brief was run once with a large model and
once with a small model; each run saved its items to a JSON file. This script
tells you whether the small model found the same items with the same values.

Input files: a JSON list of objects, or an object with an "items" list.

Usage:
    python compare.py large.json small.json --key title,company
    python compare.py a.json b.json --key id --ignore evidence,link --strict
    python compare.py a.json b.json --key id --report report.json

Options:
    --key      field(s) that identify the same item in both files (required)
    --ignore   fields not to compare (default: evidence,snippet,link,url,source)
    --strict   compare values exactly (default: trim, collapse spaces, ignore case)
    --report   also write the full result to a JSON file
    --names    labels for the two files in the output (default: A,B)

Exit code 0 = identical, 1 = differences found, 2 = input error.
Only the standard library is used.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_IGNORE = "evidence,snippet,link,url,source"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    sys.exit(2)


def load_items(path: Path) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read {path}: {exc}")
    if isinstance(data, dict) and isinstance(data.get("items"), list):
        data = data["items"]
    if not isinstance(data, list) or not all(isinstance(i, dict) for i in data):
        fail(f"{path} must contain a list of objects or {{\"items\": [...]}}")
    return data


def label(item: dict, keys: list[str]) -> str:
    """Item key with its original spelling, for display."""
    return " | ".join(str(item.get(f, "")) for f in keys)


def normalize(value, strict: bool) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        text = json.dumps(value, sort_keys=True, ensure_ascii=False)
    else:
        text = str(value)
    if strict:
        return text
    return re.sub(r"\s+", " ", text).strip().lower()


def index(items: list[dict], keys: list[str], strict: bool):
    by_key: dict[tuple, dict] = {}
    duplicates: list[tuple] = []
    missing_key = 0
    for item in items:
        k = tuple(normalize(item.get(f), strict) for f in keys)
        if all(part == "" for part in k):
            missing_key += 1
            continue
        if k in by_key:
            duplicates.append(k)
            continue
        by_key[k] = item
    return by_key, duplicates, missing_key


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Compare two extraction results field by field.")
    parser.add_argument("file_a", type=Path)
    parser.add_argument("file_b", type=Path)
    parser.add_argument("--key", required=True)
    parser.add_argument("--ignore", default=DEFAULT_IGNORE)
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--report", type=Path)
    parser.add_argument("--names", default="A,B")
    args = parser.parse_args(argv)

    keys = [k.strip() for k in args.key.split(",") if k.strip()]
    ignore = {f.strip() for f in args.ignore.split(",") if f.strip()} | set(keys)
    name_a, name_b = (args.names.split(",") + ["A", "B"])[:2]

    items_a = load_items(args.file_a)
    items_b = load_items(args.file_b)
    idx_a, dup_a, nokey_a = index(items_a, keys, args.strict)
    idx_b, dup_b, nokey_b = index(items_b, keys, args.strict)

    only_a = sorted(set(idx_a) - set(idx_b))
    only_b = sorted(set(idx_b) - set(idx_a))
    matched = sorted(set(idx_a) & set(idx_b))

    differences = []
    fields_compared = 0
    for k in matched:
        a, b = idx_a[k], idx_b[k]
        fields = sorted((set(a) | set(b)) - ignore)
        for field in fields:
            fields_compared += 1
            va, vb = normalize(a.get(field), args.strict), normalize(b.get(field), args.strict)
            if va != vb:
                differences.append({"item": label(a, keys), "field": field, name_a: a.get(field), name_b: b.get(field)})
    only_a_labels = [label(idx_a[k], keys) for k in only_a]
    only_b_labels = [label(idx_b[k], keys) for k in only_b]

    summary = {
        f"items_{name_a}": len(items_a),
        f"items_{name_b}": len(items_b),
        "matched": len(matched),
        f"only_in_{name_a}": len(only_a),
        f"only_in_{name_b}": len(only_b),
        "fields_compared": fields_compared,
        "fields_different": len(differences),
        f"duplicate_keys_{name_a}": len(dup_a),
        f"duplicate_keys_{name_b}": len(dup_b),
        f"items_without_key_{name_a}": nokey_a,
        f"items_without_key_{name_b}": nokey_b,
    }

    print("Summary")
    width = max(len(k) for k in summary)
    for k, v in summary.items():
        print(f"  {k.ljust(width)}  {v}")

    if only_a_labels:
        print(f"\nOnly in {name_a}:")
        for text in only_a_labels:
            print(f"  {text}")
    if only_b_labels:
        print(f"\nOnly in {name_b}:")
        for text in only_b_labels:
            print(f"  {text}")
    if differences:
        print("\nDifferent fields:")
        for d in differences:
            print(f"  {d['item']} · {d['field']}: {name_a}={d[name_a]!r} {name_b}={d[name_b]!r}")
    if dup_a or dup_b or nokey_a or nokey_b:
        print("\nWarning: duplicate keys or items without a key were skipped. Check --key.")

    if args.report:
        report = {
            "summary": summary,
            f"only_in_{name_a}": only_a_labels,
            f"only_in_{name_b}": only_b_labels,
            "differences": differences,
            "settings": {"key": keys, "ignore": sorted(ignore - set(keys)), "strict": args.strict},
        }
        args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nReport written to {args.report}")

    identical = not (only_a or only_b or differences)
    print("\nResult: identical" if identical else "\nResult: differences found")
    return 0 if identical else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
