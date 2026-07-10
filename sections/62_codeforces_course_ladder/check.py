#!/usr/bin/env python3
"""Validate the artifacts of the external Codeforces ladder."""

from pathlib import Path


ROOT = Path(__file__).resolve().parent
REQUIRED = ("EXTERNAL_ONLY.md", "README.md", "PRACTICE.md", "problem_sheet.qmd", "lesson.qmd", "editorial.qmd")


def main() -> None:
    missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
    if missing:
        raise SystemExit(f"Section 62: missing {', '.join(missing)}")
    print("Section 62: external ladder artifacts are present. Submit the linked tasks on Codeforces.")


if __name__ == "__main__":
    main()
