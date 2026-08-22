from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_prime_or_composite',
        'b_complete_factorization',
        'c_large_totient',
        'd_large_divisor_statistics',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(91,PROBLEMS,ROOT))
