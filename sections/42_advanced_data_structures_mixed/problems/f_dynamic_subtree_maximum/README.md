# F. Dynamic Subtree Maximum

Maintain one integer value at every vertex of a rooted tree.

- `U u x`: replace the value at vertex `u` with `x` (not an addition).
- `Q u`: print the largest current value in the subtree of `u`.

An update changes only one vertex. Values and answers may be negative.

## Input

The first line contains `n q`. The second line contains the initial values
`a_1 ... a_n`. The next `n - 1` lines each contain `u v`, an undirected edge.
The edges form a tree with vertices numbered `1` through `n`, rooted at `1`.
The next `q` lines contain the operations or queries described below.

The subtree of `u` includes `u` and all its descendants. For `n = 1`, there
are no edge lines. Process updates and queries in input order.


## Constraints

`1 <= n,q <= 200000`, `-10^9 <= a_i,x <= 10^9`, `1 <= u,v <= n`.

## Output

Print one answer per query on its own line, in query order. Updates produce
no output.

## Sample

### Input

```text
5 5
1 2 3 4 5
1 2
1 3
3 4
3 5
Q 3
U 4 -10
Q 3
U 5 -2
Q 3
```

### Output

```text
5
5
3
```

### Explanation

Vertex 3 has subtree `{3,4,5}`. Its values change from `3,4,5` to
`3,-10,5`, then `3,-10,-2`; the maxima are `5`, `5`, and `3`.
