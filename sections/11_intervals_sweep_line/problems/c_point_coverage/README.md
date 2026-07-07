# C. Point Coverage

## Statement

For each test case, you are given `n` closed intervals `[l_i, r_i]` and `q`
query points. For each query point, output how many intervals contain it.

An interval `[l, r]` contains point `x` when:

```text
l <= x <= r
```

Answers must be printed in the original query order.

## Input

```text
T
n q
l1 r1
l2 r2
...
ln rn
x1 x2 ... xq
...
```

The sum of `n + q` over all test cases is at most `200000`.

## Output

For each test case, print `q` integers: the coverage count for the query
points in their original order.

