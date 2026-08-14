# Offline companion: ABC083_B -- Some Sums

This is an original, locally judgeable companion for [ABC083_B -- Some Sums](https://atcoder.jp/contests/abc083/tasks/abc083_b?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


For each test case, given closed integer intervals `[l,r]`, find the maximum
number of intervals containing one integer time and the smallest time achieving
that maximum. Intervals with `l=r` contain that one time.

## Input
```text
T
n
l1 r1
...
```
`1 <= T <= 50`, `1 <= n <= 200000`, total `n <= 200000`, and
`-10^9 <= l <= r <= 10^9`.

## Output
Print `maximum earliest_time` for each test case.

## Sample
```text
2
3
1 3
3 5
3 3
2
-2 -1
0 1
```
```text
3 3
1 -2
```
