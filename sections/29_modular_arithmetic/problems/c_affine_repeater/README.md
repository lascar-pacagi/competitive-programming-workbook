# C. Affine Repeater

For each query, define:

```text
f(x) = a*x + b
```

All operations are modulo `1,000,000,007`.

Starting from `x`, apply `f` exactly `k` times. Print the final value.

## Input

```text
q
a1 b1 x1 k1
a2 b2 x2 k2
...
aq bq xq kq
```

`1 <= q <= 2 * 10^5`, `0 <= a,b,x <= 10^18`, `0 <= k <= 10^18`.

## Output

Print one answer per query.

## Sample

Input:

```text
4
2 3 1 3
1 5 10 4
0 7 9 5
10 0 2 6
```

Output:

```text
29
30
7
2000000
```
