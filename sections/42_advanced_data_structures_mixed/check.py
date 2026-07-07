"""Friendly checker for Section 42."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_dynamic_order_statistics",
    SECTION / "problems" / "b_range_add_range_sum",
    SECTION / "problems" / "c_static_rectangle_count",
]

def main() -> int:
    target = os.environ.get("CP_TARGET", "student")
    print(f"Section 42: checking {target} submissions...\n", flush=True)
    for problem in PROBLEMS:
        for lang in ("cpp", "py"):
            result = subprocess.run([sys.executable, "tools/judge.py", str(problem), "--lang", lang, "--random-count", "25"], cwd=ROOT)
            if result.returncode:
                return result.returncode
    print("\nSection 42 complete: all checked submissions were accepted.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
