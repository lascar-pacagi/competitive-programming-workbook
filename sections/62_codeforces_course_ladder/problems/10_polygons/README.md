# Offline companion: 166B -- Polygons (2100, geometry challenge)

This is an original, locally judgeable companion for [166B -- Polygons (2100, geometry challenge)](https://codeforces.com/problemset/problem/166/B). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


For each test case, construct a sequence of `n` integers between `0` and `k`
inclusive whose sum is exactly `s`. Among all valid sequences, print the
lexicographically smallest one. Print `-1` if none exists.

## Input

```text
T
n k s
...
```

`1 <= T <= 100`, `1 <= n <= 200000`, `0 <= k,s <= 10^9`, and total `n` is at
most `200000`.

## Output

Print the sequence or `-1`.

## Sample

```text
3
4 3 7
2 1 3
3 0 0
```

```text
0 1 3 3
-1
0 0 0
```
