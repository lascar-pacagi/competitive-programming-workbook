# Critical Link Audit

A courier network has `n` stations and `m` numbered one-way links. Link `i`
lets a courier travel from station `u[i]` to station `v[i]`. Couriers start at
station `1`. Self-links and repeated links are allowed.

For every link, the auditors ask: if this link alone were closed, how many
stations that couriers can currently reach from station `1` would become
unreachable?

## Input

```text
n m
m lines: u v
```

- `1 <= n, m <= 200000`;
- `1 <= u, v <= n`.

## Output

Print `m` lines. Line `i` is the number of stations lost when link `i` is
closed. A link that couriers cannot use at all loses no stations.

## Sample input

```text
6 8
1 2
1 3
2 4
3 4
4 5
5 4
5 6
6 6
```

## Sample output

```text
1
1
0
0
2
0
1
0
```
