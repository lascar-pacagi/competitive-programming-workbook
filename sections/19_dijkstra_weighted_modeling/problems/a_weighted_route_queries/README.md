# A. Weighted Route Queries

You are given a directed graph with nonnegative edge weights, a source `s`, and
several target queries. For each target, print the shortest distance from `s`,
or `-1` if it is unreachable.

## Input

```text
n m s q
u1 v1 w1
...
um vm wm
x1 x2 ... xq
```

`1 <= n <= 2 * 10^5`, `0 <= m <= 2 * 10^5`, `0 <= wi <= 10^9`.

## Output

Print `q` integers.

## Sample

Input:

```text
5 6 1 5
1 2 4
1 3 2
3 2 1
2 4 7
3 5 5
5 4 1
1 2 3 4 5
```

Output:

```text
0 3 2 8 7
```

