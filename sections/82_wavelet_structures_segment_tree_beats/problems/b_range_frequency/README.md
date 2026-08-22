# Range Frequency Threshold

For every static query `(l,r,x)`, count values in `a[l..r]` that are at most `x`. Bounds are `n,q <= 200000`; values and `x` fit signed 32-bit.

Sample input
```text
5 2
5 1 4 2 3
2 5 3
1 3 0
```
Sample output
```text
3
0
```
