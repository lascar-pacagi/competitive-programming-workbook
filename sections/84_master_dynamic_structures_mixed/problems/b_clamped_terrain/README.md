# Clamped Terrain

Maintain values under `LOWER l r x` (replace by `max(value,x)`), `UPPER l r x` (replace by `min(value,x)`), and `SUM l r`. Bounds are `200000`; answers fit 64-bit.

Sample input
```text
4 4
1 8 3 6
LOWER 1 3 4
UPPER 2 4 5
SUM 1 4
SUM 2 3
```
Sample output
```text
18
9
```
