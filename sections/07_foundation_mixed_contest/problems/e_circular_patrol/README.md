# E. Circular Patrol

A robot patrols positions `1` through `n` arranged in a circle. It starts
at position `p`. Each command is `L` (one step counterclockwise) or `R`
(one step clockwise), with wraparound.

For every test case, print the robot's final position and the number of
distinct positions it visited. The starting position counts as visited.

## Input

```text
T
n p commands
...
```

The total of `n + len(commands)` is at most `200000`.

## Output

Print `final_position distinct_visited` for each test case.

## Sample

```text
3
5 1 RRLLR
1 1 LRR
6 4 RRRR
```

```text
2 3
1 1
2 5
```
