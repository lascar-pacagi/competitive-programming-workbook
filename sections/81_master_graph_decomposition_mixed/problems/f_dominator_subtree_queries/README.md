# Dominator Subtree Queries

All vertices are reachable from root `1` in a directed graph. For every query vertex `v`, print how many vertices `x` have the property that every path from `1` to `x` passes through `v`.

Input: `n m q`, directed edges, then query vertices. `n <= 1500`,
`m <= 10000`, and `q <= 200000`.

Sample input
```text
5 5 2
1 2
1 3
2 4
3 4
4 5
4
1
```
Sample output
```text
2
5
```
