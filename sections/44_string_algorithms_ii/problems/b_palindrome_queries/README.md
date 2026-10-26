# B. Palindrome Queries

You are given a string `s` of length `n` and `q` queries. Each query selects
a contiguous part of `s` using two positions `l` and `r`. Determine whether
that selected substring is a palindrome.

A **palindrome** reads the same from left to right and from right to left.
For example, `a`, `aca`, and `abba` are palindromes; `bac` is not.

Positions are **1-based**, and both endpoints are included: a query `l r`
selects the characters at positions `l`, `l + 1`, ..., `r`. Its length is
`r - l + 1`. The string does not change between queries.

## Input

The first line contains the string `s`.
The second line contains the integer `q`.
Each of the next `q` lines contains two integers `l` and `r`, describing one
query.

- `1 <= n <= 200000`.
- `1 <= q <= 200000`.
- `s` contains only lowercase English letters (`a`-`z`).
- For every query, `1 <= l <= r <= n`.

## Output

For each query, print `YES` if the selected substring is a palindrome, and
`NO` otherwise. Print one answer per line, in query order.

## Sample

Input:

```text
abacaba
4
1 7
2 4
3 5
1 3
```

Output:

```text
YES
NO
YES
YES
```

The four selected substrings are `abacaba`, `bac`, `aca`, and `aba`.
Only `bac` is not a palindrome.
