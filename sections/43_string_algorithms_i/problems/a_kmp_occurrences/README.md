# A. KMP Occurrences

You are given two strings: a pattern `p` and a text `t`. Find every starting
position in `t` at which the entire pattern occurs as a contiguous substring.

Positions are **1-based**: the first character of `t` is at position `1`.
Overlapping occurrences count separately. For example, `aaa` occurs in
`aaaaa` at positions `1`, `2`, and `3`.

## Input

The first line contains the pattern `p`.
The second line contains the text `t`.

- `1 <= |p|, |t| <= 200000`.
- Both strings contain only lowercase English letters (`a`-`z`).
- The pattern may be longer than the text.

## Output

Print the number of occurrences on the first line.
On the second line, print their starting positions in increasing order,
separated by spaces.

If there are no occurrences, print `0` on the first line and leave the second
line empty.

## Sample

Input:

```text
aba
abacaba
```

Output:

```text
2
1 5
```

The substrings at positions `1`-`3` and `5`-`7` are both `aba`.
