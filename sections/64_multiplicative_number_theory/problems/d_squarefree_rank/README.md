# D. Square-Free Rank

A positive integer is **square-free** if no square greater than `1` divides
it. Thus `1, 2, 3, 5, 6, 7, 10, ...` are square-free, while `4`, `8`, and `12`
are not.

For each query, print the `k`-th positive square-free integer.

## Input

```text
q
k1
k2
...
kq
```

- `1 <= q <= 30`
- `1 <= ki <= 10^11`

## Output

Print one answer per line.

## Sample

```text
4
1
4
7
10
```

```text
1
5
10
14
```
