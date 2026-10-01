# Rabbit Cycle

A breeder tracks rabbit pairs with the Fibonacci sequence `F(0) = 0`,
`F(1) = 1`, `F(i) = F(i-1) + F(i-2)`, but only records each value modulo `m`.
The recorded sequence is periodic. For each `m`, print the length of its
shortest period: the smallest `L >= 1` such that `F(i + L) = F(i) (mod m)` for
every `i >= 0`.

## Input

```text
q
q lines: m
```

- `1 <= q <= 1000`;
- `1 <= m <= 10^18`.

## Output

Print one period per line. Every answer fits in a signed 64-bit integer.

## Sample input

```text
5
1
2
10
1000
1000000000000000000
```

## Sample output

```text
1
3
60
1500
1500000000000000000
```
