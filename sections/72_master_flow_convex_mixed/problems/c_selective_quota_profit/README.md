# C. Selective Quota Profit

There are `n` workers and `p` projects, but exactly `K` workers must be chosen.
Each chosen worker is assigned to one eligible project and each worker is used
at most once. Project `j` must receive between `low[j]` and `high[j]` chosen
workers. Maximize total assignment profit, or print `IMPOSSIBLE`.

## Input

`n p m K`; then `p` lines `low high`; then `m` distinct lines
`worker project profit`.

`1 <= n,p <= 200`, `0 <= K <= n`, `0 <= m <= 20000`, and
`0 <= profit <= 10^6`.

## Sample

```text
4 2 6 3
1 2
1 2
1 1 8
1 2 4
2 1 5
2 2 9
3 1 7
4 2 6
```

```text
24
```
