# Exponential Polynomial Ledger

An account grows by a factor `r` every month, and in month `i` it also records
a weight `i^d`. The ledger total after `n` months is

```text
T(n) = sum over i = 0 .. n-1 of  r^i * i^d.
```

Print `T(n)` modulo `998244353`. Here `0^0 = 1`.

## Input

One line with `n r d`.

- `0 <= n <= 10^18`;
- `0 <= r <= 10^18`;
- `0 <= d <= 500000`.

## Output

Print `T(n)` modulo `998244353`.

## Sample input

```text
5 2 3
```

## Sample output

```text
1274
```

The terms for `i = 0, 1, 2, 3, 4` are `0, 2, 32, 216, 1024`.
