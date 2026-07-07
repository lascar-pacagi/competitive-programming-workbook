# C. Cluster Split

You are given an undirected weighted graph and an integer `k`. Choose edges of
minimum total cost so that the graph is divided into exactly `k` connected
groups.

All vertices must belong to one of the groups. If it is impossible to reach
exactly `k` groups using the given edges, print `IMPOSSIBLE`.

## Input

```text
n m k
u1 v1 w1
u2 v2 w2
...
um vm wm
```

`1 <= k <= n <= 2 * 10^5`  
`0 <= m <= 2 * 10^5`  
`0 <= wi <= 10^9`

## Output

Print the minimum total cost, or `IMPOSSIBLE`.

## Sample

Input:

```text
5 6 2
1 2 1
2 3 2
3 4 10
4 5 1
1 5 8
2 5 7
```

Output:

```text
4
```
