# Bridge Distance Queries

A connected undirected multigraph is given. For every query `(u,v)`, report how many bridges must be crossed by every path from `u` to `v`.

Input: `n m q`, `m` edges, then `q` queries. `n,m,q <= 200000`.

Sample input
```text
4 4 2
1 2
2 3
3 1
3 4
1 4
1 2
```
Sample output
```text
1
0
```
