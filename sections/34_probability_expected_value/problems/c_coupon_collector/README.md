# C. Coupon Collector

There are `n` coupon types. Each draw independently gives one uniformly random
type. For each query `n`, print the expected number of draws needed to collect
all `n` types, modulo `1,000,000,007`.

## Input

```text
q
n1
n2
...
nq
```

`1 <= q <= 200,000`, `1 <= n <= 1,000,000`.

## Output

Print one answer per query.

## Sample

Input:

```text
4
1
2
3
4
```

Output:

```text
1
3
500000009
333333344
```
