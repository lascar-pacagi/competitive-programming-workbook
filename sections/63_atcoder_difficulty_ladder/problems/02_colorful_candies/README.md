# Offline companion: ABC210_C -- Colorful Candies

This is an original, locally judgeable companion for [ABC210_C -- Colorful Candies](https://atcoder.jp/contests/abc210/tasks/abc210_c?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


## Statement

For each test case, count the nonempty contiguous subarrays whose largest value
minus smallest value is at most `k`.

## Input

```text
T
n k
a1 a2 ... an
...
```

`1 <= T <= 50`, `1 <= n <= 200000`, the total `n` over all test cases is at
most `200000`, `0 <= k <= 10^9`, and `|ai| <= 10^9`.

## Output

Print one count for each test case.

## Sample

Input:

```text
3
4 2
1 3 2 5
5 0
4 4 -1 -1 -1
3 1
-3 -2 -1
```

Output:

```text
7
9
5
```
