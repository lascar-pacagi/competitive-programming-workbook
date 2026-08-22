from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_quantile_prefix_sum',
        'b_clamped_terrain',
        'c_reversible_string_hash',
        'd_dynamic_forest_sum',
        'e_earliest_connection',
        'f_affine_forest_paths',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(84,PROBLEMS,ROOT))
