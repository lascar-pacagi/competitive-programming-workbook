# A. Subtree Sizes

You are given an undirected tree with `n` vertices. Root the tree at vertex `1`.
For every vertex `v`, output the size of the subtree of `v`.

The subtree of `v` contains `v` and every descendant of `v` after the tree is
rooted at `1`.

## Input

```text
n
u1 v1
u2 v2
...
u(n-1) v(n-1)
```

`1 <= n <= 2 * 10^5`  
The edges form a tree.

## Output

Print `n` integers. The `i`-th integer is the subtree size of vertex `i`.

## Sample

Input:

```text
7
1 2
1 3
2 4
2 5
3 6
6 7
```

Output:

```text
7 3 3 1 1 2 1
```

