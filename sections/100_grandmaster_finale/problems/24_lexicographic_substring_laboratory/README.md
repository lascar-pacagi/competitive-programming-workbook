# Lexicographic Substring Laboratory

For query `(l,r,k)`, consider the suffixes of `s` starting at positions
`l..r`, sorted lexicographically. Print the starting position of the `k`-th
suffix and its LCP with the next suffix in that restricted order. For the last
suffix print LCP `0`.

## Input
```text
s
q
q lines: l r k
```
Lowercase `s`; `1 <= |s|,q <= 200000`; `1 <= l <= r <= |s|`, `1 <= k <= r-l+1`.

## Sample input
```text
banana
3
1 6 2
2 5 2
3 3 1
```
## Sample output
```text
4 3
2 0
3 0
```
