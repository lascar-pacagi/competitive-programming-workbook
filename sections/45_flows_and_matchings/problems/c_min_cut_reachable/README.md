# C. Min Cut Reachable Side

You are given a directed graph on `n` vertices where every edge has a capacity.
Vertex `1` is the source and vertex `n` is the sink.

Compute a maximum flow from `1` to `n`. Then, in the residual graph, let `S` be
the set of vertices still reachable from vertex `1` using only edges that have
residual capacity remaining. Print the flow value and `S`.

## Input

```text
n m
u1 v1 c1
u2 v2 c2
...
um vm cm
```

- `2 <= n <= 500`
- `0 <= m <= 5,000`
- `1 <= ui, vi <= n` and `ui != vi`
- `0 <= ci <= 10^9`

The format is identical to problem A.

## Output

Print two lines.

- The first line is the maximum flow value.
- The second line lists the vertices of `S` in increasing order, separated by
  single spaces.

`S` always contains vertex `1`, and never contains vertex `n`.

## Sample

```text
4 5
1 2 3
1 3 2
2 3 1
2 4 2
3 4 4
```

```text
5
1
```

The maximum flow is `5`. Both edges leaving vertex `1` end up saturated, so the
residual walk from `1` cannot move anywhere and `S = {1}`.
