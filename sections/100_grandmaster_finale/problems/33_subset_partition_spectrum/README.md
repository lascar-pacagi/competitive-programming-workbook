# Subset Partition Spectrum

All arithmetic is modulo `998244353`.

Functions `f` and `g` are given on all subsets of `{0, 1, ..., k-1}`; a subset
is written as a bit mask `S` in `[0, 2^k)`. For every mask `S` print

```text
h[S] = sum over masks A with A subset of S of f[A] * g[S \ A],
```

that is, the sum over all ways to split `S` into two disjoint parts.

## Input

```text
k
f[0] f[1] ... f[2^k - 1]
g[0] g[1] ... g[2^k - 1]
```

- `0 <= k <= 16`;
- all values lie in `[0, 998244353)`.

## Output

Print `h[0] ... h[2^k - 1]` on one line.

## Sample input
```text
2
1 2 3 4
5 6 7 8
```
## Sample output
```text
5 16 22 60
```
