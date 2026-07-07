# B. All Symbols

For each query, count strings of length `n` over an alphabet of `k` symbols such
that every symbol appears at least once. Print the answer modulo
`1,000,000,007`.

## Input

```text
q
n1 k1
n2 k2
...
nq kq
```

`1 <= q <= 20,000`, `0 <= n <= 10^9`, `1 <= k <= 5000`.

## Output

Print one answer per query.

## Sample

Input:

```text
4
3 2
3 3
2 3
0 1
```

Output:

```text
6
6
0
0
```
