# Polynomial Constraint Recovery

All arithmetic is modulo the prime `998244353`.

A hidden polynomial `F(x) = c[0] + c[1] x + ... + c[n-1] x^(n-1)` has degree
less than `n`. You are told its values at `n` distinct points, in arbitrary
order: `F(x_i) = y_i`. Recover the coefficients.

## Input

```text
n
n lines: x_i y_i
```

- `1 <= n <= 50000`;
- `0 <= x_i, y_i < 998244353`, and the `x_i` are pairwise distinct (zero is
  allowed).

## Output

Print `c[0] c[1] ... c[n-1]` on one line.

## Sample input
```text
2
3 7
0 1
```
## Sample output
```text
1 2
```
