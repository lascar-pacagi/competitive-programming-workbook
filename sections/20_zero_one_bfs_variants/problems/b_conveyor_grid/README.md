# B. Conveyor Grid

Each grid cell contains one preferred direction: `U`, `D`, `L`, or `R`.
Moving from a cell in its preferred direction costs `0`; moving in any other
valid direction costs `1`.

Find the minimum cost to move from the top-left cell to the bottom-right cell.

## Input

```text
n m
row1
...
rown
```

`1 <= n,m <= 1000`.

## Output

Print the minimum cost.

## Sample

Input:

```text
3 3
RRD
ULL
UUR
```

Output:

```text
1
```
