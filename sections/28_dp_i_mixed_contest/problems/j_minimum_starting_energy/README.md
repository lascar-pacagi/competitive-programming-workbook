# J. Minimum Starting Energy

Choose a path from the top-left cell `(0, 0)` to the bottom-right cell
`(n-1, m-1)`. From a cell, you may move one cell right or one cell down.

Your energy is allowed to be `0`, but it may never become negative.

Before entering `(0, 0)`, choose an integer starting energy `E >= 0`. Every
visited cell, including the starting and destination cells, is then processed
in this order:

1. Enter the cell and add its value to your current energy.
2. If your energy is now negative, the path is invalid immediately.
3. Otherwise, if this is not the destination, move right or down without
   changing your energy.

In particular, you may enter a cell with energy `0`: its value is applied
before the energy is checked. If the result is still nonnegative, the route
remains valid. Once the energy becomes negative, however, the route has
already failed and a later positive cell cannot repair it.

Find the smallest possible starting energy `E` for which at least one valid
path reaches the destination.

For a one-cell grid `[5]`, the answer is `0`: after entering the cell, the
energy becomes `5`, which is valid.

For example, on the one-row grid `[-3, 5]`, starting with `3` is valid: the
energies after the two cells are `0` and `5`. Starting with `2` is invalid
because the energy becomes `-1` immediately after the first cell.

## Input

```text
n m
grid[0][0] ... grid[0][m-1]
...
grid[n-1][0] ... grid[n-1][m-1]
```

`1 <= n,m <= 500`

`-10^9 <= grid[r][c] <= 10^9`

## Output

Print the minimum starting energy, which may be `0`.

## Sample Input

```text
3 3
-2 -3 3
-5 -10 1
10 30 -5
```

## Sample Output

```text
6
```

One optimal path for the sample visits values
`-2, -3, 3, 1, -5`. Starting with `6`, the energy after each cell is
`4, 1, 4, 5, 0`, so the path is valid. Starting with `5` cannot produce any
valid path to the destination.
