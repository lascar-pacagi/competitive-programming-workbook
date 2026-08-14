# H. Toggle K-th Active

There are `n` positions, initially inactive. Process two operations:

- `T i`: toggle position `i`;
- `K k`: print the position of the `k`-th active position from the left, or
  `-1` if fewer than `k` positions are active.

## Input
```text
n q
q operations
```
`1 <= n,q <= 200000`.

## Sample
```text
5 7
K 1
T 3
T 5
K 2
T 3
K 1
K 2
```
```text
-1
5
5
-1
```
