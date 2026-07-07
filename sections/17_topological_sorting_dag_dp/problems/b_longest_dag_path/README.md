# B. Longest DAG Path

You are given a directed acyclic graph. Find the maximum number of edges in any
directed path.

## Input

```text
n m
u1 v1
u2 v2
...
um vm
```

`1 <= n <= 2 * 10^5`  
`0 <= m <= 2 * 10^5`  
The graph is guaranteed to be acyclic.

## Output

Print one integer: the length of the longest directed path.

## Sample

Input:

```text
5 6
1 2
1 3
2 4
3 4
4 5
2 5
```

Output:

```text
3
```

