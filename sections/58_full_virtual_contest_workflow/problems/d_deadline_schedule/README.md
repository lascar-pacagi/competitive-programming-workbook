# D. Deadline Schedule

You have `n` tasks. Task `i` takes `duration[i]` time units and must be
finished no later than `deadline[i]`. You can work on only one task at a time,
without interruption.

Find the maximum number of tasks that can be completed on time.

## Input

```text
n
duration1 deadline1
duration2 deadline2
...
durationn deadlinen
```

## Constraints

```text
1 <= n <= 200,000
1 <= duration[i], deadline[i] <= 1,000,000,000,000
```

## Output

Print the maximum number of tasks that can be completed on time.

## Sample

Input:

```text
4
3 4
2 3
1 3
2 5
```

Output:

```text
3
```
