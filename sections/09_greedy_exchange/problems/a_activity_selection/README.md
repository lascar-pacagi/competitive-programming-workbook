# A. Activity Selection

## Statement

For each test case, you are given `n` activities. Activity `i` occupies the
half-open interval `[s_i, e_i)`, where `s_i < e_i`.

Choose as many activities as possible so that no two chosen activities overlap.
Two activities are compatible when the first ends at or before the second
starts.

## Input

```text
T
n
s1 e1
s2 e2
...
sn en
...
```

The sum of `n` over all test cases is at most `200000`.

## Output

For each test case, print the maximum number of activities that can be chosen.

