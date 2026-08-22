# D. Weighted Compositions

Choose an integer `xi` for every type `i`, with `0 <= xi <= ai`. Type `i`
contributes `wi * xi` to the total. Count choices whose total is exactly `K`,
modulo `998244353`.

## Input

```text
n K
w1 a1
...
wn an
```

- `1 <= n <= 5000`
- `0 <= K <= 50000`
- `1 <= wi <= K+1`
- `0 <= ai <= K`
- the total number of nonzero coefficients across the truncated per-type
  polynomials is at most `200000`

## Output

Print the count.

## Sample

```text
3 7
1 2
2 2
3 2
```

```text
3
```
