# A. Path Affine Composition

Each tree vertex `u` stores `f_u(x)=a_u*x+b_u` modulo `998244353`.

- `U u a b`: replace the function at `u`;
- `Q u v x`: walk along the simple path from `u` to `v`, applying vertex
  functions in that order, and print the final value.

## Input

```text
n q
a1 b1
...
an bn
n-1 edges
q operations
```

`1 <= n,q <= 200000`; coefficients and `x` are in `0..998244352`.

## Sample

```text
3 4
1 1
2 0
1 3
1 2
2 3
Q 1 3 1
Q 3 1 1
U 2 1 5
Q 1 3 1
```

```text
7
9
10
```
