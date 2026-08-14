# Offline companion: ABC137_D -- Summer Vacation

This is an original, locally judgeable companion for [ABC137_D -- Summer Vacation](https://atcoder.jp/contests/abc137/tasks/abc137_d?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


You are given a directed graph with nonnegative road costs. Find the minimum
total cost of a route from vertex `1` to vertex `n` that uses an **even**
number of roads. A route may revisit vertices and roads. If no such route
exists, print `-1`.

Using zero roads is allowed, so when `n = 1` the answer is `0`.

## Input

```text
n m
u1 v1 w1
...
um vm wm
```

`1 <= n <= 200000`, `0 <= m <= 200000`, and `0 <= wi <= 10^9`. Vertices are
numbered from `1` to `n`. Roads are directed; repeated roads may appear.

## Output

Print the smallest possible total cost of an even-hop route from `1` to `n`,
or `-1` if no such route exists.

## Sample

```text
5 6
1 2 3
2 5 100
1 3 10
3 4 1
4 5 1
2 3 1
```

```text
6
```

The route `1 -> 2 -> 3 -> 4 -> 5` has four roads and total cost `6`.
