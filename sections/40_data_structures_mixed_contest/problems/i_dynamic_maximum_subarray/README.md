# I. Dynamic Maximum Subarray

After every point assignment `a[i] = x`, print the maximum sum of a nonempty
contiguous subarray of the whole array.

## Input
```text
n q
a1 ... an
i1 x1
...
iq xq
```
`1 <= n,q <= 200000`, `|a_i|,|x_i| <= 10^9`.

## Sample
```text
4 3
-1 2 3 -5
4 4
1 5
2 -10
```
```text
9
14
7
```
