# Offline companion: ABC354_G -- Select Strings

This is an original, locally judgeable companion for [ABC354_G -- Select Strings](https://atcoder.jp/contests/abc354/tasks/abc354_g?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


Process operations on a set of lines. `1 m b` adds `y=m*x+b`; `2 x` prints the
minimum value at `x` and the smallest insertion index of a line attaining it.

The first operation is always an insertion, there is at least one query, and
every query has a prior line.

## Input

```text
q
operation 1
...
```

`1 <= q <= 200,000`, `|m|,|b|,|x| <= 10^9`.

## Output

For each query, print `value index`.

## Sample

```text
5
1 2 3
1 -1 10
2 1
1 2 3
2 5
```

```text
5 1
5 2
```
