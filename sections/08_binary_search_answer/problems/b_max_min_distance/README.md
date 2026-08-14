# B. Maximum Minimum Distance

## Statement

You are given `n` positions on a line and must choose `k` of them. Maximize the
minimum distance between any two chosen positions.

The positions are already given from left to right, in non-decreasing order.
Equal positions are allowed.

### Example

Suppose the available positions are:

```text
1 2 4 8 9
```

and `k = 3`. If we choose positions `1`, `4`, and `8`, the distances between
consecutive chosen positions are `4 - 1 = 3` and `8 - 4 = 4`. The minimum
distance of this choice is therefore `3`.

It is impossible to choose three positions with every consecutive chosen pair
at least `4` apart. Thus the largest possible minimum distance is `3`.

You choose only from the given positions; you may not create a new position
between them.

## Input

```text
T
n k
x1 x2 ... xn
...
```

`1 <= T <= 30`, `2 <= k <= n`, the total `n` over all test cases is at most
`200000`, and positions fit in signed 32-bit integers.

## Output

For each test case, print the largest possible minimum distance.
