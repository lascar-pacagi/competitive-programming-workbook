# D. Factory Deadline

There are `n` machines. Machine `i` finishes one item every `time[i]` minutes
and may work in parallel with every other machine. Find the minimum whole
number of minutes needed to finish at least `goal` items.

## Input

```text
T
n goal
time1 time2 ... timen
...
```

`1 <= T <= 30`, `1 <= n <= 200000`, `1 <= goal <= 10^9`,
`1 <= time[i] <= 10^9`, and the total `n` is at most `200000`.

## Output

Print the minimum completion time for each test case.

## Sample

```text
3
2 7
2 3
1 5
10
3 1
8 9 10
```

```text
9
50
8
```
