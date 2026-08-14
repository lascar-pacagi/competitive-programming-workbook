# Offline companion: 600E -- Lomsat gelral

This is an original, locally judgeable companion for [600E -- Lomsat gelral](https://codeforces.com/problemset/problem/600/E). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


Two couriers both start at the top-left cell of an `n` by `m` value grid. Each
courier must reach the bottom-right cell. On every move, a courier goes exactly
one cell right or one cell down.

Each visited cell contributes its value to the total, but a cell contributes at
most once even if both couriers visit it. Find the maximum total value that can
be collected by choosing both routes.

## Input

```text
n m
a[0][0] a[0][1] ... a[0][m-1]
...
a[n-1][0] ... a[n-1][m-1]
```

## Output

Print the maximum total value collected.

## Constraints

```text
1 <= n, m <= 70
-10^9 <= a[r][c] <= 10^9
```

The start and finish cells are visited by both couriers, but each is counted
only once.

## Sample

Input:

```text
3 3
1 2 3
4 5 6
7 8 9
```

Output:

```text
42
```

## Files

Implement one of:

```text
solve.cpp
solve.py
```

The reference implementations are `solution.cpp` and `solution.py`. Read the
section editorial only after making a serious attempt.
