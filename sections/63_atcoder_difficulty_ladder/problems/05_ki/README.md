# Offline companion: ABC138_D -- Ki

This is an original, locally judgeable companion for [ABC138_D -- Ki](https://atcoder.jp/contests/abc138/tasks/abc138_d?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


Given an undirected unweighted graph and several station vertices, print for
every vertex its distance to the nearest station, or `-1` if none is reachable.

## Input
```text
n m k
u1 v1
...
um vm
s1 s2 ... sk
```
`1 <= n <= 200000`, `0 <= m <= 200000`, and `1 <= k <= n`; vertices are
1-indexed.

## Output
Print n distances in vertex order.

## Sample
```text
5 4 2
1 2
2 3
3 4
4 5
1 5
```
```text
0 1 2 1 0
```
