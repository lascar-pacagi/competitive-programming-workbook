# Offline companion: 1292C -- Xenon's Attack on the Gangs

This is an original, locally judgeable companion for [1292C -- Xenon's Attack on the Gangs](https://codeforces.com/problemset/problem/1292/C). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


There are `n` desks, numbered from `1` to `n`. Desk `i` has a non-negative
capacity `a[i]`.

Process `q` operations:

- `1 i x`: set the capacity of desk `i` to `x`.
- `2 x`: print the smallest index of a desk whose current capacity is at least
  `x`. Print `0` if no such desk exists.

## Input

```text
n q
a1 a2 ... an
operation 1
operation 2
...
operation q
```

## Constraints

```text
1 <= n, q <= 200,000
0 <= a[i], x <= 1,000,000,000 for assignment operations
1 <= x <= 1,000,000,000 for query operations
1 <= i <= n
```

## Output

For every type-2 operation, print one answer on its own line.

## Sample

Input:

```text
5 7
3 0 4 2 1
2 3
2 4
1 1 1
2 3
1 3 0
2 3
2 1
```

Output:

```text
1
3
3
0
1
```
