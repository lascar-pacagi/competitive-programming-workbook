# I. Exactly K Colors

For each query, count the strings of length `n` over an alphabet of `m`
available colors that use exactly `k` distinct colors at least once.

Print every answer modulo `1000000007`.

## Input

```text
q
n1 m1 k1
...
```

`1 <= q <= 200000`, `1 <= n <= 10^18`, `1 <= k <= m <= 200000`, and the
sum of `k` over all queries is at most `200000`.

## Output

Print one answer per query.

## Sample

```text
3
3 3 2
4 2 2
2 5 3
```

```text
18
14
0
```
