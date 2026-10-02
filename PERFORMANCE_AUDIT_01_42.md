# Performance test audit: sections 1–42

Examined 234 local problems using fixed tests, 25 random cases per generator (seed 20261001), and dedicated performance generators.

Dedicated performance generators: 234/234. Generator failures: 0.

The normal judge runs these tests even with `--random-count 0`, under each manifest's existing per-case deadline. Sections 1–41 use the explicit profile registry in `tools/course_performance_profiles.json`; section 42 uses its own construction generators. Existing large cases are preserved as dedicated tests, independent of the requested random count.

## Workload review

The added cases exercise constraint-scale arrays, query streams, long trees, dense graphs, grids, sieve bounds, DP dimensions, and bounded exponential searches. Expected answers come from construction identities or existing generator oracles. Small randomized cases remain useful for correctness.

199 problems produced an input of at least 100 KB; 35 did not. File size is only an inventory aid: a scalar limit, cubic DP, or subset search can require substantial work from a small input. Dedicated cases were reviewed against the individual constraints rather than this byte threshold.

Section 42 H includes three n=q=200000 workloads: growing paths, reversed unions, and disconnected paths. BFS-per-query implementations in both C++ and Python exceeded the existing 3-second deadline. A C++ linear range-sum implementation passed section 36 A’s sample but exceeded its 2-second deadline on the dedicated varying-range workload.

## Reference validation

Checked 234 problems in C++ and Python: 1412 fixed/performance executions, 0 failures.

The new workloads exposed two Python reference bottlenecks. Section 20 C (Warp Maze) now uses a padded flat grid, rejects stale 0-1 BFS entries, and stops when the goal is settled. Its tests include an unreachable goal that requires exploring a million-cell region. Section 35 O (GCD Sum) now preprocesses answers using smallest prime factors and the prime-power recurrence, replacing divisor scans per query. Its test uses 200000 distinct large queries. Both editorials were updated; no time limits or course prerequisites were changed.

Reference validation used three workers for the full course; final revised cases were rechecked sequentially. For reproducible local timing, use one worker. These checks establish reference acceptance on this machine, not a machine-independent guarantee that every slower approach will be rejected.

## Reproduce

```bash
python3 tools/check_performance_tests.py --through 42 --workers 1 --output /tmp/performance-reference-results.json
python3 tools/audit_performance_tests.py --through 42 --count 25 --seed 20261001 --output /tmp/performance-audit.json --report PERFORMANCE_AUDIT_01_42.md --validation /tmp/performance-reference-results.json
```

## Inventory

Every row records actual generated/fixed input size and the presence of a dedicated generator. Input names refer to temporary generated files when the kind is random or stress.

