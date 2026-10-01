# Moving Convex Robots

Robot `A` and robot `B` are convex polygons, each given by its vertices in
counterclockwise order; both are closed sets. Robot `A` stays fixed. For each
query vector `t = (tx, ty)`, translate robot `B` by `t` and print `YES` if the
translated `B` intersects `A` (touching counts), otherwise `NO`.

## Input

```text
n m q
n lines: x y      (vertices of A)
m lines: x y      (vertices of B)
q lines: tx ty
```

- `3 <= n, m`, `n + m <= 200000`, `1 <= q <= 200000`;
- every coordinate and every `tx, ty` has absolute value at most `10^8`;
- both polygons are strictly convex.

## Output

Print one line per query.

## Sample input

```text
4 4 3
0 0
2 0
2 2
0 2
0 0
1 0
1 1
0 1
1 1
2 0
4 0
```

## Sample output

```text
YES
YES
NO
```
