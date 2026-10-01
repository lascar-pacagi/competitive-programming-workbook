# Tariff Revision Network

A regulator maintains a connected network of `n` cities and `m` numbered
two-way links. Link `i` joins cities `u[i]` and `v[i]` and currently has a
yearly tariff `w[i]`. A link may join a city to itself, and several links may
join the same pair of cities.

Tariffs are revised one at a time. Revision `j` sets the tariff of link
`e[j]` to `x[j]`; the revision is permanent and later revisions start from the
updated network. No link is ever added or removed.

After every revision, print the minimum total tariff of a set of links that
keeps all `n` cities connected.

## Input

```text
n m q
m lines: u v w
q lines: e x
```

- `1 <= n, m, q <= 200000`;
- `1 <= u, v <= n` and `1 <= e <= m`;
- `1 <= w, x <= 10^9`;
- the initial links connect all cities.

## Output

Print `q` lines; line `j` is the answer after revision `j`.

## Sample input

```text
4 6 4
1 2 5
2 3 2
3 4 7
4 1 3
1 3 4
2 4 6
2 1
3 8
5 1
4 9
```

## Sample output

```text
8
8
5
8
```
