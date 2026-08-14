# Offline companion: AGC017_F -- Zigzag

This is an original, locally judgeable companion for [AGC017_F -- Zigzag](https://atcoder.jp/contests/agc017/tasks/agc017_f?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


You are given `n` half-open time intervals `[start, end)`. Choose as many
intervals as possible so that no two chosen intervals overlap. Intervals that
only touch are compatible: `[2,5)` and `[5,8)` may both be chosen.

## Input

```text
n
start1 end1
start2 end2
...
startn endn
```

## Constraints

```text
1 <= n <= 200000
0 <= starti < endi <= 1000000000
```

## Output

Print the largest possible number of pairwise compatible intervals.

## Sample

```text
5
0 4
1 2
2 5
4 6
5 7
```

```text
3
```

One optimal schedule is `[1,2)`, `[2,5)`, `[5,7)`.
