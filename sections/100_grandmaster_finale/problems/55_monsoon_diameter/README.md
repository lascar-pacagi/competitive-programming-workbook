# Monsoon Diameter

A road network is a tree of `n` villages. During the monsoon every road
slowly floods: on day `t` (days are numbered from `0`), road `i` takes
`a[i] * t + b[i]` minutes to travel.

For each of the first `m` days, the rescue service wants the travel time of
the slowest route: the maximum, over all pairs of villages (a village paired
with itself is allowed), of the travel time along the unique road path between
them on that day.

## Input

```text
n m
n-1 lines: u v a b
```

- `1 <= n <= 100000`, `1 <= m <= 1000000`;
- `0 <= a <= 100000`, `0 <= b <= 10^9`;
- the roads form a tree.

## Output

Print `m` integers on one line: the answers for days `0, 1, ..., m-1`.

## Sample input

```text
5 6
1 2 0 10
1 3 3 1
1 4 1 6
4 5 2 0
```

## Sample output

```text
16 19 22 25 31 37
```
