# Hull Membership Queries

`n` sensor positions are given. For each query point, print `IN` if it lies
strictly inside the convex hull of the sensors, `BOUNDARY` if it lies on the
hull's boundary, and `OUT` otherwise. The hull may be a single point or a
segment.

## Input

```text
n q
n lines: x y      (sensors)
q lines: x y      (queries)
```

- `1 <= n, q <= 200000`;
- integer coordinates with absolute value at most `10^9`.

## Output

Print one line per query.

## Sample input

```text
5 3
0 0
4 0
4 3
0 3
2 1
2 2
4 1
5 1
```

## Sample output

```text
IN
BOUNDARY
OUT
```
