# Binomial Ledger

An auditor needs many binomial coefficients `C(n, k)` (the number of ways to
choose `k` items out of `n`), each reduced modulo the same integer `m`. The
modulus `m` need not be prime. When `k > n`, `C(n, k) = 0`.

## Input

```text
m q
q lines: n k
```

- `1 <= m <= 10^6`;
- `1 <= q <= 100000`;
- `0 <= n, k <= 10^18`.

## Output

Print `C(n, k) mod m` for every query on its own line.

## Sample input

```text
360 4
10 3
100 50
1000000000000000000 999999999999999999
7 9
```

## Sample output

```text
120
216
280
0
```
