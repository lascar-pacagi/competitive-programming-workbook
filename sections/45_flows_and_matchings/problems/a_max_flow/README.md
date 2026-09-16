# A. Max Flow

You are given a directed graph on `n` vertices where every edge has a
capacity. Vertex `1` is the source and vertex `n` is the sink. Print the value
of a maximum flow from `1` to `n`.

## Input

```text
n m
u1 v1 c1
u2 v2 c2
...
um vm cm
```

- `2 <= n <= 500`
- `0 <= m <= 5,000`
- `1 <= ui, vi <= n` and `ui != vi`
- `0 <= ci <= 10^9`

Each line gives one directed edge from `ui` to `vi` of capacity `ci`. The same
ordered pair may appear more than once; treat repeats as separate parallel
edges rather than merging them. An edge is directed: `u v c` says nothing about
whether flow may travel from `v` to `u`.

## Output

Print one integer, the maximum flow value. It fits in a signed 64-bit integer,
but the sum of capacities may not fit in 32 bits, so accumulate in `long long`.

If the sink is unreachable from the source, the answer is `0`.

## Sample

```text
4 5
1 2 3
1 3 2
2 3 1
2 4 2
3 4 4
```

```text
5
```

One way to reach `5` sends two units along `1 -> 2 -> 4`, two along
`1 -> 3 -> 4`, and one along `1 -> 2 -> 3 -> 4`.
