# Condensation Profile

Given a directed graph, contract every strongly connected component. Print the number of components, the number with indegree zero, and the number with outdegree zero in the resulting condensation DAG.

Input: `n m`, followed by `m` directed edges. `1 <= n <= 200000` and
`0 <= m <= 200000`.

Sample input
```text
4 4
1 2
2 1
2 3
3 4
```
Sample output
```text
3 1 1
```
