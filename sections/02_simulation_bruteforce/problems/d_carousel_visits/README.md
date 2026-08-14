# D. Carousel Visits

## Statement

A carousel has positions numbered `1` through `n` in clockwise order. It starts
at position `p`. A command string contains only:

- `R`: move one position clockwise;
- `L`: move one position counterclockwise.

The carousel wraps around: moving right from `n` reaches `1`, and moving left
from `1` reaches `n`.

For each test case, print the final position and the smallest position number
visited the maximum number of times. The starting position counts as a visit.

## Input

```text
T
n p s
...
```

`1 <= T <= 50`, `1 <= n <= 200000`, `1 <= p <= n`, and `s` is nonempty. The
total of all `n + len(s)` is at most `200000`.

## Output

For each test case, print:

```text
final_position most_visited_position
```

## Sample

```text
3
5 1 RRLLR
1 1 LRR
4 3 LLL
```

```text
2 2
1 1
4 1
```
