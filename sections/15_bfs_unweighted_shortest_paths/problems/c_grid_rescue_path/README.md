# C. Grid Rescue Path

You are given a grid with walls, one start cell `S`, and one goal cell `G`.
You may move one cell at a time in the four directions.

Find the shortest path from `S` to `G`. If several shortest paths exist, output
the lexicographically smallest move string using the character order:

```text
D < L < R < U
```

This tie-breaking rule makes the expected output unique.

## Input

```text
n m
row1
row2
...
rown
```

`1 <= n, m <= 1000`  
Each row contains only `.`, `#`, `S`, and `G`. There is exactly one `S` and
exactly one `G`.

## Output

If `G` is unreachable, print:

```text
NO
```

Otherwise print:

```text
YES
length
path
```

where `path` is the required move string. If `S` and `G` are the same cell
there would be an empty path, but that case is not used in this problem because
the grid contains one `S` and one separate `G`.

## Sample

Input:

```text
5 7
#######
#S...G#
#.###.#
#.....#
#######
```

Output:

```text
YES
4
RRRR
```

