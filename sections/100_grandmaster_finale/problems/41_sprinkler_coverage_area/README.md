# Sprinkler Coverage Area

A park is watered by `n` sprinklers. Sprinkler `i` wets the closed disc with
centre `(x[i], y[i])` and radius `r[i]`. Several sprinklers may be identical.

Print the total area of ground that is wet (covered by at least one disc).

## Input

```text
n
n lines: x y r
```

- `1 <= n <= 2000`;
- `|x|, |y| <= 10^4` and `1 <= r <= 10^4`, all integers.

## Output

Print the area. Answers with absolute or relative error at most `10^-7` are
accepted.

## Sample input

```text
3
0 0 2
2 0 2
10 10 1
```

## Sample output

```text
23.3608550879
```
