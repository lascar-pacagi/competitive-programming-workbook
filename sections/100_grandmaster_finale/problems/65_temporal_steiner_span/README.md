# Temporal Steiner Span

A fibre network is a tree of `n` sites joined by `n-1` cables; cable `i` has
length `w[i]`. Sites are numbered in the order in which customers signed up,
so site `v` joined at time `v`.

For a query `(l, r)`, the operator wants to light up only the sites that
joined during `[l, r]`, that is, sites `l, l+1, ..., r`. Lighting a cable costs
its length, and the lit cables must connect all these sites to each other
(other sites may be passed through). Print the minimum total length of lit
cables.

Queries are independent.

## Input

```text
n q
n-1 lines: u v w
q lines: l r
```

- `1 <= n, q <= 200000`;
- `1 <= w <= 10^9`;
- the cables form a tree;
- `1 <= l <= r <= n`.

## Output

Print one line per query.

## Sample input

```text
7 5
1 2 3
1 3 1
2 4 2
2 5 5
3 6 4
6 7 1
4 5
2 3
5 7
1 1
1 7
```

## Sample output

```text
7
4
14
0
16
```
