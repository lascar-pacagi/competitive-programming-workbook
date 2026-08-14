# L. Profitable Disjoint Routes

A directed acyclic graph has vertices `1..n`; every edge goes from a smaller
vertex to a larger vertex and has an integer profit. Choose exactly `k`
pairwise edge-disjoint paths from vertex `1` to vertex `n`. Paths may share
vertices, including their endpoints. Maximize the sum of the profits of all
used edges, or print `IMPOSSIBLE` if `k` paths do not exist.

## Input
```text
n m k
u1 v1 profit1
...
um vm profitm
```
`2 <= n <= 150`, `1 <= m <= 1000`, `1 <= k <= 20`, `u_i < v_i`, and
`|profit_i| <= 10^6`. There are no duplicate directed edges.

## Sample
```text
4 5 2
1 2 5
2 4 4
1 3 3
3 4 10
2 3 1
```
```text
22
```
