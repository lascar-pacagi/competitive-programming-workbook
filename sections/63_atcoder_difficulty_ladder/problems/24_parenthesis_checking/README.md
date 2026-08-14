# Offline companion: ABC223_F -- Parenthesis Checking

This is an original, locally judgeable companion for [ABC223_F -- Parenthesis Checking](https://atcoder.jp/contests/abc223/tasks/abc223_f?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


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
