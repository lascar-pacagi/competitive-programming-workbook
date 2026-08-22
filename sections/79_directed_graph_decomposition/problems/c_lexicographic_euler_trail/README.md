# Lexicographic Euler Trail

A directed multigraph is given. Find the lexicographically smallest vertex sequence of an Euler trail that starts at vertex `1` and uses every edge exactly once. Parallel edges and loops are allowed.

Input: `n m`, then `m` directed edges; `n,m <= 200000`.

Output the `m+1` vertices, or `IMPOSSIBLE`.

Sample input
```text
3 3
1 2
2 1
1 3
```
Sample output
```text
1 2 1 3
```
