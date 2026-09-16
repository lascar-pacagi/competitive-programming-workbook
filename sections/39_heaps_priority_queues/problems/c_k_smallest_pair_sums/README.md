# C. K Smallest Pair Sums

Two arrays `a` and `b` are sorted in nondecreasing order. Among all `n * m` values `a[i] + b[j]`, print the `k` smallest in nondecreasing order. Keep repeated sums.

## Input

The first line contains `n`, `m`, and `k`. The second line contains `a`, and the third line contains `b`.

## Output

Print the `k` smallest pair sums in nondecreasing order.

## Constraints

- `1 <= n, m <= 200000`
- `1 <= k <= min(200000, n * m)`
- `-10^9 <= a[i], b[j] <= 10^9`
- Both arrays are sorted in nondecreasing order.

## Sample

Input:

```text
3 3 5
1 4 8
2 3 10
```

Output:

```text
3 4 6 7 10
```
