# B. Exact Red Spanning Tree

Each edge of a connected undirected weighted graph is red or blue. Find the minimum weight of a spanning tree containing exactly `k` red edges, or print `IMPOSSIBLE`.

## Input
`n m k`, followed by `m` lines `u v weight color`, where `color` is `R` or `B`.

`2 <= n <= 200`, `n-1 <= m <= 5000`, `0 <= k < n`, `|weight| <= 10^9`.

## Sample
```text
4 5 2
1 2 3 R
2 3 2 B
3 4 4 R
1 4 8 B
1 3 6 R
```
```text
9
```
