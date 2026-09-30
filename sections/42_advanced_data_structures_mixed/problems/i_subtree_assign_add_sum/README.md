# I. Subtree Assign, Add, and Sum

Maintain integer values on a rooted tree under three operations:

- `1 u x`: assign `x` to every vertex in the subtree of `u`.
- `2 u x`: add `x` to every vertex in the subtree of `u`.
- `3 u`: print the sum of the current values in the subtree of `u`.

Assignment replaces previous values; addition changes those values by `x`.

## Input

The first line contains `n q`. The second line contains the initial values
`a_1 ... a_n`. The next `n - 1` lines each contain `u v`, an undirected edge.
The edges form a tree with vertices numbered `1` through `n`, rooted at `1`.
The next `q` lines contain the operations or queries described below.

The subtree of `u` includes `u` and all its descendants. For `n = 1`, there
are no edge lines. Process updates and queries in input order.


## Constraints

`1 <= n,q <= 200000`, `1 <= u,v <= n`. Initial values and assignment
values have absolute value at most `10^9`; addition values have absolute
value at most `10^6`. All intermediate sums fit signed 64-bit integers.

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
3 3
1 3 7
2 4 -2
3 3
3 1
```

### Output

```text
12
19
22
```

### Explanation

The subtree of `3` starts with values `3,4,5`. Assigning `7` to all
three and then subtracting `2` at vertex `4` leaves `7,5,7`, summing to `19`.
Vertices `1` and `2` contribute another `3` to the whole-tree sum.
