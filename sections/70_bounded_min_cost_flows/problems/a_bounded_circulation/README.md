# A. Bounded Circulation

You are given a directed graph. Edge `i` must carry an integer flow between its lower and upper bounds. At every vertex, total incoming flow must equal total outgoing flow. Print `YES` if such a circulation exists, otherwise `NO`.

## Input
`n m`, followed by `m` lines `u v low high`. Parallel edges are allowed.

`1 <= n <= 200`, `0 <= m <= 2000`, `0 <= low <= high <= 10^9`.

## Sample
```text
3 3
1 2 2 4
2 3 1 3
3 1 2 5
```
```text
YES
```
