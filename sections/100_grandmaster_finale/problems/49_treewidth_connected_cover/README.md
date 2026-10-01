# Decomposition Vertex Cover

A graph has `n` weighted vertices and `m` edges. You are also given a valid
**nice tree decomposition** of the graph of width at most `15`. Find the
minimum total weight of a vertex cover (a vertex set touching every edge).

The decomposition has `t` nodes numbered `1..t` in topological order (children
before parents). Node `t` is the root and has an empty bag. Each node is one of:

- `L` — a leaf with an empty bag;
- `I c v` — the bag of child node `c` plus vertex `v`;
- `F c v` — the bag of child node `c` without vertex `v`;
- `J a b` — two children `a`, `b` with identical bags; the node has that bag.

Every graph edge has both endpoints together in some bag, and the nodes whose
bag contains any fixed vertex form a connected subtree.

## Input

```text
n m
w_1 ... w_n
m lines: u v
t
t lines: node descriptions as above
```

- `1 <= n <= 60`, `0 <= m <= n(n-1)/2`, `0 <= w_i <= 10^9`;
- `1 <= t <= 200000`, every bag has at most `16` vertices;
- the total `sum over nodes of 2^|bag|` is at most `2000000`.

## Output

Print the minimum weight of a vertex cover.

## Sample input

```text
2 1
5 7
1 2
5
L
I 1 1
I 2 2
F 3 1
F 4 2
```

## Sample output

```text
5
```
