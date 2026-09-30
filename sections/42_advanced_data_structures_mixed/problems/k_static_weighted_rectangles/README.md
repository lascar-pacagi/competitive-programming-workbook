# K. Static Weighted Rectangles

You are given `n` fixed weighted points and `q` rectangular queries. For each
rectangle, print the sum of the weights of all points inside it, including
points on its boundary. Points at the same coordinates contribute separately.
Weights may be negative. There are no updates, and all queries are available
before processing begins.

## Input

The first line contains `n q`. The next `n` lines each contain `x y w`,
the coordinates and weight of one point. Each of the next `q` lines contains
`a b c d`, describing the inclusive rectangle `a <= x <= c`, `b <= y <= d`.


## Constraints

`1 <= n,q <= 200000`, all coordinates have absolute value at most `10^9`,
`a <= c`, `b <= d`, and `|w| <= 10^9`. Use signed 64-bit sums.

## Output

Print one answer per query on its own line, in query order. Updates produce
no output.

## Sample

### Input

```text
4 3
1 1 5
2 3 4
1 1 -2
5 5 7
1 1 2 3
1 2 2 3
0 0 1 1
```

### Output

```text
7
4
3
```

### Explanation

The two points at `(1,1)` contribute `5-2=3`. The first rectangle
also contains the point of weight `4` at `(2,3)`.
