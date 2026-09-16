# C. Range Add, Range GCD

Maintain an array under range additions and range GCD queries.

## Input

The first line contains `n` and `q`. The second line contains `n` integers.

Each of the next `q` lines has one of these forms:

- `1 l r x`: add `x` to every value in the inclusive range `[l, r]`.
- `2 l r`: print the GCD of all values in the inclusive range `[l, r]`.

## Output

For every operation of type `2`, print one nonnegative GCD.

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Every array value remains within signed 64-bit range.
- `1 <= l <= r <= n`

## Sample

```text
5 5
6 10 14 22 26
2 1 5
1 2 4 2
2 2 4
1 1 5 3
2 3 5
```

```text
2
4
1
```
