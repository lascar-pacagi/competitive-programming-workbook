# R. Exact Divisor Count

For each query `(N,K)`, count the positive integers `x <= N` having exactly
`K` positive divisors. Here `N <= 10^6` and `1 <= K <= 100`.

There are at most `200` queries. The answer fits in signed 64-bit integer.

## Input

```text
q
N_1 K_1
...
N_q K_q
```

## Output

Print one answer per query.

## Sample

```text
3
10 4
100 3
100 1
```

```text
3
4
1
```
