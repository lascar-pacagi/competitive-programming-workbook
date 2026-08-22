# B. Summatory Totient

For a positive integer `x`, `phi(x)` is the number of integers in `1..x` that
are coprime with `x`. Define

```text
Phi(n) = phi(1) + phi(2) + ... + phi(n).
```

Answer independent queries for `Phi(n)` modulo `1,000,000,007`.

## Input

```text
q
n1
n2
...
nq
```

- `1 <= q <= 30`
- `1 <= ni <= 10^9`

## Output

Print `q` lines, one answer per query.

## Sample

```text
3
1
5
10
```

```text
1
10
32
```
