# E. Functional Walk Minimum

Each vertex has one outgoing edge and an integer value. For query `(v,k)`,
follow exactly `k` edges. Print the final vertex and the minimum value among
the starting vertex and all visited vertices.

## Input
```text
n q
next1 ... nextn
value1 ... valuen
v k
...
```
`1 <= n,q <= 200000`, `0 <= k <= 10^18`.

## Sample
```text
4 3
2 3 4 2
8 5 7 1
1 2
3 3
4 0
```
```text
3 5
3 1
4 1
```
