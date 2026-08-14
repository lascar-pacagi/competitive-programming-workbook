# Offline companion: ABC187_E -- Through Path

This is an original, locally judgeable companion for [ABC187_E -- Through Path](https://atcoder.jp/contests/abc187/tasks/abc187_e?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


An undirected road has a difficulty value. The difficulty of a route is the
largest value of any road on that route.

Find the minimum possible route difficulty from city `1` to city `n`. Print
`-1` if city `n` is unreachable from city `1`.

## Input

```text
n m
u1 v1 w1
...
um vm wm
```

`1 <= n <= 200000`, `0 <= m <= 200000`, and `0 <= wi <= 10^9`. Roads are
undirected. Repeated roads may appear.

## Output

Print the minimum possible route difficulty, or `-1`.

## Sample

```text
5 6
1 2 4
2 5 8
1 3 3
3 4 5
4 5 5
2 3 2
```

```text
5
```

The route `1 -> 3 -> 4 -> 5` has maximum road difficulty `5`.
