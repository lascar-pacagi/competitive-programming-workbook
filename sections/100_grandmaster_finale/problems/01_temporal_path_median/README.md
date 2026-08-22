# Temporal Path Median

A rooted communication tree grows away from station `1`. Every station `v`
has an integer timestamp `a[v]`. For each query `(u,v)`, consider the multiset
of timestamps on the simple path from `u` to `v`, including both endpoints.

Output two integers:

1. the **lower median**, the element at position `(length+1)/2` after sorting
   the path values in nondecreasing order;
2. the minimum possible value of `sum |a[x]-z|` over all integer choices of
   `z`, where the sum is over vertices on the path.

The lower median is requested even when the path length is even. It is always
one minimizer of the second quantity.

## Input

```text
n q
a[1] a[2] ... a[n]
n-1 lines: u v
q lines: u v
```

- `1 <= n,q <= 200000`
- `-10^9 <= a[v] <= 10^9`
- the edges form a tree.

## Output

For every query, print `median minimum_sum` on its own line. The sum fits in a
signed 64-bit integer.

## Sample input

```text
5 3
5 1 9 3 7
1 2
1 3
2 4
2 5
4 3
4 5
3 3
```

## Sample output

```text
3 10
3 6
9 0
```
