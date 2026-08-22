"""Friendly checker for Section 67."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks
SECTION = Path(__file__).resolve().parent
PROBLEMS = [SECTION / "problems" / name for name in (
    "a_branching_multiset", "b_versioned_range_add", "c_dynamic_connectivity",
    "d_tree_path_kth",
)]
if __name__ == "__main__":
    raise SystemExit(run_section_checks(67, PROBLEMS, ROOT))
