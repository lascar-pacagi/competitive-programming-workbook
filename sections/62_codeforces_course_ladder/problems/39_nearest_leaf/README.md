# Offline companion: 1110F -- Nearest Leaf

This is an original, locally judgeable companion for [1110F -- Nearest Leaf](https://codeforces.com/problemset/problem/1110/F). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


You have `n` positive file sizes. Repeatedly choose two current files, merge
them into one file, and pay a cost equal to their combined size. Find the
smallest possible total cost to end with one file.

## Input
```text
n
s1 s2 ... sn
```
`1 <= n <= 200000`, `1 <= si <= 10^9`.

## Output
Print the minimum total merge cost.

## Sample
```text
4
4 3 2 6
```
```text
29
```
Merge `2+3=5`, then `4+5=9`, then `6+9=15`.
