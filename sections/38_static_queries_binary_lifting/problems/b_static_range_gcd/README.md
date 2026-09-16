# B. Static Range GCD

Given an immutable positive array, answer GCD queries on subarrays.

## Input

The first line contains `n` and `q`. The second line contains `n` integers. Each of the next `q` lines contains `l` and `r`, describing an inclusive 1-based range.

## Output

For each query, print the GCD of all values in the range.

## Constraints

- `1 <= n, q <= 200000`
- `1 <= a[i] <= 10^9`
- `1 <= l <= r <= n`

## Sample

Input:

```text
5 3
12 18 6 10 15
1 3
2 5
4 5
```

Output:

```text
6
1
5
```
