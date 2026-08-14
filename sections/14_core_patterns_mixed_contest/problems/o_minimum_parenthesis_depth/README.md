# O. Minimum Parenthesis Depth

Replace every `?` in a string by either `(` or `)`. Among all replacements
that form a valid parenthesis sequence, minimize its maximum nesting depth.
Print that minimum, or `-1` if no valid replacement exists.

The depth after a prefix is its number of opening parentheses minus its number
of closing parentheses. The maximum nesting depth is the largest such value.

## Input

One string `s`.

`1 <= |s| <= 200000`, and every character is `(`, `)`, or `?`.

## Output

Print the minimum possible maximum nesting depth, or `-1`.

## Sample

```text
((??))
```

```text
2
```
