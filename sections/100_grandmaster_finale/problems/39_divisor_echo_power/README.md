# Divisor Echo Power

For functions `a` and `b` on the positive integers, define their **divisor
product** by

```text
(a # b)(n) = sum over all pairs (x, y) with x * y = n of a(x) * b(y).
```

The operation `#` is associative and commutative, and its identity `e` has
`e(1) = 1` and `e(n) = 0` for `n > 1`.

You are given `f(1), ..., f(N)` with `f(1) = 1`, and an integer `k`. Print the
values at `1, ..., N` of

```text
g = f # f # ... # f      (k factors; g = e when k = 0),
```

modulo `998244353`.

## Input

```text
N k
f(1) f(2) ... f(N)
```

- `1 <= N <= 500000`;
- `0 <= k <= 10^18`;
- `0 <= f(i) < 998244353` and `f(1) = 1`.

## Output

Print `g(1) ... g(N)` on one line.

## Sample input

```text
8 2
1 1 1 1 1 1 1 1
```

## Sample output

```text
1 2 2 3 2 4 2 4
```

With `f` constantly `1` and `k = 2`, `g(n)` is the number of divisors of `n`.
