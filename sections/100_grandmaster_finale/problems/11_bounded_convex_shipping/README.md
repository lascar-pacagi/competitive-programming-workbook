# Bounded Convex Shipping

For every directed edge `e`, choose an integer flow `x[e]` satisfying
`lower[e] <= x[e] <= upper[e]`. At every vertex, total incoming flow must equal
total outgoing flow.

Sending `x` units through an edge costs

```text
c*x + d*x*(x-1)/2.
```

All marginal costs are nonnegative because `c,d >= 0`. Find the minimum total
cost of a feasible circulation, or report `IMPOSSIBLE`.

## Input

```text
n m
m lines: u v lower upper c d
```

- `1 <= n <= 100`, `1 <= m <= 500`;
- `0 <= lower <= upper <= 10^9`;
- `0 <= c,d <= 10^9`;
- `sum(upper-lower) <= 6000`;
- every edge cost at its upper bound and every feasible total objective fit in
  a signed 64-bit integer.

Parallel edges are allowed.

## Output

Print the minimum cost, or `IMPOSSIBLE`.

## Sample input

```text
3 3
1 2 1 3 2 1
2 3 1 3 1 2
3 1 0 3 3 0
```

## Sample output

```text
6
```
