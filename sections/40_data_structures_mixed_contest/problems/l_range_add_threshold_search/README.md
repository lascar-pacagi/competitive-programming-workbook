# L. Range Add Threshold Search

Maintain an integer array under range additions. There are two kinds of
operations:

- `A l r x`: add `x` to every element from position `l` through position `r`.
- `Q l r x`: print the smallest position `i` in `[l, r]` for which
  `a[i] >= x`, or `-1` if no such position exists.

All positions are 1-based. Additions and thresholds may be negative.

## Input

```text
n q
a1 ... an
q operations
```

`1 <= n,q <= 200000`, `|a_i|,|x| <= 10^9`.

## Output

For every `Q` operation, print the requested position or `-1`.

## Sample

```text
6 8
1 4 -2 3 0 5
Q 2 5 3
A 1 3 -4
Q 1 3 1
Q 3 6 4
A 4 6 2
Q 3 5 5
A 2 4 -6
Q 1 6 3
```

```text
2
-1
6
4
6
```
