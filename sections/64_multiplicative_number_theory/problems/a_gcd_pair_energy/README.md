# A. GCD Pair Energy

A laboratory stores `n` positive resonance values `a1..an`. The energy of an
unordered pair of distinct specimens `i < j` is
`gcd(ai, aj)^k`.

Compute the sum of the energies of all unordered pairs modulo
`1,000,000,007`.

## Input

```text
n k
a1 a2 ... an
```

- `2 <= n <= 200000`
- `1 <= ai <= 200000`
- `0 <= k <= 10^9`

For `k=0`, every positive gcd to the zeroth power is `1`.

## Output

Print one integer: the required sum modulo `1,000,000,007`.

## Sample

```text
3 2
2 4 6
```

```text
12
```

The three gcds are `2, 2, 2`; each contributes `2^2=4`.
