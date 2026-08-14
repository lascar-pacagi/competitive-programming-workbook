# Offline companion: ABC245_F -- Endless Walk

This is an original, locally judgeable companion for [ABC245_F -- Endless Walk](https://atcoder.jp/contests/abc245/tasks/abc245_f?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


Split all given positive integers into two groups. Let the two group sums be
`A` and `B`. Find the minimum possible value of `|A - B|`.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 200`, `1 <= ai <= 1000`, and `sum(ai) <= 100000`.

## Output

Print the minimum possible difference.

## Sample

```text
4
1 6 11 5
```

```text
1
```

One split is `{11}` and `{1, 5, 6}`, with sums `11` and `12`.
