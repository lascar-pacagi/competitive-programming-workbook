# Offline companion: Almost Union-Find

This is an original, locally judgeable companion for [Almost Union-Find](https://open.kattis.com/problems/almostunionfind). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


An undirected network has cables with nonnegative maintenance costs. You may
deactivate cables and save their maintenance costs, but every pair of computers
that was connected before deactivation must still be connected afterwards.

Find the maximum total maintenance cost that can be saved.

## Input

```text
n m
u1 v1 w1
u2 v2 w2
...
um vm wm
```

`1 <= n <= 200000`, `0 <= m <= 200000`, and `0 <= wi <= 10^9`. Computers are
numbered from `1` to `n`. Repeated cables may appear; no cable joins a computer
to itself.

## Output

Print one integer: the maximum total saved cost.

## Sample

```text
5 5
1 2 4
2 3 1
1 3 3
4 5 7
1 2 9
```

```text
13
```

One optimal choice keeps cables of costs `1`, `3`, and `7`, so it deactivates
the cables of costs `4` and `9`.
