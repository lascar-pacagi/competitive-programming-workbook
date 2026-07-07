# C. Minimum Capacity

## Statement

You are given package weights in order and an integer `d`. Each day, you can
ship a contiguous sequence of remaining packages whose total weight is at most
the ship capacity. Packages must be shipped in the given order.

Print the minimum capacity that allows all packages to be shipped within at
most `d` days.

## Input

```text
T
n d
w1 w2 ... wn
...
```

`1 <= T <= 30`, the total `n` over all test cases is at most `200000`,
`1 <= d`, and weights are positive integers.

## Output

For each test case, print the minimum feasible capacity.

