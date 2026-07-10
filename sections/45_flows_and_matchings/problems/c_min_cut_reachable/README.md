# C. Min Cut Reachable Side

After max flow from 1 to n, print the flow value and the source-side reachable vertices in the residual graph.

## Input

```text
n m
u1 v1 c1
...
um vm cm
```

Vertices are numbered from 1 to `n`. Every capacity is a nonnegative 64-bit
integer; the test data guarantees that the maximum-flow value fits in signed
`long long`.

## Sample

Input:

```text
4 5
1 2 3
1 3 2
2 3 1
2 4 2
3 4 4
```
