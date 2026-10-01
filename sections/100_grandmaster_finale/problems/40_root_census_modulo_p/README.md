# Root Census Modulo p

A polynomial `f(x) = c[0] + c[1] x + ... + c[d] x^d` has integer coefficients,
and `p` is a prime. Count the residues `x` in `{0, 1, ..., p-1}` with
`f(x) = 0 (mod p)`. (If every coefficient is divisible by `p`, all `p`
residues count.)

## Input

```text
p d
c[0] c[1] ... c[d]
```

- `2 <= p <= 10^18`, and `p` is prime;
- `0 <= d <= 3000`;
- `0 <= c[i] <= 10^18`.

## Output

Print the number of roots modulo `p`.

## Sample input

```text
7 3
6 0 0 1
```

## Sample output

```text
3
```

The roots of `x^3 + 6 = x^3 - 1` modulo `7` are `1, 2, 4`.
