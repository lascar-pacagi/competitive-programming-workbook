# I. Rerooted Subtree Sums

A fixed undirected tree has an integer value at each vertex. Its current root
starts at vertex `1`. Process:

- `R r`: choose vertex `r` as the current root; the edges and values stay fixed.
- `U u x`: assign value `x` to vertex `u` only.
- `Q u`: print the sum of values in the subtree of `u` under the current root.

The subtree includes `u`. Rooting the tree at `r` makes a vertex's parent its
neighbor on the path toward `r`; its subtree contains itself and all descendants
under that orientation. Changing the root can therefore change query answers.

## Input

```text
n q
a1 ... an
n-1 lines: u v
q operations
```

The edges form a tree on vertices `1..n`; they are undirected and may appear in
any order. There are no edge lines when `n=1`.

`1 <= n,q <= 200000`, `1 <= u,v,r <= n`, and `|a_i|,|x| <= 10^9`.
Use signed 64-bit sums.

## Output

Print one sum per `Q` in operation order. Other operations produce no output.

## Sample

```text
5 8
1 2 3 4 5
1 2
1 3
3 4
3 5
Q 3
R 4
Q 3
Q 4
U 2 -2
Q 3
R 1
Q 3
```

```text
12
11
15
7
12
```

With root 4, the subtree of 3 contains vertices `{1,2,3,5}`, while the
subtree of 4 is the whole tree. Updating vertex 2 reduces the first sum by 4.
After restoring root 1, vertex 2 is again outside the subtree of 3.
