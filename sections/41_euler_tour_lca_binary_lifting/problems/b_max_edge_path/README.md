# B. Max Edge On Path

You are given a rooted weighted tree with `n` vertices, rooted at `1`. Every
vertex other than the root is joined to its parent by one weighted edge. For
each query `u v`, print the largest edge weight on the unique path between `u`
and `v`.

## Input

```text
n q
parent2 weight2
parent3 weight3
...
parentn weightn
u1 v1
u2 v2
...
uq vq
```

- `1 <= n, q <= 200,000`
- `1 <= parenti < i` for `2 <= i <= n`
- `1 <= weighti <= 10^9`
- `1 <= u, v <= n`

`weighti` is the weight of the edge joining vertex `i` to `parenti`.

## Output

Print one integer per query. When `u == v` the path contains no edge at all;
print `0` in that case. Weights are positive, so `0` is unambiguous as the
"no edge" answer.

## Sample

```text
5 3
1 7
1 2
2 9
2 4
4 5
3 4
2 2
```

```text
9
9
0
```

The edges are `2-1` of weight `7`, `3-1` of weight `2`, `4-2` of weight `9`,
and `5-2` of weight `4`. The first query walks `4 -> 2 -> 5` over weights `9`
and `4`. The second walks `3 -> 1 -> 2 -> 4` over weights `2`, `7` and `9`. The
third stays put and so meets no edge.
