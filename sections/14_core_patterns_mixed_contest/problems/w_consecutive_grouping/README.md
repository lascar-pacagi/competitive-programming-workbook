# W. Consecutive Grouping

Given a multiset of integers, determine whether all its elements can be
partitioned into one or more groups such that every group:

- contains at least three elements; and
- after sorting, consists of consecutive integers with difference exactly one.

Every input occurrence must belong to exactly one group.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 200000` and `-10^9 <= a_i <= 10^9`.

## Output

Print `YES` if such a partition exists, otherwise print `NO`.

## Sample Input

```text
6
1 2 3 3 4 5
```

## Sample Output

```text
YES
```
