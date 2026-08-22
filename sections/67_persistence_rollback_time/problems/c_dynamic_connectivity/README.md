# C. Dynamic Connectivity

An undirected graph starts with `n` isolated vertices. Process operations:

- `+ u v`: add edge `{u,v}`;
- `- u v`: remove edge `{u,v}`;
- `? u v`: print whether `u` and `v` are currently connected.

An edge is never added while already present and is removed only while present.

## Input

```text
n q
q operations
```

`1 <= n,q <= 200000`, `u != v`.

## Output

For every query, print `YES` or `NO`.

## Sample

```text
4 8
+ 1 2
+ 2 3
? 1 3
- 1 2
? 1 3
+ 3 4
? 2 4
? 1 1
```

```text
YES
NO
YES
YES
```
