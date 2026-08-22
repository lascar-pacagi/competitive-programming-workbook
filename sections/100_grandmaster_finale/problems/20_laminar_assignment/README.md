# Laminar Assignment

A rooted tree has some vertices marked as leaves. There are `w` workers. An
offer `(v,c)` for worker `i` means that the worker may be assigned to any leaf
in the subtree of `v`, at cost `c`. Assign every worker to a distinct leaf and
minimize total cost, or report `IMPOSSIBLE`.

## Input

```text
n w
parent[2] ... parent[n]
for i=1..w: t followed by t pairs v c
```

- root is vertex `1`; `parent[v] < v`;
- `1 <= n <= 1000`, `1 <= w <= 300`, total offers `<= 5000`;
- `0 <= c <= 10^9`; every worker has at least one offer.

A vertex with no children is a leaf. Duplicate offers are allowed.

## Output

Print the minimum cost, or `IMPOSSIBLE`.

## Sample input

```text
5 2
1 1 2 2
2 2 7 3 1
1 2 4
```

## Sample output

```text
5
```
