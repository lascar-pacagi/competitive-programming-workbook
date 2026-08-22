# Parametric Quota Cut

There are `n` projects. Selecting project `u` earns signed profit `p[u]`. A
dependency `u v` means that selecting `u` requires selecting `v`.

Find the maximum total profit of a dependency-closed set containing exactly
`K` projects.

The instance satisfies the following essential promise:

> There exists an integer penalty `lambda` such that **every** set maximizing
> `sum(p[u]-lambda)` over all dependency-closed sets contains exactly `K`
> projects.

Without this promise, the exact-cardinality closure problem is not what the
intended parametric-cut method solves.

## Input

```text
n m K
p[1] ... p[n]
m lines: u v
```

- `1 <= n <= 200`, `0 <= m <= 2000`, `0 <= K <= n`;
- `|p[u]| <= 10^9`;
- dependencies may contain cycles.

## Output

Print the maximum profit of a valid set of exactly `K` projects.

## Sample input

```text
3 1 2
8 3 4
1 2
```

## Sample output

```text
11
```
