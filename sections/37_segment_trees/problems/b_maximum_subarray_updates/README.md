# B. Maximum Subarray Updates

Maintain an array under point assignments. After every assignment, print the
maximum sum of a non-empty contiguous subarray of the entire array.

## Input

The first line contains `n` and `q`. The second line contains the `n` initial
array values. Each of the next `q` lines contains `i x`, meaning `a[i] = x`.
All indices are 1-based.

## Constraints

- `1 <= n, q <= 200,000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= i <= n`

## Output

After every assignment, print the maximum non-empty subarray sum on its own
line.

## Sample

```text
4 3
1 -2 3 4
2 -10
4 -5
1 -1
```

```text
7
3
3
```
