# Terminal Backbone Frontier

A weighted undirected graph has `n` vertices and `m` edges, and `k` of its
vertices are terminals, numbered `0..k-1` in the order given. For each query
mask, consider the terminals whose bits are set in the mask and print the
minimum total weight of a set of edges that connects all of them (other
vertices may be used).

## Input

```text
n m k q
m lines: u v w
one line: t_0 t_1 ... t_(k-1)      (terminal vertices)
q lines: mask
```

- `1 <= n <= 60`, `0 <= m <= 500`, `1 <= k <= 10`, `1 <= q <= 1000`;
- `1 <= w <= 10^9`;
- `1 <= mask < 2^k`; every query's terminals are connected in the graph.

## Output

Print one minimum weight per query.

## Sample input

```text
4 4 3 2
1 2 1
2 3 1
3 4 1
1 4 10
1 3 4
3
7
```

## Sample output

```text
2
3
```
