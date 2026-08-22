# M. Totient Prefix

For each query `n`, compute `phi(1) + phi(2) + ... + phi(n)` modulo
`1000000007`, where `phi(x)` is the number of integers in `1..x` that are
coprime with `x`.

The input contains up to `200000` queries and every `n` is at most `1000000`.

## Input

```text
q
n_1 n_2 ... n_q
```

## Output

Print one answer per query.

## Sample

```text
3
1 5 10
```

```text
1
10
32
```
