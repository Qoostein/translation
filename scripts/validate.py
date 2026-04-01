#!/usr/bin/env python3
"""
Validate that every locales/*.json file:
  - is valid JSON object with string values
  - has exactly the same keys as locales/en.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    locales_dir = repo / "locales"
    en_path = locales_dir / "en.json"

    if not en_path.is_file():
        print(f"error: missing {en_path}", file=sys.stderr)
        return 1

    with en_path.open(encoding="utf-8") as f:
        en = json.load(f)

    if not isinstance(en, dict):
        print("error: en.json must be a JSON object", file=sys.stderr)
        return 1

    en_keys = set(en)
    for k, v in en.items():
        if not isinstance(k, str) or not isinstance(v, str):
            print(f"error: en.json must be string keys and string values, bad entry: {k!r}", file=sys.stderr)
            return 1

    errors = 0
    json_files = sorted(locales_dir.glob("*.json"))
    if not json_files:
        print(f"error: no JSON files in {locales_dir}", file=sys.stderr)
        return 1

    for path in json_files:
        try:
            with path.open(encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            print(f"error: {path.name}: invalid JSON — {e}", file=sys.stderr)
            errors += 1
            continue

        if not isinstance(data, dict):
            print(f"error: {path.name}: root must be a JSON object", file=sys.stderr)
            errors += 1
            continue

        for k, v in data.items():
            if not isinstance(k, str) or not isinstance(v, str):
                print(f"error: {path.name}: must use string keys and string values", file=sys.stderr)
                errors += 1
                break

        keys = set(data)
        missing = en_keys - keys
        extra = keys - en_keys
        if missing:
            print(f"error: {path.name}: missing keys ({len(missing)}):", file=sys.stderr)
            for k in sorted(missing)[:20]:
                print(f"  - {k}", file=sys.stderr)
            if len(missing) > 20:
                print(f"  - … and {len(missing) - 20} more", file=sys.stderr)
            errors += 1
        if extra:
            print(f"error: {path.name}: extra keys ({len(extra)}):", file=sys.stderr)
            for k in sorted(extra)[:20]:
                print(f"  - {k}", file=sys.stderr)
            if len(extra) > 20:
                print(f"  - … and {len(extra) - 20} more", file=sys.stderr)
            errors += 1

        if not missing and not extra:
            print(f"ok {path.name} ({len(keys)} keys)")

    if errors:
        print(f"\nvalidation failed with {errors} error(s)", file=sys.stderr)
        return 1

    print(f"all {len(json_files)} locale file(s) match en.json ({len(en_keys)} keys)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
