# C. Route Matrices

Each tree vertex stores a `2 by 2` matrix modulo `998244353`. A path query asks
for the matrix product in vertex order from `u` to `v`; point updates replace
one matrix. Matrix multiplication is not commutative.

## Input
```text
n q
four entries of each matrix, row-major
n-1 edges
operations: U u a b c d, or Q u v
```
`1 <= n,q <= 200000`.

## Output
For every query print the four row-major entries.

## Sample
```text
2 2
1 1 0 1
2 0 0 2
1 2
Q 1 2
Q 2 1
```
```text
2 2 0 2
2 2 0 2
```
