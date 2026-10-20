# B. All Borders

You are given a string `s` of length `n`. A **proper border** is a nonempty
string that is both a prefix and a suffix of `s`, but is shorter than `s`.
A prefix consists of the first characters of `s`; a suffix consists of the
last characters. The prefix and suffix may overlap.

Find the lengths of all proper borders of `s`.

## Input

The only line contains `s`.

- `1 <= n <= 200000`.
- `s` contains only lowercase English letters (`a`-`z`).

## Output

Print all proper border lengths in increasing order, separated by spaces.
Do not include `0` or `n`. If there are no proper borders, print an empty line.

## Sample

Input:

```text
ababa
```

Output:

```text
1 3
```

The proper borders are `a` and `aba`, of lengths `1` and `3`.
