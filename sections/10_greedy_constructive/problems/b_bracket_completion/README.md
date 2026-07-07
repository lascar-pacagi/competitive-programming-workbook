# B. Bracket Completion

## Statement

For each test case, you are given a string `s` of length `n` consisting of
characters `'('`, `')'`, and `'?'`.

Replace every `'?'` with either `'('` or `')'` so that the final string is a
regular bracket sequence and no strict prefix is itself a regular bracket
sequence. In other words, the balance must stay positive until the final
character, where it becomes zero.

Among all possible valid completions, output the lexicographically smallest
one. If no valid completion exists, output `IMPOSSIBLE`.

In lexicographic order, `'('` is smaller than `')'`.

## Input

```text
T
s1
s2
...
sT
```

The sum of string lengths is at most `200000`.

## Output

For each test case, print the required string or `IMPOSSIBLE`.
