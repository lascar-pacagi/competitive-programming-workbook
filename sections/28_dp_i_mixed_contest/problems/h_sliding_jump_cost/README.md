# H. Sliding Jump Cost

There are `n` checkpoints in a line. You start on checkpoint `0` and must reach
checkpoint `n-1`. From checkpoint `i`, you may jump to any checkpoint from
`i+1` through `i+k`.

Visiting checkpoint `i` costs `cost[i]`. The start and destination costs are
both included. Find the minimum total cost of a valid route.

## Input

```text
n k
cost[0] cost[1] ... cost[n-1]
```

`1 <= n,k <= 200000`

`-10^9 <= cost[i] <= 10^9`

## Output

Print the minimum total cost.

## Sample Input

```text
5 2
5 1 4 2 3
```

## Sample Output

```text
11
```
