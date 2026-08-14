# Offline companion: Catering

This is an original, locally judgeable companion for [Catering](https://open.kattis.com/problems/catering). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


You are given an undirected weighted graph. Travel from vertex `1` to vertex
`n`. You may choose at most one traversed edge and pay zero for it instead of
its weight. Print the minimum possible travel cost.

## Input

```text
n m
u1 v1 w1
...
um vm wm
```

## Constraints

```text
2 <= n <= 200000
n-1 <= m <= 200000
1 <= ui, vi <= n
1 <= wi <= 1000000000
```

The graph is connected.

## Output

Print the minimum cost from `1` to `n` using the coupon at most once.

## Sample

```text
4 4
1 2 5
2 4 5
1 3 2
3 4 8
```

```text
2
```

Use the coupon on edge `3-4`; route `1-3-4` then costs `2`.
