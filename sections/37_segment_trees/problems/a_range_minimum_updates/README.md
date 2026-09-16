# A. Range Minimum Updates

Maintain an array under two kinds of operations:

- `1 i x`: assign `a[i] = x`.
- `2 l r`: print the minimum value in `a[l..r]`.

All indices are 1-based.

## Input

The first line contains `n` and `q`. The second line contains the `n` initial
array values. Each of the next `q` lines describes one operation.

## Constraints

- `1 <= n, q <= 200,000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= i <= n`
- `1 <= l <= r <= n`

## Output

For every operation of type `2`, print the requested minimum on its own line.

## Sample

```text
5 5
5 4 3 2 1
2 1 5
1 3 10
2 2 4
1 5 -7
2 4 5
```

```text
1
2
-7
```
