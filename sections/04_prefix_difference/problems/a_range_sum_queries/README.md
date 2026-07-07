# A. Range Sum Queries

## Statement

You are given an array and several range queries. Each query gives 1-indexed
inclusive endpoints `l` and `r`. Print the sum:

```text
a_l + a_{l+1} + ... + a_r
```

## Input

```text
T
n q
a1 a2 ... an
l1 r1
...
lq rq
...
```

`1 <= T <= 30`, the total `n + q` over all test cases is at most `200000`, and
array values fit in signed 32-bit integers.

## Output

For each query, print the range sum on its own line.

