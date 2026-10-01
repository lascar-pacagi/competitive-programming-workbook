# Window Substring Census

A telemetry log is a string `s` of lowercase letters. For a window `(l, r)`,
the analysts look at the piece `s[l..r]` (one-based, inclusive) and ask how
many **different** nonempty strings occur in it as contiguous substrings.

Answer all windows. They are independent.

## Input

```text
s
q
q lines: l r
```

- `1 <= |s|, q <= 200000`;
- `1 <= l <= r <= |s|`.

## Output

Print one line per window.

## Sample input

```text
abcab
4
1 5
2 4
4 5
1 1
```

## Sample output

```text
12
6
3
1
```
