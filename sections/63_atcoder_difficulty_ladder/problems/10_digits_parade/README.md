# Offline companion: ABC135_D -- Digits Parade

This is an original, locally judgeable companion for [ABC135_D -- Digits Parade](https://atcoder.jp/contests/abc135/tasks/abc135_d?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


You are given a grid containing walls `#`, open cells `.`, a start `S`, a goal
`G`, and lowercase letters `a` through `z`.

From a non-wall cell, you may move to a four-neighbor non-wall cell for cost
`1`. If you stand on a lowercase letter, you may teleport to any other cell
with the same letter for cost `0`. Teleports may be used any number of times.

Find the minimum cost from `S` to `G`, or print `-1` if the goal is
unreachable.

## Input

```text
n m
row1
...
rown
```

`1 <= n,m <= 1000`. Each row has `m` characters. There is exactly one `S` and
one `G`.

## Output

Print the minimum cost, or `-1`.

## Sample

```text
3 5
S#a#G
.a.a.
.....
```

```text
4
```

Walk to the left `a`, teleport to the right `a` for free, then walk to `G`.
