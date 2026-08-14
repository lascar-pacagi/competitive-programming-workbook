# D. Equal Index Pairs

## Statement

For each test case, count the pairs of indices `(i, j)` such that:

```text
1 <= i < j <= n
a[i] = a[j]
```

Values may be negative. Print the number of pairs.

## Input

```text
T
n
a1 a2 ... an
...
```

`1 <= T <= 100`, `1 <= n <= 200000`, the sum of all `n` is at most `200000`,
and `|ai| <= 10^9`.

## Output

Print one pair count per test case.

## Sample

Input:

```text
3
4
1 1 1 1
5
1 2 1 2 1
3
-1 0 1
```

Output:

```text
6
4
0
```
