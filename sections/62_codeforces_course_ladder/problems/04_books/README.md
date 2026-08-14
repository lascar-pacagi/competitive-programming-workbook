# Offline companion: 279B -- Books (1400)

This is an original, locally judgeable companion for [279B -- Books (1400)](https://codeforces.com/problemset/problem/279/B). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


There are `n` signal positions, initially all zero. Each operation adds integer
`x` to every position from `l` through `r`, inclusive. After all operations,
print the largest final signal and the smallest position at which it occurs.

## Input

```text
n q
l1 r1 x1
...
```

`1 <= n,q <= 200000`, `1 <= l <= r <= n`, and `|x| <= 10^9`.

## Output

Print `maximum smallest_position`.

## Sample

```text
5 3
1 3 4
2 5 -2
4 4 9
```

Output:

```text
7 4
```
