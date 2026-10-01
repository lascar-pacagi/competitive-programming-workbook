# Connected Structure Series

All arithmetic is modulo `998244353`.

You are given the first `n` coefficients of a formal power series
`A(x) = A[0] + A[1] x + A[2] x^2 + ...` with `A[0] = 1`. Find the first `n`
coefficients of the unique power series `B(x)` such that

```text
B[0] = 0   and   A'(x) = A(x) * B'(x),
```

where `'` denotes the formal derivative. (For example, when `A` counts
labelled structures that split uniquely into connected parts, `B` counts the
connected ones.)

## Input

```text
n
A[0] A[1] ... A[n-1]
```

- `1 <= n <= 200000`;
- `0 <= A[i] < 998244353` and `A[0] = 1`.

## Output

Print `B[0] B[1] ... B[n-1]` on one line.

## Sample input
```text
3
1 1 499122177
```
## Sample output
```text
0 1 0
```
