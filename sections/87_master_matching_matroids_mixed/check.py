from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_bottleneck_assignment',
        'b_roommate_rescue',
        'c_cut_threshold_pairs',
        'd_rainbow_spanning_tree',
        'e_broadcast_backbone',
        'f_two_map_forest',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(87,PROBLEMS,ROOT))
