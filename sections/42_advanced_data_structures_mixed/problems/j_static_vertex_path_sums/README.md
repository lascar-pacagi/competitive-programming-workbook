# J. Static Vertex Path Sums

Every vertex of an undirected tree has a fixed integer value. For each query
`u v`, print the sum of the values on the unique simple path from `u` to `v`,
including both endpoints. Values never change. If `u = v`, the answer is
just the value at that vertex. Negative values are allowed.

## Input

The first line contains `n q`. The second line contains the initial values
`a_1 ... a_n`. The next `n - 1` lines each contain `u v`, an undirected edge.
The edges form a tree with vertices numbered `1` through `n`, rooted at `1`.
The next `q` lines contain the queries described below.

The subtree of `u` includes `u` and all its descendants. For `n = 1`, there
are no edge lines. Each query line contains `u v`.


## Constraints

`1 <= n,q <= 200000`, `-10^9 <= a_i <= 10^9`, `1 <= u,v <= n`.

## Output

Print one answer per query on its own line, in query order. Updates produce
no output.

## Sample

### Input

```text
5 3
1 2 3 4 5
1 2
1 3
3 4
3 5
2 4
4 5
3 3
```

### Output

```text
10
12
3
```

### Explanation

The paths are `2 -> 1 -> 3 -> 4`, `4 -> 3 -> 5`, and the single
vertex `3`. Their sums are `10`, `12`, and `3`.
