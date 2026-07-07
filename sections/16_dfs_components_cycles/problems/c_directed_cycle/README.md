# C. Directed Cycle

You are given a directed graph. Decide whether it contains at least one
directed cycle.

A directed cycle is a sequence of distinct vertices
`v1, v2, ..., vk` with directed edges:

```text
v1 -> v2 -> ... -> vk -> v1
```

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
The graph may have disconnected parts. It has no self-loops, but repeated
directed edges are possible.

## Output

Print:

```text
CYCLIC
```

if the graph contains a directed cycle. Otherwise print:

```text
ACYCLIC
```

## Sample

Input:

```text
5 5
1 2
2 3
3 4
4 2
4 5
```

Output:

```text
CYCLIC
```

