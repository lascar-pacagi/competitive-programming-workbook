# A. Peak Active

## Statement

For each test case, you are given `n` half-open intervals `[l_i, r_i)`, where
`l_i < r_i`.

Find the maximum number of intervals active at the same time.

An interval `[l, r)` is active at time `x` when:

```text
l <= x < r
```

## Input

```text
T
n
l1 r1
l2 r2
...
ln rn
...
```

The sum of `n` over all test cases is at most `200000`.

## Output

For each test case, print the maximum active count.

