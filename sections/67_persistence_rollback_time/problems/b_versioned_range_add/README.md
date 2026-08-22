# B. Versioned Range Add

Version `0` is an array `a[1..n]`. Process:

- `A v l r x`: create the next version from version `v` by adding `x` to every
  position in `[l,r]`;
- `Q v l r`: print the sum of `[l,r]` in version `v`.

Only additions create versions. Versions may branch. All values and answers fit
signed 64-bit integers.

## Input

```text
n q
a1 ... an
q operations
```

`1 <= n,q <= 200000`, `-10^9 <= ai,x <= 10^9`.

## Sample

```text
4 6
1 2 3 4
Q 0 1 4
A 0 2 4 5
Q 1 1 4
A 0 1 2 -3
Q 2 1 3
Q 0 2 2
```

```text
10
25
0
2
```
