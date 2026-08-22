# Palindromic Range Census

Every distinct palindromic substring of `s` has one **discovery interval**:
its leftmost occurrence `[start,end]`. For each query `[l,r]`, count discovery
intervals wholly contained in `[l,r]`.

## Input
```text
s
q
q lines: l r
```
`s` is lowercase; `1 <= |s|,q <= 200000`.

## Output
One count per query.

## Sample input
```text
ababa
3
1 5
2 5
3 4
```
## Sample output
```text
5
2
0
```
