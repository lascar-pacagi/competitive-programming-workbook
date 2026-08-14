# J. Subtree K-th Smallest

The tree is rooted at `1` and vertex values are static. For each `u k`, print
the `k`-th smallest value in the subtree of `u`. Equal values occupy separate
positions in the sorted multiset.

## Input
```text
n q
a1 ... an
n-1 edges
q lines: u k
```
`1 <= n,q <= 200000`; every query has `1 <= k <= subtree_size(u)`.

## Sample
```text
5 3
5 1 4 2 3
1 2
1 3
3 4
3 5
3 2
1 4
2 1
```
```text
3
4
1
```
