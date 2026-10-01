# Periodic Loop Frontier

A security robot patrols a warehouse floor made of `W` columns and `N` rows of
square cells. A **patrol** is a closed route that moves between cells sharing
a side, visits every cell exactly once, and returns to its starting cell.

Two patrols are the same when they use the same set of cell-to-cell moves (the
starting cell and the direction of travel do not matter).

Count the patrols of the `W x N` floor modulo `998244353`.

## Input

One line with `W N`.

- `1 <= W <= 10`;
- `1 <= N <= 10^18`.

## Output

Print the number of patrols modulo `998244353`.

## Sample input

```text
4 6
```

## Sample output

```text
37
```
