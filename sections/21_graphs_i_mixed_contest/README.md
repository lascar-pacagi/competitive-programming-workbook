# Section 21: Graphs I Mixed Contest

This section closes Graphs I with a short mixed contest. The main skill is
choosing between BFS/DFS, topological sorting, DSU/Kruskal, Dijkstra, and
0-1 BFS from the statement shape.

## Category Coverage

The additional local blind-practice problems fill categories not represented
by a distinct algorithm in the four-problem timed core. The section checker
runs all seven problems.

| Graph category | Problem |
|---|---|
| BFS and unweighted shortest paths | [E. Station Coverage Report](problems/e_station_coverage_report/README.md) |
| DFS, components, and cycles | [F. Component Repair](problems/f_component_repair/README.md) |
| Topological sorting and DAG DP | B. Build Timeline |
| DSU and minimum spanning trees | A. Existing Network |
| Dijkstra and weighted-state modeling | [G. Alternating Road Route](problems/g_alternating_road_route/README.md) |
| 0-1 BFS | C. One-Way Reversals |

Reliable Link is retained as an additional minimax-connectivity problem. Its
editorial uses an increasing-edge DSU sweep, so it does not replace the
dedicated Dijkstra problem above.

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises as a timed set:
   - `a_existing_network`
   - `b_build_timeline`
   - `c_one_way_reversals`
   - `d_reliable_link` (blind practice: use its README only)
   - `e_station_coverage_report`
   - `f_component_repair`
   - `g_alternating_road_route`
3. Run the checker:

```bash
python3 sections/21_graphs_i_mixed_contest/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/21_graphs_i_mixed_contest/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
