from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_half_plane_region',
        'b_circle_overlap',
        'c_common_tangent_count',
        'd_largest_inscribed_circle',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(94,PROBLEMS,ROOT))
