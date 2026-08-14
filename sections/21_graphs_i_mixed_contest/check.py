"""Friendly checker for Section 21."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_existing_network",
    SECTION / "problems" / "b_build_timeline",
    SECTION / "problems" / "c_one_way_reversals",
    SECTION / "problems" / "d_reliable_link",
    SECTION / "problems" / "e_station_coverage_report",
    SECTION / "problems" / "f_component_repair",
    SECTION / "problems" / "g_alternating_road_route",
]

def main() -> int:
    return run_section_checks(21, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
