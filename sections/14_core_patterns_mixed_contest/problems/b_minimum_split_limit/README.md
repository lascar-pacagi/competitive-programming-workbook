# B. Minimum Split Limit

## Statement

For each test case, you are given `n` positive integers and an integer `d`.
Split the array into at most `d` nonempty contiguous groups. The cost of a group
is the sum of its elements.

Find the smallest possible value of the maximum group cost.

## Input

```text
T
n d
a1 a2 ... an
...
```

The constraints are:

```text
1 <= d <= n
1 <= a_i <= 10^9
sum of n over all test cases <= 200000
```

## Output

For each test case, print the minimum possible maximum group cost.
