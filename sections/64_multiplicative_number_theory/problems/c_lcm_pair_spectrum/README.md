# C. LCM Pair Spectrum

You are given `n` positive integers, each at most `M`. For every
`x = 1,2,...,M`, count the unordered index pairs `i < j` for which

```text
lcm(ai, aj) = x.
```

Print all counts modulo `1,000,000,007`.

## Input

```text
n M
a1 a2 ... an
```

- `2 <= n <= 200000`
- `1 <= M <= 200000`
- `1 <= ai <= M`

Equal values at different indices are distinct choices.

## Output

Print `M` integers. The `x`-th integer is the number of pairs whose lcm is
exactly `x`.

## Sample

```text
4 6
1 2 3 6
```

```text
0 1 1 0 0 4
```
