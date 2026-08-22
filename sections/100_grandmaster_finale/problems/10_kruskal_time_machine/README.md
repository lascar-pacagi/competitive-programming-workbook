# Kruskal Time Machine

An undirected weighted graph has an integer value on every vertex. For a query
`(v,W,k)`, keep only edges of weight at most `W` and consider the connected
component containing `v`. Output its `k`-th smallest vertex value, counting
duplicates.

## Input

```text
n m q
a[1] ... a[n]
m lines: u v weight
q lines: v W k
```

- `1 <= n,q <= 200000` and `0 <= m <= 200000`
- edge weights and vertex values are signed 32-bit integers;
- parallel edges and disconnected graphs are allowed;
- `k` is valid for the queried threshold component.

## Output

Print one value for every query.

## Sample input

```text
5 5 4
8 1 6 3 5
1 2 4
2 3 7
3 4 2
4 5 9
1 5 10
1 3 1
3 2 2
2 7 2
5 9 3
```

## Sample output

```text
8
6
3
5
```
