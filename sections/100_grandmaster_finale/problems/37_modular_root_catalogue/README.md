# Modular Root Catalogue

For an odd prime `p`, let `g` be the smallest primitive root modulo `p`: the
smallest `g` whose powers `g^0, g^1, ..., g^(p-2)` are all different modulo
`p`. Given `k` and `a`, print the smallest integer `y >= 0` such that

```text
(g^y)^k = a (mod p),
```

or `-1` if no such `y` exists.

## Input

```text
q
q lines: p k a
```

- `1 <= q <= 20`;
- `p` is an odd prime with `p <= 10^12`;
- `1 <= k <= 10^18` and `1 <= a < p`.

## Output

Print one answer per query.

## Sample input
```text
2
7 2 2
7 2 3
```
## Sample output
```text
1
-1
```
