# B. Minimum Network

You are given an undirected weighted graph. Choose edges of minimum total cost
so that every vertex is connected to every other vertex.

If this is impossible, print `IMPOSSIBLE`.

## Input

```text
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```

`1 <= n <= 2 * 10^5`  
`0 <= m <= 2 * 10^5`  
`-10^9 <= wi <= 10^9`

Repeated edges are allowed.

## Output

Print the minimum total cost, or `IMPOSSIBLE`.

## Sample

Input:

```text
4 5
1 2 3
1 3 1
2 3 2
2 4 4
3 4 5
```

Output:

```text
7
```

