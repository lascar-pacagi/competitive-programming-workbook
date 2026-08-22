# A. Orthogonal Crossings

Count intersections between closed horizontal and closed vertical segments. Every horizontal is `x1 x2 y`; every vertical is `x y1 y2`. An endpoint touching counts, and overlapping collinear pairs are irrelevant because only opposite orientations are counted.

Input: `H V`, then H horizontals and V verticals. `H+V <= 200000`.

Sample:
```text
2 2
0 4 1
2 5 3
1 0 4
4 1 3
```
```text
3
```
