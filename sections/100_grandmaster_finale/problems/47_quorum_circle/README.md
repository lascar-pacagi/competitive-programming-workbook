# Quorum Circle

`n` committee members stand at integer points of a field (several may stand at
the same point). The chair wants to draw a circle on the ground so that at
least `k` members stand inside it or on its boundary. Print the smallest
possible radius.

## Input

```text
n k
n lines: x y
```

- `1 <= k <= n <= 600`;
- `|x|, |y| <= 10^4`.

## Output

Print the radius. Answers with absolute or relative error at most `10^-7` are
accepted.

## Sample input

```text
5 3
0 0
4 0
0 3
10 10
10 10
```

## Sample output

```text
2.5000000000
```

The circle with diameter from `(4, 0)` to `(0, 3)` also passes through
`(0, 0)`.
