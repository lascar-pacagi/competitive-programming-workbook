# C. Token Budget

## Statement

For each query, you are given an input size `n` and an operation budget `B`.
Among these complexity classes:

```text
linear      n
nlogn       n * ceil(log2(n))
quadratic   n^2
cubic       n^3
```

print the slowest class whose estimated operation count is at most `B`. If
even `linear` exceeds `B`, print `none`.

For `n = 1`, use `ceil(log2(n)) = 1` for this contest estimate.

## Input

```text
Q
n B
...
```

`1 <= n <= 10^9`, `0 <= B <= 10^18`.

## Output

For each query, print one of:

```text
cubic
quadratic
nlogn
linear
none
```

