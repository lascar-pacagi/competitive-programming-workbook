# C. Range Add Point Query

Maintain an array under two kinds of operations:

- `1 l r x`: add `x` to every value in `a[l..r]`.
- `2 i`: print the current value of `a[i]`.

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

For every operation of type `2`, print the requested value on its own line.

## Sample

```text
5 5
10 20 30 40 50
2 3
1 2 4 5
2 3
1 1 5 -10
2 5
```

```text
30
35
40
```
