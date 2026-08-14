# D. Weighted Tree Distances

You are given a rooted weighted tree with root `1`. For each query `u v`,
print the sum of edge weights on the unique path from `u` to `v`.

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
- `-10^9 <= weighti <= 10^9`
- `1 <= u, v <= n`

`weighti` is the weight of the edge from node `i` to `parenti`.

## Output

Print one distance per query.

## Sample

```text
5 4
1 7
1 2
2 9
2 4
4 5
3 4
2 2
1 5
```

```text
13
18
0
11
```

For the first query, the path is `4 -> 2 -> 5`, so its weight is `9 + 4`.
