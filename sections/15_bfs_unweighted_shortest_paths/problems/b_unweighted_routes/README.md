# B. Unweighted Routes

You are given a directed graph where every edge costs exactly one move. From a
source vertex `s`, answer several shortest-distance queries.

If a target is unreachable from `s`, its distance is `-1`.

## Input

```text
n m s q
u1 v1
...
um vm
x1 x2 ... xq
```

- `n` is the number of vertices, numbered from `1` through `n`.
- `m` is the number of directed edges.
- `s` is the source vertex.
- `q` is the number of distance queries.
- Each pair `u_i v_i` describes a directed edge from `u_i` to `v_i`.
- Each `x_i` is a target vertex whose distance from `s` must be reported.

- `1 <= n <= 2 * 10^5`
- `0 <= m <= 2 * 10^5`
- `1 <= s <= n`
- `1 <= u_i, v_i, x_i <= n`
- `1 <= q <= 2 * 10^5`

Edges are directed: an edge `u v` lets you move from `u` to `v`, not
necessarily from `v` to `u`.

## Output

Print `q` integers: the distance from `s` to each query target.

## Sample

Input:

```text
6 6 1 6
1 2
1 3
2 4
3 4
4 5
6 5
1 2 4 5 6 3
```

Output:

```text
0 1 2 3 -1 1
```
