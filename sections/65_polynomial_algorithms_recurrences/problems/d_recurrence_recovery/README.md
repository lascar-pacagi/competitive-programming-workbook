# D. Recurrence Recovery

You observe a prefix `s[0]..s[L-1]` of an infinite sequence over the prime
field modulo `998244353`. The sequence is guaranteed to have a unique minimal
linear recurrence of order `r` with `2r <= L`, and the given prefix is long
enough to determine it.

Print `r` and `s[n]`.

The all-zero sequence has order `0`; all of its future terms are zero.

## Input

```text
L n
s[0] s[1] ... s[L-1]
```

- `1 <= L <= 2000`
- `0 <= n <= 10^18`
- every observed value is in `0..998244352`

## Output

Print `r s[n]`.

## Sample

```text
8 20
0 1 1 2 3 5 8 13
```

```text
2 6765
```
