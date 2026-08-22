# Distinct Substring Rank

For each positive `k`, print the `k`-th **distinct nonempty substring** of `s`
in lexicographic order, or `-1` if it does not exist.

## Input
```text
s
q
q lines: k
```
Lowercase `s`; `|s|,q <= 200000`; `k <= 10^18`.

## Sample input
```text
aba
6
1
2
3
5
6
```
## Sample output
```text
a
ab
aba
ba
-1
```
