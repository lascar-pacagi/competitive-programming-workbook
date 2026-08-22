from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_series_inverse',
        'b_series_logarithm',
        'c_series_exponential',
        'd_series_square_root',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(88,PROBLEMS,ROOT))
