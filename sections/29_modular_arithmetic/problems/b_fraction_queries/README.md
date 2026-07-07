# B. Fraction Queries

Let `p` be a prime number. For each query, compute:

```text
a / b modulo p
```

In modular arithmetic this means:

```text
a * inverse(b) modulo p
```

The input guarantees that `b` is not divisible by `p`.

## Input

```text
p q
a1 b1
a2 b2
...
aq bq
```

`2 <= p <= 10^9 + 7`, `p` is prime, `1 <= q <= 2 * 10^5`,
`0 <= a <= 10^18`, `1 <= b <= 10^18`, and `b mod p != 0`.

## Output

Print one answer per query.

## Sample

Input:

```text
1000000007 3
1 2
10 4
7 3
```

Output:

```text
500000004
500000006
333333338
```
