from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_unique_sink_population',
        'b_strong_connectivity_repairs',
        'c_eulerian_word_chain',
        'd_robbins_orientation',
        'e_failed_vertex_routes',
        'f_dominator_subtree_queries',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(81,PROBLEMS,ROOT))
