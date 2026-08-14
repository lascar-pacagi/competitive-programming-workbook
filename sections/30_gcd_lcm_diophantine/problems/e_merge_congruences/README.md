# E. Merge Congruences

For each query, find the smallest nonnegative integer `x` satisfying

```text
x == r1 (mod m1)
x == r2 (mod m2)
```

The moduli need not be coprime. Print `-1` if no solution exists.

## Input
```text
q
r1 m1 r2 m2
...
```
`1 <= q <= 200000`, `1 <= m1,m2 <= 10^9`, and
`0 <= r1 < m1`, `0 <= r2 < m2`.

## Sample
```text
4
2 6 5 9
1 4 2 6
3 5 3 7
0 1000000000 999999999 1000000000
```
```text
14
-1
3
-1
```
