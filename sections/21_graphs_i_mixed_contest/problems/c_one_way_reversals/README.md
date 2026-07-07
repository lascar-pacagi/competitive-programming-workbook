# C. One-Way Reversals

There are `n` cities and `m` one-way roads. You may travel along a road in its
given direction for cost `0`, or travel against it by paying cost `1` to reverse
that road for your trip.

Find the minimum cost to travel from city `1` to city `n`, or print `-1` if it
is impossible.

## Input

```text
n m
u1 v1
...
um vm
```

`1 <= n <= 2 * 10^5`, `0 <= m <= 2 * 10^5`.

## Output

Print the minimum number of reversals, or `-1`.

## Sample

Input:

```text
5 5
1 2
3 2
3 4
5 4
2 5
```

Output:

```text
0
```

