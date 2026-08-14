# Offline companion: 911G -- Mass Change Queries

This is an original, locally judgeable companion for [911G -- Mass Change Queries](https://codeforces.com/problemset/problem/911/G). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


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
