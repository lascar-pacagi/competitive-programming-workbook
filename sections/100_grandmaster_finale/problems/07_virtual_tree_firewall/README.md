# Virtual Tree Firewall

You are given a tree whose edges have positive removal costs. Each query marks
a set of terminal vertices. Remove edges so that every resulting connected
component contains at most one marked terminal.

For every query, minimize lexicographically:

1. the total removal cost;
2. among solutions of minimum cost, the number of removed edges.

Queries are independent; removed edges are restored before the next query.

## Input

```text
n q
n-1 lines: u v cost
q queries: k v1 v2 ... vk
```

- `1 <= n,q <= 200000`
- `1 <= cost <= 10^9`
- terminals in one query are distinct;
- the sum of `k` over all queries is at most `200000`.

## Output

For each query, print `minimum_cost minimum_edge_count`.

## Sample input

```text
5 3
1 2 5
2 3 2
2 4 3
4 5 4
2 3 5
3 1 3 5
1 4
```

## Sample output

```text
2 1
5 2
0 0
```
