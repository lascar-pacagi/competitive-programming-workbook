# Temporal Geometric Alliances

Rollback parity DSU over a time segment tree is the temporal-alliance kernel after geometric candidate edges are generated.

There are `n` switches, each assigned a bit. Constraints are inserted and
removed over time. A constraint `(u,v,p)` requires

```text
bit[u] xor bit[v] = p,
```

where `p` is `0` or `1`.

Operations are numbered from `1` to `q`:

- `+ u v p`: insert a constraint. Its identifier is this operation number.
- `- id`: remove the constraint inserted by operation `id`. It is guaranteed
  to be active.
- `?`: report the number of bit assignments satisfying every active
  constraint, modulo `1,000,000,007`.

If the active constraints are inconsistent, report `0`. Parallel and
self-constraints are allowed.

## Input

```text
n q
q operations
```

- `1 <= n,q <= 200000`

## Output

Print one answer for every `?` operation.

## Sample input

```text
3 11
?
+ 1 2 0
?
+ 2 3 1
?
+ 1 3 0
?
- 6
?
- 2
?
```

## Sample output

```text
8
4
2
0
2
4
```
