# Composite Discrete Log

For each query `(a, b, m)`, print the smallest integer `x >= 0` such that
`a^x = b (mod m)`, or `-1` if none exists. The base need not be coprime to the
modulus, and `a^0 = 1`.

## Input

```text
q
q lines: a b m
```

- `1 <= q <= 20`;
- `1 <= a, b < m <= 10^12`.

## Output

Print one answer per query.

## Sample input
```text
3
2 8 12
4 2 14
3 5 7
```
## Sample output
```text
3
2
5
```
