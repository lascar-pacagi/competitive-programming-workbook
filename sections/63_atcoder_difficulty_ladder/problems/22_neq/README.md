# Offline companion: ABC172_E -- NEQ

This is an original, locally judgeable companion for [ABC172_E -- NEQ](https://atcoder.jp/contests/abc172/tasks/abc172_e?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


For each query, there are `r` distinct red performers and `b` distinct blue
performers. Count the number of lineups containing every performer exactly once
such that no two red performers stand next to each other.

Print each answer modulo `1,000,000,007`.

## Input

```text
q
r1 b1
r2 b2
...
rq bq
```

- `1 <= q <= 200,000`
- `0 <= r, b <= 1,000,000`

## Output

Print one answer per query.

## Sample

```text
4
2 2
3 1
0 3
1 0
```

```text
12
0
6
1
```

For the first query, `R1 B1 R2 B2` is valid, while `R1 R2 B1 B2` is not.
