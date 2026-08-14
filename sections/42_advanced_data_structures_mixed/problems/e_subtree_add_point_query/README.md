# E. Subtree Add, Point Query

A rooted tree has a value at every vertex. Process:

- `A u x`: add `x` to every vertex in the subtree of `u`;
- `Q u`: print the current value of `u`.

The tree is rooted at vertex `1`.

## Input
```text
n q
a1 ... an
n-1 edges
q operations
```
`1 <= n,q <= 200000`, and values fit in signed 64-bit integers.

## Sample
```text
5 6
1 2 3 4 5
1 2
1 3
3 4
3 5
Q 4
A 3 10
Q 4
Q 2
A 1 -1
Q 3
```
```text
4
14
2
12
```
