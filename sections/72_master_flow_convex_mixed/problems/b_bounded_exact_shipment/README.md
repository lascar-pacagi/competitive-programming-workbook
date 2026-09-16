# B. Bounded Exact Shipment

Send exactly `F` units from `s` to `t`. Every directed edge has a lower bound,
an upper bound, and a nonnegative cost per unit. Find the minimum total cost of
a feasible shipment, or print `IMPOSSIBLE`.

## Input

`n m F`, then `s t`, followed by `m` lines
`u v low high cost`.

`2 <= n <= 200`, `0 <= m <= 2000`, `0 <= F <= 200`,
`0 <= low <= high <= 200`, and `0 <= cost <= 10^6`.

## Sample

```text
4 5 3
1 4
1 2 1 2 1
1 3 0 2 4
2 3 0 1 2
2 4 0 2 3
3 4 1 2 1
```

```text
13
```
