# Failed Vertex Routes

For each `(u,v,c)`, vertex `c` fails. Answer whether `u` and `v` remain connected. Queries with `c=u` or `c=v` have answer `NO`.

Input: a connected undirected graph as `n m q`, its edges, then queries; bounds `200000`.

Sample input
```text
4 3 2
1 2
2 3
2 4
3 4 2
1 3 4
```
Sample output
```text
NO
YES
```
