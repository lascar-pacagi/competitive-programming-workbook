# Safe Radius Region

A strictly convex polygon is given by its vertices in counterclockwise order.
Print the largest radius of a circle that fits entirely inside the polygon.

## Input

```text
n
n lines: x y
```

- `3 <= n <= 200000`;
- `|x|, |y| <= 10^6`.

## Output

Print the radius. Answers with absolute or relative error at most `10^-7` are
accepted.

## Sample input

```text
4
0 0
2 0
2 2
0 2
```

## Sample output

```text
1.0000000000
```
