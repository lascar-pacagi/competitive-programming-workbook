# F. Subtree Mode Profile

Each vertex has a positive color. For every rooted subtree (root `1`), print
two values: its maximum color frequency and the number of distinct colors that
attain this maximum.

## Input
```text
n
c1 ... cn
n-1 edges
```
`1 <= n <= 200000`, `1 <= ci <= 10^9`.

## Sample
```text
4
1 2 1 3
1 2
1 3
3 4
```
```text
2 1
1 1
1 2
1 1
```
