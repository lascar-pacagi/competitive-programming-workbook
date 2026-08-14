# P. Common Deadline

You have `n` independent tasks. Task `i` takes `duration_i` units of time, and
every chosen task must be completed before the same time limit `T`. Tasks run
one at a time and cannot be interrupted. Choose as many tasks as possible.

## Input

```text
n T
duration1 duration2 ... durationn
```

`1 <= n <= 200000`, `1 <= T <= 10^18`, and
`1 <= duration_i <= 10^9`.

## Output

Print the maximum possible number of completed tasks.

## Sample

```text
5 10
6 2 4 3 8
```

```text
3
```
