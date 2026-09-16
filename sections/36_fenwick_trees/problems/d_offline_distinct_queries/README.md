# D. Offline Distinct Range Queries

You are given a fixed array and `q` range queries. For each query `[l, r]`,
print the number of distinct values occurring in `a[l..r]`.

## Input

The first line contains `n` and `q`. The second line contains the `n` array
values. Each of the next `q` lines contains two integers `l` and `r`.

Constraints:

- `1 <= n, q <= 200,000`
- `-10^18 <= a[i] <= 10^18`
- `1 <= l <= r <= n`

## Output

Print one line for each query: the number of distinct values in its range.

## Sample

```text
7 5
1 2 1 3 2 4 1
1 7
2 5
3 3
4 7
2 2
```

```text
4
3
1
4
1
```
