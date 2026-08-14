# L. Dynamic Inversion Swaps

You are given a permutation. After each operation swapping positions `i` and
`j`, print its number of inversions: pairs `x < y` with `a[x] > a[y]`.

## Input
```text
n q
a1 ... an
i1 j1
...
iq jq
```
`1 <= n,q <= 200000`. The array is a permutation of `1..n`.

## Sample
```text
5 3
3 1 5 2 4
1 2
3 5
2 4
```
```text
3
2
1
```
