# Offline companion: 86D -- Powerful Array (2200)

This is an original, locally judgeable companion for [86D -- Powerful Array (2200)](https://codeforces.com/problemset/problem/86/D). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


There are `n` build steps and `m` dependency rules. A rule `a b` means step
`a` must be completed before step `b`.

Classify the dependency graph:

- print `IMPOSSIBLE` if no valid order exists;
- print `AMBIGUOUS` if two or more valid orders exist;
- otherwise print `UNIQUE` and the only valid order.

## Input

```text
n m
a1 b1
a2 b2
...
am bm
```

`1 <= n <= 200000`, `0 <= m <= 200000`. Steps are numbered from `1` to `n`.
No dependency is repeated, and `a != b` for every rule.

## Output

For an impossible graph, print:

```text
IMPOSSIBLE
```

For a graph with multiple valid orders, print:

```text
AMBIGUOUS
```

Otherwise print `UNIQUE` on the first line and the only valid order on the
second line.

## Sample 1

```text
4 3
1 2
2 3
3 4
```

```text
UNIQUE
1 2 3 4
```

## Sample 2

```text
3 1
1 3
```

```text
AMBIGUOUS
```
