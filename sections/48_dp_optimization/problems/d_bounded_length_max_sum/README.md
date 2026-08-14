# D. Bounded-Length Maximum Sum

Given an integer array, choose a nonempty contiguous subarray whose length is
between `L` and `R`, inclusive. Print the maximum possible sum.

## Input

```text
n L R
a1 a2 ... an
```

## Constraints

```text
1 <= L <= R <= n <= 200000
-1000000000 <= ai <= 1000000000
```

## Output

Print one integer: the largest sum of a subarray with an allowed length.

## Sample

```text
6 2 4
-2 3 -1 5 -6 4
```

```text
7
```

The subarray `3 -1 5` has length three and sum seven.
