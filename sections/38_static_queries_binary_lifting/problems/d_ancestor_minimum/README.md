# D. Ancestor Minimum

You are given a rooted tree with root `1`. Every node has an integer label.
For each query `(v, k)`, consider node `v` and its first `k` ancestors. Print
the minimum label among these `k+1` nodes.

If the `k`-th ancestor of `v` does not exist, print `-1`.

## Input

```text
n q
label1 label2 ... labeln
parent2 parent3 ... parentn
v1 k1
v2 k2
...
vq kq
```

- `1 <= n, q <= 200,000`
- `-10^9 <= labeli <= 10^9`
- `1 <= parenti < i` for `2 <= i <= n`
- `1 <= vi <= n`
- `0 <= ki <= n`

## Output

Print one answer per query.

## Sample

```text
5 5
8 5 7 3 6
1 1 2 2
4 0
4 1
5 2
3 1
4 3
```

```text
3
3
5
7
-1
```

For `(5, 2)`, the relevant path is `5 -> 2 -> 1`, whose labels are
`6, 5, 8`.
