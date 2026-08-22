"""Friendly checker for Section 68."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/name for name in (
    "a_path_affine_composition","b_toggle_nearest_beacon",
    "c_marked_pair_distances","d_subtree_mode_sum")]
if __name__=="__main__":raise SystemExit(run_section_checks(68,PROBLEMS,ROOT))
