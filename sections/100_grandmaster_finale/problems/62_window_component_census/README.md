# Window Component Census

A network has `n` routers and a log of `m` cable installations. Installation
`i` connected routers `u[i]` and `v[i]`; a cable may join a router to itself
and the same pair may be cabled several times.

An analyst replays windows of the log. For a window `(l, r)`, start from the
`n` isolated routers and install exactly the cables `l, l+1, ..., r`. Print
the number of connected groups of routers in the resulting network.

Windows are independent of each other.

## Input

```text
n m q
m lines: u v
q lines: l r
```

- `1 <= n, m, q <= 200000`;
- `1 <= u, v <= n`;
- `1 <= l <= r <= m`.

## Output

Print one line per window.

## Sample input

```text
5 6 4
1 2
2 3
1 3
4 4
3 4
5 1
1 3
2 5
4 6
1 6
```

## Sample output

```text
3
2
3
1
```
