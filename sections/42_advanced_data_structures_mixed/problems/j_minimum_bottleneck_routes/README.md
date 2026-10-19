# J. Minimum Bottleneck Routes

An undirected weighted graph may contain cycles, parallel edges, self-loops,
and disconnected components. All edges are fixed. For each query `u v`, choose
a path from `u` to `v` that minimizes its largest edge weight, and print that
minimum possible largest weight. This is a bottleneck cost, not the sum of
edge weights.

Print `-1` when no path exists. For `u=v`, the empty path has bottleneck cost
`0`. Every edge weight is nonnegative.

## Input

```text
n m q
m lines: u v w
q lines: u v
```

`1 <= n,q <= 200000`, `0 <= m <= 200000`, `1 <= u,v <= n`, and
`0 <= w <= 10^9`. Edges are undirected and may arrive in any order.

## Output

Print one bottleneck cost per query, in input order.

## Sample

```text
5 5 5
1 2 8
2 3 3
1 3 5
3 4 7
2 4 10
1 2
1 4
2 3
1 5
5 5
```

```text
5
7
3
-1
0
```

The route `1 -> 3 -> 2` has largest weight 5, improving on the direct edge
of weight 8. Vertex 5 is isolated, but it is reachable from itself.
