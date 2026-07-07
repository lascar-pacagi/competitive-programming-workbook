# A. Prime Counter

Given `n` and `q` range queries, count primes in each interval `[l, r]`.

## Input

```text
n q
l1 r1
l2 r2
...
lq rq
```

`1 <= n <= 1,000,000`, `1 <= q <= 200,000`, `1 <= l <= r <= n`.

## Output

Print one answer per query.

## Sample

Input:

```text
20 4
1 20
2 10
14 16
17 17
```

Output:

```text
8
4
0
1
```
