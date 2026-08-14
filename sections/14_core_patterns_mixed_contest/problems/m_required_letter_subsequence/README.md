# M. Required Letter Subsequence

Given a lowercase string `s`, choose a subsequence of exactly `k` characters.
The chosen subsequence must contain the required letter `x` at least `r` times.
Print the lexicographically smallest valid subsequence.

## Input

```text
s
k x r
```

`1 <= k <= |s| <= 200000`, `x` is a lowercase English letter,
`1 <= r <= k`, and `s` contains `x` at least `r` times.

## Output

Print the lexicographically smallest valid subsequence.

## Sample

```text
cbacbac
4 b 2
```

```text
baba
```