| Problem | Cases | Largest input (bytes) | First line | Evidence |
|---|---:|---:|---|---|
| [01 a_sum_constraints](sections/01_complexity_io_constraints/problems/a_sum_constraints/README.md) | 28 | 2200009 | `1` | dedicated stress |
| [01 b_until_threshold](sections/01_complexity_io_constraints/problems/b_until_threshold/README.md) | 28 | 4400007 | `200000` | dedicated stress |
| [01 c_token_budget](sections/01_complexity_io_constraints/problems/c_token_budget/README.md) | 28 | 6200007 | `200000` | dedicated stress |
| [01 d_batch_pages](sections/01_complexity_io_constraints/problems/d_batch_pages/README.md) | 28 | 4400007 | `200000` | dedicated stress |
| [02 a_robot_walk](sections/02_simulation_bruteforce/problems/a_robot_walk/README.md) | 28 | 200003 | `1` | dedicated stress |
| [02 b_ticket_split](sections/02_simulation_bruteforce/problems/b_ticket_split/README.md) | 28 | 1704 | `100` | dedicated stress |
| [02 c_best_subset](sections/02_simulation_bruteforce/problems/c_best_subset/README.md) | 28 | 479 | `12` | dedicated stress |
| [02 d_carousel_visits](sections/02_simulation_bruteforce/problems/d_carousel_visits/README.md) | 28 | 100016 | `1` | dedicated stress |
| [03 a_value_counts](sections/03_counting_frequencies/problems/a_value_counts/README.md) | 28 | 1177796 | `1` | dedicated stress |
| [03 b_frequency_winner](sections/03_counting_frequencies/problems/b_frequency_winner/README.md) | 28 | 1288904 | `1` | dedicated stress |
| [03 c_pair_sum_count](sections/03_counting_frequencies/problems/c_pair_sum_count/README.md) | 28 | 400011 | `1` | dedicated stress |
| [03 d_equal_index_pairs](sections/03_counting_frequencies/problems/d_equal_index_pairs/README.md) | 28 | 400009 | `1` | dedicated stress |
| [04 a_range_sum_queries](sections/04_prefix_difference/problems/a_range_sum_queries/README.md) | 28 | 1488912 | `1` | dedicated stress |
| [04 b_range_add_final_array](sections/04_prefix_difference/problems/b_range_add_final_array/README.md) | 28 | 1100016 | `1` | dedicated stress |
| [04 c_subarray_sum_count](sections/04_prefix_difference/problems/c_subarray_sum_count/README.md) | 28 | 400011 | `1` | dedicated stress |
| [04 d_signal_peak](sections/04_prefix_difference/problems/d_signal_peak/README.md) | 28 | 2200014 | `200000 200000` | dedicated stress |
| [05 a_min_adjacent_gap](sections/05_sorting_as_tool/problems/a_min_adjacent_gap/README.md) | 28 | 1288904 | `1` | dedicated stress |
| [05 b_rank_table](sections/05_sorting_as_tool/problems/b_rank_table/README.md) | 28 | 1800009 | `1` | dedicated stress |
| [05 c_merge_intervals](sections/05_sorting_as_tool/problems/c_merge_intervals/README.md) | 28 | 2577799 | `1` | dedicated stress |
| [05 d_compact_team](sections/05_sorting_as_tool/problems/d_compact_team/README.md) | 28 | 1288911 | `1` | dedicated stress |
| [06 a_sorted_two_sum](sections/06_two_pointers_sliding_windows/problems/a_sorted_two_sum/README.md) | 28 | 1288902 | `1` | dedicated stress |
| [06 b_longest_bounded_window](sections/06_two_pointers_sliding_windows/problems/b_longest_bounded_window/README.md) | 28 | 400016 | `1` | dedicated stress |
| [06 c_count_subarrays_at_most](sections/06_two_pointers_sliding_windows/problems/c_count_subarrays_at_most/README.md) | 28 | 400016 | `1` | dedicated stress |
| [06 d_cover_all_labels](sections/06_two_pointers_sliding_windows/problems/d_cover_all_labels/README.md) | 28 | 1288911 | `1` | dedicated stress |
| [07 a_inventory_cleanup](sections/07_foundation_mixed_contest/problems/a_inventory_cleanup/README.md) | 28 | 1288906 | `1` | dedicated stress |
| [07 b_peak_load](sections/07_foundation_mixed_contest/problems/b_peak_load/README.md) | 28 | 1100016 | `1` | dedicated stress |
| [07 c_best_study_streak](sections/07_foundation_mixed_contest/problems/c_best_study_streak/README.md) | 28 | 400016 | `1` | dedicated stress |
| [07 d_balanced_break](sections/07_foundation_mixed_contest/problems/d_balanced_break/README.md) | 28 | 400009 | `1` | dedicated stress |
| [07 e_circular_patrol](sections/07_foundation_mixed_contest/problems/e_circular_patrol/README.md) | 27 | 100012 | `1` | dedicated stress |
| [08 a_square_threshold](sections/08_binary_search_answer/problems/a_square_threshold/README.md) | 28 | 3800007 | `200000` | dedicated stress |
| [08 b_max_min_distance](sections/08_binary_search_answer/problems/b_max_min_distance/README.md) | 28 | 1288906 | `1` | dedicated stress |
| [08 c_minimum_capacity](sections/08_binary_search_answer/problems/c_minimum_capacity/README.md) | 28 | 400011 | `1` | dedicated stress |
| [08 d_factory_deadline](sections/08_binary_search_answer/problems/d_factory_deadline/README.md) | 28 | 400020 | `1` | dedicated stress |
| [09 a_activity_selection](sections/09_greedy_exchange/problems/a_activity_selection/README.md) | 28 | 2577794 | `1` | dedicated stress |
| [09 b_rescue_boats](sections/09_greedy_exchange/problems/b_rescue_boats/README.md) | 28 | 400011 | `1` | dedicated stress |
| [09 c_deadline_schedule](sections/09_greedy_exchange/problems/c_deadline_schedule/README.md) | 28 | 1800009 | `1` | dedicated stress |
| [09 d_workshop_badges](sections/09_greedy_exchange/problems/d_workshop_badges/README.md) | 28 | 2577789 | `1` | dedicated stress |
| [10 a_non_decreasing_repairs](sections/10_greedy_constructive/problems/a_non_decreasing_repairs/README.md) | 28 | 1288904 | `1` | dedicated stress |
| [10 b_bracket_completion](sections/10_greedy_constructive/problems/b_bracket_completion/README.md) | 28 | 200003 | `1` | dedicated stress |
| [10 c_bounded_sum_sequence](sections/10_greedy_constructive/problems/c_bounded_sum_sequence/README.md) | 28 | 126 | `19` | dedicated stress |
| [10 d_pattern_permutation](sections/10_greedy_constructive/problems/d_pattern_permutation/README.md) | 28 | 200009 | `1` | dedicated stress |
| [11 a_peak_active](sections/11_intervals_sweep_line/problems/a_peak_active/README.md) | 28 | 1800009 | `1` | dedicated stress |
| [11 b_covered_length](sections/11_intervals_sweep_line/problems/b_covered_length/README.md) | 28 | 2577794 | `1` | dedicated stress |
| [11 c_point_coverage](sections/11_intervals_sweep_line/problems/c_point_coverage/README.md) | 28 | 1488906 | `1` | dedicated stress |
| [11 d_first_busiest](sections/11_intervals_sweep_line/problems/d_first_busiest/README.md) | 28 | 800009 | `1` | dedicated stress |
| [12 a_next_greater](sections/12_stacks_queues_deques/problems/a_next_greater/README.md) | 28 | 1288904 | `1` | dedicated stress |
| [12 b_sliding_window_max](sections/12_stacks_queues_deques/problems/b_sliding_window_max/README.md) | 28 | 1288906 | `1` | dedicated stress |
| [12 c_shortest_subarray_at_least](sections/12_stacks_queues_deques/problems/c_shortest_subarray_at_least/README.md) | 28 | 400016 | `1` | dedicated stress |
| [12 d_bounded_spread_subarrays](sections/12_stacks_queues_deques/problems/d_bounded_spread_subarrays/README.md) | 28 | 400011 | `1` | dedicated stress |
| [13 a_coordinate_compression](sections/13_offline_processing/problems/a_coordinate_compression/README.md) | 28 | 1288899 | `1` | dedicated stress |
| [13 b_range_count_at_most](sections/13_offline_processing/problems/b_range_count_at_most/README.md) | 28 | 2188906 | `1` | dedicated stress |
| [13 c_distinct_range_queries](sections/13_offline_processing/problems/c_distinct_range_queries/README.md) | 28 | 1877801 | `1` | dedicated stress |
| [13 d_activation_totals](sections/13_offline_processing/problems/d_activation_totals/README.md) | 28 | 2977794 | `200000 200000` | dedicated stress |
| [14 a_complete_window](sections/14_core_patterns_mixed_contest/problems/a_complete_window/README.md) | 28 | 1288911 | `1` | dedicated stress |
| [14 b_minimum_split_limit](sections/14_core_patterns_mixed_contest/problems/b_minimum_split_limit/README.md) | 28 | 400011 | `1` | dedicated stress |
| [14 c_active_colors](sections/14_core_patterns_mixed_contest/problems/c_active_colors/README.md) | 28 | 2077801 | `1` | dedicated stress |
| [14 d_first_free_slot](sections/14_core_patterns_mixed_contest/problems/d_first_free_slot/README.md) | 28 | 2688908 | `1` | dedicated stress |
| [14 e_smallest_distinct_subsequence](sections/14_core_patterns_mixed_contest/problems/e_smallest_distinct_subsequence/README.md) | 27 | 200003 | `1` | dedicated stress |
| [14 f_adjacent_cancellation](sections/14_core_patterns_mixed_contest/problems/f_adjacent_cancellation/README.md) | 27 | 200004 | `2` | dedicated stress |
| [14 g_next_smaller_distance](sections/14_core_patterns_mixed_contest/problems/g_next_smaller_distance/README.md) | 27 | 1288902 | `200000` | dedicated stress |
| [14 h_smallest_fixed_subsequence](sections/14_core_patterns_mixed_contest/problems/h_smallest_fixed_subsequence/README.md) | 27 | 200008 | `zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfe` | dedicated stress |
| [14 i_wildcard_parentheses](sections/14_core_patterns_mixed_contest/problems/i_wildcard_parentheses/README.md) | 27 | 200004 | `2` | dedicated stress |
| [14 j_interval_point_cover](sections/14_core_patterns_mixed_contest/problems/j_interval_point_cover/README.md) | 27 | 2577802 | `200000` | dedicated stress |
| [14 k_deadline_selection](sections/14_core_patterns_mixed_contest/problems/k_deadline_selection/README.md) | 27 | 2756582 | `200000` | dedicated stress |
| [14 l_smallest_after_deletions](sections/14_core_patterns_mixed_contest/problems/l_smallest_after_deletions/README.md) | 27 | 200008 | `3558961923120276353944635038347725680769711762628407709379872749331333095371559127778574882357073380` | dedicated stress |
| [14 m_required_letter_subsequence](sections/14_core_patterns_mixed_contest/problems/m_required_letter_subsequence/README.md) | 27 | 200015 | `zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfe` | dedicated stress |
| [14 n_wildcard_choice_map](sections/14_core_patterns_mixed_contest/problems/n_wildcard_choice_map/README.md) | 27 | 200001 | `????????????????????????????????????????????????????????????????????????????????????????????????????` | dedicated stress |
| [14 o_minimum_parenthesis_depth](sections/14_core_patterns_mixed_contest/problems/o_minimum_parenthesis_depth/README.md) | 30 | 200001 | `????????????????????????????????????????????????????????????????????????????????????????????????????` | dedicated stress |
| [14 p_common_deadline](sections/14_core_patterns_mixed_contest/problems/p_common_deadline/README.md) | 27 | 1978091 | `200000 1000000000000000000` | dedicated stress |
| [14 q_event_attendance](sections/14_core_patterns_mixed_contest/problems/q_event_attendance/README.md) | 27 | 3956135 | `200000` | dedicated stress |
| [14 r_coverage_patches](sections/14_core_patterns_mixed_contest/problems/r_coverage_patches/README.md) | 27 | 3777803 | `200000 1000000000000000000` | dedicated stress |
| [14 s_advantage_assignment](sections/14_core_patterns_mixed_contest/problems/s_advantage_assignment/README.md) | 27 | 4155856 | `200000` | dedicated stress |
| [14 t_minimum_refueling](sections/14_core_patterns_mixed_contest/problems/t_minimum_refueling/README.md) | 27 | 5755819 | `1000000000000000000 1 200000` | dedicated stress |
| [14 u_circular_fuel_start](sections/14_core_patterns_mixed_contest/problems/u_circular_fuel_start/README.md) | 27 | 3955780 | `200000` | dedicated stress |
| [14 v_smallest_separated_rearrangement](sections/14_core_patterns_mixed_contest/problems/v_smallest_separated_rearrangement/README.md) | 27 | 200001 | `hklqswumzdtegyxcvebfomgkgsiimzygkahzrhxipoflmqwxbomsupddvpmfnwfuxqjbpoawshovsqoepxishhcgggbskygodlks` | dedicated stress |
| [14 w_consecutive_grouping](sections/14_core_patterns_mixed_contest/problems/w_consecutive_grouping/README.md) | 27 | 2077771 | `200000` | dedicated stress |
| [14 x_subarray_minimum_total](sections/14_core_patterns_mixed_contest/problems/x_subarray_minimum_total/README.md) | 27 | 1378020 | `200000` | dedicated stress |
| [14 y_maximum_width_ramp](sections/14_core_patterns_mixed_contest/problems/y_maximum_width_ramp/README.md) | 27 | 2077771 | `200000` | dedicated stress |
| [14 z_smallest_alternating_partition](sections/14_core_patterns_mixed_contest/problems/z_smallest_alternating_partition/README.md) | 27 | 200001 | `0111000000011010111010001110110111001101010110011011000000010101100111111001101000110000110001100100` | dedicated stress |
| [15 a_connected_groups](sections/15_bfs_unweighted_shortest_paths/problems/a_connected_groups/README.md) | 28 | 2577797 | `1` | dedicated stress |
| [15 b_unweighted_routes](sections/15_bfs_unweighted_shortest_paths/problems/b_unweighted_routes/README.md) | 28 | 3866699 | `200000 199999 1 200000` | dedicated stress |
| [15 c_grid_rescue_path](sections/15_bfs_unweighted_shortest_paths/problems/c_grid_rescue_path/README.md) | 29 | 1001010 | `1000 1000` | dedicated stress |
| [15 d_nearest_station](sections/15_bfs_unweighted_shortest_paths/problems/d_nearest_station/README.md) | 28 | 2577799 | `200000 199999 1` | dedicated stress |
| [16 a_subtree_sizes](sections/16_dfs_components_cycles/problems/a_subtree_sizes/README.md) | 29 | 2577788 | `200000` | dedicated stress |
| [16 b_undirected_cycle](sections/16_dfs_components_cycles/problems/b_undirected_cycle/README.md) | 29 | 2577795 | `200000 199999` | dedicated stress |
| [16 c_directed_cycle](sections/16_dfs_components_cycles/problems/c_directed_cycle/README.md) | 29 | 2577795 | `200000 199999` | dedicated stress |
| [16 d_component_audit](sections/16_dfs_components_cycles/problems/d_component_audit/README.md) | 29 | 2577804 | `200000 200000` | dedicated stress |
| [17 a_lexicographic_course_order](sections/17_topological_sorting_dag_dp/problems/a_lexicographic_course_order/README.md) | 29 | 635 | `55 111` | dedicated stress |
| [17 b_longest_dag_path](sections/17_topological_sorting_dag_dp/problems/b_longest_dag_path/README.md) | 29 | 2577795 | `200000 199999` | dedicated stress |
| [17 c_project_schedule](sections/17_topological_sorting_dag_dp/problems/c_project_schedule/README.md) | 29 | 4777796 | `200000 199999` | dedicated stress |
| [17 d_unique_build_order](sections/17_topological_sorting_dag_dp/problems/d_unique_build_order/README.md) | 29 | 2577795 | `200000 199999` | dedicated stress |
| [18 a_network_growth](sections/18_dsu_minimum_spanning_trees/problems/a_network_growth/README.md) | 28 | 2577804 | `200000 200000` | dedicated stress |
| [18 b_minimum_network](sections/18_dsu_minimum_spanning_trees/problems/b_minimum_network/README.md) | 29 | 4777784 | `200000 199999` | dedicated stress |
| [18 c_cluster_split](sections/18_dsu_minimum_spanning_trees/problems/c_cluster_split/README.md) | 29 | 2977800 | `200000 199999 100000` | dedicated stress |
| [18 d_cable_savings](sections/18_dsu_minimum_spanning_trees/problems/d_cable_savings/README.md) | 29 | 3055604 | `100001 200000` | dedicated stress |
| [19 a_weighted_route_queries](sections/19_dijkstra_weighted_modeling/problems/a_weighted_route_queries/README.md) | 28 | 6066688 | `200000 199999 1 200000` | dedicated stress |
| [19 b_grid_toll_path](sections/19_dijkstra_weighted_modeling/problems/b_grid_toll_path/README.md) | 28 | 2000010 | `1000 1000` | dedicated stress |
| [19 c_discount_route](sections/19_dijkstra_weighted_modeling/problems/c_discount_route/README.md) | 29 | 2977793 | `200000 199999` | dedicated stress |
| [19 d_even_hop_route](sections/19_dijkstra_weighted_modeling/problems/d_even_hop_route/README.md) | 29 | 2977799 | `200000 200000` | dedicated stress |
| [20 a_binary_weight_routes](sections/20_zero_one_bfs_variants/problems/a_binary_weight_routes/README.md) | 28 | 4266697 | `200000 199999 1 200000` | dedicated stress |
| [20 b_conveyor_grid](sections/20_zero_one_bfs_variants/problems/b_conveyor_grid/README.md) | 29 | 1001010 | `1000 1000` | dedicated stress |
| [20 c_warp_maze](sections/20_zero_one_bfs_variants/problems/c_warp_maze/README.md) | 30 | 1001010 | `1000 1000` | dedicated stress |
| [20 d_letter_portals](sections/20_zero_one_bfs_variants/problems/d_letter_portals/README.md) | 29 | 1001010 | `1000 1000` | dedicated stress |
| [21 a_existing_network](sections/21_graphs_i_mixed_contest/problems/a_existing_network/README.md) | 29 | 2977795 | `200000 0 199999` | dedicated stress |
| [21 b_build_timeline](sections/21_graphs_i_mixed_contest/problems/b_build_timeline/README.md) | 29 | 6066698 | `200000 199999 200000` | dedicated stress |
| [21 c_one_way_reversals](sections/21_graphs_i_mixed_contest/problems/c_one_way_reversals/README.md) | 29 | 2577795 | `200000 199999` | dedicated stress |
| [21 d_reliable_link](sections/21_graphs_i_mixed_contest/problems/d_reliable_link/README.md) | 29 | 2955604 | `100001 200000` | dedicated stress |
| [21 e_station_coverage_report](sections/21_graphs_i_mixed_contest/problems/e_station_coverage_report/README.md) | 27 | 2577799 | `200000 199999 1` | dedicated stress |
| [21 f_component_repair](sections/21_graphs_i_mixed_contest/problems/f_component_repair/README.md) | 27 | 2577781 | `200000 199998` | dedicated stress |
| [21 g_alternating_road_route](sections/21_graphs_i_mixed_contest/problems/g_alternating_road_route/README.md) | 27 | 3377791 | `200000 199999` | dedicated stress |
| [22 a_broken_stairs](sections/22_one_dimensional_dp/problems/a_broken_stairs/README.md) | 29 | 644459 | `200000 100000` | dedicated stress |
| [22 b_training_score](sections/22_one_dimensional_dp/problems/b_training_score/README.md) | 29 | 2200008 | `200000` | dedicated stress |
| [22 c_energy_route](sections/22_one_dimensional_dp/problems/c_energy_route/README.md) | 29 | 1288900 | `200000 50` | dedicated stress |
| [22 d_exact_change](sections/22_one_dimensional_dp/problems/d_exact_change/README.md) | 29 | 145 | `200000 20` | dedicated stress |
| [23 a_budget_selection](sections/23_knapsack_subset_dp/problems/a_budget_selection/README.md) | 29 | 2610 | `200 10000` | dedicated stress |
| [23 b_unlimited_training](sections/23_knapsack_subset_dp/problems/b_unlimited_training/README.md) | 29 | 2610 | `200 10000` | dedicated stress |
| [23 c_possible_sums](sections/23_knapsack_subset_dp/problems/c_possible_sums/README.md) | 29 | 505 | `100` | dedicated stress |
| [23 d_balanced_split](sections/23_knapsack_subset_dp/problems/d_balanced_split/README.md) | 29 | 805 | `200` | dedicated stress |
| [24 a_safe_paths](sections/24_grid_dp/problems/a_safe_paths/README.md) | 29 | 1001010 | `1000 1000` | dedicated stress |
| [24 b_lowest_toll](sections/24_grid_dp/problems/b_lowest_toll/README.md) | 29 | 11000010 | `1000 1000` | dedicated stress |
| [24 c_limited_turns](sections/24_grid_dp/problems/c_limited_turns/README.md) | 29 | 6489 | `80 80 40` | dedicated stress |
| [24 d_two_couriers](sections/24_grid_dp/problems/d_two_couriers/README.md) | 30 | 9806 | `70 70` | dedicated stress |
| [25 a_merge_piles](sections/25_interval_dp/problems/a_merge_piles/README.md) | 29 | 405 | `200` | dedicated stress |
| [25 b_palindrome_repairs](sections/25_interval_dp/problems/b_palindrome_repairs/README.md) | 29 | 1001 | `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` | dedicated stress |
| [25 c_treasure_balloons](sections/25_interval_dp/problems/c_treasure_balloons/README.md) | 29 | 1005 | `200` | dedicated stress |
| [25 d_endgame_advantage](sections/25_interval_dp/problems/d_endgame_advantage/README.md) | 29 | 33006 | `3000` | dedicated stress |
| [26 a_festival_invite](sections/26_tree_dp_basics/problems/a_festival_invite/README.md) | 29 | 4777789 | `200000` | dedicated stress |
| [26 b_road_pairing](sections/26_tree_dp_basics/problems/b_road_pairing/README.md) | 29 | 2577788 | `200000` | dedicated stress |
| [26 c_tree_colorings](sections/26_tree_dp_basics/problems/c_tree_colorings/README.md) | 29 | 2577788 | `200000` | dedicated stress |
| [26 d_road_guards](sections/26_tree_dp_basics/problems/d_road_guards/README.md) | 29 | 2977788 | `200000` | dedicated stress |
| [27 a_skill_coverage](sections/27_bitmask_dp/problems/a_skill_coverage/README.md) | 30 | 239 | `10 19` | dedicated stress |
| [27 b_assignment_profit](sections/27_bitmask_dp/problems/b_assignment_profit/README.md) | 29 | 3567 | `18` | dedicated stress |
| [27 c_inspection_route](sections/27_bitmask_dp/problems/c_inspection_route/README.md) | 29 | 515 | `16` | dedicated stress |
| [27 d_compatible_lineup](sections/27_bitmask_dp/problems/d_compatible_lineup/README.md) | 29 | 226 | `20 0` | dedicated stress |
| [28 a_training_schedule](sections/28_dp_i_mixed_contest/problems/a_training_schedule/README.md) | 29 | 400008 | `200000` | dedicated stress |
| [28 b_two_carts](sections/28_dp_i_mixed_contest/problems/b_two_carts/README.md) | 29 | 791 | `60 200 200` | dedicated stress |
| [28 c_prerequisite_tree](sections/28_dp_i_mixed_contest/problems/c_prerequisite_tree/README.md) | 29 | 1266 | `80 300` | dedicated stress |
| [28 d_circular_exhibition](sections/28_dp_i_mixed_contest/problems/d_circular_exhibition/README.md) | 29 | 400007 | `200000` | dedicated stress |
| [28 e_one_diagonal_path](sections/28_dp_i_mixed_contest/problems/e_one_diagonal_path/README.md) | 27 | 500008 | `500 500` | dedicated stress |
| [28 f_matrix_chain](sections/28_dp_i_mixed_contest/problems/f_matrix_chain/README.md) | 27 | 3011 | `500` | dedicated stress |
| [28 g_hamiltonian_route](sections/28_dp_i_mixed_contest/problems/g_hamiltonian_route/README.md) | 27 | 669 | `18` | dedicated stress |
| [28 h_sliding_jump_cost](sections/28_dp_i_mixed_contest/problems/h_sliding_jump_cost/README.md) | 27 | 2077777 | `200000 85985` | dedicated stress |
| [28 i_grouped_cargo](sections/28_dp_i_mixed_contest/problems/i_grouped_cargo/README.md) | 27 | 29935 | `200 5000` | dedicated stress |
| [28 j_minimum_starting_energy](sections/28_dp_i_mixed_contest/problems/j_minimum_starting_energy/README.md) | 27 | 2597212 | `500 500` | dedicated stress |
| [28 k_last_crystal_removed](sections/28_dp_i_mixed_contest/problems/k_last_crystal_removed/README.md) | 27 | 1505 | `300` | dedicated stress |
| [28 l_weighted_tree_guards](sections/28_dp_i_mixed_contest/problems/l_weighted_tree_guards/README.md) | 27 | 4450528 | `200000` | dedicated stress |
| [29 a_power_queries](sections/29_modular_arithmetic/problems/a_power_queries/README.md) | 29 | 8400007 | `200000` | dedicated stress |
| [29 b_fraction_queries](sections/29_modular_arithmetic/problems/b_fraction_queries/README.md) | 29 | 800018 | `1000000007 200000` | dedicated stress |
| [29 c_affine_repeater](sections/29_modular_arithmetic/problems/c_affine_repeater/README.md) | 29 | 6800007 | `200000` | dedicated stress |
| [29 d_nested_power_queries](sections/29_modular_arithmetic/problems/d_nested_power_queries/README.md) | 29 | 4800007 | `200000` | dedicated stress |
| [30 a_gcd_lcm_queries](sections/30_gcd_lcm_diophantine/problems/a_gcd_lcm_queries/README.md) | 29 | 2800007 | `200000` | dedicated stress |
| [30 b_general_inverse](sections/30_gcd_lcm_diophantine/problems/b_general_inverse/README.md) | 29 | 4200007 | `200000` | dedicated stress |
| [30 c_linear_diophantine](sections/30_gcd_lcm_diophantine/problems/c_linear_diophantine/README.md) | 29 | 4600007 | `200000` | dedicated stress |
| [30 d_clock_offset](sections/30_gcd_lcm_diophantine/problems/d_clock_offset/README.md) | 29 | 3888902 | `200000` | dedicated stress |
| [30 e_merge_congruences](sections/30_gcd_lcm_diophantine/problems/e_merge_congruences/README.md) | 27 | 6977787 | `200000` | dedicated stress |
| [30 f_shared_maintenance_window](sections/30_gcd_lcm_diophantine/problems/f_shared_maintenance_window/README.md) | 27 | 10777788 | `200000` | dedicated stress |
| [31 a_prime_counter](sections/31_sieve_primes_factorization/problems/a_prime_counter/README.md) | 29 | 2000015 | `1000000 200000` | dedicated stress |
| [31 b_factor_signature](sections/31_sieve_primes_factorization/problems/b_factor_signature/README.md) | 29 | 1400008 | `200000` | dedicated stress |
| [31 c_divisor_queries](sections/31_sieve_primes_factorization/problems/c_divisor_queries/README.md) | 29 | 1400008 | `200000` | dedicated stress |
| [31 d_square_completion](sections/31_sieve_primes_factorization/problems/d_square_completion/README.md) | 29 | 1400007 | `200000` | dedicated stress |
| [32 a_choose_queries](sections/32_combinatorics_under_modulo/problems/a_choose_queries/README.md) | 29 | 3000007 | `200000` | dedicated stress |
| [32 b_rearrange_letters](sections/32_combinatorics_under_modulo/problems/b_rearrange_letters/README.md) | 29 | 1000001 | `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` | dedicated stress |
| [32 c_distribute_candies](sections/32_combinatorics_under_modulo/problems/c_distribute_candies/README.md) | 29 | 3200007 | `200000` | dedicated stress |
| [32 d_separated_lineup](sections/32_combinatorics_under_modulo/problems/d_separated_lineup/README.md) | 29 | 2000007 | `200000` | dedicated stress |
| [33 a_multiples_union](sections/33_inclusion_exclusion/problems/a_multiples_union/README.md) | 29 | 64 | `1000000000000000000 20` | dedicated stress |
| [33 b_all_symbols](sections/33_inclusion_exclusion/problems/b_all_symbols/README.md) | 29 | 3004 | `200` | dedicated stress |
| [33 c_bounded_candies](sections/33_inclusion_exclusion/problems/c_bounded_candies/README.md) | 29 | 2404 | `200` | dedicated stress |
| [33 d_seating_without_matches](sections/33_inclusion_exclusion/problems/d_seating_without_matches/README.md) | 28 | 8 | `1000000` | dedicated stress |
| [34 a_expected_prize](sections/34_probability_expected_value/problems/a_expected_prize/README.md) | 29 | 1200007 | `200000` | dedicated stress |
| [34 b_first_success](sections/34_probability_expected_value/problems/b_first_success/README.md) | 29 | 2600007 | `200000` | dedicated stress |
| [34 c_coupon_collector](sections/34_probability_expected_value/problems/c_coupon_collector/README.md) | 29 | 1600007 | `200000` | dedicated stress |
| [34 d_simultaneous_wins](sections/34_probability_expected_value/problems/d_simultaneous_wins/README.md) | 29 | 800007 | `200000` | dedicated stress |
| [35 a_blocked_path](sections/35_math_mixed_contest/problems/a_blocked_path/README.md) | 29 | 20 | `1000000 1000000 1 2` | dedicated stress |
| [35 b_coprime_pairs](sections/35_math_mixed_contest/problems/b_coprime_pairs/README.md) | 29 | 1000008 | `200000` | dedicated stress |
| [35 c_at_least_one](sections/35_math_mixed_contest/problems/c_at_least_one/README.md) | 29 | 800007 | `200000` | dedicated stress |
| [35 d_complete_alphabet](sections/35_math_mixed_contest/problems/d_complete_alphabet/README.md) | 30 | 23 | `1000000000000000000 20` | dedicated stress |
| [35 e_modular_appointment](sections/35_math_mixed_contest/problems/e_modular_appointment/README.md) | 27 | 5000007 | `200000` | dedicated stress |
| [35 f_festival_synchronization](sections/35_math_mixed_contest/problems/f_festival_synchronization/README.md) | 27 | 5000007 | `200000` | dedicated stress |
| [35 g_capped_allocation](sections/35_math_mixed_contest/problems/g_capped_allocation/README.md) | 27 | 206 | `20 0` | dedicated stress |
| [35 h_gcd_one_subsets](sections/35_math_mixed_contest/problems/h_gcd_one_subsets/README.md) | 27 | 400013 | `200000` | dedicated stress |
| [35 i_exactly_k_colors](sections/35_math_mixed_contest/problems/i_exactly_k_colors/README.md) | 27 | 5800007 | `200000` | dedicated stress |
| [35 j_target_lcm_subsets](sections/35_math_mixed_contest/problems/j_target_lcm_subsets/README.md) | 27 | 2000018 | `200000 223092870` | dedicated stress |
| [35 k_weighted_coupon_collection](sections/35_math_mixed_contest/problems/k_weighted_coupon_collection/README.md) | 27 | 44 | `20` | dedicated stress |
| [35 l_random_divisor_descent](sections/35_math_mixed_contest/problems/l_random_divisor_descent/README.md) | 27 | 1400008 | `200000` | dedicated stress |
| [35 m_totient_prefix](sections/35_math_mixed_contest/problems/m_totient_prefix/README.md) | 27 | 1600008 | `200000` | dedicated stress |
| [35 n_squarefree_queries](sections/35_math_mixed_contest/problems/n_squarefree_queries/README.md) | 27 | 1600008 | `200000` | dedicated stress |
| [35 o_gcd_sum](sections/35_math_mixed_contest/problems/o_gcd_sum/README.md) | 27 | 1400008 | `200000` | dedicated stress |
| [35 p_subarray_gcd_sum](sections/35_math_mixed_contest/problems/p_subarray_gcd_sum/README.md) | 27 | 1600008 | `200000` | dedicated stress |
| [35 q_coprime_rectangles](sections/35_math_mixed_contest/problems/q_coprime_rectangles/README.md) | 27 | 80005 | `5000` | dedicated stress |
| [35 r_exact_divisor_count](sections/35_math_mixed_contest/problems/r_exact_divisor_count/README.md) | 27 | 2004 | `200` | dedicated stress |
| [36 a_point_add_range_sum](sections/36_fenwick_trees/problems/a_point_add_range_sum/README.md) | 27 | 2988910 | `200000 200000` | dedicated stress |
| [36 b_inversion_count](sections/36_fenwick_trees/problems/b_inversion_count/README.md) | 27 | 1288902 | `200000` | dedicated stress |
| [36 c_range_add_point_query](sections/36_fenwick_trees/problems/c_range_add_point_query/README.md) | 27 | 2988910 | `200000 200000` | dedicated stress |
| [36 d_offline_distinct_queries](sections/36_fenwick_trees/problems/d_offline_distinct_queries/README.md) | 29 | 3436169 | `200000 200000` | dedicated stress |
| [37 a_range_minimum_updates](sections/37_segment_trees/problems/a_range_minimum_updates/README.md) | 27 | 2700015 | `200000 200000` | dedicated stress |
| [37 b_maximum_subarray_updates](sections/37_segment_trees/problems/b_maximum_subarray_updates/README.md) | 27 | 2288910 | `200000 200000` | dedicated stress |
| [37 c_lazy_range_add_sum](sections/37_segment_trees/problems/c_lazy_range_add_sum/README.md) | 27 | 3577805 | `200000 200000` | dedicated stress |
| [37 d_first_available](sections/37_segment_trees/problems/d_first_available/README.md) | 29 | 1788909 | `200000 200000` | dedicated stress |
| [38 a_static_range_minimum](sections/38_static_queries_binary_lifting/problems/a_static_range_minimum/README.md) | 27 | 3977804 | `200000 200000` | dedicated stress |
| [38 b_static_range_gcd](sections/38_static_queries_binary_lifting/problems/b_static_range_gcd/README.md) | 27 | 3088910 | `200000 200000` | dedicated stress |
| [38 c_kth_ancestor](sections/38_static_queries_binary_lifting/problems/c_kth_ancestor/README.md) | 27 | 3977792 | `200000 200000` | dedicated stress |
| [38 d_ancestor_minimum](sections/38_static_queries_binary_lifting/problems/d_ancestor_minimum/README.md) | 29 | 4488902 | `200000 200000` | dedicated stress |
| [39 a_running_median](sections/39_heaps_priority_queues/problems/a_running_median/README.md) | 27 | 1288902 | `200000` | dedicated stress |
| [39 b_course_rooms](sections/39_heaps_priority_queues/problems/b_course_rooms/README.md) | 27 | 2688897 | `200000` | dedicated stress |
| [39 c_k_smallest_pair_sums](sections/39_heaps_priority_queues/problems/c_k_smallest_pair_sums/README.md) | 27 | 800023 | `200000 200000 200000` | dedicated stress |
| [39 d_merge_costs](sections/39_heaps_priority_queues/problems/d_merge_costs/README.md) | 28 | 400007 | `200000` | dedicated stress |
| [40 a_hotel_queries](sections/40_data_structures_mixed_contest/problems/a_hotel_queries/README.md) | 27 | 800016 | `200000 200000` | dedicated stress |
| [40 b_list_removals](sections/40_data_structures_mixed_contest/problems/b_list_removals/README.md) | 27 | 1688903 | `200000` | dedicated stress |
| [40 c_range_add_range_gcd](sections/40_data_structures_mixed_contest/problems/c_range_add_range_gcd/README.md) | 27 | 1350014 | `100000 100000` | dedicated stress |
| [40 d_salary_queries](sections/40_data_structures_mixed_contest/problems/d_salary_queries/README.md) | 29 | 5577804 | `200000 200000` | dedicated stress |
| [40 e_functional_walk_minimum](sections/40_data_structures_mixed_contest/problems/e_functional_walk_minimum/README.md) | 27 | 6977804 | `200000 200000` | dedicated stress |
| [40 f_mutable_priority_queue](sections/40_data_structures_mixed_contest/problems/f_mutable_priority_queue/README.md) | 27 | 2216691 | `200000` | dedicated stress |
| [40 g_streaming_room_count](sections/40_data_structures_mixed_contest/problems/g_streaming_room_count/README.md) | 27 | 2688897 | `200000` | dedicated stress |
| [40 h_toggle_kth_active](sections/40_data_structures_mixed_contest/problems/h_toggle_kth_active/README.md) | 27 | 1577804 | `200000 200000` | dedicated stress |
| [40 i_dynamic_maximum_subarray](sections/40_data_structures_mixed_contest/problems/i_dynamic_maximum_subarray/README.md) | 27 | 2288910 | `200000 200000` | dedicated stress |
| [40 j_sliding_median_cost](sections/40_data_structures_mixed_contest/problems/j_sliding_median_cost/README.md) | 27 | 1288904 | `200000 100000` | dedicated stress |
| [40 k_budget_prefix_search](sections/40_data_structures_mixed_contest/problems/k_budget_prefix_search/README.md) | 27 | 2100015 | `200000 200000` | dedicated stress |
| [40 l_range_add_threshold_search](sections/40_data_structures_mixed_contest/problems/l_range_add_threshold_search/README.md) | 28 | 3100015 | `200000 200000` | dedicated stress |
| [41 a_tree_distances](sections/41_euler_tour_lca_binary_lifting/problems/a_tree_distances/README.md) | 27 | 3977797 | `200000 200000` | dedicated stress |
| [41 b_max_edge_path](sections/41_euler_tour_lca_binary_lifting/problems/b_max_edge_path/README.md) | 27 | 4377795 | `200000 200000` | dedicated stress |
| [41 c_kth_node_path](sections/41_euler_tour_lca_binary_lifting/problems/c_kth_node_path/README.md) | 27 | 4377797 | `200000 200000` | dedicated stress |
| [41 d_weighted_distances](sections/41_euler_tour_lca_binary_lifting/problems/d_weighted_distances/README.md) | 29 | 5288891 | `200000 200000` | dedicated stress |
| [42 a_dynamic_order_statistics](sections/42_advanced_data_structures_mixed/problems/a_dynamic_order_statistics/README.md) | 27 | 1577804 | `200000 200000` | dedicated stress |
| [42 b_range_assign_add](sections/42_advanced_data_structures_mixed/problems/b_range_assign_add/README.md) | 27 | 3371444 | `200000 200000` | dedicated stress |
| [42 c_static_rectangle_count](sections/42_advanced_data_structures_mixed/problems/c_static_rectangle_count/README.md) | 27 | 7955594 | `200000 200000` | dedicated stress |
| [42 d_nested_ranges_count](sections/42_advanced_data_structures_mixed/problems/d_nested_ranges_count/README.md) | 29 | 2688902 | `200000` | dedicated stress |
| [42 e_subtree_add_point_query](sections/42_advanced_data_structures_mixed/problems/e_subtree_add_point_query/README.md) | 27 | 4677796 | `200000 200000` | dedicated stress |
| [42 f_dynamic_subtree_maximum](sections/42_advanced_data_structures_mixed/problems/f_dynamic_subtree_maximum/README.md) | 27 | 5055596 | `200000 200000` | dedicated stress |
| [42 g_subtree_value_count](sections/42_advanced_data_structures_mixed/problems/g_subtree_value_count/README.md) | 27 | 5666691 | `200000 200000` | dedicated stress |
| [42 h_incremental_connectivity](sections/42_advanced_data_structures_mixed/problems/h_incremental_connectivity/README.md) | 29 | 2577803 | `200000 200000` | dedicated stress |
| [42 i_subtree_assign_add_sum](sections/42_advanced_data_structures_mixed/problems/i_subtree_assign_add_sum/README.md) | 27 | 4727796 | `200000 200000` | dedicated stress |
| [42 j_static_vertex_path_sums](sections/42_advanced_data_structures_mixed/problems/j_static_vertex_path_sums/README.md) | 27 | 5866691 | `200000 200000` | dedicated stress |
| [42 k_static_weighted_rectangles](sections/42_advanced_data_structures_mixed/problems/k_static_weighted_rectangles/README.md) | 27 | 8555594 | `200000 200000` | dedicated stress |
| [42 l_subtree_add_maximum](sections/42_advanced_data_structures_mixed/problems/l_subtree_add_maximum/README.md) | 27 | 4777796 | `200000 200000` | dedicated stress |
