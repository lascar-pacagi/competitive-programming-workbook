# Offline Dynamic Hull Queries: Hull Kernel

This kernel answers the tangent/orientation membership query used at every offline hull node.

Build the strict convex hull of the input points. For each query point print `IN`, `BOUNDARY`, or `OUT` relative to the closed hull. Degenerate hulls of one point or one segment are allowed.

Input: `n q`, then n points and q queries. `n,q <= 200000`.

Sample:
```text
5 3
0 0
4 0
4 3
0 3
2 1
2 2
4 1
5 1
```
```text
IN
BOUNDARY
OUT
```
