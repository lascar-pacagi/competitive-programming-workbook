# D. Weighted Crossings

Each horizontal and vertical segment has an integer weight. For every horizontal-vertical intersection, add the product of their weights. Print the total. Segments are closed.

Input: `H V`; H lines `x1 x2 y weight`; V lines `x y1 y2 weight`. `H+V <= 200000`, `|weight| <= 1000`.

Sample:
```text
1 2
0 5 2 3
1 0 3 4
5 2 4 4
```
```text
24
```
