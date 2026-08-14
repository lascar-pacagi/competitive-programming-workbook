# E. One Diagonal Path

Move from the top-left to the bottom-right of a value grid. A normal move
goes right or down. Exactly once, you must move diagonally down-right.
Maximize the sum of all visited cells. Print `-1` when using a diagonal
move is impossible.

## Input
```text
n m
grid values
```
`1 <= n,m <= 500`, `|value| <= 10^9`.

## Output
Print the maximum sum.

## Sample
```text
3 3
1 2 3
4 5 6
7 8 9
```
```text
23
```
