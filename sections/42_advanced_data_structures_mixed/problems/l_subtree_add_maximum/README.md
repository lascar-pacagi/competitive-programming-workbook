# L. Subtree Add, Subtree Maximum

Maintain vertex values in a rooted tree:

- `A u x`: add `x` to every vertex in the subtree of `u`.
- `Q u`: print the largest current value in the subtree of `u`.

The subtree includes `u` itself. Updates accumulate, and values and answers
may be negative. Every query sees all preceding updates.

## Input

The first line contains `n q`. The second line contains the initial values
`a_1 ... a_n`. The next `n - 1` lines each contain `u v`, an undirected edge.
The edges form a tree with vertices numbered `1` through `n`, rooted at `1`.
The next `q` lines contain the operations or queries described below.

The subtree of `u` includes `u` and all its descendants. For `n = 1`, there
are no edge lines. Process updates and queries in input order.


## Constraints

`1 <= n,q <= 200000`, `1 <= u,v <= n`, `|a_i| <= 10^9`,
`|x| <= 10^6`. Use signed 64-bit values.

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
A 3 5
Q 1
A 1 -20
Q 3
```

### Output

```text
5
10
-10
```

### Explanation

The first addition changes the subtree of `3` to `8,9,10`. Subtracting
`20` from the whole tree changes those values to `-12,-11,-10`.
