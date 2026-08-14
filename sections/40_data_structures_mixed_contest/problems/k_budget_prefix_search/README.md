# K. Budget Prefix Search

Maintain an integer array under assignments. For `Q l b`, print the smallest
`r >= l` such that

```text
a[l] + a[l+1] + ... + a[r] > b,
```

or `-1` if no such position exists. Values and budgets may be negative.
Operations are `U i x` and `Q l b`.

## Input
```text
n q
a1 ... an
q operations
```
`1 <= n,q <= 200000`, `|a_i|,|x|,|b| <= 10^9`.

## Sample
```text
5 5
2 -5 4 3 -1
Q 1 3
Q 2 2
U 2 1
Q 1 3
Q 4 1
```
```text
4
-1
3
4
```
