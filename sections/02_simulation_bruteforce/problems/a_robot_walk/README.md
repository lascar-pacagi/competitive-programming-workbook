# A. Robot Walk

## Statement

A robot starts at coordinate `(0, 0)` on an infinite grid. It receives a string
of commands:

- `U`: move one unit up;
- `D`: move one unit down;
- `L`: move one unit left;
- `R`: move one unit right.

For each test case, print the final coordinates and the maximum Manhattan
distance from the origin reached at any time, including the starting position.

The Manhattan distance of `(x, y)` is `|x| + |y|`.

## Input

```text
T
s
...
```

`1 <= T <= 100`, and the total length of all command strings is at most
`200000`.

## Output

For each test case, print:

```text
final_x final_y max_distance
```

