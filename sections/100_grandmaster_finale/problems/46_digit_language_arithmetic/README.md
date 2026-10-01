# Digit Language Arithmetic

For each query `(N, P)`, where `P` is a nonempty string of decimal digits,
count the integers `x` with `0 <= x <= N` whose usual decimal representation
does **not** contain `P` as a contiguous substring. The representation of zero
is `0`; positive integers are written without leading zeroes.

## Input

```text
q
q lines: N P
```

- `1 <= q <= 1000`;
- `0 <= N <= 10^18`;
- `1 <= |P| <= 18`.

## Output

Print one count per query.

## Sample input

```text
2
20 1
105 05
```

## Sample output

```text
10
105
```
