# A. Tree Distances

You are given a rooted tree with `n` vertices, rooted at `1`. For each query
`u v`, print the number of edges on the unique path between `u` and `v`.

## Input

```text
n q
parent2
parent3
...
parentn
u1 v1
u2 v2
...
uq vq
```

- `1 <= n, q <= 200,000`
- `1 <= parenti < i` for `2 <= i <= n`
- `1 <= u, v <= n`

`parenti` is the parent of vertex `i`. Because every parent is smaller than its
child, the vertices already arrive in an order where each parent is known
before its child; vertex `1` has no parent line.

## Output

Print one integer per query: the number of **edges** on the path. A path
between a vertex and itself has no edges, so the answer is `0`.

## Sample

```text
5 4
1
1
2
2
4 5
3 4
2 2
1 5
```

```text
2
3
0
2
```

The tree is `1` with children `2` and `3`, and `2` with children `4` and `5`.
The first query walks `4 -> 2 -> 5`, which is `2` edges. The second walks
`3 -> 1 -> 2 -> 4`, which is `3`. The third asks for the distance from a vertex
to itself, and the fourth walks `1 -> 2 -> 5`.
