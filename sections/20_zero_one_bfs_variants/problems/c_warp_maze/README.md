# C. Warp Maze

You are given a grid with open cells `.`, walls `#`, a start `S`, and a goal
`G`.

From an open cell, you may:

- walk to a four-neighbor open cell for cost `0`;
- warp to any open cell within Chebyshev distance at most `2` for cost `1`.

For cells `(r1, c1)` and `(r2, c2)`, their Chebyshev distance is
`max(|r1 - r2|, |c1 - c2|)`. Thus, a warp may move at most two rows and at
most two columns, including diagonally: its possible destinations lie in the
`5 x 5` square centered on the current cell.

Print the minimum cost from `S` to `G`, or `-1` if unreachable.

## Input

```text
n m
row1
...
rown
```

`1 <= n,m <= 1000`.

## Output

Print the minimum warp cost.

## Sample

Input:

```text
4 4
S.#.
..#.
.#..
.#.G
```

Output:

```text
1
```
