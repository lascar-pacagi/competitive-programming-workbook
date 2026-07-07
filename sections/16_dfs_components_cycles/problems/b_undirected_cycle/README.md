# B. Undirected Cycle

You are given a simple undirected graph. Decide whether it contains at least
one cycle.

## Input

```text
n m
u1 v1
u2 v2
...
um vm
```

`1 <= n <= 2 * 10^5`  
`0 <= m <= 2 * 10^5`  
The graph has no self-loops and no repeated edges.

## Output

Print:

```text
CYCLIC
```

if the graph contains a cycle. Otherwise print:

```text
ACYCLIC
```

## Sample

Input:

```text
5 4
1 2
2 3
3 1
4 5
```

Output:

```text
CYCLIC
```

