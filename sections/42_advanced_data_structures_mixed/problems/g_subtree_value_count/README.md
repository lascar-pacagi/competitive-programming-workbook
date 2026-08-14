# G. Subtree Value Count

Vertex values are static. For each query `u lo hi`, count vertices in the
subtree of `u` whose value lies in the inclusive interval `[lo, hi]`. The tree
is rooted at `1`.

## Input
```text
n q
a1 ... an
n-1 edges
q lines: u lo hi
```
`1 <= n,q <= 200000`, `|value|,|lo|,|hi| <= 10^9`.

## Sample
```text
5 3
5 1 4 2 3
1 2
1 3
3 4
3 5
3 2 3
1 4 5
2 0 10
```
```text
2
2
1
```
