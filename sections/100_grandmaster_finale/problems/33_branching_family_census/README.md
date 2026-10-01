# Branching Family Census

A family archive stores **plane trees**: rooted trees in which the children of
every person are ordered from left to right. A person with exactly `s`
children can be recorded in `c[s]` different styles (`0 <= s <= D`); nobody
may have more than `D` children. Two records are different if their trees
differ (as ordered trees) or some person has a different style.

For every `n` from `1` to `N`, count the records of trees with exactly `n`
persons, modulo `998244353`.

## Input

```text
N D
c[0] c[1] ... c[D]
```

- `1 <= N <= 100000`;
- `0 <= D <= 8`;
- `0 <= c[s] < 998244353`.

## Output

Print `N` integers on one line: the counts for `n = 1, 2, ..., N`.

## Sample input

```text
7 2
1 2 1
```

## Sample output

```text
1 2 5 14 42 132 429
```

With one style for a leaf, two for a single child (left or right), and one for
two children, the records are exactly the binary trees.
