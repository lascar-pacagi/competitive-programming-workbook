# C. Best Subset

## Statement

You are given `n` item values and a limit `s`. Choose any subset whose total
value is at most `s`. Print the largest possible total.

The empty subset is allowed, so the answer is always at least `0`.

## Input

```text
T
n s
v1 v2 ... vn
...
```

`1 <= T <= 30`, `0 <= n <= 20`, `0 <= s <= 10^9`, and
`0 <= vi <= 10^9`.

## Output

For each test case, print the best achievable total not exceeding `s`.

