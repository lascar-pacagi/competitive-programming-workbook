# D. Convex Polygon Distance

Two convex polygons are given in counterclockwise order. They have no repeated
vertices and no three consecutive vertices are collinear. Print the minimum
Euclidean distance between a point of the first polygon and a point of the
second. Intersecting or touching polygons have distance zero.

Input gives `n`, the `n` vertices of the first polygon, then `m` and the `m`
vertices of the second polygon.

Constraints: `3 <= n,m`, `n+m <= 400000`, and `|coordinate| <= 10^9`.
Answers within absolute or relative error `1e-8` are accepted.

Sample input:

```text
4
0 0
2 0
2 2
0 2
4
4 0
6 0
6 2
4 2
```

Sample output:

```text
2.0000000000
```
