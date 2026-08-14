# L. Weighted Tree Guards

An undirected tree has a positive installation cost for every vertex. You may
install guards on selected vertices. A vertex is protected when it contains a
guard or is adjacent to a vertex containing a guard.

Choose guards of minimum total cost so that every vertex is protected.

## Input

```text
n
cost[1] cost[2] ... cost[n]
u1 v1
...
u(n-1) v(n-1)
```

`1 <= n <= 200000`

`1 <= cost[i] <= 10^9`

The edges form a tree.

## Output

Print the minimum total installation cost.

## Sample Input

```text
5
5 1 2 10 1
1 2
1 3
3 4
3 5
```

## Sample Output

```text
3
```
