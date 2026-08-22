# B. Night Delivery

Send exactly `F` units from `s` to `t` through a directed network. An edge has an integer capacity and a cost per unit. Find the minimum total cost, or print `IMPOSSIBLE` when fewer than `F` units can be sent.

Costs may be negative, but the input graph contains no reachable negative-cost directed cycle with positive residual capacity before any flow is sent.

## Input
`n m F`, then `s t`, followed by `m` lines `u v capacity cost`.

`2 <= n <= 200`, `0 <= m <= 2000`, `0 <= F <= 200`, `0 <= capacity <= 200`, `|cost| <= 10^6`.

## Sample
```text
4 5 3
1 4
1 2 2 1
1 3 2 4
2 3 1 -2
2 4 2 3
3 4 2 1
```
```text
9
```
