# D. Forced Independent Set

You are given an undirected tree with `n` vertices. An **independent set** is a
set of vertices with no edge whose two endpoints are both selected.

For every vertex `v`, determine the largest possible size of an independent
set that is required to contain `v`.

## Input

```text
n
u1 v1
u2 v2
...
u(n-1) v(n-1)
```

The vertices are numbered `1` through `n`.

## Constraints

```text
1 <= n <= 200000
1 <= ui, vi <= n
```

The edges form a tree.

## Output

Print `n` integers. The `v`-th integer is the largest size of an independent
set that contains vertex `v`.

## Sample

```text
5
1 2
1 3
3 4
3 5
```

```text
3 3 2 3 3
```

For example, when vertex `3` must be selected, vertices `1`, `4`, and `5`
cannot be selected. Selecting `2` together with `3` gives the answer `2`.
