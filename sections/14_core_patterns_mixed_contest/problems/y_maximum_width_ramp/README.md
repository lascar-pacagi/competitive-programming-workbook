# Y. Maximum Width Ramp

Given an integer array `a`, find the maximum value of `j - i` over all pairs
of indices satisfying

```text
0 <= i <= j < n
a[i] <= a[j]
```

## Input

The first line contains an integer `n`.

The second line contains `n` integers `a[0], a[1], ..., a[n-1]`.

`1 <= n <= 200000`

`-10^9 <= a[i] <= 10^9`

## Output

Print the maximum possible width `j - i`.

## Sample Input

```text
6
6 0 8 2 1 5
```

## Sample Output

```text
4
```
