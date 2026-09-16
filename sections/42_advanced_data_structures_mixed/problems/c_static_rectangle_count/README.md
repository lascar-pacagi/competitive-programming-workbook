# C. Static Rectangle Count

A survey has plotted `n` sensors on a grid, and you are asked `q` questions
about rectangular regions of that grid. The sensors never move, and all `q`
questions are known before any answer is needed.

For each query rectangle, print how many sensors lie inside it. A sensor on the
boundary counts as inside, and two sensors at the same coordinates count
separately.

## Input

```text
n q
x1 y1
x2 y2
...
xn yn
a1 b1 c1 d1
a2 b2 c2 d2
...
aq bq cq dq
```

The first `n` lines give the sensor coordinates. Each of the next `q` lines
gives one query rectangle as `a b c d`, meaning the region

```text
a <= x <= c   and   b <= y <= d
```

so `(a, b)` is the lower-left corner and `(c, d)` the upper-right one.

## Constraints

```text
1 <= n, q <= 200,000
1 <= x, y <= 1,000,000,000
1 <= a <= c <= 1,000,000,000
1 <= b <= d <= 1,000,000,000
```

Coordinates may repeat, both among sensors and between sensors and rectangle
corners.

## Output

Print `q` lines. The `i`-th is the number of sensors inside the `i`-th
rectangle. A rectangle containing no sensor answers `0`.

## Sample

```text
4 3
1 1
2 3
4 2
5 5
1 1 3 3
3 1 5 5
2 4 4 4
```

```text
2
2
0
```

The sensors are at `(1,1)`, `(2,3)`, `(4,2)` and `(5,5)`. The first rectangle
spans `x` in `[1,3]` and `y` in `[1,3]`, catching `(1,1)` and `(2,3)`. The
second spans `[3,5]` by `[1,5]`, catching `(4,2)` and `(5,5)`. The third is the
single row `y = 4` between `x = 2` and `x = 4`, where no sensor sits.
