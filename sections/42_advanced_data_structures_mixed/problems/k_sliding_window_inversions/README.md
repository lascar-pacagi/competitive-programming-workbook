# K. Sliding Window Inversions

You are given an integer array of length `n` and a window length `k`. For every
contiguous window of exactly `k` elements, print its number of inversions.

An inversion is a pair of positions `i<j` inside that window with `a[i]>a[j]`.
Equal values do not form inversions. Count each pair once; values never change.

## Input

```text
n k
a1 ... an
```

`1 <= k <= n <= 200000` and `|a_i| <= 10^9`.

## Output

Print `n-k+1` counts in order of the windows' left endpoints. Use signed 64-bit
counts: a decreasing window has `k*(k-1)/2` inversions.

## Sample

```text
5 3
3 1 2 2 0
```

```text
2 0 2
```

The windows are `[3,1,2]`, `[1,2,2]`, and `[2,2,0]`. The equal pair of
2s is never an inversion.
