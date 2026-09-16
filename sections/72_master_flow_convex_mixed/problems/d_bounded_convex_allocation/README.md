# D. Bounded Convex Allocation

Allocate exactly `K` indistinguishable units among `n` machines. Machine `i`
must receive an integer amount `x[i]` with `low[i] <= x[i] <= high[i]` and
costs `a[i] * x[i]^2 + b[i] * x[i]`, where `a[i] > 0`.

Print the minimum total cost, or `IMPOSSIBLE`.

## Input

`n K`, followed by `n` lines `a b low high`.

`1 <= n <= 200000`, `0 <= K,low,high <= 10^14`,
`low <= high`, `1 <= a <= 10^6`, and `|b| <= 10^12`.
The answer fits a signed 128-bit integer.

## Sample

```text
2 3
1 0 1 3
2 -1 0 3
```

```text
5
```
