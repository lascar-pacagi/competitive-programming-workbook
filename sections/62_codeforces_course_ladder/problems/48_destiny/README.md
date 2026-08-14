# Offline companion: 840D -- Destiny

This is an original, locally judgeable companion for [840D -- Destiny](https://codeforces.com/problemset/problem/840/D). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


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
