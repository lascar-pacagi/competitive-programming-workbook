# C. Robot Collision Translations

Convex robots A and B are closed polygons given counterclockwise. Robot A stays fixed; B is translated by vector `t`. For every query, print whether the translated B intersects A, including boundary contact.

Input: `n m q`, polygons A and B, then q translation vectors. `n+m,q <= 200000`, `|coordinate| <= 10^8`.

Sample:
```text
4 4 3
0 0
2 0
2 2
0 2
0 0
1 0
1 1
0 1
1 1
2 0
4 0
```
```text
YES
YES
NO
```
