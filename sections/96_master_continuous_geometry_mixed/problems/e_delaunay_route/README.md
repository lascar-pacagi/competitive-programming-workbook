# E. Delaunay Route

Build the Delaunay graph of `n` sites: two sites are adjacent when they share
an edge of the Delaunay triangulation. Starting at site `s`, travel only along
these edges. Print the minimum total Euclidean length needed to reach site `t`.

`3 <= n <= 2500`; coordinates have absolute value at most `10^9`; no three
points are collinear and no four are cocircular.

## Sample

```text
3 1 2
0 0
2 0
0 2
```

```text
2.0000000000
```
