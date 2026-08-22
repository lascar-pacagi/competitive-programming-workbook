# Ancestral Pattern Index

Every vertex of a tree stores one lowercase letter. The directed path string
`S(u,v)` is obtained by reading vertex labels along the simple path from `u` to
`v`, including both endpoints.

For each query `(u,v,x,y)`:

1. output the length of the longest common prefix of `S(u,v)` and `S(x,y)`;
2. output `-1`, `0`, or `1` according as `S(u,v)` is lexicographically smaller
   than, equal to, or greater than `S(x,y)`.

## Input

```text
n q
string of n vertex labels
n-1 lines: u v
q lines: u v x y
```

- `1 <= n,q <= 100000`.

## Output

Print `lcp comparison` for every query.

## Sample input

```text
5 3
abcab
1 2
1 3
2 4
2 5
4 3 1 5
4 5 1 5
3 4 3 5
```

## Sample output

```text
2 -1
3 0
3 -1
```
