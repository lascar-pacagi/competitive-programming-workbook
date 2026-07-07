"""Friendly checker for Section 27."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_skill_coverage",
    SECTION / "problems" / "b_assignment_profit",
    SECTION / "problems" / "c_inspection_route",
]


def main() -> int:
    target = os.environ.get("CP_TARGET", "student")
    print(f"Section 27: checking {target} submissions...\n", flush=True)
    for problem in PROBLEMS:
        for lang in ("cpp", "py"):
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/judge.py",
                    str(problem),
                    "--lang",
                    lang,
                    "--random-count",
                    "25",
                ],
                cwd=ROOT,
            )
            if result.returncode:
                print("\nThe checker stopped at the first failure. Fix that problem/language and run again.")
                return result.returncode
    print("\nSection 27 complete: all checked submissions were accepted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
