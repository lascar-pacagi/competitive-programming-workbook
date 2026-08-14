# D. Exact Sum, Maximum Items

Choose a subset of the `n` values whose sum is exactly `target`.

Among all such subsets, print the largest possible number of selected values.
Print `-1` if no subset has the exact target sum. The empty subset is allowed.

## Input

```text
n target
a1 a2 ... an
```

## Constraints

```text
1 <= n <= 36
-1,000,000,000,000 <= a[i], target <= 1,000,000,000,000
```

## Output

Print the maximum number of selected values, or `-1`.

## Sample

Input:

```text
5 5
4 3 2 1 -1
```

Output:

```text
4
```
