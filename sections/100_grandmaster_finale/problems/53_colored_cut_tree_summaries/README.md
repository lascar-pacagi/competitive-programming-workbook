# Colored Cut-Tree Summaries

Gomory--Hu compression turns pair min-cuts into tree path minima before color-specific virtual-tree aggregation.

You are given an undirected capacitated multigraph. For two distinct vertices
`s` and `t`, let `cut(s,t)` be the minimum total capacity of edges whose removal
disconnects `s` from `t`.

For each threshold `X`, count the unordered vertex pairs `{s,t}` satisfying
`cut(s,t) >= X`.

The graph is not necessarily connected. Parallel edges are allowed.

## Input

```text
n m q
m lines: u v capacity
q lines: X
```

- `1 <= n <= 100`;
- `0 <= m <= 1500`;
- `1 <= q <= 200000`;
- `1 <= capacity <= 10^9`;
- `0 <= X <= 10^18`;
- `u != v`.

## Output

For every query, print the number of qualifying unordered pairs.

## Sample input

```text
4 3 4
1 2 5
2 3 2
2 4 4
0
3
5
6
```

## Sample output

```text
6
3
1
0
```
