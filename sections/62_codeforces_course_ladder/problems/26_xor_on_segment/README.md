# Offline companion: 242E -- XOR on Segment

This is an original, locally judgeable companion for [242E -- XOR on Segment](https://codeforces.com/problemset/problem/242/E). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


An undirected tree has a positive activation cost at every junction. Activate a
set of junctions so that every road has at least one activated endpoint. Find
the minimum total activation cost.

## Input

```text
n
c1 c2 ... cn
u1 v1
...
u(n-1) v(n-1)
```

`1 <= n <= 200000` and `1 <= ci <= 10^9`. Vertices are numbered from `1` to
`n`, and the roads form a tree.

## Output

Print the minimum total activation cost.

## Sample

```text
5
5 2 4 1 3
1 2
1 3
3 4
3 5
```

```text
6
```

Activating junctions `2` and `3` covers every road and costs `2 + 4 = 6`.
