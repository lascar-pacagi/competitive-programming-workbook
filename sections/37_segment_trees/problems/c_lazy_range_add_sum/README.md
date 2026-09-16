# C. Lazy Range Add Sum

Maintain an array under two kinds of operations:

- `1 l r x`: add `x` to every value in `a[l..r]`.
- `2 l r`: print the sum of `a[l..r]`.

All indices are 1-based.

## Input

The first line contains `n` and `q`. The second line contains the `n` initial
array values. Each of the next `q` lines describes one operation.

## Constraints

- `1 <= n, q <= 200,000`
- `-10^9 <= a[i] <= 10^9`
- `-10^6 <= x <= 10^6`
- `1 <= l <= r <= n`

## Output

For every operation of type `2`, print the requested range sum on its own line.

## Sample

```text
5 5
1 2 3 4 5
2 1 5
1 2 4 10
2 3 5
1 1 5 -1
2 1 2
```

```text
15
32
11
```
