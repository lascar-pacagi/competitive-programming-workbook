# B. Time-Boxed Schedule

You have independent tasks. Task `i` takes `duration_i` minutes and must finish
no later than `deadline_i`. Starting at minute 0, you can perform at most one
task at a time. Find the maximum number of tasks that can be completed by their
deadlines.

## Input

The first line contains `n`. Each of the next `n` lines contains
`duration deadline`.

## Output

Print the maximum number of tasks that can be completed on time.

## Constraints

`1 <= n <= 200000`, durations and deadlines are positive integers up to
`10^9`.

## Sample

Input:

```text
5
4 4
3 5
2 6
1 7
5 8
```

Output:

```text
3
```
