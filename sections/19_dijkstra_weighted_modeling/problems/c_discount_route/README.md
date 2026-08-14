# C. Discount Route

You need to travel from vertex `1` to vertex `n` in a directed weighted graph.
You may use one discount on at most one edge. If the original edge cost is `w`,
the discounted cost is `floor(w / 2)`.

Print the minimum possible total cost, or `-1` if vertex `n` is unreachable.

## Input

```text
n m
u1 v1 w1
...
um vm wm
```

`1 <= n <= 2 * 10^5`, `0 <= m <= 2 * 10^5`, `0 <= wi <= 10^9`.
Parallel directed edges and self-loops may appear. Each input edge is a
separate travel option.

## Output

Print the answer.

## Sample

Input:

```text
4 4
1 2 10
2 4 10
1 3 100
3 4 1
```

Output:

```text
15
```
