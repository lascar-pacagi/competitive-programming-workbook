# Mandatory Station Queries

For each query `(u,v,c)` in a connected undirected graph, answer whether every path from `u` to `v` contains `c`. Endpoints count as contained.

Input: `n m q`, the edges, then the queries; all bounds are `200000`.

Output `YES` or `NO` per query.

Sample input
```text
4 3 2
1 2
2 3
2 4
1 3 2
3 4 1
```
Sample output
```text
YES
NO
```
