"""Friendly checker for Section 14."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_complete_window",
    SECTION / "problems" / "b_minimum_split_limit",
    SECTION / "problems" / "c_active_colors",
    SECTION / "problems" / "d_first_free_slot",
    SECTION / "problems" / "e_smallest_distinct_subsequence",
    SECTION / "problems" / "f_adjacent_cancellation",
    SECTION / "problems" / "g_next_smaller_distance",
    SECTION / "problems" / "h_smallest_fixed_subsequence",
    SECTION / "problems" / "i_wildcard_parentheses",
    SECTION / "problems" / "j_interval_point_cover",
    SECTION / "problems" / "k_deadline_selection",
    SECTION / "problems" / "l_smallest_after_deletions",
    SECTION / "problems" / "m_required_letter_subsequence",
    SECTION / "problems" / "n_wildcard_choice_map",
    SECTION / "problems" / "o_minimum_parenthesis_depth",
    SECTION / "problems" / "p_common_deadline",
    SECTION / "problems" / "q_event_attendance",
    SECTION / "problems" / "r_coverage_patches",
    SECTION / "problems" / "s_advantage_assignment",
    SECTION / "problems" / "t_minimum_refueling",
    SECTION / "problems" / "u_circular_fuel_start",
    SECTION / "problems" / "v_smallest_separated_rearrangement",
    SECTION / "problems" / "w_consecutive_grouping",
    SECTION / "problems" / "x_subarray_minimum_total",
    SECTION / "problems" / "y_maximum_width_ramp",
    SECTION / "problems" / "z_smallest_alternating_partition",
]

def main() -> int:
    return run_section_checks(14, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
