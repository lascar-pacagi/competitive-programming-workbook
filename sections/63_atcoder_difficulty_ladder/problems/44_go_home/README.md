# Offline companion: AGC023_D -- Go Home

This is an original, locally judgeable companion for [AGC023_D -- Go Home](https://atcoder.jp/contests/agc023/tasks/agc023_d?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


You are given a simple polygon with integer-coordinate vertices in boundary
order. Count lattice points `(x,y)` that lie **strictly inside** the polygon.

Consecutive polygon vertices may be collinear.

## Input

```text
n
x1 y1
x2 y2
...
xn yn
```

## Constraints

```text
3 <= n <= 200,000
-1,000,000,000,000 <= x[i], y[i] <= 1,000,000,000,000
the polygon is simple
```

## Output

Print the number of lattice points strictly inside the polygon.

## Sample

Input:

```text
4
0 0
2 0
2 2
0 2
```

Output:

```text
1
```
