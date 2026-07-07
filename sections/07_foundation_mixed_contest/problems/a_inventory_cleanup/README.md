# A. Inventory Cleanup

## Statement

You are given an array of item colors and an integer `k`. You may delete any
items. Print the minimum number of deletions needed so that at most `k`
distinct colors remain.

## Input

```text
T
n k
c1 c2 ... cn
...
```

`1 <= T <= 50`, the total `n` over all test cases is at most `200000`,
`0 <= k <= n`, and color values fit in signed 32-bit integers.

## Output

For each test case, print the minimum number of deletions.

