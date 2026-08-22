# D. Rectangle Union Perimeter

Given axis-aligned rectangles, print the area and perimeter of their union.
Overlapping boundary or interior is counted only once. Every rectangle is
half-open as a set of cells for counting purposes, but the geometric union and
its perimeter are the usual closed shapes.

Input starts with `n`, followed by `n` lines `x1 y1 x2 y2` with
`x1 < x2` and `y1 < y2`.

Constraints: `1 <= n <= 200000`, `|coordinate| <= 10^9`. Both answers fit in
signed 64-bit integers.

Sample input:

```text
2
0 0 3 2
2 1 4 3
```

Sample output:

```text
9 14
```
