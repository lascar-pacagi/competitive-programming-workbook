# C. Huge Linear Recurrence

A sequence modulo `998244353` has order `k`. Its first terms are
`a[0]..a[k-1]`, and for every `m >= k`,

```text
a[m] = c[0]a[m-1] + c[1]a[m-2] + ... + c[k-1]a[m-k]
       (mod 998244353).
```

Compute `a[n]`.

## Input

```text
k n
a[0] a[1] ... a[k-1]
c[0] c[1] ... c[k-1]
```

- `1 <= k <= 400`
- `0 <= n <= 10^18`
- every input value is in `0..998244352`

## Output

Print `a[n]`.

## Sample

```text
2 10
0 1
1 1
```

```text
55
```
