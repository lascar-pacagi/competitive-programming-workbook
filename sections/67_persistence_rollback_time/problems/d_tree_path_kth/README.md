# D. Tree Path K-th

You are given a tree with a fixed integer value on every vertex. For each
query `u v k`, print the `k`-th smallest value among all vertices on the simple
path from `u` to `v`. Equal values occupy separate positions in the order.

Input starts with `n q`, followed by the `n` values, the `n-1` edges, and then
the `q` queries. Vertices are numbered from 1.

Constraints: `1 <= n,q <= 200000`, `|value| <= 10^9`, and every query has
`1 <= k <= number of vertices on the path`.

Sample input:

```text
5 4
8 3 8 1 6
1 2
1 3
2 4
2 5
4 3 2
4 5 2
1 1 1
3 5 3
```

Sample output:

```text
3
3
8
8
```
