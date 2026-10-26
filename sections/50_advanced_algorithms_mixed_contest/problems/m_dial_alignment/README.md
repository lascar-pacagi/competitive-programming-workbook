# M. Dial Alignment

A circular dial has `n` letters, written clockwise as a string `s`. A reader
expects to see a string `t` of the same length when it starts at the chosen
position and reads exactly one full turn clockwise.

Count the starting positions that produce `t`. More precisely, offset `k`
is valid when `s[k:] + s[:k] == t`, for `0 <= k < n`. Different offsets count
separately, even when repeated letters make their rotations identical.

## Input

The first line contains `s`. The second line contains `t`.

- `1 <= n <= 200000`.
- Both strings have length `n` and contain only lowercase English letters.

## Output

Print the number of valid offsets, between `0` and `n` inclusive.

## Sample

Input:

```text
abab
baba
```

Output:

```text
2
```

Offsets `1` and `3` both produce `baba`. They are two different dial positions.
