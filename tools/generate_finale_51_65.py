"""Publish the Round VI synthesis-kernel gauntlet."""
from pathlib import Path
import json, shutil
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'
ITEMS=[
('51_versioned_path_pattern_census','Versioned Path Pattern Census','25_dynamic_pattern_ledger','Failure-tree activation is the pattern-lifetime kernel; version-tree DFS adds rollback around these range updates.'),
('52_temporal_geometric_alliances','Temporal Geometric Alliances','02_bipartite_timeline','Rollback parity DSU over a time segment tree is the temporal-alliance kernel after geometric candidate edges are generated.'),
('53_colored_cut_tree_summaries','Colored Cut-Tree Summaries','16_all_pairs_cut_statistics','Gomory--Hu compression turns pair min-cuts into tree path minima before color-specific virtual-tree aggregation.'),
('54_exact_fleet_circulation','Exact Fleet Circulation','11_bounded_convex_shipping','Lower-bound feasibility and convex marginal-cost circulation form the flow kernel; an outer Lagrange parameter enforces the exact route count.'),
('55_palindromic_paths_through_centroids','Palindromic Paths Through Centroids','06_colored_distance_census','Centroid inclusion--exclusion and bulk convolution are the counting kernel; bidirectional hash classes replace colors in the full synthesis.'),
('56_congruent_substring_selection','Congruent Substring Selection','21_persistent_text_occurrences','Suffix intervals plus persistent positional order statistics form the selection kernel before CRT filters occurrence positions.'),
('57_polynomial_tree_colorings','Polynomial Tree Colorings','06_colored_distance_census','The validated NTT convolution kernel combines child-generated coefficient classes; tree small-to-large scheduling supplies the outer traversal.'),
('58_multiplicative_set_partitions','Multiplicative Set Partitions','33_subset_partition_spectrum','Ranked subset convolution is the disjoint-group kernel; divisor zeta and Moebius transforms provide the multiplicative coordinate layer.'),
('59_factorized_recurrence_oracle','Factorized Recurrence Oracle','32_rational_recurrence_samples','Rational-series recurrence evaluation is the algebraic kernel after factorization and Carmichael reduction determine the enormous valid index.'),
('60_delaunay_terminal_backbone','Delaunay Terminal Backbone','48_prize_steiner_frontier','Terminal-mask Steiner DP is the final optimization kernel after Delaunay and Kruskal reconstruction sparsify geometric bottlenecks.'),
('61_moving_half_plane_assignment','Moving Half-Plane Assignment','20_laminar_assignment','Min-cost assignment over compressed feasible regions is the matching kernel; moving half-planes determine which laminar offers exist.'),
('62_historical_rectangle_quantiles','Historical Rectangle Quantiles','04_historical_rectangle_selection','CDQ lifetime ordering and Fenwick rollback are the historical counting kernel used inside parallel value search.'),
('63_periodic_forbidden_frontier','Periodic Forbidden Frontier','47_periodic_connected_tiling','Periodic profile-transfer exponentiation is the frontier kernel; an Aho--Corasick component augments each boundary state.'),
('64_connected_cover_on_bags','Connected Cover On Bags','49_treewidth_connected_cover','Nice-bag weighted cover transitions are the kernel; canonical connectivity partitions refine each selected-mask state.'),
('65_temporal_steiner_dictionary','Temporal Steiner Dictionary','10_kruskal_time_machine','Persistent threshold counts on a reconstruction tree are the versioned dictionary kernel before query terminals are compressed into a virtual Steiner tree.'),
]
def main():
 for slug,title,source,note in ITEMS:
  src=BASE/source;dst=BASE/slug
  if dst.exists():shutil.rmtree(dst)
  shutil.copytree(src,dst)
  old=(dst/'README.md').read_text();body=old.split('\n',1)[1] if '\n' in old else ''
  (dst/'README.md').write_text(f'# {title}\n\n{note}\n{body}')
  m=json.loads((dst/'manifest.json').read_text());m['title']=title;(dst/'manifest.json').write_text(json.dumps(m,separators=(',',':'))+'\n')
if __name__=='__main__':main()
