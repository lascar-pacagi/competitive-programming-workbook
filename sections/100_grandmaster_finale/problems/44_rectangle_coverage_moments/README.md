# Rectangle Coverage Moments

A sweep segment tree tracks the second coverage moment: area covered at least twice.

Print the exact area covered by at least two of the axis-aligned rectangles. Boundaries have zero area; rectangles may overlap or be degenerate.

Input: `n`, then `x1 y1 x2 y2`. `1 <= n <= 50000`, `|coordinate| <= 10^9`.

Sample:
```text
2
0 0 3 2
1 1 4 3
```
```text
2
```
