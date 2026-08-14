# D. Balanced Split

Split all given positive integers into two groups. Let the two group sums be
`A` and `B`. Find the minimum possible value of `|A - B|`.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 200`, `1 <= ai <= 1000`, and `sum(ai) <= 100000`.

## Output

Print the minimum possible difference.

## Sample

```text
4
1 6 11 5
```

```text
1
```

One split is `{11}` and `{1, 5, 6}`, with sums `11` and `12`.
