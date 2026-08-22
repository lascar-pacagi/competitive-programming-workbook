# Convex Resource Schedule

Split the nonnegative sequence `a[1..n]` into exactly `K` nonempty contiguous
batches. A batch whose sum is `s` costs `s^2`. Find the minimum total cost.

## Input

```text
n K
a[1] ... a[n]
```

- `1 <= K <= n <= 5000`;
- `0 <= a[i] <= 10000`;
- the answer fits in a signed 64-bit integer.

## Output

Print the minimum cost.

## Sample input

```text
5 3
2 1 4 1 2
```

## Sample output

```text
34
```
