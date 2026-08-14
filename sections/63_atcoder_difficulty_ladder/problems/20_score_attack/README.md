# Offline companion: ABC061_D -- Score Attack

This is an original, locally judgeable companion for [ABC061_D -- Score Attack](https://atcoder.jp/contests/abc061/tasks/abc061_d?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


For each query, find the smallest non-negative integer `x` such that:

```text
a * x == b (mod m)
```

If no such integer exists, print `-1`.

## Input

```text
q
a1 b1 m1
a2 b2 m2
...
aq bq mq
```

- `1 <= q <= 2 * 10^5`
- `1 <= a, b, m <= 10^9`

## Output

Print one answer per query.

## Sample

```text
4
6 8 14
6 7 14
10 1 17
25 9 1
```

```text
6
-1
12
0
```

For the first query, `6 * 6 = 36`, and `36` leaves remainder `8` modulo
`14`. No value can solve the second query because every multiple of `6` has an
even remainder modulo `14`.
