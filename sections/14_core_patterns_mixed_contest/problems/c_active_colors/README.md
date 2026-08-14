# C. Active Colors

## Statement

For each test case, you are given `n` colored half-open intervals
`[l_i, r_i)`. Interval `i` has color `c_i`. You are also given `q` query
points.

For each query point `x`, output the number of distinct colors that have at
least one active interval at `x`.

An interval `[l, r)` is active at `x` when:

```text
l <= x < r
```

Answers must be printed in the original query order.

## Input

```text
T
n q
l1 r1 c1
l2 r2 c2
...
ln rn cn
x1 x2 ... xq
...
```

The constraints are:

```text
-10^18 <= l_i < r_i <= 10^18
1 <= c_i <= 10^18
-10^18 <= x_j <= 10^18
sum of n + q over all test cases <= 200000
```

## Output

For each test case, print `q` integers on one line.
