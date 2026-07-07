# A. Training Schedule

You are planning `n` training days. On each day, some activities are available:

```text
0 = no activity
1 = C++ practice only
2 = Python practice only
3 = both activities are available
```

You may do at most one activity per day, or rest. You cannot do the same
activity on two consecutive days.

Find the minimum number of rest days.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 2 * 10^5`, `0 <= ai <= 3`.

## Output

Print the minimum number of rest days.

## Sample

Input:

```text
4
3 1 2 0
```

Output:

```text
1
```
