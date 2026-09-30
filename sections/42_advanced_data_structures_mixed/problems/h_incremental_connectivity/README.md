# H. Incremental Connectivity

An undirected graph has `n` vertices numbered from `1` to `n` and initially
has no edges. Process `q` operations:

- `A u v`: add an undirected edge between `u` and `v`.
- `Q u v`: print `YES` if a path currently connects `u` and `v`, otherwise `NO`.

Repeated edges and self-loops are allowed. Edges are never deleted. A vertex
is always connected to itself.

## Input

The first line contains `n q`. Each of the next `q` lines contains one
operation in one of the formats above.

## Constraints

`1 <= n,q <= 200000`, `1 <= u,v <= n`.

## Output

Print one answer per query on its own line, in query order. Updates produce
no output.

## Sample

### Input

```text
4 7
Q 1 3
A 1 2
A 2 3
Q 1 3
Q 1 4
A 3 4
Q 1 4
```

### Output

```text
NO
YES
NO
YES
```

### Explanation

The first two insertions connect vertices `1,2,3`. Vertex `4` joins
that component only after the final insertion.
