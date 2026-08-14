# Offline companion: ABC237_G -- Range Sort Query

This is an original, locally judgeable companion for [ABC237_G -- Range Sort Query](https://atcoder.jp/contests/abc237/tasks/abc237_g?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


There are `n` employees, numbered from `1` to `n`, with current salaries
`s[1], s[2], ..., s[n]`.

Process `q` operations:

- `! k x`: change employee `k`'s salary to `x`.
- `? a b`: count employees whose current salary lies between `a` and `b`,
  inclusive.

## Input

```text
n q
s1 s2 ... sn
operation 1
operation 2
...
operation q
```

## Constraints

```text
1 <= n, q <= 200,000
-1,000,000,000 <= s[i], x, a, b <= 1,000,000,000
a <= b
1 <= k <= n
```

## Output

For every `?` operation, print its answer on its own line.

## Sample

Input:

```text
5 6
10 20 30 40 50
? 15 45
! 2 35
? 30 35
! 5 5
? 1 10
? 36 100
```

Output:

```text
3
2
2
1
```
