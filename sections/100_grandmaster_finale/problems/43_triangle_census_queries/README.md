# Triangle Census Queries

A survey marks `n` trees in a forest at integer points; no two trees share an
`x`-coordinate and no three trees are collinear. Each query names three trees
`a, b, c`, which are fenced into a triangle. Print how many of the other trees
stand strictly inside that triangle.

## Input

```text
n q
n lines: x y
q lines: a b c      (distinct tree numbers)
```

- `3 <= n <= 2000`, `1 <= q <= 500000`;
- `|x|, |y| <= 10^9`;
- all `x` are distinct and no three points are collinear.

## Output

Print one count per query.

## Sample input

```text
6 3
0 0
10 1
4 9
3 2
5 4
7 3
1 2 3
4 5 6
1 3 6
```

## Sample output

```text
3
0
2
```
