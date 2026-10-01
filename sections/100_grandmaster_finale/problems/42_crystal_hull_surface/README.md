# Crystal Hull Surface

A jeweller embeds `n` tiny reflectors at integer points of space and coats the
smallest convex solid that contains all of them. Print the area of the coated
surface, i.e. the surface area of the convex hull of the points.

It is guaranteed that the points are not all on one plane, and that every
plane touching the hull without cutting through it contains at most three of
the points (so the hull's faces are triangles, and no point lies on the hull
boundary except at its vertices). Points may repeat only strictly inside the
hull.

## Input

```text
n
n lines: x y z
```

- `4 <= n <= 2000`;
- `|x|, |y|, |z| <= 10^9`.

## Output

Print the surface area. Answers with absolute or relative error at most
`10^-7` are accepted.

## Sample input

```text
5
0 0 0
1 0 0
0 1 0
0 0 1
1 1 1
```

## Sample output

```text
4.0980762114
```
