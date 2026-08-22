# Quantile Prefix Sum

For each static query `(l,r,k)`, print the sum of the `k` smallest values in `a[l..r]`, counting duplicates. `n,q <= 200000`; values are nonnegative and answers fit 64-bit.

Sample input
```text
5 2
5 1 4 2 3
1 5 3
2 4 2
```
Sample output
```text
6
3
```
