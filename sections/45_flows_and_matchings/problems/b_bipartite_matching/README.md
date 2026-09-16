# B. Bipartite Matching

You are given a bipartite graph: `n` vertices on the left, `m` vertices on the
right, and `e` edges between them. A matching is a set of edges no two of which
share a vertex. Print the size of a largest matching.

## Input

```text
n m e
a1 b1
a2 b2
...
ae be
```

- `1 <= n, m <= 500`
- `0 <= e <= n * m`
- `1 <= ai <= n` and `1 <= bi <= m`

Each line `ai bi` is an edge joining left vertex `ai` to right vertex `bi`. The
two sides are numbered independently, so left vertex `1` and right vertex `1`
are different vertices. No edge is listed twice.

## Output

Print one integer: the largest number of edges that can be chosen so that every
left vertex appears at most once and every right vertex appears at most once.
The answer is at most `min(n, m)`, and it is `0` when `e = 0`.

## Sample

```text
3 3 4
1 1
1 2
2 2
3 3
```

```text
3
```

Left `1` takes right `1`, left `2` takes right `2`, and left `3` takes right
`3`, so all three are matched and no larger matching exists: there are only
three vertices on each side.
