# Dynamic Forest Ledger

Maintain a forest of `n` vertices. Vertex `i` initially stores `a[i]` modulo
`1,000,000,007`. Process the following operations:

- `LINK u v`: add edge `(u,v)`. The vertices are currently disconnected.
- `CUT u v`: remove edge `(u,v)`. This edge currently exists.
- `AFFINE u v m b`: for every vertex `x` on the simple path `u--v`, replace
  its value by `(m*value[x]+b) mod MOD`.
- `SUM u v`: output the sum modulo `MOD` of values on path `u--v`.

Every path operation is guaranteed to use connected vertices.

## Input

```text
n q
a[1] ... a[n]
q operations
```

- `1 <= n,q <= 200000`
- all initial values, `m`, and `b` lie in `[0,MOD)`.

## Sample input

```text
4 8
1 2 3 4
LINK 1 2
LINK 2 3
SUM 1 3
AFFINE 1 3 2 1
SUM 1 3
LINK 3 4
CUT 2 3
SUM 3 4
```

## Sample output

```text
6
15
11
```
