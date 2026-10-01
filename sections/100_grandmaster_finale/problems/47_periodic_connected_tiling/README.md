# Periodic Domino Tower

A tower floor plan is `W` columns wide. A block of `P` rows, each a string of
`W` characters (`.` free, `#` blocked), is repeated exactly `H` times from top
to bottom, giving a board of `P*H` rows. Count the ways to cover every free
cell with non-overlapping dominoes (`1 x 2` or `2 x 1`) that use only free
cells, modulo `1000000007`. The empty board (`H = 0`) has one tiling.

## Input

```text
H P W
P lines: the block rows
```

- `0 <= H <= 10^18`;
- `1 <= P, W <= 5`.

## Output

Print the number of tilings modulo `1000000007`.

## Sample input

```text
2 1 2
..
```

## Sample output

```text
2
```
