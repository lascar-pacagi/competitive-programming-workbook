# Offline companion: 158B -- Taxi (1100)

This is an original, locally judgeable companion for [158B -- Taxi (1100)](https://codeforces.com/problemset/problem/158/B). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


Choose exactly `k` values from an array of `n` values. The spread of a chosen
team is its largest value minus its smallest value. For each test case, print
the minimum possible spread.

## Input

```text
T
n k
a1 a2 ... an
...
```

`1 <= T <= 50`, `1 <= k <= n <= 200000`, the total `n` over all test cases is
at most `200000`, and values fit in signed 32-bit integers.

## Output

Print one minimum spread per test case.

## Sample

```text
3
5 3
4 1 9 7 5
4 1
10 -2 8 1
5 4
3 3 3 3 3
```

```text
3
0
0
```
