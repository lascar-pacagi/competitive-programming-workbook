# L. Path Add, Path Maximum

Maintain vertex values in a tree:

- `A u v x`: add `x` to every vertex on the simple path from `u` to `v`;
- `M u v`: print the maximum value on that path.

## Input
```text
n q
a1 ... an
n-1 edges
q operations
```
`1 <= n,q <= 200000`; values and answers fit signed 64-bit integers.

## Sample
```text
5 5
1 2 3 4 5
1 2
1 3
3 4
3 5
M 2 4
A 2 4 5
M 5 2
A 3 5 -10
M 3 5
```
```text
4
8
-2
```
