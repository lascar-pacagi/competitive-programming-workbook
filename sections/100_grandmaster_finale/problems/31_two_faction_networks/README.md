# Two-Faction Networks

A **network** on `n` labelled towns is any set of roads, each joining two
different towns (at most one road per pair). A network is **two-faction** if
the towns can be split into two groups so that every road joins towns of
different groups, and it is **connected** if every town can reach every other
town.

For every `n` from `1` to `N`, count the connected two-faction networks on `n`
labelled towns, modulo `998244353`.

## Input

One integer `N`.

- `1 <= N <= 200000`.

## Output

Print `N` integers on one line: the counts for `n = 1, 2, ..., N`.

## Sample input

```text
6
```

## Sample output

```text
1 1 3 19 195 3031
```
