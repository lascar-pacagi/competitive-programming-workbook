# A. Point Add Range Sum

Maintain an array under two kinds of operations:

- `1 i x`: add `x` to `a[i]`.
- `2 l r`: print the sum of `a[l..r]`.

All indices are 1-based.

## Input

The first line contains `n` and `q`. The second line contains the `n` initial
array values. Each of the next `q` lines describes one operation.

Constraints:

- `1 <= n, q <= 200,000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= i <= n`
- `1 <= l <= r <= n`

## Output

For every operation of type `2`, print the requested range sum on its own line.

## Sample

```text
5 6
1 2 3 4 5
2 1 5
1 3 10
2 2 4
1 5 -2
2 4 5
2 3 3
```

```text
15
19
7
13
```
