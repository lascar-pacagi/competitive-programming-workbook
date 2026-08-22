# Delaunay Terminal Backbone

Terminal-mask Steiner DP is the final optimization kernel after Delaunay and Kruskal reconstruction sparsify geometric bottlenecks.

Steiner subset DP precomputes the complete terminal-mask cost frontier.

A weighted undirected graph has `k <= 10` distinguished terminals. For each query mask, print the minimum weight of a connected subgraph containing the terminals whose bits occur in the mask. `n <= 60`, `m <= 500`, `q <= 1000`; masks are nonzero.

Input gives `n m k q`, the edges, one line of `k` terminal vertices, then the `q` masks.

Sample input
```text
4 4 3 2
1 2 1
2 3 1
3 4 1
1 4 10
1 3 4
3
7
```
Sample output
```text
2
3
```
