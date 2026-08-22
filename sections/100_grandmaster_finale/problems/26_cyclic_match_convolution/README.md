# Cyclic Match Convolution

Strings `a,b` have equal length and use `a,b,c,?`; `?` matches every symbol.
For each left rotation `d` of `b`, compare `a[i]` with `b[(i+d) mod n]`.
Print all shifts having at most `K` mismatches.

## Input
```text
n K
a
b
```
`1 <= n <= 200000`, `0 <= K <= n`.

## Output
First print the number of valid shifts, then their zero-based indices.

## Sample input
```text
4 0
a?bc
bcaa
```
## Sample output
```text
1
2
```
