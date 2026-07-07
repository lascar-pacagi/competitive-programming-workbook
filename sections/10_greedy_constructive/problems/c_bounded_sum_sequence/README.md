# C. Bounded Sum Sequence

## Statement

For each test case, you are given integers `n`, `m`, and `s`.

Construct the lexicographically smallest sequence of length `n` such that:

- every element is between `1` and `m`;
- the sum of all elements is exactly `s`.

If no such sequence exists, print `IMPOSSIBLE`.

## Input

```text
T
n m s
...
```

`1 <= n <= 200000`, `1 <= m <= 10^9`, and `0 <= s <= 10^18`. The sum of `n`
over all test cases is at most `200000`.

## Output

For each test case, print either `IMPOSSIBLE` or the required sequence on one
line.

