# Affine Forest Paths

Values are modulo `998244353`. Maintain a forest under `LINK`, `CUT`, `AFFINE u v a b` (replace every value on the path by `a*x+b`), and `SUM u v`. Operations are valid and queried vertices connected; `n,q <= 200000`.

Sample input
```text
3 5
1 2 3
LINK 1 2
LINK 2 3
AFFINE 1 3 2 1
SUM 1 3
SUM 2 3
```
Sample output
```text
15
12
```
