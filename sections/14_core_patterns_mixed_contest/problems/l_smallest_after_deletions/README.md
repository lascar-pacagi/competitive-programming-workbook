# L. Smallest After Deletions

You are given a string `s` of decimal digits. Delete exactly `k` digits while
preserving the order of the remaining digits. Print the lexicographically
smallest remaining string.

Leading zeroes are kept. For example, deleting one digit from `102` can produce
`02`.

## Input

```text
s
k
```

`1 <= |s| <= 200000`, every character of `s` is between `0` and `9`, and
`0 <= k < |s|`.

## Output

Print the lexicographically smallest string obtainable after exactly `k`
deletions.

## Sample

```text
1432219
3
```

```text
1219
```
