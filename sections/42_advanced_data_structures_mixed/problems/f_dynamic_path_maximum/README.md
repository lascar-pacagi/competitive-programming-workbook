# F. Dynamic Path Maximum

Maintain vertex values in a tree. `U u x` assigns value `x` to `u`; `Q u v`
prints the maximum vertex value on the simple path from `u` to `v`.

## Input
```text
n q
a1 ... an
n-1 edges
q operations
```
`1 <= n,q <= 200000`, `|value| <= 10^9`.

## Sample
```text
5 5
1 2 3 4 5
1 2
1 3
3 4
3 5
Q 2 4
U 1 10
Q 2 4
U 5 -2
Q 5 2
```
```text
4
10
10
```
