# Spanning Weight Spectrum

A power grid has `n` substations and `m` numbered cables. Cable `i` joins
substations `u[i]` and `v[i]` and has an integer maintenance weight `w[i]`
with `0 <= w[i] <= K`. Cables that join a substation to itself are useless;
several cables may join the same pair.

A **backbone** is a set of exactly `n-1` cables that connects every
substation. Two backbones are different when they use different cable
numbers. The weight of a backbone is the sum of its cable weights, so it lies
between `0` and `(n-1)K`.

For every `W` from `0` to `(n-1)K`, count the backbones of weight exactly `W`,
modulo `998244353`.

## Input

```text
n m K
m lines: u v w
```

- `1 <= n <= 70`, `0 <= m <= 3000`, `0 <= K <= 12`;
- `1 <= u, v <= n` and `0 <= w <= K`.

## Output

Print `(n-1)K + 1` integers on one line: the counts for `W = 0, 1, ...,
(n-1)K`. When `n = 1`, the only backbone is the empty set.

## Sample input

```text
4 6 2
1 2 0
2 3 1
3 4 2
4 1 1
1 3 2
2 2 1
```

## Sample output

```text
0 0 1 3 3 1 0
```
