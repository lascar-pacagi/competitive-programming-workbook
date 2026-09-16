"""Friendly checker for Section 40."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_hotel_queries",
    SECTION / "problems" / "b_list_removals",
    SECTION / "problems" / "c_range_add_range_gcd",
    SECTION / "problems" / "d_salary_queries",
    SECTION / "problems" / "e_functional_walk_minimum",
    SECTION / "problems" / "f_mutable_priority_queue",
    SECTION / "problems" / "g_streaming_room_count",
    SECTION / "problems" / "h_toggle_kth_active",
    SECTION / "problems" / "i_dynamic_maximum_subarray",
    SECTION / "problems" / "j_sliding_median_cost",
    SECTION / "problems" / "k_budget_prefix_search",
    SECTION / "problems" / "l_range_add_threshold_search",
]

def main() -> int:
    return run_section_checks(40, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
