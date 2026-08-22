# D. Subtree Mode Sum

Every vertex of a rooted tree (root `1`) has a positive color. For each vertex
`u`, consider color frequencies inside `u`'s subtree. Print the sum of all color
values attaining the maximum frequency.

## Input

```text
n
c1 ... cn
n-1 edges
```

`1 <= n <= 200000`, `1 <= ci <= 10^9`.

## Sample

```text
5
1 2 1 3 2
1 2
1 3
3 4
3 5
```

```text
3 2 6 3 2
```
