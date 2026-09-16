# A. Running Median

After every inserted number, print the lower median of the prefix. For a prefix of length `m`, this is the element at 1-based position `(m + 1) / 2` after sorting.

## Input

The first line contains `n`. The second line contains the `n` integers in arrival order.

## Output

Print the lower median after each insertion.

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Sample

Input:

```text
7
5 1 9 2 8 3 7
```

Output:

```text
5 1 5 2 5 3 5
```
