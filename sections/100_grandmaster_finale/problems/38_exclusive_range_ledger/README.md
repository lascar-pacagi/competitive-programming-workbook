# Exclusive Range Ledger

A ledger holds `n` nonnegative integers `a[1..n]`. For a query `(l, r, x)`,
count the subsets of positions `{l, l+1, ..., r}` (the empty subset included)
whose values have bitwise XOR exactly `x`. Two subsets are different when they
use different positions, even if the values coincide. Print the count modulo
`1,000,000,007`.

## Input

```text
n q
a[1] ... a[n]
q lines: l r x
```

- `1 <= n, q <= 300000`;
- `0 <= a[i], x < 2^30`;
- `1 <= l <= r <= n`.

## Output

Print one count per query.

## Sample input

```text
5 4
3 5 6 3 0
1 3 0
1 3 7
2 5 3
4 4 1
```

## Sample output

```text
2
0
4
0
```
