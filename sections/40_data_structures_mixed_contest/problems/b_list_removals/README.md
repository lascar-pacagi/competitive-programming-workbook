# B. List Removals

Repeatedly remove and print the `k`-th currently present element, counting from the left.

## Input

The first line contains `n`. The second line contains the `n` list values. The third line contains `n` removal ranks: at step `t`, remove the `k_t`-th remaining element.

## Output

Print the values in their removal order.

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `1 <= k_t <= n - t + 1`

## Sample

Input:

```text
5
10 20 30 40 50
2 3 1 1 1
```

Output:

```text
20 40 10 30 50
```
