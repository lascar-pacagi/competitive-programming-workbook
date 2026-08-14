# Offline companion: ABC196_E -- Filters

This is an original, locally judgeable companion for [ABC196_E -- Filters](https://atcoder.jp/contests/abc196/tasks/abc196_e?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


You are choosing a lineup from `n` performers. Performer `i` contributes an
audience score `wi`, which may be negative. Some pairs of performers cannot
appear together.

Choose any subset of performers such that no incompatible pair is chosen.
The empty lineup is allowed. Print the maximum possible total audience score.

## Input

```text
n m
w1 w2 ... wn
u1 v1
u2 v2
...
um vm
```

- `1 <= n <= 20`
- `0 <= m <= n(n - 1) / 2`
- `-10^9 <= wi <= 10^9`
- `1 <= ui, vi <= n`, `ui != vi`
- Every incompatible pair appears at most once. Pairs are undirected.

## Output

Print the greatest total score of a compatible lineup.

## Sample

```text
4 2
8 6 -3 7
1 2
2 4
```

```text
15
```

One optimal lineup is performers `1` and `4`. Their total is `8 + 7 = 15`.
