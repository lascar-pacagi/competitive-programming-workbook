# C. Best Study Streak

## Statement

You are given `n` nonnegative daily study times and a budget `k`. Choose a
contiguous streak with total study time at most `k`.

Print the maximum length of such a streak and the earliest 1-indexed starting
position among maximum-length streaks. If no nonempty streak is valid, print
`0 0`.

## Input

```text
T
n k
a1 a2 ... an
...
```

`1 <= T <= 50`, the total `n` over all test cases is at most `200000`,
`0 <= ai`, and `0 <= k`.

## Output

For each test case, print:

```text
best_length earliest_start
```

