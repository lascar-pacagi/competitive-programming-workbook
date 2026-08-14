# Offline companion: ABC253_F -- Operations on a Matrix

This is an original, locally judgeable companion for [ABC253_F -- Operations on a Matrix](https://atcoder.jp/contests/abc253/tasks/abc253_f?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


An array of `n` integers starts filled with zero. Process `q` operations:

- `1 l r x`: add `x` to every element with index in `[l, r]`.
- `2 l r`: print the sum of all elements with index in `[l, r]`.

All indices are 1-based.

## Input

```text
n q
operation 1
operation 2
...
operation q
```

- `1 <= n, q <= 200,000`
- `1 <= l <= r <= n`
- `-10^6 <= x <= 10^6`

## Output

Print one line for every operation of type `2`.

## Sample

```text
5 6
1 2 4 3
2 1 5
1 1 5 -1
2 2 3
1 3 3 10
2 3 5
```

```text
9
4
13
```

After the first update the array is `[0, 3, 3, 3, 0]`.
