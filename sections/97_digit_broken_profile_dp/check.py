from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_digit_sum_range',
        'b_forbidden_decimal_pattern',
        'c_obstacle_domino_tilings',
        'd_grid_independent_sets',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(97,PROBLEMS,ROOT))
