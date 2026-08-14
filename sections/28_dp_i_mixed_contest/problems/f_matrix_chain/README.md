# F. Matrix Chain

Matrices `1..n` have compatible dimensions: matrix `i` is
`d[i-1] x d[i]`. Choose the parenthesization requiring the fewest scalar
multiplications.

## Input
```text
n
d0 d1 ... dn
```
`1 <= n <= 500`, `1 <= d[i] <= 10^4`.

## Output
Print the minimum multiplication count.

## Sample
```text
3
10 30 5 60
```
```text
4500
```
