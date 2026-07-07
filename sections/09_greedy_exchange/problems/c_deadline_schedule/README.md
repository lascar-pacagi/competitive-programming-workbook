# C. Deadline Schedule

## Statement

For each test case, there are `n` optional tasks. Task `i` takes `p_i` units
of time and has deadline `d_i`. You may choose any subset of tasks and perform
chosen tasks one after another, starting at time `0`. A chosen task is on time
if its completion time is at most its deadline.

Find the maximum number of tasks that can all be completed on time.

## Input

```text
T
n
p1 d1
p2 d2
...
pn dn
...
```

The sum of `n` over all test cases is at most `200000`.

## Output

For each test case, print the maximum number of tasks.

