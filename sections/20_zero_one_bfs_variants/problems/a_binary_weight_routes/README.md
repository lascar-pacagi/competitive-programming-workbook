# A. Binary Weight Routes

You are given a directed graph where each edge has weight `0` or `1`. From a
source vertex `s`, answer shortest-distance queries.

If a target is unreachable, its distance is `-1`.

## Input

```text
n m s q
u1 v1 w1
...
um vm wm
x1 x2 ... xq
```

`1 <= n <= 2 * 10^5`, `0 <= m <= 2 * 10^5`, and every `wi` is `0` or `1`.

## Output

Print `q` integers.

## Sample

Input:

```text
5 6 1 5
1 2 1
1 3 0
3 2 0
2 4 1
3 5 1
5 4 0
1 2 3 4 5
```

Output:

```text
0 0 0 1 1
```

