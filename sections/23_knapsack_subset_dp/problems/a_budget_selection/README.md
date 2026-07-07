# A. Budget Selection

You have `n` optional training resources. Resource `i` costs `cost[i]` and
gives `value[i]` skill points. You may choose each resource at most once.

Your budget is `W`. Find the maximum total value you can get without exceeding
the budget.

## Input

```text
n W
cost1 value1
...
costn valuen
```

`1 <= n <= 200`, `0 <= W <= 10000`, `1 <= cost[i] <= W + 1`,
`0 <= value[i] <= 10^9`.

## Output

Print the maximum total value.

## Sample

Input:

```text
4 7
3 4
4 5
2 3
5 8
```

Output:

```text
11
```

