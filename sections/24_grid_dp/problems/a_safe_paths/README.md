# A. Safe Paths

You are given an `n x m` grid. A cell is either open `.` or blocked `#`.
Starting from the top-left cell, you want to reach the bottom-right cell. You
may only move right or down, and you may not enter blocked cells.

Count the number of valid paths modulo `1_000_000_007`.

## Input

```text
n m
row1
...
rown
```

`1 <= n,m <= 1000`.

## Output

Print the number of valid paths.

## Sample

Input:

```text
3 4
....
.#..
....
```

Output:

```text
4
```
