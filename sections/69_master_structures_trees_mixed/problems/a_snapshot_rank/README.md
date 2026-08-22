# A. Snapshot Range Rank

Version `0` is an empty sequence. `A v x` creates a new version by appending
`x` to version `v`. Versions may branch. `Q v l r k` asks for the k-th smallest
value among positions `[l,r]` of version `v`.

## Input
```text
M q
q operations
```
`1 <= M,q <= 200000`; values lie in `1..M`; every query is valid.

## Sample
```text
9 6
A 0 5
A 1 2
A 1 8
A 2 7
Q 4 2 3 2
Q 3 1 2 1
```
```text
7
5
```
