"""Friendly checker for Section 42."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_dynamic_order_statistics",
    SECTION / "problems" / "b_range_add_range_sum",
    SECTION / "problems" / "c_static_rectangle_count",
    SECTION / "problems" / "d_nested_ranges_count",
    SECTION / "problems" / "e_subtree_add_point_query",
    SECTION / "problems" / "f_dynamic_path_maximum",
    SECTION / "problems" / "g_subtree_value_count",
    SECTION / "problems" / "h_connectivity_countdown",
    SECTION / "problems" / "i_persistent_version_sums",
    SECTION / "problems" / "j_subtree_kth_smallest",
    SECTION / "problems" / "k_sparse_rectangle_sums",
    SECTION / "problems" / "l_path_add_path_maximum",
]

def main() -> int:
    return run_section_checks(42, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
