# C. Prerequisite Tree

There are `n` lessons arranged as a rooted tree with lesson `1` as the root.
Lesson `i` has study time `t[i]` and value `v[i]`.

You may choose any set of lessons with total study time at most `B`, but the
set must respect prerequisites: if lesson `x` is chosen and `x` is not the
root, then the parent of `x` must also be chosen.

Find the maximum total value.

## Input

```text
n B
t1 v1
t2 v2
...
tn vn
p2 p3 ... pn
```

`1 <= n <= 80`, `1 <= B <= 300`, `1 <= t[i] <= B`,
`1 <= v[i] <= 10^9`. For each `i >= 2`, `p[i]` is the parent of `i`.

## Output

Print the maximum total value.

## Sample

Input:

```text
5 7
2 5
3 8
2 4
4 7
1 3
1 1 2 2
```

Output:

```text
17
```
