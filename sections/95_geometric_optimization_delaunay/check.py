from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_minimum_enclosing_circle',
        'b_delaunay_radius_sum',
        'c_euclidean_network',
        'd_largest_empty_delaunay_circle',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(95,PROBLEMS,ROOT))
