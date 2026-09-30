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
    SECTION / "problems" / "b_range_assign_add",
    SECTION / "problems" / "c_static_rectangle_count",
    SECTION / "problems" / "d_nested_ranges_count",
    SECTION / "problems" / "e_subtree_add_point_query",
    SECTION / "problems" / "f_dynamic_subtree_maximum",
    SECTION / "problems" / "g_subtree_value_count",
    SECTION / "problems" / "h_incremental_connectivity",
    SECTION / "problems" / "i_subtree_assign_add_sum",
    SECTION / "problems" / "j_static_vertex_path_sums",
    SECTION / "problems" / "k_static_weighted_rectangles",
    SECTION / "problems" / "l_subtree_add_maximum",
]

def main() -> int:
    return run_section_checks(42, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
