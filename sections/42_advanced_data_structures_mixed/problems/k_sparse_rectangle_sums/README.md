# K. Sparse Rectangle Sums

An initially empty weighted plane receives operations:

- `U x y d`: add `d` to point `(x,y)` (creating it if necessary);
- `Q x1 y1 x2 y2`: print the total weight in the inclusive rectangle
  `[x1,x2] x [y1,y2]`.

## Input
```text
q
q operations
```
`1 <= q <= 200000`, coordinates have absolute value at most `10^9`, and all
answers fit signed 64-bit integers.

## Sample
```text
6
U 1 1 5
U 2 3 4
Q 1 1 2 3
U 1 1 -2
Q 1 2 2 3
Q 0 0 1 1
```
```text
9
4
3
```
