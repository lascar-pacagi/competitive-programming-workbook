# C. Kth Ancestor

In a tree rooted at node `1`, answer queries asking for the `k`-th ancestor of a node. The 0-th ancestor of a node is the node itself. Print `-1` if the requested ancestor does not exist.

## Input

The first line contains `n` and `q`. The second line contains the parents of nodes `2, 3, ..., n`. Each of the next `q` lines contains `v` and `k`.

## Output

For each query, print the `k`-th ancestor of `v`, or `-1` if it does not exist.

## Constraints

- `1 <= n, q <= 200000`
- `1 <= parent[v] < v` for `2 <= v <= n`
- `1 <= v <= n`
- `0 <= k <= n`

## Sample

Input:

```text
5 5
1 1 2 2
4 1
4 2
4 3
1 0
3 1
```

Output:

```text
2
1
-1
1
1
```
