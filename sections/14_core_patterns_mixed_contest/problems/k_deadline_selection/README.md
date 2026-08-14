# K. Deadline Selection

There are `n` jobs. Job `i` takes `duration_i` time and must finish no later
than `deadline_i`. Starting at time zero, run at most one job at a time and
choose any subset and order. Print the maximum number of jobs that can meet
their deadlines.

## Input

```text
n
duration1 deadline1
...
durationn deadlinen
```

`1 <= n <= 200000`, `1 <= duration_i, deadline_i <= 10^9`.

## Output

Print the maximum feasible number of jobs.

## Sample

```text
5
3 4
2 5
4 6
1 6
3 9
```

```text
4
```
