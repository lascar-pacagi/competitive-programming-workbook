# Glacier Cut

An ice shelf is a convex polygon with `n` integer corners (given in order,
clockwise or counterclockwise, with no three corners collinear). Each query is
a straight crack through two distinct integer points `A` and `B`; it splits
the plane along the line `AB`. Print the area of the part of the shelf lying
to the **left** of the directed line from `A` to `B`.

Queries are independent.

## Input

```text
n q
n lines: x y
q lines: ax ay bx by
```

- `3 <= n <= 100000`, `1 <= q <= 200000`;
- every coordinate (corners and query points) has absolute value at most
  `10^5`;
- the polygon is strictly convex and `A != B` in every query.

## Output

Print one area per query. Answers with absolute or relative error at most
`10^-7` are accepted.

## Sample input

```text
4 3
0 0
4 0
4 4
0 4
0 2 4 2
0 0 1 1
5 0 5 1
```

## Sample output

```text
8.0
8.0
16.0
```
