"""Run every available section checker in numerical order."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    checkers = sorted((ROOT / "sections").glob("[0-9][0-9]_*/check.py"))
    if not checkers:
        print("No section checkers were found.")
        return 1

    for checker in checkers:
        print(f"\n=== {checker.parent.name} ===", flush=True)
        result = subprocess.run([sys.executable, str(checker)], cwd=ROOT)
        if result.returncode:
            print(f"\nStopped at {checker.parent.name}.")
            return result.returncode

    print("\nAll available sections pass.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

