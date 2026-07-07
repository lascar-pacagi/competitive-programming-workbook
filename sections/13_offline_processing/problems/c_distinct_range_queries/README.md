# C. Distinct Range Queries

## Statement

For each test case, you are given an array `a` and `q` queries. A query `l r`
asks for the number of distinct values in `a[l..r]`.

Indices are one-based and inclusive.

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

The sum of `n + q` over all test cases is at most `200000`.

## Output

For each query, print the answer in original query order, one per line.

