# D. Cover All Labels

## Statement

For each test case, you are given a sequence of `n` labels. Every label is an
integer from `1` to `m`.

Find the minimum length of a nonempty contiguous subarray that contains every
label from `1` through `m` at least once. If no such subarray exists, print
`-1`.

## Input

```text
T
n m
a1 a2 ... an
...
```

`1 <= T <= 50`, `1 <= n, m <= 200000`, the total `n` over all test cases is
at most `200000`, and `1 <= ai <= m`.

## Output

For each test case, print the minimum possible subarray length, or `-1`.

## Sample

Input:

```text
3
8 3
1 2 1 3 2 3 1 2
5 4
1 2 1 2 1
4 1
1 1 1 1
```

Output:

```text
3
-1
1
```
