# C. Inspection Route

A technician starts at location `1`, must visit every location exactly once,
and then return to location `1`. Moving directly from location `i` to location
`j` costs `c[i][j]`. Costs may be asymmetric.

Find the minimum total cost of such a route.

## Input

```text
n
c1,1 c1,2 ... c1,n
c2,1 c2,2 ... c2,n
...
cn,1 cn,2 ... cn,n
```

`1 <= n <= 16`, `0 <= c[i][j] <= 10^9`, and `c[i][i] = 0`.

## Output

Print the minimum total cost.

## Sample

Input:

```text
4
0 10 15 20
5 0 9 10
6 13 0 12
8 8 9 0
```

Output:

```text
35
```
