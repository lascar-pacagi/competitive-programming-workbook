# B. General Inverse

For each query, given `a` and `m`, find the modular inverse of `a` modulo `m`.

Print the smallest non-negative integer `x` such that:

```text
a*x == 1 (mod m)
```

If no such `x` exists, print `-1`.

## Input

```text
q
a1 m1
a2 m2
...
aq mq
```

`1 <= q <= 2 * 10^5`, `1 <= a,m <= 10^9`.

## Output

Print one answer per query.

## Sample

Input:

```text
4
3 11
10 17
6 9
25 1
```

Output:

```text
4
12
-1
0
```
