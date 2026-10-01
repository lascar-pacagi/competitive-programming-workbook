# Staircase Moments

A staircase has steps of height `q(x) = floor((a*x + b) / c)` at positions
`x = 0, 1, ..., n`. For each query print, modulo `998244353`, the three
moments

```text
F = sum of q(x),     G = sum of x * q(x),     H = sum of q(x)^2,
```

all sums taken over `x = 0, 1, ..., n`.

## Input

```text
T
T lines: n a b c
```

- `1 <= T <= 100000`;
- `0 <= n, a, b <= 10^18` and `1 <= c <= 10^18`.

## Output

For each query print `F G H` on its own line.

## Sample input

```text
2
4 3 1 2
10 5 7 3
```

## Sample output

```text
16 47 74
114 754 1490
```
