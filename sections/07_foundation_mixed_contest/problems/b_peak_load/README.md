# B. Peak Load

## Statement

A server records `n` jobs. Job `i` runs during every integer time from `li`
through `ri`, inclusive, and contributes `wi` load units.

At time `t`, the total load is the **sum** of `wi` over every job whose
interval contains `t`. Overlapping jobs therefore add their loads. For example,
jobs `[2, 4]` with load `5` and `[3, 5]` with load `7` give total load `12` at
times `3` and `4`.

For each test case, print the maximum total load and the earliest time when
that maximum occurs.

## Input

```text
T
n m
l1 r1 w1
...
ln rn wn
...
```

All times satisfy `1 <= li <= ri <= m`. The total `n + m` over all test cases
is at most `200000`. Loads may be negative or positive.

## Output

For each test case, print:

```text
maximum_load earliest_time
```
