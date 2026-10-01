# Universal Exponent Clock

For a positive integer `n`, let `L(n)` be the smallest positive integer `L`
such that `a^L = 1 (mod n)` for every integer `a` coprime to `n`. Define
`L(1) = 1`. Answer several queries.

## Input

```text
q
q lines: n
```

- `1 <= q <= 200`;
- `1 <= n < 2^64`.

## Output

Print `L(n)` for every query on its own line.

## Sample input
```text
3
1
8
15
```
## Sample output
```text
1
2
4
```
