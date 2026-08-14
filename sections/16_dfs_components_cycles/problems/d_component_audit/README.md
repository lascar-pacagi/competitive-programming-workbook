# D. Component Audit

An undirected simple graph has `n` vertices and `m` roads. A connected
component is called a **tree component** when it contains no cycle; otherwise
it is a **cyclic component**. Count both kinds of components.

## Input

```text
n m
u1 v1
...
um vm
```

`1 <= n <= 200000`, `0 <= m <= 200000`. Vertices are numbered from `1` to
`n`. Every road joins two distinct vertices, and no road is listed twice.

## Output

Print two integers: the number of tree components, followed by the number of
cyclic components.

## Sample

```text
8 6
1 2
2 3
4 5
5 6
6 4
7 8
```

```text
2 1
```
