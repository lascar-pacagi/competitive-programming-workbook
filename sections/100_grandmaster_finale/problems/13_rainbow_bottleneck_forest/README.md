# Rainbow Bottleneck Forest

You are given an undirected multigraph. Every edge has a color and a positive
weight. Choose exactly `K` edges such that:

- the chosen edges contain no cycle;
- no two chosen edges have the same color.

Minimize the maximum weight of a chosen edge. Print `-1` if no such choice
exists.

Parallel edges are allowed.

## Input

```text
n m K
m lines: u v color weight
```

- `1 <= n <= 100`;
- `0 <= m <= 300`;
- `1 <= K <= n-1`;
- `1 <= color <= 10^9`;
- `1 <= weight <= 10^9`;
- `u != v`.

## Output

Print the minimum possible maximum chosen-edge weight, or `-1`.

## Sample input

```text
4 5 3
1 2 1 4
2 3 2 7
3 4 1 2
1 3 3 6
2 4 4 5
```

## Sample output

```text
6
```
