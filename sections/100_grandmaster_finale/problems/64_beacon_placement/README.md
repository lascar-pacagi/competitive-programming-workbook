# Beacon Placement

`n` beacons must be installed along a straight coast. Beacon `i` can be
installed at exactly one of two surveyed sites, coordinate `a[i]` or
coordinate `b[i]` (the two sites may coincide, and sites of different beacons
may coincide as well).

Install every beacon so that the smallest distance between two installed
beacons is as large as possible, and print that largest possible smallest
distance.

## Input

```text
n
n lines: a b
```

- `2 <= n <= 30000`;
- `0 <= a[i], b[i] <= 10^9`.

## Output

Print one integer.

## Sample input

```text
4
1 9
3 10
5 6
2 12
```

## Sample output

```text
3
```

Installing the beacons at `9, 3, 6, 12` achieves distance `3`.
