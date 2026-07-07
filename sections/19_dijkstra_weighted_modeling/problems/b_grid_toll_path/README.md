# B. Grid Toll Path

Each grid cell has an entry toll. Starting at the top-left cell, move in four
directions to the bottom-right cell. The total cost includes the toll of every
cell visited, including the start and finish. Print the minimum possible cost.

## Input

```text
n m
grid rows
```

`1 <= n,m <= 1000`, `0 <= toll <= 10^9`.

## Output

Print the minimum cost.

## Sample

Input:

```text
3 4
1 9 1 1
1 9 1 9
1 1 1 1
```

Output:

```text
6
```
