# B. Window Minimum DP

`dp[i]=a[i]+min(dp[j])` over the previous `w` positions. Print `dp[n]`.

## Sample

Input:

```text
5 2
5 1 4 2 3
```
