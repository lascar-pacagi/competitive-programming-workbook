# C. Team Quota Profit

Assign every worker to exactly one eligible project. Project `j` must receive between `low[j]` and `high[j]` workers. An eligible assignment has a profit; maximize total profit, or print `IMPOSSIBLE`.

## Input
`n p m`; `p` lines `low high`; then `m` distinct lines `worker project profit`.

`1 <= n,p <= 200`, `0 <= m <= 20000`, `0 <= profit <= 10^6`.

## Sample
```text
3 2 5
1 2
1 2
1 1 8
1 2 4
2 1 5
2 2 9
3 1 7
```
```text
24
```
