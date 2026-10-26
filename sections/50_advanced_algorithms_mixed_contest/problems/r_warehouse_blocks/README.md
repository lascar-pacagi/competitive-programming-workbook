# R. Warehouse Blocks

There are `n` customers along a straight road, at nondecreasing integer
positions `x[1] ... x[n]`. Divide this ordered list into exactly `k` nonempty
contiguous blocks. Different customers remain distinct even if their positions
are equal.

Each block gets its own warehouse, placed at any integer coordinate. Its cost
is the sum of distances from the customers in that block to its warehouse.
A customer's distance is the absolute difference of the two coordinates.
Different warehouses may occupy the same coordinate.

Choose the blocks and warehouse coordinates to minimize the total cost.

## Input

The first line contains `n k`. The second line contains the `n` positions.

- `1 <= n <= 30000` and `1 <= k <= min(n, 30)`.
- `0 <= x[1] <= ... <= x[n] <= 1000000000`.

## Output

Print the minimum total cost. The answer may exceed 32-bit integer range.

## Sample

Input:

```text
5 2
0 2 3 10 11
```

Output:

```text
4
```

Use the block at positions `0,2,3` with a warehouse at `2`, costing `3`,
and the block at `10,11` with a warehouse at `10`, costing `1`.
