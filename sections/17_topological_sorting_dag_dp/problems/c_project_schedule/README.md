# C. Project Schedule

There are `n` jobs. Job `i` takes `duration[i]` days. Some jobs must finish
before other jobs can start.

For every job, compute the earliest day on which it can finish. If the
dependency graph has a cycle, print `IMPOSSIBLE`.

All jobs with no unfinished prerequisites may start on day `0`.

## Input

```text
n m
d1 d2 ... dn
a1 b1
a2 b2
...
am bm
```

A dependency `a b` means job `a` must finish before job `b` can start.

`1 <= n <= 2 * 10^5`  
`0 <= m <= 2 * 10^5`  
`1 <= duration[i] <= 10^9`

## Output

Print `IMPOSSIBLE` if there is a dependency cycle.

Otherwise print `n` integers. The `i`-th integer is the earliest finish day of
job `i`.

## Sample

Input:

```text
5 5
3 2 4 6 1
1 3
2 3
3 4
2 5
5 4
```

Output:

```text
3 2 7 13 3
```

