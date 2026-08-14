# K. Online Line DP

Arrays `x`, `slope`, and `fee` are given. Let `dp[0]=0`; for `i>0`:

```text
dp[i] = fee[i] + min(dp[j] + slope[j] * x[i]) over 0 <= j < i
```

Print `dp[n-1]`. Values and the final answer fit signed 64-bit integers.

## Input
```text
n
x1 ... xn
slope1 ... slopen
fee1 ... feen
```
`n <= 200000`.

## Sample
```text
4
0 2 5 1
3 -1 4 2
0 7 1 6
```
```text
9
```
