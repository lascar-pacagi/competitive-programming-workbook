# C. Sum Polygon Queries

Polygons `A` and `B` are convex and given counterclockwise, without repeated first vertices or consecutive collinear edges. For each point `p`, decide whether `p = a+b` for some `a` in `A` and `b` in `B`. Boundary points count.

Input: `n m q`, polygon A, polygon B, then q points. `3 <= n,m`, `n+m,q <= 200000`, `|coordinate| <= 10^8`.

Sample:
```text
4 3 3
0 0
2 0
2 2
0 2
0 0
1 0
0 1
1 1
3 2
4 4
```
```text
YES
YES
NO
```
