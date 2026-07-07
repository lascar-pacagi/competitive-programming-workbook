# A. Choose Queries

For each query, compute:

```text
C(n, k) modulo 1,000,000,007
```

where `C(n,k)` is the number of ways to choose `k` objects from `n`.

## Input

```text
q
n1 k1
n2 k2
...
nq kq
```

`1 <= q <= 200,000`, `0 <= k <= n <= 1,000,000`.

## Output

Print one answer per query.

## Sample

Input:

```text
5
5 2
10 0
10 10
6 3
1000000 1
```

Output:

```text
10
1
1
20
1000000
```
