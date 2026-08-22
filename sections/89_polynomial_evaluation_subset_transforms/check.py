from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_multipoint_evaluation',
        'b_polynomial_interpolation',
        'c_xor_convolution',
        'd_subset_convolution',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(89,PROBLEMS,ROOT))
