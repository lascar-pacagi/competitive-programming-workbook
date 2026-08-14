# I. Persistent Version Sums

Version `0` is the initial array. Process:

- `U v i x`: create the next version by copying version `v` and assigning
  position `i` to `x`;
- `Q v l r`: print the sum on `[l,r]` in version `v`.

Versions are numbered `1,2,...` in update order. Queries create no version.

## Input
```text
n q
a1 ... an
q operations
```
`1 <= n,q <= 200000`; all sums fit signed 64-bit integers.

## Sample
```text
3 6
1 2 3
Q 0 1 3
U 0 2 10
Q 1 1 3
U 0 1 -5
Q 2 1 2
Q 0 2 3
```
```text
6
14
-3
5
```
