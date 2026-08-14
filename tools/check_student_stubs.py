"""Fail if a public student stub contains personal solution code."""

from __future__ import annotations

from pathlib import Path

from manage_submissions import CPP_STUB, PYTHON_STUB, ROOT, submission_files


def main() -> int:
    invalid: list[Path] = []
    for path in submission_files():
        expected = CPP_STUB if path.suffix == ".cpp" else PYTHON_STUB
        if path.read_text(encoding="utf-8") != expected:
            invalid.append(path.relative_to(ROOT))

    if invalid:
        print("Personal code was found in public student stubs:")
        for path in invalid:
            print(f"- {path}")
        print("Run: python3 tools/manage_submissions.py migrate")
        return 1

    print(f"All {len(submission_files())} public student stubs are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
