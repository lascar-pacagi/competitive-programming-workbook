# A. Static Range Minimum

Given an immutable array, answer minimum queries on subarrays.

## Input

The first line contains `n` and `q`. The second line contains `n` integers. Each of the next `q` lines contains `l` and `r`, describing an inclusive 1-based range.

## Output

For each query, print the minimum value in the range.

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `1 <= l <= r <= n`

## Sample

Input:

```text
6 4
5 2 7 1 3 4
1 6
2 3
3 5
4 4
```

Output:

```text
1
2
1
1
```
