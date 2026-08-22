# C. Massive Convex Allocation

Allocate exactly `K` indistinguishable units among `n` machines. Machine `i` receives an integer `x[i]` with `0 <= x[i] <= cap[i]` and costs `a[i]*x[i]^2 + b[i]*x[i]`, where `a[i] > 0`. Print the minimum total cost, or `IMPOSSIBLE` if total capacity is too small.

## Input
`n K`, followed by `n` lines `a b cap`.

`1 <= n <= 200000`, `0 <= K,cap[i] <= 10^14`, `1 <= a[i] <= 10^6`, `|b[i]| <= 10^12`. The answer fits a signed 128-bit integer.

## Sample
```text
3 5
1 0 4
2 -1 3
3 2 5
```
```text
15
```
