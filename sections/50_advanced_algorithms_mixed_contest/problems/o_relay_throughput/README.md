# O. Relay Throughput

A directed communication network has stations `1..n`. Station `1` supplies
data, and station `n` receives it. A directed link can carry at most its link
capacity per second. Station `v` can process at most `limit[v]` units per
second, regardless of how many links it has.

At every intermediate station, total incoming data must equal total outgoing
data, and this amount cannot exceed its processing limit. The supplier's total
outgoing data cannot exceed `limit[1]`; the receiver's total incoming data
cannot exceed `limit[n]`. Links never enter station `1` or leave station `n`.

Data may be split among links. Find the maximum total delivery per second
while respecting every link capacity and every station limit.

## Input

The first line contains `n m`. The second line contains `n` integers
`limit[1] ... limit[n]`. Each of the next `m` lines contains `u v capacity`,
describing one directed link from `u` to `v`.

- `2 <= n <= 250`; `0 <= m <= 4000`.
- `0 <= limit[v] <= 1000000000`.
- `1 <= u, v <= n`, `u != v`, `u != n`, and `v != 1`.
- `0 <= capacity <= 1000000000`.
- Parallel links are allowed and have separate capacities. Cycles among
  intermediate stations are allowed.

## Output

Print the maximum total delivery. The maximum is an integer.

## Sample

Input:

```text
4 4
20 2 3 20
1 2 9
1 3 9
2 4 9
3 4 9
```

Output:

```text
5
```

Send `2` units through station `2` and `3` through station `3`. Their combined
processing limit prevents any larger delivery, despite the larger link capacities.
