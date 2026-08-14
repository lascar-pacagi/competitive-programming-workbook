# I. Wildcard Parentheses

Each string contains `(`, `)`, and `?`. Replace every `?` independently by
`(` or `)`. Print `YES` if the result can be a valid parenthesis sequence,
otherwise print `NO`.

## Input

```text
T
s1
...
sT
```

Every string is nonempty, and the total length is at most `200000`.

## Output

Print one answer per string.

## Sample

```text
5
(?)
??
(?))
?)(
((?
```

```text
NO
YES
YES
NO
NO
```
