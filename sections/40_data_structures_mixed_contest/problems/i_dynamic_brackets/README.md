# I. Dynamic Brackets

Maintain a string of opening and closing parentheses. Process:

- `T i`: change `(` to `)` or `)` to `(` at position `i`.
- `Q l r`: decide whether the substring from `l` through `r` is a balanced
  parenthesis sequence when considered on its own.

A sequence is balanced if every prefix has at least as many opening as closing
parentheses, and the entire sequence has equal numbers of each. No characters
outside the queried substring contribute. Positions are 1-based.

## Input

```text
n q
s
q operations
```

`1 <= n,q <= 200000`, `s` has length `n` and contains only `(` and `)`,
`1 <= i <= n`, and `1 <= l <= r <= n`.

## Output

For each `Q`, print `YES` or `NO` on its own line.

## Sample

```text
6 7
(()())
Q 1 6
Q 2 5
T 1
Q 1 6
Q 2 3
T 1
Q 1 5
```

```text
YES
YES
NO
YES
NO
```

The first two substrings are balanced. Flipping position 1 makes the whole
string begin with a closing parenthesis, but the substring at positions 2–3
remains `()`. An odd-length substring cannot be balanced.
