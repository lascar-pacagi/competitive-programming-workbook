# C. Merge Intervals

## Statement

For each test case, you are given closed intervals `[l, r]`. Merge all
overlapping or touching intervals. Two intervals touch if the second starts at
most one position after the first ends.

For example, `[1, 3]` and `[4, 5]` merge into `[1, 5]`.

Print the merged intervals in increasing order.

## Input

```text
T
n
l1 r1
...
ln rn
...
```

`1 <= T <= 30`, the total `n` over all test cases is at most `200000`, and
endpoints fit in signed 32-bit integers. Each input interval satisfies `l <= r`.

## Output

For each test case, first print the number of merged intervals. Then print each
merged interval on its own line as `l r`.

