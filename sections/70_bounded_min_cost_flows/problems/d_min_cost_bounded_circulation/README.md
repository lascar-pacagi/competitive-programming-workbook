# D. Minimum-Cost Bounded Circulation

A directed edge `u -> v` must carry an integer flow between `low` and `high`,
inclusive, and costs `cost` per unit. Find a circulation satisfying flow
conservation at every vertex with minimum total cost, or print `IMPOSSIBLE`.

All costs are nonnegative.

Input consists of `n m`, followed by `m` lines
`u v low high cost`.

Constraints: `1 <= n <= 200`, `0 <= m <= 2000`,
`0 <= low <= high <= 200`, and `0 <= cost <= 10^6`.

Sample input:

```text
3 3
1 2 2 2 3
2 3 0 2 1
3 1 0 2 2
```

Sample output:

```text
12
```
