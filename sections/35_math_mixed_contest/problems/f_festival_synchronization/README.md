# F. Festival Synchronization

For each query, find the smallest nonnegative integer `x` satisfying both:

```text
x == r1 (mod m1)
x == r2 (mod m2)
```

The moduli are not necessarily coprime. Print `-1` if no such integer exists.

## Input

```text
q
r1 m1 r2 m2
...
```

`1 <= q <= 200000`, `1 <= m1,m2 <= 10^9`, and
`0 <= r1 < m1`, `0 <= r2 < m2`.

## Output

Print one answer per query.

## Sample

```text
3
3 4 5 6
0 2 1 4
4 5 4 7
```

```text
11
-1
4
```
