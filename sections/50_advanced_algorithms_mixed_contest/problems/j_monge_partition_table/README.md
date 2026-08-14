# J. Monge Partition Table

Partition positions `1..n` into exactly `k` nonempty contiguous groups.
The input gives `cost[l][r]` for every possible group `[l,r]`. It is
guaranteed that this interval-cost table is Monge, so optimal split
positions are monotone. Print the minimum total cost.

## Input
```text
n k
n x n table
```
Entries below the diagonal are ignored. `n <= 1000`, `k <= 50`.

## Sample
```text
4 2
1 4 9 16
0 1 4 9
0 0 1 4
0 0 0 1
```
```text
8
```
