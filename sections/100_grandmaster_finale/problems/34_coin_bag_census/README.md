# Coin Bag Census

A mint issues `n` coin types; type `i` has value `w[i]`. Different types may
share a value but are still different types, and every type is available in
unlimited supply.

A **bag** is a multiset of coins: it records only how many coins of each type
it holds. For every total `s` from `1` to `S`, count the bags of total value
exactly `s`, modulo `998244353`.

## Input

```text
n S
w[1] ... w[n]
```

- `1 <= n, S <= 200000`;
- `1 <= w[i] <= 200000`.

## Output

Print `S` integers on one line: the counts for `s = 1, 2, ..., S`.

## Sample input

```text
3 6
1 2 2
```

## Sample output

```text
1 3 3 6 6 10
```
