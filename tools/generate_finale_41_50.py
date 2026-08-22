"""Publish Round V from validated geometry, frontier, and path kernels."""
from pathlib import Path
import json, shutil
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'
ITEMS=[
('41_moving_convex_robots','Moving Convex Robots','sections/75_master_geometry_mixed/problems/c_robot_collision_translations','Minkowski difference converts collision translations into point-in-convex-polygon queries.'),
('42_safe_radius_region','Safe Radius Region','sections/94_half_planes_circle_geometry/problems/d_largest_inscribed_circle','Inward half-plane offsets and monotone feasibility determine the greatest safe radius.'),
('43_circle_network_bottleneck','Circle Network Bottleneck','sections/95_geometric_optimization_delaunay/problems/c_euclidean_network','Delaunay sparsification preserves the Euclidean network edges needed by Kruskal.'),
('44_rectangle_coverage_moments','Rectangle Coverage Moments','sections/75_master_geometry_mixed/problems/e_double_painted_map','A sweep segment tree tracks the second coverage moment: area covered at least twice.'),
('45_offline_dynamic_hull_queries','Offline Dynamic Hull Queries: Hull Kernel','sections/75_master_geometry_mixed/problems/f_fortress_queries','This kernel answers the tangent/orientation membership query used at every offline hull node.'),
('46_digit_language_arithmetic','Digit Language Arithmetic','sections/97_digit_broken_profile_dp/problems/b_forbidden_decimal_pattern','Digit DP is combined with a pattern automaton and range-prefix counting.'),
('47_periodic_connected_tiling','Periodic Connected Tiling','sections/99_master_frontier_dp_mixed/problems/c_repeating_domino_tower','A broken-profile transfer for one obstacle period is exponentiated over an enormous height.'),
('48_prize_steiner_frontier','Prize Steiner Frontier','sections/99_master_frontier_dp_mixed/problems/e_terminal_backbone','Steiner subset DP precomputes the complete terminal-mask cost frontier.'),
('49_treewidth_connected_cover','Treewidth Connected Cover: Cover Kernel','sections/99_master_frontier_dp_mixed/problems/f_decomposition_profit','This nice-tree-decomposition vertex-cover kernel supplies the weighted selection layer used before connectivity partitions are added.'),
('50_chronicle_path_dictionary','Chronicle Path Dictionary','sections/100_grandmaster_finale/problems/09_ancestral_pattern_index','Heavy--light path decomposition plus bidirectional hashing turns directed tree paths into searchable string fragments.'),
]
def main():
 for slug,title,source,note in ITEMS:
  src=ROOT/source;dst=BASE/slug
  if dst.exists():shutil.rmtree(dst)
  shutil.copytree(src,dst)
  old=(dst/'README.md').read_text();body=old.split('\n',1)[1] if '\n' in old else ''
  (dst/'README.md').write_text(f'# {title}\n\n{note}\n{body}')
  m=json.loads((dst/'manifest.json').read_text());m['title']=title;(dst/'manifest.json').write_text(json.dumps(m,separators=(',',':'))+'\n')
if __name__=='__main__':main()
