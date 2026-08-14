# D. Ribbon Cuts

Offline companion: [Codeforces 189A -- Cut Ribbon](https://codeforces.com/problemset/problem/189/A)

You have one ribbon of integer length `n`. You may repeatedly cut off a piece
whose length is one of `a`, `b`, or `c`. Every cut must leave an integer
nonnegative remaining length, and the ribbon must be used completely.

Print the largest possible number of pieces, or `-1` if no complete cutting is
possible.

## Input

```text
n a b c
```

## Constraints

```text
1 <= n <= 200000
1 <= a, b, c <= 200000
```

## Output

Print the largest possible number of pieces, or `-1`.

## Sample

```text
7 5 2 5
```

```text
2
```

One complete cutting is `5 + 2`.
