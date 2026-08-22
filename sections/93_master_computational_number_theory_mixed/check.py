from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_largest_prime_fragment',
        'b_carmichael_clock',
        'c_multiplicative_order',
        'd_power_congruence',
        'e_quadratic_residue_archive',
        'f_affine_exponent_meeting',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(93,PROBLEMS,ROOT))
