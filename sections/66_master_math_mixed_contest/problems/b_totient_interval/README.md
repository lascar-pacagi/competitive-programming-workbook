# B. Totient Interval

For positive `x`, let `phi(x)` count the integers in `1..x` coprime with `x`.
For each query, compute

```text
phi(L) + phi(L+1) + ... + phi(R)
```

modulo `1,000,000,007`.

## Input

```text
q
L1 R1
...
Lq Rq
```

- `1 <= q <= 30`
- `1 <= L <= R <= 10^9`

## Output

Print one answer per query.

## Sample

```text
3
1 1
2 5
6 10
```

```text
1
9
22
```
