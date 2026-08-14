# E. Station Coverage Report

Given an undirected unweighted graph and several station vertices, report:

1. the number of vertices unreachable from every station;
2. among reachable vertices, the vertex farthest from its nearest station;
3. that distance.

Break a tie for the farthest vertex by the smallest vertex number.

## Input

```text
n m k
m undirected edges
k station vertices
```

`1 <= n,m <= 200000`.

## Output

Print `unreachable_count vertex distance`.

## Sample

```text
6 4 2
1 2
2 3
4 5
5 6
1 6
```

```text
0 3 2
```
