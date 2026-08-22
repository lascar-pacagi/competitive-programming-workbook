# GCD Convolution Queries

The gcd-sum query is evaluated by its divisor-transform identity.

For each query `n`, compute:

```text
gcd(1,n) + gcd(2,n) + ... + gcd(n,n)
```

Print the answer modulo `1000000007`. There are at most `200000` queries and
each `n` is at most `1000000`.

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
1 6 10
```

```text
1
15
27
```
