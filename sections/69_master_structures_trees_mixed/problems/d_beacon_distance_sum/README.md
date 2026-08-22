# D. Beacon Distance Sum

An unweighted tree initially has no active vertices. `T u` toggles `u`.
`Q u` asks for the sum of distances from `u` to every active vertex. Print `0`
when none are active.

## Input
```text
n q
n-1 edges
q operations
```
`1 <= n,q <= 200000`; answers fit signed 64-bit integers.

## Sample
```text
3 5
1 2
2 3
T 1
T 3
Q 2
T 1
Q 3
```
```text
2
0
```
