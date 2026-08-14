# C. Distinct Range Queries

## Statement

For each test case, you are given an array `a` and `q` queries. A query `l r`
asks for the number of distinct values in `a[l..r]`.

Treat the input array as `a[1], a[2], ..., a[n]`. Every query satisfies
`1 <= l <= r <= n`, and `a[l..r]` includes both endpoints.

## Input

```text
T
n q
a1 a2 ... an
l1 r1
l2 r2
...
lq rq
...
```

The sum of `n + q` over all test cases is at most `200000`. Each array value
satisfies `|a_i| <= 10^18`, so C++ solutions should store array values in
`long long`.

## Output

For each query, print the answer in original query order, one per line.
