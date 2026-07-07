# B. Lowest Toll

You are given an `n x m` grid of nonnegative tolls. Starting from the top-left
cell, you want to reach the bottom-right cell. You may only move right or down.
The total cost is the sum of tolls of all visited cells, including the start
and finish.

Find the minimum possible cost.

## Input

```text
n m
a11 a12 ... a1m
...
an1 an2 ... anm
```

`1 <= n,m <= 1000`, `0 <= aij <= 10^9`.

## Output

Print the minimum cost.

## Sample

Input:

```text
3 3
5 9 1
4 2 7
6 1 3
```

Output:

```text
15
```

