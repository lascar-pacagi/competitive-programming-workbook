# D. Nested Ranges Count

You are given `n` closed intervals. For every interval `i`, compute:

1. the number of other intervals contained in interval `i`; and
2. the number of other intervals that contain interval `i`.

Interval `i = [l[i], r[i]]` contains interval `j = [l[j], r[j]]` when
`l[i] <= l[j]` and `r[j] <= r[i]`. Identical intervals count as containing
each other.

## Input

```text
n
l1 r1
l2 r2
...
ln rn
```

## Constraints

```text
1 <= n <= 200,000
-1,000,000,000 <= l[i] <= r[i] <= 1,000,000,000
```

## Output

Print two lines:

```text
contains[1] contains[2] ... contains[n]
contained_by[1] contained_by[2] ... contained_by[n]
```

## Sample

Input:

```text
4
1 6
2 5
2 5
3 4
```

Output:

```text
3 2 2 0
0 2 2 3
```
