# Quota Project Portfolio

There are `n` projects. Selecting project `u` earns signed profit `p[u]`. A
dependency `u v` means that selecting `u` requires selecting `v`.

Find the maximum total profit of a dependency-closed set containing exactly
`K` projects.

It is guaranteed that some integer `lambda` exists such that **every**
dependency-closed set maximizing `sum over its projects of (p[u] - lambda)`
contains exactly `K` projects.

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
