# Obstacle Shortcut

A courier walks from point `S` to point `T` across a square that contains `k`
buildings. Every building is a convex polygon, the buildings are pairwise
disjoint (they share no points), and `S` and `T` lie strictly outside all of
them. The courier may walk along building walls and touch corners, but may not
enter the interior of any building.

Print the length of the shortest route from `S` to `T`.

## Input

```text
sx sy tx ty
k
then, for each building:
  m
  m lines: x y      (corners in order, clockwise or counterclockwise)
```

- `0 <= k <= 100`, every `m >= 3`, and the total number of corners is at most
  `400`;
- all coordinates are integers with absolute value at most `10^6`;
- each building is strictly convex (no three corners collinear).

## Output

Print the length. Answers with absolute or relative error at most `10^-7` are
accepted.

## Sample input

```text
0 0 10 0
1
4
4 -3
6 -3
6 1
4 1
```

## Sample output

```text
10.2462112512
```

The courier walks to `(4, 1)`, along the wall to `(6, 1)`, then to `T`.
