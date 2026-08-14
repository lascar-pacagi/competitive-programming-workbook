# Offline companion: 342E -- Xenia and Tree

This is an original, locally judgeable companion for [342E -- Xenia and Tree](https://codeforces.com/problemset/problem/342/E). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


There are `n` independent games. Game `i` is won with probability `pi / qi`.
Find the expected number of unordered pairs of games that are both won, modulo
`1000000007`.

## Input
```text
n
p1 q1
...
pn qn
```
`1 <= n <= 200000`, `0 <= pi <= qi < 1000000007`. The games are independent.

## Output
Print the exact expectation modulo `1000000007`.

## Sample
```text
3
1 2
1 3
1 1
```
```text
1
```
The three pair probabilities are `1/6`, `1/2`, and `1/3`.
