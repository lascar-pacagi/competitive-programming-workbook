# E. Exact Red Forest

Each edge of an undirected weighted graph is red or blue. Find the minimum
weight of an acyclic spanning subgraph with exactly `components` connected
components and exactly `k` red edges, or print `IMPOSSIBLE`.

Such a forest contains exactly `n - components` edges.

## Input

`n m components k`, followed by `m` lines `u v weight color`, where `color`
is `R` or `B`.

`2 <= n <= 200`, `0 <= m <= 5000`, `1 <= components <= n`,
`0 <= k <= n-components`, and `|weight| <= 10^9`.

## Sample

```text
5 6 2 2
1 2 3 R
2 3 2 B
3 4 4 R
4 5 1 B
1 5 8 B
2 5 6 R
```

```text
8
```
