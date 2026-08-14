# Offline companion: 208E -- Blood Cousins

This is an original, locally judgeable companion for [208E -- Blood Cousins](https://codeforces.com/problemset/problem/208/E). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


You have an unlimited supply of coins with the given positive denominations.
Pay exactly `target` using as few coins as possible. Print `-1` if exact payment
is impossible.

## Input

```text
target k
c1 c2 ... ck
```

`0 <= target <= 200000`, `1 <= k <= 20`, and `1 <= ci <= 200000`. A
denomination may be listed more than once. You may use every listed
denomination any number of times.

## Output

Print the minimum number of coins needed to pay exactly `target`, or `-1` if
no exact payment exists.

## Sample

```text
15 3
4 7 9
```

```text
3
```

One optimal payment is `4 + 4 + 7`.
