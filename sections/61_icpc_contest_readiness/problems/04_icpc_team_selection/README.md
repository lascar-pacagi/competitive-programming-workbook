# Offline companion: ICPC Team Selection

This is an original, locally judgeable companion for [ICPC Team Selection](https://open.kattis.com/problems/icpcteamselection). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


## Statement

For each test case, there are `n` attendees. Attendee `i` is available on every
integer day from `l[i]` through `r[i]`, inclusive.

Choose the minimum number of badge-pickup days so that every attendee is
available on at least one chosen day.

## Input

```text
T
n
l1 r1
l2 r2
...
```

`1 <= T <= 50`, `1 <= n <= 200000`, the total `n` over all test cases is at
most `200000`, and `-10^9 <= l[i] <= r[i] <= 10^9`.

## Output

Print the minimum number of pickup days for each test case.

## Sample

Input:

```text
3
4
1 3
2 5
4 6
6 6
3
-5 -3
-2 0
1 4
1
7 7
```

Output:

```text
2
3
1
```
