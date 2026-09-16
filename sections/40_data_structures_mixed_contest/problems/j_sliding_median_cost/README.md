# J. Sliding Median Cost

You are given an array `a` of length `n` and a window length `k`.

For every contiguous subarray (window) of exactly `k` elements, choose an
integer `x` that minimizes the sum of the absolute differences between `x`
and all elements in that window.

For the window starting at position `l`, its cost is

```text
min over all integers x of
|a[l] - x| + |a[l + 1] - x| + ... + |a[l + k - 1] - x|.
```

Print the minimum cost of each of the `n - k + 1` windows, from left to
right. The value of `x` is chosen independently for every window and does
not need to be printed.

## Input
```text
n k
a1 ... an
```

- `n` is the number of elements in the array.
- `k` is the length of every window.
- `a1, ..., an` are the array elements.

`1 <= k <= n <= 200000`, `|a_i| <= 10^9`.

## Output

Print `n - k + 1` integers. The `i`-th integer is the minimum cost of the
window `a[i], a[i + 1], ..., a[i + k - 1]`.

## Sample
```text
5 3
1 5 2 4 3
```
```text
4 3 2
```

The three windows are:

- `[1, 5, 2]`: choose `x = 2`, giving cost `1 + 3 + 0 = 4`.
- `[5, 2, 4]`: choose `x = 4`, giving cost `1 + 2 + 0 = 3`.
- `[2, 4, 3]`: choose `x = 3`, giving cost `1 + 1 + 0 = 2`.
