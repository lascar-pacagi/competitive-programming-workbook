# Distinct Substring Rank

List every **distinct** nonempty substring of `s` in lexicographic order. For
each query `k`, describe the `k`-th string of that list by the position of its
leftmost occurrence in `s` and its length, or print `-1` if the list has fewer
than `k` strings.

## Input

```text
s
q
q lines: k
```

- `s` consists of lowercase letters, `1 <= |s| <= 200000`;
- `1 <= q <= 200000`;
- `1 <= k <= 10^18`.

## Output

For each query print `start length` (one-based `start` of the leftmost
occurrence), or `-1`.

## Sample input

```text
abab
7
1
2
3
4
5
7
8
```

## Sample output

```text
1 1
1 2
1 3
1 4
2 1
2 3
-1
```

The distinct substrings in order are `a, ab, aba, abab, b, ba, bab`.
