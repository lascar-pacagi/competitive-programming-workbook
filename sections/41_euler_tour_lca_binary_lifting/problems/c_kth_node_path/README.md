# C. Kth Node On Path

You are given a rooted tree with `n` vertices, rooted at `1`. For each query
`u v k`, print the `k`-th vertex on the unique path from `u` to `v`, counting
from `u` and starting at `1`, so `k = 1` is `u` itself.

If the path has fewer than `k` vertices, print `-1`.

## Input

```text
n q
parent2
parent3
...
parentn
u1 v1 k1
u2 v2 k2
...
uq vq kq
```

- `1 <= n, q <= 200,000`
- `1 <= parenti < i` for `2 <= i <= n`
- `1 <= u, v <= n`
- `1 <= k <= 10^9`

`parenti` is the parent of vertex `i`; vertex `1` has no parent line.

## Output

Print one integer per query: the `k`-th vertex on the path, or `-1` when the
path has fewer than `k` vertices.

## Sample

```text
5 4
1
1
2
2
4 5 1
4 5 2
4 5 3
3 5 4
```

```text
4
2
5
5
```

The tree is `1` with children `2` and `3`, and `2` with children `4` and `5`.
The path `4 -> 2 -> 5` has three vertices, so the first three queries walk
along it and return `4`, `2` and `5`. The last query walks
`3 -> 1 -> 2 -> 5`, whose fourth vertex is `5`.
