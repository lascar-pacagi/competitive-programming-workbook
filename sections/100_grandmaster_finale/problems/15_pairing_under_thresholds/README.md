# Pairing Under Thresholds

There are `n` people and `m` acceptable undirected pairs. Pairing people `u`
and `v` has difficulty `d`. A person may belong to at most one chosen pair.

For each query `k`, find the smallest threshold `D` for which at least `k`
vertex-disjoint acceptable pairs have difficulty at most `D`. Print `-1` if
even the full graph has no matching of size `k`.

Parallel pair offers are allowed.

## Input

```text
n m q
m lines: u v d
q lines: k
```

- `2 <= n <= 60`;
- `0 <= m <= 900`;
- `1 <= q <= 200000`;
- `1 <= k <= floor(n/2)`;
- `1 <= d <= 10^9`;
- `u != v`.

## Output

For every query, print its answer on a separate line.

## Sample input

```text
6 7 3
1 2 4
2 3 1
3 1 2
4 5 3
5 6 6
4 6 5
2 4 7
1
2
3
```

## Sample output

```text
1
3
7
```
