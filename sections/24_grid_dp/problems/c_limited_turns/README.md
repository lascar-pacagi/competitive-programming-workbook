# C. Limited Turns

You are given an `n x m` grid of open `.` and blocked `#` cells. Starting from
the top-left cell, reach the bottom-right cell. You may only move right or down.
You may not enter blocked cells.

A turn happens when two consecutive moves use different directions. Count the
number of valid paths that use at most `K` turns, modulo `1_000_000_007`.

The first move does not count as a turn.

## Input

```text
n m K
row1
...
rown
```

`1 <= n,m <= 80`, `0 <= K <= 40`.

## Output

Print the number of valid paths with at most `K` turns.

## Sample

Input:

```text
3 3 1
...
...
...
```

Output:

```text
2
```

