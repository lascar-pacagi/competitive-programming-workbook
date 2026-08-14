# S. Advantage Assignment

You are given two arrays `A` and `B`, each containing `n` integers. You may
permute `A` arbitrarily. Maximize the number of indices `i` for which
`A[i] > B[i]`.

Print only the maximum possible number of winning indices.

## Input

```text
n
A1 A2 ... An
B1 B2 ... Bn
```

`1 <= n <= 200000` and `-10^9 <= A_i, B_i <= 10^9`.

## Output

Print the maximum possible number of indices where the permuted value from
`A` is strictly greater than the corresponding value from `B`.

## Sample Input

```text
4
2 7 11 15
1 10 4 11
```

## Sample Output

```text
4
```
