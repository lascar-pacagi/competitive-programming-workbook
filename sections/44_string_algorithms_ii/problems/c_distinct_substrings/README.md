# C. Distinct Substrings

You are given a string `s`. Count how many different nonempty strings appear
as contiguous substrings of `s`.

A **substring** is obtained by choosing a starting position and taking one
or more consecutive characters. Two occurrences count as the same substring
value when their characters are identical, even if they begin at different
positions or overlap.

For example, `aaa` contains three occurrences of `a`, but `a` contributes
only once to the answer. Its different nonempty substrings are `a`, `aa`,
and `aaa`, so the answer for that string is `3`.

## Input

The only line contains the string `s`.

- `1 <= |s| <= 200000`.
- `s` contains only lowercase English letters (`a`-`z`).

## Output

Print one integer: the number of distinct nonempty substring values of `s`.
Do not count the empty string. The answer may exceed the range of a signed
32-bit integer.

## Sample

Input:

```text
ababa
```

Output:

```text
9
```

The nine different substrings are `a`, `b`, `ab`, `ba`, `aba`, `bab`,
`abab`, `baba`, and `ababa`.
