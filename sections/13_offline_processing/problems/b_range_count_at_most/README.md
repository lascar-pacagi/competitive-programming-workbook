# B. Range Count At Most

## Statement

For each test case, you are given an array `a` and `q` queries. A query
`l r x` asks:

```text
How many elements in a[l..r] are <= x?
```

Indices are one-based and inclusive.

## Input

```text
T
n q
a1 a2 ... an
l1 r1 x1
l2 r2 x2
...
lq rq xq
...
```

The sum of `n + q` over all test cases is at most `200000`.

## Output

For each test case, print `q` integers: the answers in the original query
order, one per line.

