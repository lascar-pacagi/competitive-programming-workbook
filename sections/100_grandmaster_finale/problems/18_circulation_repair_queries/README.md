# Circulation Repair Queries

A directed network currently carries a feasible integer circulation. Edge `e`
has lower bound `lower[e]`, upper bound `upper[e]`, and current flow `flow[e]`.

Each query independently proposes adding a new directed edge `u -> v` whose
lower and upper bounds are both `1`. You may change the old edge flows, while
respecting their bounds. Print whether the enlarged network has a feasible
circulation. The original circulation is restored before the next query.

## Input

```text
n m q
m lines: u v lower upper flow
q lines: u v
```

- `1 <= n <= 700`, `0 <= m <= 5000`, `1 <= q <= 200000`;
- `0 <= lower <= flow <= upper <= 10^9`;
- the supplied old flow conserves flow at every vertex.

## Output

For each query print `YES` or `NO`.

## Sample input

```text
3 2 2
1 2 0 1 0
2 3 0 1 0
3 1
1 3
```

## Sample output

```text
YES
NO
```
