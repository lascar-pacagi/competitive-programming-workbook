# A. Partition Quadratic Cost

Partition the array into `k` contiguous groups minimizing the sum of squared group sums.

All array values are nonnegative. This condition is part of the problem: it
makes the quadratic interval cost Monge, which permits the divide-and-conquer
optimization used by the reference solutions.

## Sample

Input:

```text
5 2
1 2 3 4 5
```
