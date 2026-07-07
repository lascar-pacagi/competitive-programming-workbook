# B. Longest Bounded Window

## Statement

For each test case, you are given an array of nonnegative integers and a limit
`k`. Print the maximum length of a contiguous subarray whose sum is at most
`k`.

The empty subarray is allowed, so the answer can be `0`.

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

For each test case, print the maximum valid length.

