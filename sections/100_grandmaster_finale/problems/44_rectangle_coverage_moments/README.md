# Double-Covered Area

`n` axis-parallel rectangles are drawn on the plane. Print the total area of the
points covered by at least two of them. Boundaries have zero area;
rectangles may overlap in any way and may be degenerate.

## Input

```text
n
n lines: x1 y1 x2 y2
```

- `1 <= n <= 50000`;
- `|x1|, |y1|, |x2|, |y2| <= 10^9`; a rectangle spans between its two given
  corners.

## Output

Print the exact area (an integer).

## Sample input

```text
2
0 0 3 2
1 1 4 3
```

## Sample output

```text
2
```
