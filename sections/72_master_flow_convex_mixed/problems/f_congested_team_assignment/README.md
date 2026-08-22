# F. Congested Team Assignment

Assign every specialist to one eligible team. Team `j` must receive between `low[j]` and `high[j]` specialists. Assignment `(i,j)` earns `profit`, while a team of final size `x` pays congestion cost `a[j]*x^2`. Maximize profit minus total congestion, or print `IMPOSSIBLE`.

## Input
`n p m`; `p` lines `low high a`; then `m` lines `specialist team profit`.

`1 <= n,p <= 250`, `0 <= m <= 30000`, `0 <= a,profit <= 10^6`.

## Sample
```text
3 2 5
1 2 1
1 2 2
1 1 8
1 2 7
2 1 6
2 2 10
3 1 7
```
```text
19
```
