"""Friendly checker for Section 16."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_subtree_sizes",
    SECTION / "problems" / "b_undirected_cycle",
    SECTION / "problems" / "c_directed_cycle",
    SECTION / "problems" / "d_component_audit",
]

def main() -> int:
    return run_section_checks(16, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
